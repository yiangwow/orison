# Review Request: Clickable recovered path
- **Author**: Codex
- **Repository**: the private archive repository
- **Branch**: `fix/clickable-recovered-path`
- **Base**: `main` @ `b5a57cc36aee0cfb461426e38164ec33ba0ccd2c`
- **Implementation head**: `853716f272b6e8354f27cbda753ebe5412383a56`
- **PR**: private archive PR #44 (OPEN)
- **Risk level**: 1
- **Scope**: Make the opening terminal's displayed recovered URL a native same-origin anchor and test pointer, keyboard, and native Back behavior; do not change routes, state, narrative order, infrastructure, deployment, or mobile behavior.
- **Source of truth**: The owner's requirement: “The opening terminal’s displayed recovered URL [must become] a real same-origin anchor. `tests/verify.py` adds pointer and keyboard activation coverage. Preserve this work; do not discard or absorb it into an unrelated redesign.”
- **Risk rationale**: This changes an existing navigation affordance but retains the same recovered-inode destination and has no API, state-schema, migration, storage, privacy, or infrastructure impact.

## Acceptance criteria

1. The recovered path emitted after the sole unpack is an `<a>` with same-origin
   `href="/.lost+found/00000000/"`, not inert text.
2. Pointer activation navigates to the recovered inode.
3. Keyboard Enter activation navigates to the recovered inode.
4. Native Back after keyboard activation returns to the terminal without
   corrupting the completed `unpacked` state.
5. The quick-command affordance and all existing routes remain available; no
   route, durable flag, schema version, migration, request, or external
   dependency is added.
6. The complete repository journey and static reference/asset checks pass.
7. The terminal-bookend redesign in PR 45 is not part of this review range.

## What changed

- `index.html`
  - changes the recovered-path element from a paragraph to an anchor;
  - assigns the existing recovered-inode path as its `href`.
- `tests/verify.py`
  - exercises keyboard activation and native Back in the interruption context;
  - exercises pointer activation in the canonical first-time journey;
  - asserts the exact same-origin path.

Diff summary:

```text
index.html       |  3 ++-
tests/verify.py  | 11 ++++++++++-
2 files changed, 12 insertions(+), 2 deletions(-)
```

## How to verify

Run from a clean checkout of implementation head
`853716f272b6e8354f27cbda753ebe5412383a56`:

```sh
git diff --check b5a57cc36aee0cfb461426e38164ec33ba0ccd2c..853716f272b6e8354f27cbda753ebe5412383a56
python3 deploy/verify_asset_versions.py
python3 tests/verify.py
```

Expected key output:

```text
{"documents": 15, "assets": {"base.css": "8d65c5a18cc9", "orison.js": "6cd727dafb4f"}, "status": "pass"}
{"documents": 15, "journey": "pass", "status": "pass"}
```

Also inspect exactly:

```sh
git diff b5a57cc36aee0cfb461426e38164ec33ba0ccd2c..853716f272b6e8354f27cbda753ebe5412383a56 -- index.html tests/verify.py
```

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
   `b5a57cc36aee0cfb461426e38164ec33ba0ccd2c..853716f272b6e8354f27cbda753ebe5412383a56`
   end to end; it contains the one anchor change and its focused tests.
5. **Scope isolation**: `git diff --stat` reports only `index.html` and
   `tests/verify.py`, with 12 insertions and 2 deletions.
6. **Authorship**: implementation commit reports
   the owner's git identity and contains no `Co-Authored-By` trailer.
7. **Architecture documentation**: N/A. The destination, route graph, state
   contract, services, ports, and architecture are unchanged.

## Known limitations / open questions

- GitHub reports no configured CI checks for the `main` base branch; the
  repository-native checks above are the executable evidence.
- Mobile implementation is outside scope. The anchor remains a native control
  and no mobile-specific behavior is added.
- PR 45 is intentionally stacked on this branch, but its redesign commits are
  excluded from the pinned review range.
- Rollback is the two-file revert to inert recovered-path text and the prior
  journey activation step; no state or infrastructure rollback is required.
