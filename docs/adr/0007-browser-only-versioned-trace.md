# ADR 0007: Move the bounded narrative trace to browser-only storage

Date: 2026-07-17

Status: Accepted

## Context

ORISON currently stores its complete narrative trace in a JavaScript-readable
version-1 cookie. The cookie is functional and first-party, but `Path=/` causes
the browser to attach it to matching document and asset requests. Cloudflare
and nginx can therefore receive state that neither system uses. The cookie also
has a small practical size budget, shallow malformed-state handling, and exact
millisecond/second observations that are more precise than the narrative needs.

Milestone 7 proposes retaining a few additional outcomes produced inside
ORISON: coarse command categories, a refused-command band, activation modality,
and whether a recovered object crossed the existing hold threshold. Adding
those fields to the request-bearing cookie would enlarge both privacy exposure
and request overhead.

Browser-only storage avoids automatic request attachment but has no native
expiry timer while the site is closed. Migration, logical expiry, storage
failure, invitation tokens, multi-tab erasure, and rollback therefore need an
explicit contract.

## Decision

Replace steady-state `orison_trace` cookie persistence with a
bounded, normalized version-2 record in `localStorage` under
`orison_trace_v2`.

On first access, read a valid version-1 cookie, normalize and coarsen it, write
and read back version 2, then delete the cookie. Never dual-write during normal
operation and never silently fall back to a request-bearing trace when browser
storage is unavailable.

Limit the serialized record to 2,048 UTF-8 bytes. Allowlist routes, answers,
flags, witness characters, and observation categories; cap every collection
and saturate counters. Replace exact creation, accumulated seconds, and focus
counts with documented day/activity/attention bands. Generate version-2 trace
IDs with `crypto.getRandomValues` and rotate the legacy ID once because the
version-1 generator includes low timestamp bits. Retain no raw commands,
keystrokes, pointer paths, exact event times, external activity, identity, or
machine-profile fields.

New invitation URLs carry the witness token in a fragment so the token is not
part of the HTTP request. Continue to accept legacy query invitations, and
scrub either form from the current history entry after capture.

`/erase/` removes version 2, expires the legacy cookie, clears runtime state,
and prevents other open ORISON tabs from resurrecting the trace. The processing
record must distinguish ORISON-controlled local erasure from network access
logs, copied invitations, and browser data outside ORISON's control.

The complete field, migration, route-consumer, threat, erasure, and rollback
contracts are recorded in `docs/LOCAL_TRACE_AUDIT.md` and are part of this
decision.

## Consequences

- Narrative state is no longer repeated to Cloudflare and nginx on every
  matching request after migration.
- Existing valid version-1 progression, answers, route order, witness, and
  known flags migrate without silent loss; the visible trace designation
  rotates once, and exact timing and unbounded values are intentionally and
  irreversibly coarsened.
- The Operator can consume four bounded interaction outcomes without becoming
  a diagnostics dashboard or durable fingerprint.
- Browser storage inspection, clearing, eviction, and same-origin script access
  remain possible. ORISON still cannot correlate browsers except through an
  intentionally shared witness token.
- Logical expiry is enforced before use on the next ORISON load. Physical bytes
  may remain in browser storage after the deadline while ORISON is closed, so
  the processing record cannot promise automatic physical deletion at an exact
  instant.
- Storage-unavailable contexts lose durable progression rather than receiving
  an undisclosed cookie fallback.
- Tests must cover fresh, migrated, malformed, oversized, expired, erased,
  invitation, multi-tab, and storage-failure states in addition to the complete
  existing journey.
- A behavioral rollback can keep version-2 persistence. An architectural
  rollback requires an explicit v2-to-v1 converter; a plain code revert would
  make migrated traces appear fresh.
