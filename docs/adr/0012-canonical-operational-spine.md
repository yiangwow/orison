# ADR 0012: Give the rendered journey one canonical operational spine

Date: 2026-07-22

Status: Accepted; route and Archive placement amended by ADR 0013; current-run
ending and late handoffs amended by ADR 0015

## Context

ORISON's individual recovery, archive, Operator, Parent Process, and detached-
child interactions are internally stateful, but successive milestones left the
rendered journey with several mechanically valid orders. In particular, any
three archive rooms could expose the dead letter, response attachment became
eligible on the first Operator probe, and the automated journey used direct
route entry around the late return. The result required external instructions
even though each destination was already implemented.

The correction must preserve the existing routes, browser-only version-2
record, hidden-path fiction, authored browser Back interactions, optional
Carrier, Parent Process, Migrating Gap, privacy boundary, and native revisit
behavior. It must make available operations legible without adding a quest log,
progress meter, tutorial, or explanation of ORISON's purpose.

## Decision

Give the visitor-facing journey one canonical operational spine:

```text
unpack → inode → examination / mount
→ Camera 06 → Weather 19 outcome
→ Integrity 32 decision → Staff 71 indexing
→ dead letter → Operator → Extent → occupied Operator
→ repeat unpack / response attachment
→ Parent Process → detached child request
```

Treat a Weather outcome as earned only after Camera 06 supplied the comparison
route and either browser Back confirmed the forecast or the source remained
through the held interval. Expose the dead letter only after that outcome, one
Integrity match-or-drift decision, and one Staff visit. Preserve already-earned
letter and Operator states so existing traces never regress.

Amend ADR 0009's attachment eligibility: a new response attachment requires
`operator-occupied` and all five retained answers, not merely
`operator-probe`. Existing `response-attached` traces may still review their
completed ledger regardless of the rule under which they earned it.

Place one state-derived unresolved-operation register at the stable archive
intro beside the recovered object index. It exposes only the current earned
fault and its one available operation; it never lists future conditions or
completion history. Ordinary objects and optional revisits remain available
around that spine. Completed examination and mount work is acknowledged on
inode and examination revisits
instead of being presented as necessary again.

While that register is active, retain the first-access source at the head of
the object index but return it to ordinary record scale. Likewise, collapse the
duplicate full-width Operator-return interrupt into its ordinary record row.
The register is the sole dominant unresolved operation. Once Parent Process is
eligible and the register disappears, the first-access source may resume its
derived historical prominence beside the parent interlock and receipt.

Use stable interface vocabulary: `open` enters a record, `return` names a
deterministic destination, `run` executes a command, `request` enters one fixed
missing address, and `erase` removes the local trace. `trace` names the local
record, `observer` the active visitor role, `source` retained behavioral input,
`operator` the authority role, `parent` process ownership, and `witness` an
invitation relationship.

Do not add a route, flag, schema version, migration, backend, or access-control
claim. The canonical contract governs rendered controls and eligibility, not
the retrievability of known static URLs. Existing Extent and fragment guards
remain unchanged.

## Consequences

- Camera/Weather, Integrity, and Staff become causal evidence rather than
  optional milestones the critical journey can silently skip.
- Occupied authority visibly causes the recovery return and response
  attachment; Parent Process eligibility and completion remain unchanged.
- Existing version-2 and migrated traces retain all previously earned states;
  no stored record requires conversion.
- The archive gains one prominent in-world handoff without becoming a menu or
  checklist, while route-specific visual identities remain intact.
- Tests must complete the fresh desktop journey through rendered controls,
  prove each prerequisite gate, preserve native Back, replay old attachment
  state, and retain invitation, erasure, Parent, fragment, privacy, and request
  boundaries.
- Behavioral rollback restores the former Letter and attachment predicates and
  removes the state-derived handoffs. No state conversion or infrastructure
  rollback is required.
