# Review: Mobile aperture containment
- **Reviewer**: Claude
- **Verdict**: APPROVE

## Verification performed

Reviewed exactly `080bfaaa601afccb6427bfa494f938ef40d2da09..bf8c2b0c4cc912f53d3151a16eb5bd70f8614e3e` (base → implementation head), per REQUEST.md. The PR base branch has advanced only through cycle-005 artifacts; the pinned base — not the moving branch tip — was used as the review base.

- `git fetch origin` — exit 0.
- `git rev-parse --verify 080bfaaa601afccb6427bfa494f938ef40d2da09^{commit}` and `...bf8c2b0c4cc912f53d3151a16eb5bd70f8614e3e^{commit}` — both exist. `git merge-base` confirms `080bfaaa…` is the merge base and `git rev-parse bf8c2b0…^` confirms it is the exact parent of the implementation head.
- `gh pr view 48 --json number,state,isDraft,baseRefName,headRefName,commits,files` — OPEN, not draft, `docs/stabilization-housekeeping` ← `fix/mobile-aperture-containment`, exactly two commits: implementation `bf8c2b0c4cc912f53d3151a16eb5bd70f8614e3e` and request `69f0f489a02c14bd8f1832d849c06d2e014be077`.
- `git diff --name-only bf8c2b0…..69f0f48…` — only `.peer-review/006-mobile-aperture-containment/REQUEST.md`; no implementation commits after the reviewed head.
- `git diff --check 080bfaa…..bf8c2b0…` — exit 0, no output.
- `git diff --name-status 080bfaa…..bf8c2b0…` — exactly `.lost+found/00000000/archive/index.html`, `docs/CURRENT_STATE.md`, `tests/verify.py` (3 files, 98 insertions, 1 deletion). `assets/` untouched.
- `python3 -m py_compile tests/verify.py` — exit 0.
- `node --check assets/orison.js` — exit 0.
- `python3 deploy/verify_asset_versions.py` — exit 0; `{"documents": 15, "assets": {"base.css": "8d65c5a18cc9", "orison.js": "6cd727dafb4f"}, "status": "pass"}`.
- `python3 tests/verify.py` — full repository browser journey run by me; exit 0; `{"documents": 15, "journey": "pass", "status": "pass"}`, which includes the three new aperture containment contexts and asserts zero browser errors and zero off-origin requests across state, migration, erasure, Back/Forward, keyboard, fragment, and retained-terminal paths.
- `git show -s --format='%H%n%an <%ae>%n%B' bf8c2b0…` — the owner's git identity, message `fix: contain mobile aperture`, no Co-Authored-By trailer.

Independent assessment of the change and test design (read, not just re-run):

- **Narrow-layout-only CSS**: the single changed declaration (`right: -0.8rem` → `right: 0`) sits at `.lost+found/00000000/archive/index.html:885`, inside the `@media (max-width: 720px)` block spanning lines 833–905. The desktop default `.aperture-slip` rule (line 623, `right: clamp(0.25rem, 1.5vw, 1.25rem)`) is unchanged, and no `.aperture-slip` rule exists in the `min-width: 721px` media block.
- **Visual-viewport assertion** (`tests/verify.py:145`): compares `max(documentElement.scrollWidth, body.scrollWidth)` against `window.visualViewport.width` (with a `clientWidth` fallback), which directly measures the horizontal-expansion failure mode.
- **One-pixel tolerance**: I ran a negative control in a throwaway copy under `/tmp` (repo untouched): with `-0.8rem` restored at 375×812, the assertion fails with `documentWidth: 388, visualWidth: 375` — a 13px overflow that the +1 tolerance cannot mask. A positive control on the fixed CSS measured `documentWidth: 375, visualWidth: 375` (delta 0), so the tolerance is pure rounding headroom, not a concealed defect.
- **Visible/hidden synchronization**: the test anchors on the durable `aperture-slip` state flag (`wait_for_flag`, set inside `revealApertureSlip` at line 1194 of the archive document) plus Playwright `visible`/`hidden` element states — not a fixed delay. The hide timer (680ms normal / 1150ms reduced motion, line 1199) fits the 3s hidden-wait cap. `assets/base.css:81` (`[hidden] { display: none !important; }`) guarantees the hidden phase genuinely removes the element from layout. The seeded state (`forecast` set, `aperture-slip` absent, `seen.archive` reaching 2 on the test's archive visit, previous route `mirror`) satisfies the eligibility gate at lines 1980–1990.
- **Motion coverage**: 375×812 and 390×844 under `no-preference` and 390×640 under `reduce`, each in a fresh mobile context with touch, matching acceptance criteria.
- **docs/CURRENT_STATE.md**: records the correction, validation, unchanged contracts, and Chromium-only/keyboard/privacy.txt limitations, and explicitly states the branch is not yet reviewed, merged, or deployed.

Recheck immediately before writing this review: `git fetch origin`; `git rev-parse origin/fix/mobile-aperture-containment` → `69f0f489a02c14bd8f1832d849c06d2e014be077` with parent `bf8c2b0c4cc912f53d3151a16eb5bd70f8614e3e`; `gh pr view 48` → `{"head": "69f0f489a02c14bd8f1832d849c06d2e014be077", "state": "OPEN"}`. The pinned implementation head is unchanged and remains the branch tip minus only the REQUEST.md commit.

## Findings

None. All eight acceptance criteria verified; no BLOCKER, MAJOR, MINOR, or NIT findings. This is a verified empty list, not a skim: every REQUEST.md verification command was re-run by me with matching output, the diff was read end to end, and the regression's ability to detect the original defect was demonstrated with a negative control.

## What I did NOT check

- Firefox and WebKit engines — only Chromium (via the repository's Playwright suite) was exercised; browser binaries for other engines are not installed and I did not mutate the environment.
- Physical mobile devices, real OS virtual keyboards, and Safari address-bar/safe-area behavior — only Chromium mobile emulation was used.
- The author's production-image replay claims (116 mobile states, 31 focus audits, nginx/container delivery checks) — the image and container were removed before handoff; I verified only repository-native evidence.
- Viewport widths between 391px and 720px inside the media query other than those the suite covers; containment at the three specified viewports plus the suite's desktop checks is what I executed.
- `privacy.txt` mobile presentation — explicitly out of scope in REQUEST.md.
- Cycle-005 peer-review artifacts on the advanced base branch — outside the pinned review range by design.
