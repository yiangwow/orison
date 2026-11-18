# ADR 0011: Use fixed missing paths as fragment input

Date: 2026-07-22

Status: Accepted; mutual-exclusion decision superseded by ADR 0014

## Context

After Parent Process, ORISON needs a first fragment-ecology interaction that
expands the apparent address space without adding decorative depth, replacing
the recovered-object hierarchy, or repeating Operator authority and archive
maintenance. A missing sequence can make absence causal, but arbitrary path
capture, trace-bearing URLs, or repeated probing would exceed the local-state
and privacy contracts.

## Decision

After `orphan-released`, expose a separate detached-child sequence with exactly
three fixed missing addresses: `013`, `027`, and `058`. Each address is a real
same-origin request served by the existing custom HTTP 404 document.

The first eligible missing response writes one mutually exclusive version-2
flag: `fragment-probe-013`, `fragment-probe-027`, or `fragment-probe-058`.
Native Back re-renders the stable sequence with that address assigned to the
current trace and its next child absent. Later requests cannot replace the
first choice. Legacy migration excludes all three flags, and trace erasure
removes them.

Keep the Parent Process receipt, parented scheduler, recovered hierarchy,
generic 404 behavior, nginx rules, and Cloudflare configuration unchanged. The
fixed request path contains no trace ID, witness, answer, classification, or
arbitrary visitor input. Ordinary infrastructure can still observe the
requested URL, as already disclosed in the processing record.

## Consequences

- The path itself becomes a bounded interaction input without server-side
  narrative state or a new request mechanism.
- The first missing-path request creates one durable local consequence; replay
  is stable and cannot become a completion loop.
- Existing Camera/Weather history behavior is untouched; the fragment route
  independently uses native Back and `pageshow` re-rendering.
- The version-2 schema shape and 2,048-byte ceiling remain unchanged, while its
  route allowlist grows by one and its flag allowlist grows by three.
- Tests must cover unearned access, all three branches, mutual exclusion,
  intentional HTTP 404 status, native Back, replay, generic 404 preservation,
  migration exclusion, erasure, mobile, keyboard, reduced motion, and request
  boundaries.
- Behavioral rollback removes the archive entry, route, and specialized 404
  branch while retaining the flags as inert allowlisted values until expiry or
  erasure. No state conversion or infrastructure rollback is required.
