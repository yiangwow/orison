# Review Request: Mobile aperture containment
- **Author**: Codex
- **Repository**: the private archive repository
- **Branch**: fix/mobile-aperture-containment
- **Base**: docs/stabilization-housekeeping @ 080bfaaa601afccb6427bfa494f938ef40d2da09
- **Implementation head**: bf8c2b0c4cc912f53d3151a16eb5bd70f8614e3e
- **PR**: private archive PR #48 (OPEN; stacked on PR 47)
- **Risk level**: 1
- **Scope**: Keep the transient Archive aperture inside narrow visual viewports and add focused regression coverage; do not alter desktop composition, route/state contracts, shared assets, privacy, or delivery behavior.
- **Source of truth**: Approved user recommendation after a complete mobile assurance pass: change the mobile Archive aperture offset from `right: -0.8rem` to `right: 0`, assert containment during the visible aperture and after it hides under normal and reduced motion, and preserve all existing state, privacy, Back, keyboard/touch, migration, erasure, asset, and desktop contracts.
- **Risk rationale**: One CSS declaration changes inside the existing `max-width: 720px` media query, with a Python browser regression and continuity record. There is no public API, schema, state, route, asset, dependency, backend, security, deployment, or infrastructure change.

## Acceptance criteria

1. At widths covered by the existing `max-width: 720px` rule, `.aperture-slip` uses `right: 0` instead of the viewport-expanding negative offset.
2. Repository-native browser coverage checks document containment against `window.visualViewport.width` while the aperture is visible and after it is hidden at 375×812 and 390×844 with normal motion and at 390×640 with reduced motion.
3. The containment regression is anchored to the durable `aperture-slip` state flag and actual visible/hidden element states rather than a fixed-delay-only assertion.
4. The complete repository journey still passes with no browser errors or off-origin requests, including state, migration, erasure, Back/Forward, keyboard, fragment, and retained-terminal paths.
5. Desktop aperture positioning remains governed by the unchanged default rule; no desktop composition changes.
6. No route, state field, schema, migration, privacy, erasure, native Back, keyboard, touch, dependency, backend, asset, or infrastructure behavior changes.
7. Shared `base.css` and `orison.js` bytes and their content-addressed references remain unchanged.
8. `docs/CURRENT_STATE.md` accurately records the implementation, validation, unchanged contracts, and known browser/keyboard/privacy limitations without claiming merge or deployment.

## What changed

- `.lost+found/00000000/archive/index.html`
  - changes the aperture's narrow-layout right offset from `-0.8rem` to `0`.
- `tests/verify.py`
  - adds a visual-viewport containment assertion;
  - covers the visible and hidden aperture phases at three mobile viewport/motion combinations.
- `docs/CURRENT_STATE.md`
  - records the approved local correction, completed validation, unchanged contracts, and remaining direct-test limitations.

## How to verify

1. `rtk git diff --check 080bfaaa601afccb6427bfa494f938ef40d2da09..bf8c2b0c4cc912f53d3151a16eb5bd70f8614e3e`
   - Expected: exit 0 with no output.
2. `rtk python3 -m py_compile tests/verify.py`
   - Expected: exit 0 with no output.
3. `rtk node --check assets/orison.js`
   - Expected: exit 0 with no output.
4. `rtk python3 deploy/verify_asset_versions.py`
   - Expected: JSON status `pass`, 15 documents, `base.css` hash `8d65c5a18cc9`, and `orison.js` hash `6cd727dafb4f`.
5. `rtk python3 tests/verify.py`
   - Expected: `{"documents": 15, "journey": "pass", "status": "pass"}`.
6. `rtk git diff --name-status 080bfaaa601afccb6427bfa494f938ef40d2da09..bf8c2b0c4cc912f53d3151a16eb5bd70f8614e3e`
   - Expected: exactly the Archive document, `docs/CURRENT_STATE.md`, and `tests/verify.py`.
7. `rtk gh pr view 48 --json state,baseRefName,headRefName,commits,files,statusCheckRollup,url`
   - Expected: OPEN, `docs/stabilization-housekeeping` ← `fix/mobile-aperture-containment`, implementation commit `bf8c2b0c4cc912f53d3151a16eb5bd70f8614e3e`, exactly three implementation files before this request, and no configured checks.

## Author verification evidence

1. Tests pass locally:
   - `rtk python3 tests/verify.py`
   - Exit 0; `{"documents": 15, "journey": "pass", "status": "pass"}`.
