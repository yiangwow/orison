# Review Request: Terminal bookend and custody hinge
- **Author**: Codex
- **Repository**: the private archive repository
- **Branch**: `redesign/terminal-bookend`
- **Base**: `fix/clickable-recovered-path` @ `853716f272b6e8354f27cbda753ebe5412383a56`
- **Implementation head**: `587aad8a60253c9d1f0c74e307726db2e6ef1c01`
- **PR**: private archive PR #45 (OPEN, stacked on PR 44)
- **Risk level**: 2
- **Scope**: Recompose the public desktop journey so occupied Operator remains the climax, Parent becomes a compact custody hinge, and cumulative fragment completion closes at a state-derived retained root terminal; do not add routes, durable state, a conventional ending, mobile work, infrastructure, or deployment changes.
- **Source of truth**: The owner required one coherent whole-site correction that preserves the sole first unpack and the causal sequence through Operator, Extent, reconciliation, ordered Archive, Parent, and cumulative `013`/`027`/`058`; establishes a real ending without “The End,” lore explanation, menu, progress UI, or a new route; preserves local-only state, complete erasure, meaningful native Back, ambiguity, systems language, and hidden-path fiction; and waits for explicit approval before implementation and delivery. The owner approved the recommended transformed-root bookend and subsequently authorized this formal review preparation.
- **Risk rationale**: This changes public desktop narrative hierarchy, navigation consequences, state-derived rendering, viewport composition, and motion timing. It does not change the public route set, storage schema, migration, backend, network/privacy boundary, deployment configuration, or infrastructure.

## Acceptance criteria

1. The first unpack remains the sole full unpack, reveals no later evidence
   early, and enters the recovered inode.
2. The forward causal sequence remains: evidence → unresolved Operator → Extent
   interruption → occupied Operator → explicit response reconciliation →
   ordered Archive → Parent custody → cumulative fixed fragment requests.
3. Extent returns directly to the same Operator endpoint and occupied Operator
   remains the only monumental visual climax.
4. Completed response reconciliation enters ordered Archive directly without
   repeating the already-completed inode visit.
5. Parent remains in Archive's left operational column as a compact actionable
   custody control and persistent receipt. Its release and fragment actions fit
   within the initial 1440×700 desktop viewport.
6. `013`, `027`, and `058` remain independently requestable and visibly
   retained in every order during one continuous forward run.
7. The all-three receipt returns forward to `/`, where existing flags derive a
   quiet retained terminal with no completion flag, new route, badge, or
   forward Archive loop. Native Back returns to the completed fragment receipt;
   reload and later revisit reproduce the retained terminal.
8. Staff and Archive use the same Weather/Integrity/order/revisit predicate and
   cannot report opposing pending/indexed states on a reachable path.
9. The one-time aperture manifestation is limited to the safe early
   Camera/Weather return, rechecks eligibility at fire time, and cannot overlap
   reconciliation, Parent, fragments, or a late operation.
10. Mono remains the causal/actionable voice, serif the interpretive voice, and
    narrow sans the institutional evidence voice. Green, bone, and red preserve
    their existing system/record/fault roles while record-title scale is
    bounded below Operator.
11. Pointer, keyboard, native Back/Forward, reload, interruption, reduced
    motion, migration, partial/completed revisit, fixed/generic 404 behavior,
    invitation isolation, record-size bounds, and cross-tab erasure continue to
    pass.
12. No analytics, external request, external asset, dependency, route, durable
    state field, flag, schema version, migration, backend, infrastructure,
    deployment, or mobile implementation is added.
13. ADR 0015 records the ending decision, consequences, and rollback; ADRs
    0004, 0012, 0013, and 0014 plus continuity documentation identify the
    amendment and current delivery state.

## What changed

- Root terminal and journey closure:
  - `index.html`
  - `.lost+found/00000000/fragments/index.html`
- Archive hierarchy, Parent, Staff consistency, and aperture timing:
  - `.lost+found/00000000/archive/index.html`
  - `.lost+found/00000000/archive/staff/index.html`
- Desktop scale and constrained-height hierarchy:
  - `.lost+found/00000000/operator/index.html`
  - `.lost+found/00000000/examination/index.html`
  - `.lost+found/00000000/archive/mirror/index.html`
  - `.lost+found/00000000/archive/weather/index.html`
  - `.lost+found/00000000/archive/choir/index.html`
- Journey/state/accessibility regression coverage:
  - `tests/verify.py`
