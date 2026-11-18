#!/usr/bin/env python3
"""Verify ORISON's static references and critical browser journey."""

from __future__ import annotations

import json
import threading
import time
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from itertools import permutations
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

try:
    from playwright.sync_api import Page, sync_playwright
except ImportError as error:
    raise SystemExit(
        "Playwright is required. Run: "
        "python3 -m pip install -r tests/requirements.txt && "
        "python3 -m playwright install chromium"
    ) from error


ROOT = Path(__file__).resolve().parents[1]
STORAGE_KEY = "orison_trace_v2"
FRAGMENT_ADDRESSES = ("013", "027", "058")
INTENTIONAL_MISSING = {
    f"/.lost+found/00000000/fragments/{address}/"
    for address in FRAGMENT_ADDRESSES
}


def activate(page: Page, selector: str, key: str = "Enter") -> None:
    page.wait_for_load_state("networkidle")
    control = page.locator(selector).first
    control.wait_for(state="visible")
    control.focus()
    assert control.evaluate("element => element === document.activeElement")
    page.keyboard.press(key)


class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[tuple[int, str, str]] = []

    def handle_starttag(
        self,
        tag: str,
        attributes: list[tuple[str, str | None]],
    ) -> None:
        for name, value in attributes:
            if name in {"href", "src"} and value:
                self.references.append((self.getpos()[0], name, value))


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, _format: str, *args: object) -> None:
        return

    def send_error(
        self,
        code: int,
        message: str | None = None,
        explain: str | None = None,
    ) -> None:
        if code != 404:
            super().send_error(code, message, explain)
            return

        body = (ROOT / "404.html").read_bytes()
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)


def runtime_documents() -> list[Path]:
    documents = [ROOT / "index.html", ROOT / "404.html"]
    documents.extend((ROOT / "erase").rglob("*.html"))
    documents.extend((ROOT / ".lost+found").rglob("*.html"))
    return sorted(set(documents))


def local_target(document: Path, reference: str) -> Path | None:
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None

    path = unquote(parsed.path)
    target = ROOT / path.lstrip("/") if path.startswith("/") else document.parent / path
    target = target.resolve()
    if target.is_dir():
        target /= "index.html"
    return target


def verify_references() -> int:
    failures: list[str] = []
    documents = runtime_documents()

    for document in documents:
        parser = ReferenceParser()
        parser.feed(document.read_text(encoding="utf-8"))
        for line, attribute, reference in parser.references:
            parsed = urlsplit(reference)
            if parsed.scheme in {"http", "https"} or parsed.netloc:
                failures.append(
                    f"{document.relative_to(ROOT)}:{line}: external {attribute} {reference}"
                )
                continue
            if parsed.path in INTENTIONAL_MISSING:
                continue
            target = local_target(document, reference)
            if target is not None and not target.exists():
                failures.append(
                    f"{document.relative_to(ROOT)}:{line}: missing {attribute} {reference}"
                )

    if failures:
        raise AssertionError("Static reference validation failed:\n" + "\n".join(failures))
    return len(documents)


def state(page: Page) -> dict[str, object]:
    value = page.evaluate(f"localStorage.getItem('{STORAGE_KEY}')")
    assert value, "ORISON state was not written"
    return json.loads(value)


def wait_for_flag(page: Page, flag: str, timeout_ms: int = 5_000) -> None:
    deadline = time.monotonic() + timeout_ms / 1_000
    while time.monotonic() < deadline:
        if flag in state(page)["flags"]:
            return
        page.wait_for_timeout(25)
    raise AssertionError(f"Timed out waiting for state flag: {flag}")


def assert_visual_viewport_contained(page: Page) -> None:
    dimensions = page.evaluate(
        """() => ({
            documentWidth: Math.max(
                document.documentElement.scrollWidth,
                document.body.scrollWidth
            ),
            visualWidth: window.visualViewport
                ? window.visualViewport.width
                : document.documentElement.clientWidth
        })"""
    )
    assert dimensions["documentWidth"] <= dimensions["visualWidth"] + 1, dimensions


def assert_stacked_handoff(page: Page, selector: str) -> None:
    result = page.locator(f"{selector} .handoff-record__result").bounding_box()
    action = page.locator(f"{selector} .handoff-record__action").bounding_box()
    assert result is not None and action is not None
    assert result["y"] + result["height"] <= action["y"] + 1


def assert_within_viewport(page: Page, selector: str) -> None:
    box = page.locator(selector).bounding_box()
    viewport = page.viewport_size
    assert box is not None and viewport is not None
    assert box["x"] >= 0 and box["x"] + box["width"] <= viewport["width"]
    assert box["y"] >= 0 and box["y"] + box["height"] <= viewport["height"]


def watch_page(
    page: Page,
    allowed_netloc: str,
    browser_errors: list[str],
    external_requests: list[str],
) -> None:
    def record_console(message: object) -> None:
        if getattr(message, "type") != "error":
            return
        text = getattr(message, "text")
        if text.startswith(
            "Failed to load resource: the server responded with a status of 404"
        ):
            return
        browser_errors.append(f"console: {text}")

    page.on(
        "console",
        record_console,
    )
    page.on("pageerror", lambda error: browser_errors.append(f"page: {error}"))

    def record_response(response: object) -> None:
        status = getattr(response, "status")
        request = getattr(response, "request")
        if status < 400:
            return
        if status == 404 and getattr(request, "resource_type") == "document":
            return
        browser_errors.append(f"response: {status} {getattr(response, 'url')}")

    page.on("response", record_response)

    def record_request(request: object) -> None:
        url = getattr(request, "url")
        parsed = urlsplit(url)
        if parsed.scheme in {"http", "https"} and parsed.netloc != allowed_netloc:
            external_requests.append(url)

    page.on("request", record_request)