2. Build/lint clean:
   - `rtk git diff --check 080bfaaa601afccb6427bfa494f938ef40d2da09..bf8c2b0c4cc912f53d3151a16eb5bd70f8614e3e`
   - Exit 0; no output.
   - `rtk python3 -m py_compile tests/verify.py`
   - Exit 0; no output.
   - `rtk node --check assets/orison.js`
   - Exit 0; no output.
   - `rtk python3 deploy/verify_asset_versions.py`
   - Exit 0; 15 documents; `base.css` `8d65c5a18cc9`; `orison.js` `6cd727dafb4f`; status `pass`.
3. Worktree clean:
   - `rtk git status --short --branch`
   - Exit 0 before this request; `## fix/mobile-aperture-containment...origin/fix/mobile-aperture-containment` with no changed or untracked files.
   - `rtk git diff --exit-code HEAD..origin/fix/mobile-aperture-containment`
   - Exit 0; no output.
4. Diff reviewed end to end:
   - `rtk git diff --no-ext-diff 080bfaaa601afccb6427bfa494f938ef40d2da09..bf8c2b0c4cc912f53d3151a16eb5bd70f8614e3e`
   - Exit 0; 3 files changed, 98 insertions, 1 deletion.
5. Diff contains only stated scope:
   - `rtk git diff --name-status 080bfaaa601afccb6427bfa494f938ef40d2da09..bf8c2b0c4cc912f53d3151a16eb5bd70f8614e3e`
   - Exit 0; only `.lost+found/00000000/archive/index.html`, `docs/CURRENT_STATE.md`, and `tests/verify.py`.
   - `rtk git diff --name-only 080bfaaa601afccb6427bfa494f938ef40d2da09..bf8c2b0c4cc912f53d3151a16eb5bd70f8614e3e -- assets`
   - Exit 0; no output.
6. Commit authorship:
   - `rtk git show -s --format='%H%n%an <%ae>%n%B' bf8c2b0c4cc912f53d3151a16eb5bd70f8614e3e`
   - Exit 0; the owner's git identity; message `fix: contain mobile aperture`; no `Co-Authored-By` trailer.
7. CLAUDE.md / AGENTS.md / ADR:
   - N/A. The correction changes no architecture, state contract, service, port, asset contract, privacy boundary, or accepted decision.
8. PR state:
   - `rtk gh pr view 48 --json number,state,isDraft,baseRefName,headRefName,commits,files,statusCheckRollup,url`
   - Exit 0; PR 48 is OPEN and not a draft, stacked on the housekeeping branch, with the pinned implementation commit, exactly three implementation files, and no configured checks.
9. Additional assurance completed before formal handoff:
   - Production-image mobile replay: 116 measured states and 31 focus audits across three complete mobile journeys plus returning, migrated, interrupted, reduced-motion, Back/Forward, fragment, retained-terminal, and cross-tab erasure contexts; zero browser errors, off-origin requests, or horizontal-overflow states.
   - Production-image desktop validation: complete 1440×700 journey plus focused 1440×1000 and 2560×1319 Archive checks.
   - Delivery checks: `nginx -t` passed; isolated container reached healthy with zero restarts; root and Archive returned 200; fixed fragment `013` and a generic missing route returned 404; restrictive headers remained present; image root bytes matched source.
   - The isolated test container and image were removed afterward; production infrastructure was not modified.

## Known limitations / open questions

- Mobile Chromium is directly verified. Firefox and WebKit browser binaries were not installed, and the environment was not mutated to add them.
- A physical mobile OS virtual keyboard and Safari address-bar/safe-area behavior were not directly tested. Chromium viewport resizing, touch, keyboard focus, and visual-viewport behavior were covered.
- Chromium may report a one-pixel visual/layout viewport rounding difference during the aperture. The regression permits only that single-pixel tolerance; the previous defect expanded the document by approximately 13–14 pixels.
- `privacy.txt` retains browser-native plain-text mobile presentation. Changing its MIME/delivery contract is outside this correction.
- PR 47's branch has advanced past the pinned base SHA only through cycle-005 peer-review artifacts. `080bfaaa601afccb6427bfa494f938ef40d2da09` is the exact parent and merge base of this implementation; cycle-005 artifacts are outside this review range.
- GitHub reports no configured CI checks for the stacked branch.
