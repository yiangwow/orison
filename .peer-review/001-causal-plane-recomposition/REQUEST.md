# Review Request: Recompose ORISON causal journey
- **Author**: Codex
- **Repository**: the private archive repository
- **Branch**: feat/causal-plane-recomposition
- **Base**: main @ efabb5ce437989a5f57050e13084538808f8607c
- **Implementation head**: 4f5976fd881620afa4fe0d0ac4c0de9b094c1025
- **PR**: private archive PR #41 (OPEN)
- **Risk level**: 3
- **Scope**: Recompose the existing desktop journey into one causal system/record rhythm, including cumulative fixed-fragment requests, without adding routes, changing the v2 state schema, implementing mobile, or changing infrastructure/deployment.
- **Source of truth**: The owner's 2026-07-22 request requires one bounded whole-site structural correction: a consequential sole first unpack; an earned, distinct late response reconciliation; Operator -> Extent -> the same transformed Operator; an Archive split between operations and ordered recovered records; cumulative 013/027/058 requests; and a shared black/green/bone/fault-red role palette while preserving local-only state, erasure, Back, keyboard, reduced motion, ambiguity, and hidden-path fiction.
- **Risk rationale**: The patch changes public visitor behavior and the meaning of persisted journey-state combinations, including the response-attachment and fixed-fragment completion contracts. It retains the v2 schema but is conservatively Level 3 because those state and delivery guarantees are externally observable.

## Acceptance criteria
1. A fresh root exposes one mechanically dense unpack whose completion alone writes `unpacked`; it does not reveal future-derived evidence.
2. The late root never repeats `unpack orison.zip`; eligible traces expose an explicit reconciliation operation that writes `response-attached` only after the operation completes, while interrupted operations and valid existing v2 traces remain coherent.
3. The unresolved Operator leads to Extent, Extent returns directly to the same Operator endpoint, and that endpoint is visibly transformed; Archive is not inserted between Extent and the return.
4. Archive's left column contains current interpretation and operations (Parent plus fragment continuation), while its right column contains only Camera/Mirror, Weather, Integrity, Carrier, Staff, Letter, and Operator in stable order.
5. Fragment requests 013, 027, and 058 are independently actionable and retained; all six request orders work without browser Back, duplicates are idempotent, and finality appears only after all three are retained.
6. Existing v2 state, migration, complete erasure, privacy, reload/revisit, native Back, keyboard operation, and reduced-motion behavior remain valid.
7. The shared palette uses near-black as foundation, luminous green for primary/system activity, bone for records/interpretation, and red only for faults, absence, or unresolved work, without flattening route-specific composition.
8. No new route, state key/schema version, generated asset, backend, infrastructure, deployment, global navigation, quest UI, lore exposition, or mobile implementation is introduced.
9. Rollback is the normal PR-level revert of `efabb5ce437989a5f57050e13084538808f8607c..4f5976fd881620afa4fe0d0ac4c0de9b094c1025`; because the schema version is unchanged and all old flags remain readable, rollback requires no data migration.

## What changed
- Reworked `index.html` so the sole first unpack carries the archive-recovery payoff and late eligible traces explicitly run `reconcile response 00000000`.
- Corrected `.lost+found/00000000/operator/index.html` and `.lost+found/00000000/extent/index.html` to form the direct interruption-and-return beat.
- Reorganized `.lost+found/00000000/archive/index.html`, `.lost+found/00000000/fragments/index.html`, and `404.html` around stable records, current operations, and cumulative fragment receipts.
- Harmonized `assets/base.css` and route-local styles across the root, recovered records, Extent, Operator, Archive, fragments, and intentional 404 surfaces; updated all 15 content-addressed CSS references.
- Expanded `tests/verify.py` for fresh, interrupted, replayed, migrated, erased, keyboard, Back/forward, reduced-motion, Parent, and all fragment-order paths.
- Added `docs/adr/0013-recompose-causal-and-record-planes.md` and `docs/adr/0014-cumulative-fixed-fragment-requests.md`; marked the conflicting portions of ADRs 0008, 0009, 0011, and 0012 as superseded or amended.
- Updated `VISION.md`, `ARCHITECTURE.md`, `ROADMAP.md`, `docs/CURRENT_STATE.md`, `docs/EXPANSION_SESSIONS.md`, `docs/LOCAL_TRACE_AUDIT.md`, and `docs/APPARENT_TRANSFER_LOG.md`.
- The complete diff contains 30 files, 775 insertions, and 439 deletions; no infrastructure or deployment file changed.