- Architectural and continuity record:
  - `docs/adr/0015-close-the-current-run-at-the-recovery-terminal.md`
  - `docs/adr/0004-rare-deniable-embodiment.md`
  - `docs/adr/0012-canonical-operational-spine.md`
  - `docs/adr/0013-recompose-causal-and-record-planes.md`
  - `docs/adr/0014-cumulative-fixed-fragment-requests.md`
  - `VISION.md`
  - `ARCHITECTURE.md`
  - `docs/CURRENT_STATE.md`
  - `docs/EXPANSION_SESSIONS.md`
  - `ROADMAP.md`

Diff summary:

```text
20 files changed, 774 insertions(+), 146 deletions(-)
```

## How to verify

Run from a clean checkout of implementation head
`587aad8a60253c9d1f0c74e307726db2e6ef1c01`:

```sh
git diff --check 853716f272b6e8354f27cbda753ebe5412383a56..587aad8a60253c9d1f0c74e307726db2e6ef1c01
python3 deploy/verify_asset_versions.py
python3 tests/verify.py
```

Expected key output:

```text
{"documents": 15, "assets": {"base.css": "8d65c5a18cc9", "orison.js": "6cd727dafb4f"}, "status": "pass"}
{"documents": 15, "journey": "pass", "status": "pass"}
```

Review exactly:

```sh
git diff 853716f272b6e8354f27cbda753ebe5412383a56..587aad8a60253c9d1f0c74e307726db2e6ef1c01
git diff --name-status 853716f272b6e8354f27cbda753ebe5412383a56..587aad8a60253c9d1f0c74e307726db2e6ef1c01
```

For the constrained desktop risk, independently inspect at least occupied
Operator, Parent ready, Parent complete, all-three fragments, and retained root
at 1440×700, with reduced motion both enabled and disabled.

## Author verification evidence

1. **Tests pass locally**: `python3 tests/verify.py` exited 0 at the pinned
   implementation head with
   `{"documents": 15, "journey": "pass", "status": "pass"}`.
2. **Build/lint clean**: this static site has no separate build/lint command.
   `python3 deploy/verify_asset_versions.py` exited 0 for 15 documents with
   status `pass`; `git diff --check` exited 0.
3. **Clean status**: `git status --porcelain=v1` emitted no output in the
   dedicated pre-request worktree before this request was written.
4. **Author diff review**: reviewed
   `853716f272b6e8354f27cbda753ebe5412383a56..587aad8a60253c9d1f0c74e307726db2e6ef1c01`
   end to end, including runtime, tests, ADR amendments, and delivery-state
   documentation.
5. **Scope isolation**: the 20-file range contains the single approved desktop
   coherence correction plus its regression coverage and architectural record.
   The clickable-path fix is isolated in the base commit and excluded from this
   range. No shared asset, deployment, server, infrastructure, or mobile file is
   changed.
6. **Authorship**: both commits in the range report
   the owner's git identity and contain no `Co-Authored-By` trailer.
7. **Architecture documentation**: ADR 0015 was added with Date, Status,
   Context, Decision, and Consequences; ADRs 0004 and 0012–0014 identify the
   amendment; VISION, ARCHITECTURE, CURRENT_STATE, EXPANSION_SESSIONS, and
   ROADMAP were updated.
8. **Desktop visual evidence**: 21 local captures covered seven late-flow
   surfaces at 2560×1319, 1440×1000, and 1440×700. All required action targets
   were within the viewport; no horizontal overflow, browser error, or
   off-origin request was observed. The repository journey independently
   asserts the critical 1440×700 actions.
9. **Independent informal critique**: before this formal cycle, Claude found a
   reachable Staff/Archive mismatch and an under-documented endpoint decision.
   Both were corrected and regression-covered; a second informal pass reported
   no new findings. This is context only and is not formal approval.

## Known limitations / open questions

- GitHub reports no configured CI checks for the stacked base branch; the
  repository-native checks above are the executable evidence.
- The PR is stacked on PR 44. Review this pinned range against its exact base
  SHA, not the moving branch tip.
- Mobile implementation and full mobile replay are explicitly outside scope.
- No server, container, deployment, public-cache, or infrastructure mutation
  was made or validated as part of this local review request.
- Visual screenshots are local evidence and are not committed artifacts; the
  reviewer should independently inspect the constrained late-flow surfaces.
- Completed root intentionally has no forward Archive link. ADR 0015 sanctions
  that non-circular endpoint; native Back retains the completion receipt during
  the finishing history, while a later direct revisit remains quiet.
- Behavioral rollback restores the prior fragment-to-Archive link, root
  presentation, Parent scale, aperture timing, Staff eligibility, and handoff
  destinations. Existing local state remains valid; no schema, migration, or
  infrastructure rollback is required.