def verify_journey(base_url: str) -> None:
    browser_errors: list[str] = []
    external_requests: list[str] = []
    allowed_netloc = urlsplit(base_url).netloc

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)

        legacy_context = browser.new_context(reduced_motion="reduce")
        legacy_state = {
            "v": 1,
            "first": 1_700_000_000_000,
            "seen": {"root": 1, "fragments": 3},
            "order": ["root", "fragments"],
            "last": "fragments",
            "flags": [
                "response-attached",
                "orphan-released",
                "fragment-probe-013",
                "fragment-probe-027",
                "fragment-probe-058",
            ],
        }
        legacy_context.add_cookies(
            [
                {
                    "name": "orison_trace",
                    "value": quote(json.dumps(legacy_state), safe=""),
                    "url": base_url,
                }
            ]
        )
        legacy_page = legacy_context.new_page()
        watch_page(legacy_page, allowed_netloc, browser_errors, external_requests)
        legacy_page.goto(base_url, wait_until="networkidle")
        migrated_flags = state(legacy_page)["flags"]
        assert "response-attached" not in migrated_flags
        assert "orphan-released" not in migrated_flags
        assert not any(flag.startswith("fragment-probe-") for flag in migrated_flags)
        migrated_state = state(legacy_page)
        assert "fragments" not in migrated_state["seen"]
        assert "fragments" not in migrated_state["order"]
        assert migrated_state["last"] == "root"
        legacy_context.close()

        unearned_context = browser.new_context(reduced_motion="reduce")
        unearned_page = unearned_context.new_page()
        watch_page(unearned_page, allowed_netloc, browser_errors, external_requests)
        unearned_page.goto(
            f"{base_url}/.lost+found/00000000/archive/weather/",
            wait_until="networkidle",
        )
        assert unearned_page.locator("#cameraSource").is_visible()
        assert "forecast" not in state(unearned_page)["flags"]
        assert "forecast-held" not in state(unearned_page)["flags"]
        unearned_page.goto(
            f"{base_url}/.lost+found/00000000/fragments/",
            wait_until="networkidle",
        )
        unearned_page.wait_for_url(
            f"{base_url}/.lost+found/00000000/archive/"
        )
        assert "fragments" not in state(unearned_page)["seen"]
        unearned_response = unearned_page.goto(
            f"{base_url}/.lost+found/00000000/fragments/013/",
            wait_until="networkidle",
        )
        assert unearned_response is not None and unearned_response.status == 404
        assert unearned_page.locator("#missingCode").inner_text() == "404"
        assert "fragment-probe-013" not in state(unearned_page)["flags"]
        unearned_context.close()

        staff_gate_context = browser.new_context(reduced_motion="reduce")
        staff_gate_page = staff_gate_context.new_page()
        watch_page(
            staff_gate_page, allowed_netloc, browser_errors, external_requests
        )
        staff_gate_page.goto(
            base_url,
            wait_until="networkidle",
        )
        staff_gate_page.evaluate(
            """() => {
                const value = JSON.parse(localStorage.getItem('orison_trace_v2'));
                value.flags = ['mirror-route', 'forecast-held'];
                value.seen = {root: 1, archive: 1, mirror: 1, weather: 1};
                value.order = ['root', 'archive', 'mirror', 'weather'];
                value.last = 'weather';
                localStorage.setItem('orison_trace_v2', JSON.stringify(value));
            }"""
        )
        staff_gate_page.goto(
            f"{base_url}/.lost+found/00000000/archive/staff/",
            wait_until="networkidle",
        )
        assert staff_gate_page.locator(".subject-row").count() == 0
        assert "pending" in staff_gate_page.locator(
            "#staffHandoffState"
        ).inner_text().lower()
        staff_gate_page.evaluate(
            """() => {
                const value = JSON.parse(localStorage.getItem('orison_trace_v2'));
                value.flags.push('checksum-match');
                value.seen.integrity = 1;
                value.order.push('integrity');
                localStorage.setItem('orison_trace_v2', JSON.stringify(value));
            }"""
        )
        staff_gate_page.goto(
            f"{base_url}/.lost+found/00000000/archive/",
            wait_until="networkidle",
        )
        assert staff_gate_page.locator("#letterFile").is_hidden()
        assert staff_gate_page.locator(
            '[data-room="staff"] .file__state'
        ).inner_text().lower().endswith("source pending")
        activate(staff_gate_page, "#operationAction")
        staff_gate_page.wait_for_url(
            f"{base_url}/.lost+found/00000000/archive/staff/"
        )
        assert staff_gate_page.locator(".subject-row").count() == 1
        assert "indexed" in staff_gate_page.locator(
            "#staffHandoffState"
        ).inner_text().lower()
        activate(staff_gate_page, "#staffHandoff .handoff-record__action")
        staff_gate_page.wait_for_url(
            f"{base_url}/.lost+found/00000000/archive/"
        )
        assert staff_gate_page.locator("#letterFile").is_visible()
        staff_gate_context.close()

        attachment_gate_context = browser.new_context(reduced_motion="reduce")
        attachment_gate_page = attachment_gate_context.new_page()
        watch_page(
            attachment_gate_page,
            allowed_netloc,
            browser_errors,
            external_requests,
        )
        attachment_gate_page.goto(base_url, wait_until="networkidle")
        attachment_gate_page.evaluate(
            """() => {
                const value = JSON.parse(localStorage.getItem('orison_trace_v2'));
                value.answers = ['valuable', 'record', 'compliant', 'process', 'earlier'];
                value.flags = ['operator-probe', 'operator-occupied'];
                localStorage.setItem('orison_trace_v2', JSON.stringify(value));
            }"""
        )
        attachment_gate_page.reload(wait_until="networkidle")
        assert (
            attachment_gate_page.locator("#commandHint").inner_text()
            == "RUN: UNPACK ORISON.ZIP"
        )
        attachment_gate_page.locator("#commandInput").fill(
            "reconcile response 00000000"
        )
        attachment_gate_page.locator("#commandInput").press("Enter")
        attachment_gate_page.get_by_text(
            "reconcile: retained response ledger is incomplete", exact=True
        ).wait_for()
        assert "response-attached" not in state(attachment_gate_page)["flags"]
        attachment_gate_page.locator("#commandHint").click()
        wait_for_flag(attachment_gate_page, "unpacked")
        pending_attachment = attachment_gate_page.get_by_role(
            "button", name="run: reconcile response 00000000"
        )
        pending_attachment.wait_for()
        assert attachment_gate_page.locator("a.archive-path").count() == 0
        assert "quick-command--primary" in (
            pending_attachment.get_attribute("class") or ""
        )
        pending_attachment.click()
        wait_for_flag(attachment_gate_page, "response-attached")
        attachment_gate_context.close()

        compatibility_context = browser.new_context(reduced_motion="reduce")
        compatibility_page = compatibility_context.new_page()
        watch_page(
            compatibility_page, allowed_netloc, browser_errors, external_requests
        )
        compatibility_page.goto(base_url, wait_until="networkidle")
        compatibility_page.evaluate(
            """() => {
                const value = JSON.parse(localStorage.getItem('orison_trace_v2'));
                value.answers = ['valuable', 'record', 'compliant', 'process', 'earlier'];
                value.flags = ['unpacked', 'operator-probe'];
                localStorage.setItem('orison_trace_v2', JSON.stringify(value));
            }"""
        )
        compatibility_page.reload(wait_until="networkidle")
        compatibility_page.locator("#commandInput").fill("unpack orison.zip")
        compatibility_page.locator("#commandInput").press("Enter")
        compatibility_page.get_by_role(
            "button", name="open: recovered inode"
        ).wait_for()
        assert "response-attached" not in state(compatibility_page)["flags"]
        compatibility_page.evaluate(
            """() => {
                const value = JSON.parse(localStorage.getItem('orison_trace_v2'));
                value.flags = ['unpacked', 'response-attached'];
                localStorage.setItem('orison_trace_v2', JSON.stringify(value));
            }"""
        )
        compatibility_page.reload(wait_until="networkidle")
        compatibility_page.locator("#commandInput").fill(
            "reconcile response 00000000"
        )
        compatibility_page.locator("#commandInput").press("Enter")
        compatibility_page.locator(".reconciliation-ledger").wait_for()
        wait_for_flag(compatibility_page, "response-attached")
        compatibility_page.goto(
            f"{base_url}/.lost+found/00000000/archive/",
            wait_until="networkidle",
        )
        assert compatibility_page.locator("#responseRecord").is_visible()
        compatibility_page.evaluate(
            """() => {
                const value = JSON.parse(localStorage.getItem('orison_trace_v2'));
                value.flags = ['letter', 'operator-probe'];
                localStorage.setItem('orison_trace_v2', JSON.stringify(value));
            }"""
        )
        compatibility_page.reload(wait_until="networkidle")
        assert compatibility_page.locator("#letterFile").is_visible()
        assert compatibility_page.locator("#operatorFile").is_visible()
        compatibility_context.close()

        bfcache_context = browser.new_context()
        bfcache_page = bfcache_context.new_page()
        watch_page(
            bfcache_page, allowed_netloc, browser_errors, external_requests
        )
        bfcache_page.goto(base_url, wait_until="networkidle")
        bfcache_page.locator("#commandInput").fill("unpack orison.zip")
        bfcache_page.locator("#commandInput").press("Enter")
        bfcache_page.get_by_text(
            "[1/4] inspecting archive envelope", exact=True
        ).wait_for()
        bfcache_page.evaluate(
            """() => {
                window.dispatchEvent(
                    new PageTransitionEvent('pagehide', { persisted: true })
                );
                window.dispatchEvent(
                    new PageTransitionEvent('pageshow', { persisted: true })
                );
            }"""
        )
        bfcache_page.wait_for_timeout(600)
        assert "unpacked" not in state(bfcache_page)["flags"]
        assert not bfcache_page.get_by_text(
            "locating end-of-central-directory record ... found", exact=True
        ).count()
        bfcache_context.close()

        interruption_context = browser.new_context()
        interruption_page = interruption_context.new_page()
        watch_page(
            interruption_page, allowed_netloc, browser_errors, external_requests
        )
        interruption_page.goto(base_url, wait_until="networkidle")
        interruption_page.locator("#commandInput").fill("unpack orison.zip")
        interruption_page.locator("#commandInput").press("Enter")
        interruption_page.get_by_text(
            "[1/4] inspecting archive envelope", exact=True
        ).wait_for()
        interruption_page.reload(wait_until="networkidle")
        assert "unpacked" not in state(interruption_page)["flags"]
        interruption_page.locator("#commandHint").click()
        interruption_page.get_by_role(
            "button", name="open: recovered inode"
        ).wait_for(timeout=10_000)
        assert "unpacked" in state(interruption_page)["flags"]
        activate(interruption_page, "a.archive-path")
        interruption_page.wait_for_url(
            f"{base_url}/.lost+found/00000000/"
        )
        interruption_page.go_back(wait_until="networkidle")
        interruption_page.wait_for_url(base_url)
        interruption_page.evaluate(
            """() => {
                const value = JSON.parse(localStorage.getItem('orison_trace_v2'));
                value.answers = ['valuable', 'record', 'compliant', 'process', 'earlier'];
                value.flags = [...new Set([...value.flags, 'operator-occupied'])];
                localStorage.setItem('orison_trace_v2', JSON.stringify(value));
            }"""
        )
        interruption_page.reload(wait_until="networkidle")
        interruption_page.get_by_text(
            "recovery state: INCOMPLETE", exact=True
        ).wait_for()
        interrupted_attachment = interruption_page.get_by_role(
            "button", name="run: reconcile response 00000000"
        )
        assert interruption_page.locator("a.archive-path").count() == 0
        assert "quick-command--primary" in (
            interrupted_attachment.get_attribute("class") or ""
        )
        interrupted_attachment.click()
        interruption_page.locator(".reconciliation-ledger").wait_for()
        interruption_page.wait_for_timeout(100)
        interruption_page.reload(wait_until="networkidle")
        assert "response-attached" not in state(interruption_page)["flags"]
        interruption_page.get_by_text(
            "recovery state: INCOMPLETE", exact=True
        ).wait_for()
        reloaded_attachment = interruption_page.get_by_role(
            "button", name="run: reconcile response 00000000"
        )
        assert interruption_page.locator("a.archive-path").count() == 0
        assert "quick-command--primary" in (
            reloaded_attachment.get_attribute("class") or ""
        )
        interruption_page.locator("#commandInput").fill(
            "reconcile response 00000000"
        )
        interruption_page.locator("#commandInput").press("Enter")
        wait_for_flag(interruption_page, "response-attached")
        assert interruption_page.locator("a.archive-path").get_attribute("href") == (
            "/.lost+found/00000000/archive/"
        )
        interruption_context.close()

        for request_order in permutations(FRAGMENT_ADDRESSES):
            branch_context = browser.new_context(reduced_motion="reduce")
            branch_page = branch_context.new_page()
            watch_page(branch_page, allowed_netloc, browser_errors, external_requests)
            branch_page.goto(base_url, wait_until="networkidle")
            branch_page.evaluate(
                """() => {
                    const value = JSON.parse(localStorage.getItem('orison_trace_v2'));
                    value.flags = ['orphan-released'];
                    localStorage.setItem('orison_trace_v2', JSON.stringify(value));
                }"""
            )
            branch_page.goto(
                f"{base_url}/.lost+found/00000000/fragments/",
                wait_until="networkidle",
            )
            for index, address in enumerate(request_order, start=1):
                branch_page.locator(f'[data-address="{address}"]').click()
                branch_page.wait_for_url(
                    f"{base_url}/.lost+found/00000000/fragments/{address}/"
                )
                branch_flags = state(branch_page)["flags"]
                assert f"fragment-probe-{address}" in branch_flags
                assert (
                    sum(flag.startswith("fragment-probe-") for flag in branch_flags)
                    == index
                )
                branch_page.locator("#missingReturn").click()
                branch_page.wait_for_url(
                    f"{base_url}/.lost+found/00000000/fragments/"
                )
                for retained_address in request_order[:index]:
                    assert branch_page.locator(
                        f'[data-address="{retained_address}"].is-trace'
                    ).count() == 1
                    assert branch_page.locator(
                        f'[data-displaced="{retained_address}"].is-gap'
                    ).count() == 1
                assert (
                    branch_page.locator("a.fragment-cell.is-gap[href]").count()
                    == len(FRAGMENT_ADDRESSES) - index
                )
            assert "all three" in branch_page.locator(
                "#fragmentTitle"
            ).inner_text().lower()
            assert "complete" in branch_page.locator(
                "#fragmentInstruction"
            ).inner_text().lower()
            assert branch_page.locator("#fragmentReturn").get_attribute("href") == "/"
            branch_context.close()

        generic_context = browser.new_context(reduced_motion="reduce")
        generic_page = generic_context.new_page()
        watch_page(generic_page, allowed_netloc, browser_errors, external_requests)
        generic_response = generic_page.goto(
            f"{base_url}/missing-region/not-a-fragment/",
            wait_until="networkidle",
        )
        assert generic_response is not None and generic_response.status == 404
        assert generic_page.locator("#missingCode").inner_text() == "404"
        assert not any(
            flag.startswith("fragment-probe-") for flag in state(generic_page)["flags"]
        )
        generic_context.close()

        aperture_viewports = (
            ({"width": 375, "height": 812}, "no-preference"),
            ({"width": 390, "height": 844}, "no-preference"),
            ({"width": 390, "height": 640}, "reduce"),
        )
        for viewport, reduced_motion in aperture_viewports:
            aperture_context = browser.new_context(
                viewport=viewport,
                is_mobile=True,
                has_touch=True,
                reduced_motion=reduced_motion,
            )
            aperture_page = aperture_context.new_page()
            watch_page(
                aperture_page,
                allowed_netloc,
                browser_errors,
                external_requests,
            )
            aperture_page.goto(base_url, wait_until="networkidle")
            aperture_page.evaluate(
                """() => {
                    const value = JSON.parse(
                        localStorage.getItem('orison_trace_v2')
                    );
                    value.flags = [
                        'unpacked',
                        'examined',
                        'mirror-route',
                        'forecast',
                        'forecast-returned'
                    ];
                    value.seen = {root: 1, archive: 1, mirror: 2, weather: 1};
                    value.order = ['root', 'archive', 'mirror', 'weather'];
                    value.last = 'mirror';
                    localStorage.setItem(
                        'orison_trace_v2',
                        JSON.stringify(value)
                    );
                }"""
            )
            aperture_page.goto(
                f"{base_url}/.lost+found/00000000/archive/",
                wait_until="networkidle",
            )
            wait_for_flag(aperture_page, "aperture-slip")
            aperture = aperture_page.locator("#apertureSlip")
            aperture.wait_for(state="visible")
            assert_visual_viewport_contained(aperture_page)
            aperture.wait_for(state="hidden", timeout=3_000)
            assert_visual_viewport_contained(aperture_page)
            aperture_context.close()

        def prepare_letter_operator(page: Page) -> None:
            page.goto(base_url, wait_until="networkidle")
            page.evaluate(
                """() => {
                    const value = JSON.parse(localStorage.getItem('orison_trace_v2'));
                    value.flags = ['forecast', 'checksum-match', 'staff'];
                    value.seen = {root: 1, archive: 1, weather: 1, integrity: 1, staff: 1};
                    value.order = ['root', 'archive', 'weather', 'integrity', 'staff'];
                    value.last = 'staff';
                    localStorage.setItem('orison_trace_v2', JSON.stringify(value));
                }"""
            )
            page.goto(
                f"{base_url}/.lost+found/00000000/dead-letter/",
                wait_until="networkidle",
            )
            assert page.locator("#operatorAddress").is_visible()

        ingress_context = browser.new_context()
        ingress_page = ingress_context.new_page()
        watch_page(ingress_page, allowed_netloc, browser_errors, external_requests)
        prepare_letter_operator(ingress_page)
        activate(ingress_page, "#operatorAddress")
        ingress_page.wait_for_url(f"{base_url}/.lost+found/00000000/operator/")
        active_ingress = ingress_page.evaluate(
            """() => {
                const ingress = document.querySelector('#operatorIngress');
                const status = document.querySelector('#sideStatus');
                const trace = JSON.parse(localStorage.getItem('orison_trace_v2'));
                return {
                    active: document.querySelector('#searchInstrument').hasAttribute(
                        'data-ingress'
                    ),
                    ariaHidden: ingress.getAttribute('aria-hidden'),
                    labelledBy: ingress.getAttribute('aria-labelledby'),
                    source: document.querySelector('#ingressSource').textContent,
                    ledgerRows: ingress.querySelectorAll('.ingress-ledger > div').length,
                    chronology: ingress.querySelector('.ingress-chronology').textContent,
                    verdict: ingress.querySelector('.ingress-verdict').textContent,
                    status: status.textContent,
                    statusRole: status.getAttribute('role'),
                    explicitLive: status.hasAttribute('aria-live'),
                    explicitAtomic: status.hasAttribute('aria-atomic'),
                    probed: trace.flags.includes('operator-probe'),
                };
            }"""
        )
        assert active_ingress["active"]
        assert active_ingress["ariaHidden"] is None
        assert active_ingress["labelledBy"] == "ingressTitle"
        assert active_ingress["source"] == state(ingress_page)["id"]
        assert active_ingress["ledgerRows"] == 3
        assert "−00:00:00.021" in active_ingress["chronology"]
        assert "rejected / source retained" in active_ingress["verdict"]
        assert active_ingress["status"] == (
            "controlling terminal absent / foreground retained"
        )
        assert active_ingress["statusRole"] == "status"
        assert not active_ingress["explicitLive"]
        assert not active_ingress["explicitAtomic"]
        assert active_ingress["probed"]
        assert ingress_page.evaluate("document.activeElement.id") != "archiveReturn"
        assert ingress_page.locator("#archiveReturn").is_visible()
        assert ingress_page.locator("#invite").is_visible()
        ingress_page.wait_for_timeout(2_600)
        assert ingress_page.locator("#operatorIngress").is_visible()
        assert ingress_page.locator("#searchInstrument").get_attribute(
            "data-ingress"
        ) == ""
        assert ingress_page.locator("#sideStatus").text_content() == (
            "controlling terminal absent / foreground retained"
        )
        ingress_page.locator("#archiveReturn").focus()
        assert ingress_page.evaluate("document.activeElement.id") == "archiveReturn"
        assert_visual_viewport_contained(ingress_page)
        ingress_context.close()

        direct_operator_context = browser.new_context(reduced_motion="reduce")
        direct_operator_page = direct_operator_context.new_page()
        watch_page(
            direct_operator_page,
            allowed_netloc,
            browser_errors,
            external_requests,
        )
        direct_operator_page.goto(
            f"{base_url}/.lost+found/00000000/operator/",
            wait_until="networkidle",
        )
        assert "operator-probe" in state(direct_operator_page)["flags"]
        assert direct_operator_page.locator("#searchInstrument").get_attribute(
            "data-ingress"
        ) is None
        assert direct_operator_page.locator("#operatorIngress").is_hidden()
        assert direct_operator_page.locator("#sideStatus").text_content() == (
            "operator not found"
        )
        direct_operator_context.close()

        migrated_operator_context = browser.new_context(reduced_motion="reduce")
        migrated_operator_context.add_cookies(
            [
                {
                    "name": "orison_trace",
                    "value": quote(
                        json.dumps(
                            {
                                "v": 1,
                                "first": 1_700_000_000_000,
                                "seen": {"root": 1, "letter": 1, "operator": 1},
                                "order": ["root", "letter", "operator"],
                                "last": "operator",
                                "flags": ["letter", "operator-probe"],
                            }
                        ),
                        safe="",
                    ),
                    "url": base_url,
                }
            ]
        )
        migrated_operator_page = migrated_operator_context.new_page()
        watch_page(
            migrated_operator_page,
            allowed_netloc,
            browser_errors,
            external_requests,
        )
        migrated_operator_page.goto(
            f"{base_url}/.lost+found/00000000/operator/",
            wait_until="networkidle",
        )
        assert "operator-probe" in state(migrated_operator_page)["flags"]
        assert migrated_operator_page.locator("#searchInstrument").get_attribute(
            "data-ingress"
        ) is None
        assert migrated_operator_page.locator("#operatorIngress").is_hidden()
        migrated_operator_context.close()

        interrupted_ingress_context = browser.new_context()
        interrupted_ingress_page = interrupted_ingress_context.new_page()
        watch_page(
            interrupted_ingress_page,
            allowed_netloc,
            browser_errors,
            external_requests,
        )
        prepare_letter_operator(interrupted_ingress_page)
        activate(interrupted_ingress_page, "#operatorAddress")
        interrupted_ingress_page.wait_for_url(
            f"{base_url}/.lost+found/00000000/operator/"
        )
        assert interrupted_ingress_page.locator("#searchInstrument").get_attribute(
            "data-ingress"
        ) is not None
        interrupted_ingress_page.reload(wait_until="networkidle")
        assert "operator-probe" in state(interrupted_ingress_page)["flags"]
        assert interrupted_ingress_page.locator("#searchInstrument").get_attribute(
            "data-ingress"
        ) is None
        assert interrupted_ingress_page.locator("#sideStatus").text_content() == (
            "operator not found"
        )
        interrupted_ingress_context.close()

        history_ingress_context = browser.new_context()
        history_ingress_page = history_ingress_context.new_page()
        watch_page(
            history_ingress_page,
            allowed_netloc,
            browser_errors,
            external_requests,
        )
        prepare_letter_operator(history_ingress_page)
        activate(history_ingress_page, "#operatorAddress")
        history_ingress_page.wait_for_url(f"{base_url}/.lost+found/00000000/operator/")
        assert history_ingress_page.locator("#searchInstrument").get_attribute(
            "data-ingress"
        ) is not None
        history_ingress_page.evaluate(
            """() => window.dispatchEvent(
                new PageTransitionEvent('pageshow', {persisted: true})
            )"""
        )
        assert history_ingress_page.locator("#searchInstrument").get_attribute(
            "data-ingress"
        ) is None
        assert history_ingress_page.locator("#sideStatus").text_content() == (
            "operator not found"
        )
        history_ingress_page.go_back(wait_until="networkidle")
        history_ingress_page.wait_for_url(
            f"{base_url}/.lost+found/00000000/dead-letter/"
        )
        history_ingress_page.go_forward(wait_until="networkidle")
        history_ingress_page.wait_for_url(
            f"{base_url}/.lost+found/00000000/operator/"
        )
        assert history_ingress_page.locator("#searchInstrument").get_attribute(
            "data-ingress"
        ) is None
        assert history_ingress_page.locator("#sideStatus").text_content() == (
            "operator inferred"
        )
        history_ingress_context.close()

        mobile_ingress_context = browser.new_context(
            viewport={"width": 375, "height": 812},
            is_mobile=True,
            has_touch=True,
            reduced_motion="reduce",
        )
        mobile_ingress_page = mobile_ingress_context.new_page()
        watch_page(
            mobile_ingress_page,
            allowed_netloc,
            browser_errors,
            external_requests,
        )
        prepare_letter_operator(mobile_ingress_page)
        activate(mobile_ingress_page, "#operatorAddress")
        mobile_ingress_page.wait_for_url(f"{base_url}/.lost+found/00000000/operator/")
        assert mobile_ingress_page.locator("#operatorIngress").is_visible()
        assert mobile_ingress_page.locator("#ingressSource").text_content() == (
            state(mobile_ingress_page)["id"]
        )
        assert mobile_ingress_page.locator(".ingress-ledger > div").count() == 3
        assert mobile_ingress_page.locator("#archiveReturn").is_visible()
        assert mobile_ingress_page.locator("#invite").is_visible()
        assert mobile_ingress_page.evaluate("document.activeElement.id") != "archiveReturn"
        assert_visual_viewport_contained(mobile_ingress_page)
        mobile_ingress_page.wait_for_timeout(950)
        assert mobile_ingress_page.locator("#searchInstrument").get_attribute(
            "data-ingress"
        ) == ""
        assert mobile_ingress_page.locator("#sideStatus").text_content() == (
            "controlling terminal absent / foreground retained"
        )
        assert_visual_viewport_contained(mobile_ingress_page)
        mobile_ingress_context.close()

        context = browser.new_context(reduced_motion="reduce")
        page = context.new_page()
        page.set_viewport_size({"width": 1440, "height": 700})
        watch_page(page, allowed_netloc, browser_errors, external_requests)

        page.goto(base_url, wait_until="networkidle")
        assert page.evaluate("document.activeElement.id") == "commandInput"
        page.keyboard.press("Tab")
        assert page.evaluate("document.activeElement.id") == "commandHint"
        page.keyboard.press("Shift+Tab")
        assert page.evaluate("document.activeElement.id") == "commandInput"
        assert page.locator(".command-submit").get_attribute("tabindex") == "-1"
        page.locator("#commandInput").fill("unpack orison.zip")
        page.locator("#commandInput").press("Enter")
        page.get_by_role("button", name="open: recovered inode").wait_for()
        first_unpack = page.locator("#terminalOutput").inner_text()
        for phase in ("[1/4]", "[2/4]", "[3/4]", "[4/4]"):
            assert phase in first_unpack
        assert "recovered path / ./.lost+found/00000000/" in first_unpack
        assert "rsp/" not in first_unpack
        assert "compatibility vector" not in first_unpack
        assert "response-attached" not in state(page)["flags"]
        assert page.locator("a.archive-path").get_attribute("href") == (
            "/.lost+found/00000000/"
        )
        page.locator("a.archive-path").click()
        page.wait_for_url(f"{base_url}/.lost+found/00000000/")

        activate(page, "#specimenAction")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/examination/")
        for _ in range(5):
            activate(page, ".answers button")
        activate(page, "#mountHint")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/archive/")
        assert page.locator("#parentInterlock").is_hidden()
        assert page.locator("#fragmentIndex").is_hidden()
        assert page.locator("#letterFile").is_hidden()

        activate(page, "#operationAction")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/archive/mirror/")
        activate(page, "#compareLink")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/archive/weather/")
        page.go_back(wait_until="networkidle")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/archive/mirror/")
        wait_for_flag(page, "forecast-returned")
        assert page.locator("#mirrorHandoff").is_visible()
        assert_stacked_handoff(page, "#mirrorHandoff")
        assert page.locator("#mirrorReturn").is_hidden()
        assert page.locator("#compareLink").get_attribute("class") == "compare is-secondary"
        activate(page, "#mirrorHandoff .handoff-record__action")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/archive/")
        wait_for_flag(page, "aperture-slip")
        assert page.locator("#letterFile").is_hidden()
        assert (
            page.locator(".directory").get_attribute("data-operation-active")
            == "true"
        )
        source_file = page.locator(".file.is-source")
        assert source_file.get_attribute("data-room") == "mirror"
        source_state = source_file.locator(".file__state").inner_text()
        assert "history return retained" in source_state.lower(), source_state
        assert page.locator("#directoryTitle").inner_text() == (
            "The returned front now has a copy."
        )
        assert source_file.evaluate(
            "element => getComputedStyle(element).gridColumnEnd"
        ) == "auto"

        activate(page, '[data-room="choir"]')
        page.wait_for_url(f"{base_url}/.lost+found/00000000/archive/choir/")
        activate(page, "#listen")
        assert page.locator("#carrierHandoff").is_visible()
        assert_stacked_handoff(page, "#carrierHandoff")
        assert "history phase retained" in page.locator(
            "#carrierHandoffState"
        ).inner_text().lower()
        activate(page, "#carrierHandoff .handoff-record__action")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/archive/")
        assert "carrier retained" in page.locator(
            '[data-room="choir"] .file__state'
        ).inner_text().lower()

        activate(page, "#operationAction")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/archive/integrity/")
        for index in range(5):
            activate(page, f'[name="sector-{index}"]', "Space")
        activate(page, "#verify")
        assert any(
            flag in state(page)["flags"]
            for flag in ("checksum-match", "checksum-drift")
        )
        assert page.locator("#integrityHandoff").is_visible()
        assert_stacked_handoff(page, "#integrityHandoff")
        assert page.locator("#integrityReturn").is_hidden()
        activate(page, "#integrityHandoff .handoff-record__action")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/archive/")
        assert page.locator("#letterFile").is_hidden()

        activate(page, "#operationAction")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/archive/staff/")
        assert page.locator("#staffHandoff").is_visible()
        assert_stacked_handoff(page, "#staffHandoff")
        assert page.locator(".subject-row").count() == 1
        assert str(state(page)["id"]) in page.locator(
            "#staffHandoffResult"
        ).inner_text()
        activate(page, "#staffHandoff .handoff-record__action")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/archive/")
        assert page.locator("#letterFile").is_visible()
        activate(page, "#operationAction")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/dead-letter/")
        activate(page, "#operatorAddress")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/operator/")

        first_operator = state(page)
        old_trace = str(first_operator["id"])
        assert "operator-probe" in first_operator["flags"]
        activate(page, 'a[href="/privacy.txt"]')
        page.wait_for_url(f"{base_url}/privacy.txt")
        page.go_back(wait_until="networkidle")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/operator/")
        assert page.locator("#sideMarker").inner_text() == "0"
        assert page.locator("#operatorRecord").get_attribute("data-mode") is None
        activate(page, "#invite")
        invitation = page.locator("#invitation").inner_text()
        assert invitation.endswith(f"#witness={old_trace}")

        invited_context = browser.new_context(reduced_motion="reduce")
        invited_page = invited_context.new_page()
        watch_page(invited_page, allowed_netloc, browser_errors, external_requests)
        invited_page.goto(invitation, wait_until="networkidle")
        assert invited_page.url == f"{base_url}/.lost+found/00000000/"
        invited_state = state(invited_page)
        assert invited_state["witness"] == old_trace
        assert "invited" in invited_state["flags"]
        assert not any(
            flag.startswith("fragment-probe-") for flag in invited_state["flags"]
        )
        invited_context.close()

        activate(page, "#archiveReturn")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/extent/")
        activate(page, "#egress")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/operator/")
        occupied_state = state(page)
        assert "operator-occupied" in occupied_state["flags"]
        assert page.locator("#authorityReference").inner_text().lower() == "she"
        assert page.locator("#rootReturn").inner_text() == (
            "return retained response to recovery utility"
        )
        assert_within_viewport(page, "#rootReturn")
        page.go_back(wait_until="networkidle")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/extent/")
        page.go_forward(wait_until="networkidle")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/operator/")
        assert page.locator("#authorityReference").inner_text().lower() == "she"

        activate(page, "#rootReturn")
        page.wait_for_url(f"{base_url}/")
        page.evaluate(
            """() => {
                const value = JSON.parse(localStorage.getItem('orison_trace_v2'));
                value.flags = value.flags.filter((flag) => flag !== 'aperture-slip');
                localStorage.setItem('orison_trace_v2', JSON.stringify(value));
            }"""
        )
        page.reload(wait_until="networkidle")
        page.get_by_text("recovery state: INCOMPLETE", exact=True).wait_for()
        pending_response = page.get_by_role(
            "button", name="run: reconcile response 00000000"
        )
        assert pending_response.is_visible()
        assert page.locator("a.archive-path").count() == 0
        assert "quick-command--primary" in (
            pending_response.get_attribute("class") or ""
        )
        assert page.evaluate("document.activeElement.id") == "commandInput"
        page.keyboard.press("Tab")
        assert page.evaluate("document.activeElement.id") == "commandHint"
        page.keyboard.press("Shift+Tab")
        assert page.evaluate("document.activeElement.id") == "commandInput"
        page.locator("#commandInput").fill("unpack orison.zip")
        page.locator("#commandInput").press("Enter")
        repeated_unpack_response = page.get_by_role(
            "button", name="run: reconcile response 00000000"
        )
        repeated_unpack_response.wait_for()
        assert page.locator("a.archive-path").count() == 0
        assert "quick-command--primary" in (
            repeated_unpack_response.get_attribute("class") or ""
        )
        assert "response-attached" not in state(page)["flags"]
        activate(page, "#commandHint")
        wait_for_flag(page, "response-attached")
        recovered_directory = page.get_by_role(
            "button", name="open: recovered directory"
        )
        recovered_directory.wait_for()
        assert "quick-command--primary" not in (
            recovered_directory.get_attribute("class") or ""
        )
        assert page.locator("a.archive-path").get_attribute("href") == (
            "/.lost+found/00000000/archive/"
        )
        activate(page, "#commandHint")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/archive/")
        page.wait_for_timeout(1_100)
        assert "aperture-slip" not in state(page)["flags"]

        interlock = page.locator("#parentInterlock")
        release = page.locator("#releaseOrphan")
        assert interlock.is_visible()
        assert page.locator("#operationRegister").is_hidden()
        assert (
            page.locator(".directory").get_attribute("data-operation-active")
            is None
        )
        assert page.locator(".file.is-source").evaluate(
            "element => getComputedStyle(element).gridColumnEnd"
        ) == "auto"
        assert page.locator("#parentInterlock").evaluate(
            "element => element.parentElement.classList.contains('directory-intro')"
        )
        assert page.locator(".directory-list > .file").count() == 7
        assert page.locator(".directory-list > .parent-interlock").count() == 0
        assert page.locator(".directory-list > .fragment-entry").count() == 0
        assert page.locator(".directory-list .file__number").all_inner_texts() == [
            "06",
            "19",
            "32",
            "44",
            "71",
            "00",
            "--",
        ]
        assert interlock.get_attribute("data-state") == "ready"
        assert (
            page.locator(".directory").get_attribute("data-parent-active") == "true"
        )
        assert_within_viewport(page, "#releaseOrphan")
        release.focus()
        assert page.evaluate("document.activeElement.id") == "releaseOrphan"
        release.press("Enter")
        wait_for_flag(page, "orphan-released")
        assert interlock.get_attribute("data-state") == "complete"
        assert page.locator(".process-lane.is-parented").count() == 7
        assert page.locator('.file[data-parented="true"]').count() == 7
        assert "its parent changed" in page.locator(
            "#parentInterlockStatus"
        ).inner_text()
        assert page.locator("#fragmentIndex").is_visible()
        assert_within_viewport(page, "#fragmentIndex")
        assert "request detached child addresses" in page.locator(
            "#fragmentIndex"
        ).inner_text().lower()
        assert "orphan 00000000 / released" in page.locator(
            "#parentInterlockCopy"
        ).inner_text()

        page.reload(wait_until="networkidle")
        assert page.locator("#parentInterlock").get_attribute("data-state") == "complete"
        assert page.locator("#releaseOrphan").is_hidden()
        assert "parent is retained" in page.locator(
            "#parentInterlockStatus"
        ).inner_text()
        assert "orphan-released" in state(page)["flags"]
        activate(page, "#fragmentIndex")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/fragments/")
        assert page.locator("a.fragment-cell.is-gap").count() == 3
        first_gap = page.locator('[data-address="013"]')
        first_gap.focus()
        assert page.evaluate("document.activeElement.dataset.address") == "013"
        with page.expect_response(
            lambda response: (
                response.url == f"{base_url}/.lost+found/00000000/fragments/013/"
                and response.request.resource_type == "document"
            )
        ) as fragment_response_info:
            first_gap.press("Enter")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/fragments/013/")
        assert fragment_response_info.value.status == 404
        assert page.locator("#missingCode").inner_text() == "013"
        assert "fragment-probe-013" in state(page)["flags"]
        page.locator("#missingReturn").click()
        page.wait_for_url(f"{base_url}/.lost+found/00000000/fragments/")
        assert page.locator('[data-address="013"].is-trace').count() == 1
        assert page.locator('[data-displaced="013"].is-gap').count() == 1
        assert page.locator("a.fragment-cell.is-gap[href]").count() == 2
        assert "2 addresses remain actionable" in page.locator(
            "#fragmentInstruction"
        ).inner_text().lower()
        page.reload(wait_until="networkidle")
        assert page.locator('[data-address="013"].is-trace').count() == 1

        for address, remaining in (("027", 1), ("058", 0)):
            page.locator(f'[data-address="{address}"]').click()
            page.wait_for_url(
                f"{base_url}/.lost+found/00000000/fragments/{address}/"
            )
            assert page.locator("#missingCode").inner_text() == address
            assert f"fragment-probe-{address}" in state(page)["flags"]
            assert page.locator("#missingReturn").inner_text() == (
                "continue child sequence"
            )
            page.locator("#missingReturn").click()
            page.wait_for_url(f"{base_url}/.lost+found/00000000/fragments/")
            assert page.locator("a.fragment-cell.is-gap[href]").count() == remaining

        assert "all three" in page.locator("#fragmentTitle").inner_text().lower()
        assert "complete" in page.locator(
            "#fragmentInstruction"
        ).inner_text().lower()
        assert sum(
            flag.startswith("fragment-probe-") for flag in state(page)["flags"]
        ) == 3
        assert page.locator("#fragmentReturn").get_attribute("href") == "/"
        assert page.locator("#fragmentReturn").inner_text().lower() == (
            "return retained requests to recovery utility"
        )

        duplicate_response = page.goto(
            f"{base_url}/.lost+found/00000000/fragments/027/",
            wait_until="networkidle",
        )
        assert duplicate_response is not None and duplicate_response.status == 404
        assert "accepted / absence reassigned" in page.locator("#recorded").inner_text()
        assert sum(
            flag.startswith("fragment-probe-") for flag in state(page)["flags"]
        ) == 3
        assert len(
            json.dumps(state(page), separators=(",", ":")).encode("utf-8")
        ) <= 2_048
        page.locator("#missingReturn").click()
        page.wait_for_url(f"{base_url}/.lost+found/00000000/fragments/")
        page.set_viewport_size({"width": 375, "height": 812})
        page.reload(wait_until="networkidle")
        assert page.evaluate(
            "document.documentElement.scrollWidth <= window.innerWidth"
        )
        assert page.locator('[data-address="013"].is-trace').is_visible()
        assert page.locator('[data-address="027"].is-trace').is_visible()
        assert page.locator('[data-address="058"].is-trace').is_visible()
        page.set_viewport_size({"width": 1440, "height": 700})
        page.reload(wait_until="networkidle")
        assert_within_viewport(page, "#fragmentReturn")
        activate(page, "#fragmentReturn")
        page.wait_for_url(f"{base_url}/")
        assert page.locator(".terminal").get_attribute("aria-label") == (
            "ORISON recovery terminal with retained completed trace"
        )
        assert page.locator("#commandForm").is_hidden()
        assert page.locator("#commandHint").is_hidden()
        terminal_text = page.locator("#terminalOutput").inner_text()
        assert "requested addresses: 013 027 058 / RETAINED" in terminal_text
        assert "recovery queue: EMPTY" in terminal_text
        assert "missing regions: 014 028 059 / UNRESOLVED" in terminal_text
        assert "input channel: IDLE / no detached operation pending" in terminal_text
        assert page.locator("a.archive-path").count() == 0
        page.go_back(wait_until="networkidle")
        page.wait_for_url(f"{base_url}/.lost+found/00000000/fragments/")
        assert "all three" in page.locator("#fragmentTitle").inner_text().lower()
        activate(page, "#fragmentReturn")
        page.wait_for_url(f"{base_url}/")
        page.reload(wait_until="networkidle")
        assert page.locator(".terminal").get_attribute("aria-label") == (
            "ORISON recovery terminal with retained completed trace"
        )
        assert "no detached operation pending" in page.locator(
            "#terminalOutput"
        ).inner_text()

        sibling = context.new_page()
        watch_page(sibling, allowed_netloc, browser_errors, external_requests)
        sibling.goto(f"{base_url}/.lost+found/00000000/archive/", wait_until="networkidle")
        page.goto(f"{base_url}/erase/", wait_until="networkidle")
        activate(page, "#erase")
        page.wait_for_url(f"{base_url}/")
        sibling.wait_for_url(f"{base_url}/")
        assert state(page)["id"] != old_trace
        assert state(sibling)["id"] != old_trace
        assert "orphan-released" not in state(page)["flags"]
        assert "orphan-released" not in state(sibling)["flags"]
        assert "fragment-probe-013" not in state(page)["flags"]
        assert "fragment-probe-013" not in state(sibling)["flags"]

        context.close()
        browser.close()

    assert not browser_errors, "Browser errors:\n" + "\n".join(browser_errors)
    assert not external_requests, "External requests:\n" + "\n".join(external_requests)


def main() -> None:
    document_count = verify_references()
    handler = partial(QuietHandler, directory=str(ROOT))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base_url = f"http://127.0.0.1:{server.server_port}"
    try:
        verify_journey(base_url)
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)

    print(json.dumps({"documents": document_count, "journey": "pass", "status": "pass"}))


if __name__ == "__main__":
    main()
