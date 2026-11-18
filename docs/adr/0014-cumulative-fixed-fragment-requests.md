# ADR 0014: Make fixed fragment requests cumulative

Date: 2026-07-22

Status: Accepted; all-three forward destination amended by ADR 0015

## Context

ADR 0011 bounded fragment input to the fixed missing addresses `013`, `027`,
and `058`, but made the first request mutually exclusive. That behavior turned
the other two visible addresses into closed choices and made completion depend
on Back or a restart rather than continued forward action. Version 2 already
allowlists an independent flag for each fixed address.

The correction must preserve intentional same-origin HTTP 404 responses,
fixed non-identifying paths, local-only narrative state, the 2,048-byte record
ceiling, generic 404 behavior, migration exclusion, expiry, erasure, and the
Parent Process gate.

## Decision

Supersede ADR 0011's mutual-exclusion rule. After `orphan-released`, each of
`013`, `027`, and `058` remains actionable until its own request has been
accepted. A specialized 404 response idempotently adds only the corresponding
existing flag: `fragment-probe-013`, `fragment-probe-027`, or
`fragment-probe-058`.

The 404 response returns to the sequence through a forward-labelled
`continue child sequence` action. The sequence renders every completed request
as a retained trace receipt, keeps every unrequested address actionable, and
reports final completion only when all three flags are present. Duplicate
requests preserve the same receipt and do not alter other addresses. Native
Back remains valid but is not required between requests.

Legacy version-1 migration continues to exclude all fragment flags. Existing
version-2 records containing one or two flags become valid mid-progress
records; records containing all three render complete. Erasure removes all
three with the rest of the trace.

## Consequences

- All six request orders produce the same complete retained set while
  preserving the order-independent local-state contract.
- No schema version, flag, route, arbitrary input surface, server-side state,
  request payload, or infrastructure rule is added.
- Ordinary infrastructure can observe the three fixed requested paths, as
  already disclosed; no trace ID, answer, witness, or classification enters a
  request URL.
- Tests must cover unearned access, all six request orders, partial v2 replay,
  duplicate requests, forward continuation without Back, HTTP 404 status,
  generic 404 preservation, reload, revisit, keyboard, reduced motion,
  migration exclusion, record size, and complete erasure.
- Behavioral rollback may restore a single rendered choice while retaining all
  three flags as inert allowlisted values until expiry or erasure. No state or
  infrastructure rollback is required.
