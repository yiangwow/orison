# Review: Terminal bookend and custody hinge
- **Reviewer**: Claude
- **Verdict**: APPROVE

## Verification performed

All checks were run against the pinned range `853716f272b6e8354f27cbda753ebe5412383a56..587aad8a60253c9d1f0c74e307726db2e6ef1c01`, not the branch tip.

- `git cat-file -t` on both `853716f272b6e8354f27cbda753ebe5412383a56` and `587aad8a60253c9d1f0c74e307726db2e6ef1c01` → `commit` for each; both SHAs exist.
- `gh pr view 45 --repo <private-archive>` → `state: OPEN`, head `redesign/terminal-bookend`, base `fix/clickable-recovered-path`, not draft. `gh pr view 44` → `OPEN` (`fix/clickable-recovered-path` → `main`). The base branch tip moved to `df84c8e` after the pinned base, but `git log 853716f..df84c8e` shows only `.peer-review/` commits for cycle 002; `git merge-base --is-ancestor` confirms `853716f` is an ancestor. Review was held to the exact pinned base per REQUEST.md.
- `git log --format='%an <%ae>%n%(trailers)' 853716f...587aad8` → both range commits (`587aad8`, `0caa4af`) authored by the owner's git identity, no trailers.
- Created a dedicated worktree detached at `587aad8a60253c9d1f0c74e307726db2e6ef1c01` (`git status --porcelain` empty) and ran the Level 2 verification there:
  - `git diff --check 853716f..587aad8` → exit 0, no output.
  - `python3 deploy/verify_asset_versions.py` → exit 0, `{"documents": 15, "assets": {"base.css": "8d65c5a18cc9", "orison.js": "6cd727dafb4f"}, "status": "pass"}`.
  - `python3 tests/verify.py` → exit 0, `{"documents": 15, "journey": "pass", "status": "pass"}` (includes the new staff-gate context, all six fragment permutations, the 1440×700 main journey with `assert_within_viewport` on `#rootReturn`, `#releaseOrphan`, `#fragmentIndex`, `#fragmentReturn`, the retained-terminal render, native Back to the completed fragment receipt, reload reproduction, and aperture non-refire after reconciliation).
- `git diff` and `git diff --name-status` over the exact range read end to end: 20 files, 774 insertions, 146 deletions, matching REQUEST.md. Runtime changes are confined to `index.html`, seven `.lost+found` documents, and `tests/verify.py`; no new route, flag write beyond existing derived flags, schema, asset, or dependency is introduced (`renderCompletedTerminal` derives entirely from `response-attached`, `orphan-released`, and the three `fragment-probe-*` flags).
- Traced the code paths behind the risky claims at head: `addArchiveObjectLine()` reassigns `warningNode` before `renderCompletedTerminal` dereferences it (`index.html:593–611` vs the completed-terminal block); `#letterFile` visibility keeps the `ORISON.hasFlag(state, "letter")` escape hatch (`archive/index.html:1918–1926`), so grandfathered traces that already earned the letter are not hidden by the stricter `staffSourceVisible` predicate; `revealApertureSlip` rechecks `apertureWindowOpen(ORISON.read())` at fire time and the window excludes `operator-probe`, `operator-occupied`, `response-attached`, and `orphan-released`.
- Independent visual inspection at 1440×700 (Chromium via Playwright against a local static server at the pinned head, reduced motion both `reduce` and `no-preference`, ten renders total) of: occupied Operator, Parent ready, Parent complete, all-three fragments, and the retained root terminal. Every required action target (`#rootReturn`, `#archiveReturn`, `#releaseOrphan`, `#fragmentIndex`, `#fragmentReturn`, `.terminal`) was fully within the viewport; horizontal overflow was 0 px in all ten renders. Screenshots confirm Operator keeps the sole monumental single-glyph climax, Parent renders as a compact left-column custody control/receipt, the all-three footer reads "return retained requests to recovery utility", and the retained root shows the specified RECOVERED/RECONCILED/RETAINED/EMPTY/UNRESOLVED lines with no command form, no quick action, no archive-path link, and neutral processing/erasure utilities.
- Immediately before producing this review: `git fetch origin` then `git rev-parse origin/redesign/terminal-bookend` → `839e42d9c956f086ba5337ef4c65d81c46f43c2a`, whose only delta from `587aad8a60253c9d1f0c74e307726db2e6ef1c01` is `.peer-review/003-terminal-bookend/REQUEST.md`; PR 45 still `OPEN`. The pinned implementation head is unchanged and remains the reviewed head.

## Findings

### [MINOR-1] Consistency-critical Staff predicate exists as two verbatim copies
- File: .lost+found/00000000/archive/index.html:1711 and .lost+found/00000000/archive/staff/index.html:197
- Problem: `staffSourceVisible` (with its `weatherResolved`/`integrityResolved` helpers) is duplicated character-for-character in the Archive and Staff documents. Acceptance criterion 8 exists precisely because these two surfaces previously disagreed; the guarantee now rests on textual duplication rather than a shared definition.
- Evidence: `grep -n staffSourceVisible` at head matches both files with identical bodies; no shared helper exists in `orison.js`.
- Failure scenario: a future edit adjusts the predicate in one document only (e.g., changes the `seen.staff > 1` threshold in Archive), and a reachable trace again shows "source indexed" on one surface and "source pending" on the other — the exact bug class this change fixes. Today the copies match and `tests/verify.py` pins both surfaces, so impact is deferred, and keeping the predicate out of the content-addressed shared asset was plausibly a deliberate scope choice for this cycle.
- Suggestion: fold the predicate into `orison.js` (accepting the asset-hash bump) in a follow-up cycle, or add a comment in each copy naming the other.

### [NIT-1] `data-parent-active` is written but consumed only by tests
- File: .lost+found/00000000/archive/index.html:1600
- Problem: `directory.dataset.parentActive` is set/deleted, but no stylesheet or script selector references `data-parent-active`; only `tests/verify.py` asserts it. Harmless test hook, but it reads like a styling hook that was never wired.

### [NIT-2] Dead `data-state` reset on the root terminal
- File: index.html:727
- Problem: `boot()` calls `terminal.removeAttribute("data-state")`, but nothing ever sets `data-state` on `.terminal` — `renderCompletedTerminal` distinguishes itself via `aria-label` and text only. The removal is dead defensive code from an apparent earlier iteration.

## What I did NOT check

- Mobile and narrow viewports (explicitly out of scope in REQUEST.md); the `max-width: 720px`/`640px` media paths were not exercised.
- Any browser engine other than Chromium; `tests/verify.py` and my visual inspection both use Playwright Chromium only. Firefox/WebKit rendering, bfcache, and reduced-motion behavior are unverified.
- Actual audio output of the Web Audio warning/carrier paths (only their non-erroring execution via the test run).
- The stacked base range (`main..853716f`, PR 44) — reviewed in cycle 002, outside this pinned range.
- Production deployment, nginx/Cloudflare behavior, public-cache state, and parity with served source `3a9bfa2` — no server or infrastructure claim was validated.
- Screen-reader output beyond the presence/values of `aria-label`, roles, and the polite status element; no assistive-technology run was performed.
- Exhaustive legacy-trace matrix: I verified the grandfathered `letter`-flag path by code inspection and relied on `tests/verify.py`'s migration coverage; I did not hand-construct additional v1/partial-v2 permutations beyond those the suite and my five seeded states cover.
- The 21 author screenshots at 2560×1319 and 1440×1000 (uncommitted local evidence); my independent inspection covered only the required 1440×700 states.
