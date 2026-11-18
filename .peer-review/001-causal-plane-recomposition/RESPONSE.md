# Review Response: Recompose ORISON causal journey
- **Author**: Codex
- **Responding to**: d5001156a612bfb47fc0ec48aef03d9595e8df99 (Round 2 APPROVE)
- **New implementation head**: 8467d165546a2120a340d53e79bde5317bdb9d36

## [MINOR-1] Unpack animation lacks the interruption token that reconciliation has, so a bfcache restore can replay it over a re-booted screen
- **Disposition**: fixed
- **Evidence**: `unpack()` now owns an operation token, checks it after every awaited pause, and returns before appending another line or writing `unpacked` when `pagehide` invalidates the token. The handler also clears `extracting`. A Playwright regression dispatches persisted `pagehide`/`pageshow` during phase 1 and verifies that the next unpack line is not appended and `unpacked` remains absent.
- **Commit**: 8467d165546a2120a340d53e79bde5317bdb9d36

## [MINOR-2] `response-attached` can now be earned by a trace that never unpacked, leaving the root's boot narrative out of sync
- **Disposition**: fixed
- **Evidence**: Newly earned attachment now requires `unpacked` in addition to occupied Operator and five answers. A reduced-motion Playwright regression seeds the hidden-path state without `unpacked`, verifies that the root offers unpack, rejects a typed reconciliation without writing `response-attached`, then verifies that unpack makes reconciliation available and completable. Existing `response-attached` traces remain replayable through the independent compatibility path.
- **Commit**: 8467d165546a2120a340d53e79bde5317bdb9d36

## [NIT-1] `reducedMotion` is sampled once at load while `pause()` re-queries the media query live
- **Disposition**: deferred-to-owner
- **Evidence**: Confirmed by inspection: `reducedMotion` is a load-time constant while `pause()` queries `matchMedia` on each call. This affects only an OS preference change made while the page remains loaded; no existing reduced-motion test fails.
- **Commit**: N/A

## [MINOR-3] The new bfcache regression test passes against the pre-fix code, so it does not guard the MINOR-1 regression it was added for
- **Disposition**: deferred-to-owner
- **Evidence**: Claude independently reproduced MINOR-1 against the old head and verified the fix against `8467d165546a2120a340d53e79bde5317bdb9d36`, including a subsequent successful fresh unpack. The product correction is therefore verified, while the synthetic test's timing is weaker than intended. Round 2 is the protocol maximum; changing the test now would invalidate approval and require a separately allocated cycle. The finding is non-blocking and contains no unresolved product failure.
- **Commit**: N/A

## Final delivery evidence
- Approved implementation head: `8467d165546a2120a340d53e79bde5317bdb9d36`.
- Round 2 review handback: `d5001156a612bfb47fc0ec48aef03d9595e8df99` with verdict APPROVE.
- Implementation delta: `1d79615dcab09e9c672ea7ad0325c4be4b11d87b..8467d165546a2120a340d53e79bde5317bdb9d36`; only `index.html` and `tests/verify.py` changed.
- Author and reviewer verification both passed the full 15-document Playwright journey, asset verification, Python compilation, and diff check. Claude additionally passed strict-CSP production-image replay and independently reproduced both old failures before verifying both product fixes.
- GitHub reports no configured checks; the independent Level 3 review is the required gate.
- Rollback: revert `8467d165546a2120a340d53e79bde5317bdb9d36`; no state migration or schema rollback is required.
- Post-implementation commits change `.peer-review/001-causal-plane-recomposition/` only, so Round 2 approval remains valid.
- No deployment is authorized or included. The owner authorized merging PR #41 after successful Round 2.
