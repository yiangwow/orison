# Review Response: Terminal bookend and custody hinge
- **Author**: Codex
- **Responding to**: `e5f28387c90f44778555c8558a6c157a61ed92e0` (`APPROVE`)
- **New implementation head**: unchanged — `587aad8a60253c9d1f0c74e307726db2e6ef1c01`

## [MINOR-1] Consistency-critical Staff predicate exists as two verbatim copies
- **Disposition**: deferred-to-owner
- **Evidence**: Independently reproduced with `rg -n -A17
  'function staffSourceVisible'`: the Archive definition begins at
  `.lost+found/00000000/archive/index.html:1711` and the Staff definition at
  `.lost+found/00000000/archive/staff/index.html:192`; their predicate bodies
  match. Current behavior is protected by the new cross-surface regression in
  `tests/verify.py`, and Claude independently exercised it successfully.
  Moving this rule into `assets/orison.js` would expand the approved scope into
  a shared content-addressed asset change, require a hash/reference update
  across all 15 documents, and invalidate the formal approval. A focused
  follow-up may centralize the rule if the owner accepts that maintenance tradeoff.
- **Commit**: N/A — no post-approval implementation change.

## [NIT-1] `data-parent-active` is written but consumed only by tests
- **Disposition**: rebutted
- **Evidence**: `tests/verify.py:781` deliberately asserts
  `data-parent-active="true"` while Parent is the active Archive operation. The
  attribute is an explicit observable state contract for the hierarchy test,
  independent of presentational CSS, and is set/deleted with the derived Parent
  eligibility at `archive/index.html:1600-1602`. It is not an abandoned styling
  selector and has no visitor-facing failure scenario.
- **Commit**: N/A

## [NIT-2] Dead `data-state` reset on the root terminal
- **Disposition**: deferred-to-owner
- **Evidence**: Independently confirmed that `index.html:727` removes the
  terminal `data-state` attribute and no current code sets that attribute.
  The line is harmless defensive cleanup, does not affect the retained
  terminal's semantic `aria-label` or visible state, and does not justify
  invalidating Level 2 approval for a post-review implementation edit.
- **Commit**: N/A — optional cleanup in a later focused change.

## Final delivery evidence

- Branch: `redesign/terminal-bookend`
- PR: private archive PR #45 — OPEN, not draft, stacked on
  `fix/clickable-recovered-path`
- Approved implementation range:
  `853716f272b6e8354f27cbda753ebe5412383a56..587aad8a60253c9d1f0c74e307726db2e6ef1c01`
- Reviewer handback head pushed before this response:
  `e5f28387c90f44778555c8558a6c157a61ed92e0`
- GitHub checks: none configured (`statusCheckRollup: null`).
- Claude independently ran:
  - `git diff --check` on the exact range → exit 0;
  - `python3 deploy/verify_asset_versions.py` → 15 documents, `status: pass`;
  - `python3 tests/verify.py` → 15 documents, journey `pass`;
  - ten Chromium renders at 1440×700 covering five critical late-flow surfaces
    with reduced motion both enabled and disabled → all required targets within
    viewport and zero horizontal overflow.
- Post-implementation diff before this response:

```text
.peer-review/003-terminal-bookend/REQUEST.md
.peer-review/003-terminal-bookend/REVIEW.md
```

The response commit is also confined to
`.peer-review/003-terminal-bookend/`; no implementation file changed after
approval. Merge and deployment remain unperformed and Level 2 merge
authorization remains with the owner.