## How to verify
1. `python3 tests/verify.py` — expect `{"documents": 15, "journey": "pass", "status": "pass"}` and exit 0.
2. `python3 deploy/verify_asset_versions.py` — expect 15 documents, `base.css` hash `8d65c5a18cc9`, `orison.js` hash `6cd727dafb4f`, status `pass`, and exit 0.
3. `python3 -m py_compile tests/verify.py` — expect no output and exit 0.
4. `git diff --check efabb5ce437989a5f57050e13084538808f8607c..4f5976fd881620afa4fe0d0ac4c0de9b094c1025` — expect no output and exit 0.
5. Inspect exactly `efabb5ce437989a5f57050e13084538808f8607c..4f5976fd881620afa4fe0d0ac4c0de9b094c1025`, with particular attention to when `unpacked` and `response-attached` are written; legacy valid-v2 replay; Operator/Extent history semantics; Archive DOM hierarchy; fragment idempotence/finality; strict CSP compatibility; and documentation/ADR consistency.
6. If Docker and Playwright are available, serve the production image and replay the desktop journey under its strict CSP; do not use or mutate the deployed server.

## Author verification evidence
1. Tests: `python3 tests/verify.py` exited 0 with `{"documents": 15, "journey": "pass", "status": "pass"}`.
2. Build/lint equivalents: `python3 deploy/verify_asset_versions.py` exited 0 with 15 documents, CSS `8d65c5a18cc9`, JS `6cd727dafb4f`, and status `pass`; `python3 -m py_compile tests/verify.py` exited 0; `git diff --check origin/main...HEAD` exited 0 with no output. This static site defines no separate build or linter command.
3. Worktree: `git status --short --branch` showed the feature branch tracking its remote and only the pre-existing, explicitly preserved out-of-scope `?? .serena/`; every in-scope file is committed.
4. Author review: reviewed the full base-to-head diff and its 30-file stat end to end, including state write timing, route transitions, all six fragment orders, CSS asset references, tests, ADR supersession, and current-state wording.
5. Scope: `git diff --stat origin/main...HEAD` reports only the 30 stated site, test, ADR, and documentation files; no server, deployment, container, or mobile-specific implementation changed.
6. Authorship: `git log origin/main..HEAD` shows both commits authored by the owner's git identity; no `Co-Authored-By` trailer is present.
7. Architecture records: ADRs 0013 and 0014 were added, affected ADRs were annotated, and the architecture/current-state/roadmap/trace documentation was updated.
8. Delivery: GitHub reports PR #41 open, head `4f5976fd881620afa4fe0d0ac4c0de9b094c1025`, base `efabb5ce437989a5f57050e13084538808f8607c`, mergeable `true`, and merge state `clean`. `gh pr checks 41` reports that no checks are configured.
9. Additional author verification before the request included a production-image build and strict-CSP desktop replay with a healthy zero-restart temporary container, plus visual inspection at 1440x1000, 2560x1319, and 960x900. Temporary validation artifacts were removed; production was not changed.

## Known limitations / open questions
- GitHub has no configured checks for this repository, so peer verification is the required independent gate.
- Mobile remains explicitly deferred and is not an approval criterion for this cycle.
- The production deployment remains on the prior release; merge and deployment require separate the owner authorization after review.
- The repository worktree contains the pre-existing untracked `.serena/`, which is outside this change and must remain preserved. The Claude invocation will use a dedicated clean detached worktree.
