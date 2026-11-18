# Milestone 8: Apparent Transfer Log

Date: 2026-07-17

Status: Historical milestone deployed; placement superseded by ADR 0013,
merged through pull request 41, and deployed from `3a9bfa2`

## Current operational-spine amendment

This historical Milestone 8 record remains valid for the meaning and visible
evidence of completed response attachment. ADR 0013 supersedes ADR 0009's
placement of that event inside a repeated `unpack orison.zip`. On the current
merged source, the first unpack is the sole archive recovery and contains no
future-derived response evidence. After occupied Operator plus five retained
answers, the distinct command `reconcile response 00000000` becomes available
and writes the existing `response-attached` flag only after its final line.
Existing valid v2 traces remain grandfathered completed receipts.

This placement change adds no route, flag, schema version, migration, backend,
privacy behavior, infrastructure, or mobile claim. It is publicly deployed from
application source `3a9bfa28d2e6d438f5838606b1371d293807aa49`.

The original Milestone 8 change was Level 3 because it expanded the allowlisted
durable flag vocabulary. The current eligibility correction is Level 1: it
derives behavior from existing state and changes no API, schema, storage,
security, or deployment contract.

## Accepted approach

Milestone 8 remains inside the existing root recovery terminal. It does not add
a route, download, file, filesystem API, permission request, external request,
or claim of host modification. The first unpack now expands archive inspection,
damaged-directory parsing, detached-inode recovery, and read-only mount, but it
does not consume route, answer, Operator, response, Parent, or fragment state.

Milestone 8 originally earned the event after first Operator access and five
retained examination answers. The current contract requires occupied Operator
and all five answers. It then exposes a distinct explicit operation:

```text
reconcile response 00000000
```

The reconciliation expands into an accelerating response-sector ledger derived
from the current bounded trace. Completion writes one coarse
flag, `response-attached`, and ends with:

```text
response-sector/00000000: source reassigned / trace <ID>
```

The flag changes subsequent root boot language and exposes a restrained
response-source record in the recovered directory without replacing its
first-opened hierarchy or other stateful progression.

## Trigger, state, and replay matrix

| Condition | Trigger availability | State read into visible lines | State change | Replay |
| --- | --- | --- | --- | --- |
| fresh or pre-occupied trace | full unpack or recovered-inode action only; reconciliation reports an incomplete ledger | archive-derived recovery evidence only | `unpacked` only after the first operation completes | condensed recovery receipt |
| `operator-probe` plus five answers, without `operator-occupied` | reconciliation unavailable | none | none | none |
| `operator-occupied` without five retained answers | reconciliation unavailable | none | none | none |
| `operator-occupied` plus five answers | quick hint and typed `reconcile response 00000000` available | trace ID; first route order and capped counts; five answers; command-category mask; refused band; modality; held rooms; integrity, carrier, returns, and optional witness | add `response-attached` only after the final operation | not yet applicable |
| navigation away before completion | operation is interrupted | transient lines only | no completion flag | eligible operation remains available |
| completed trace | inode-open hint remains primary; typed reconciliation reviews the receipt | condensed retained evidence and final classification | no second state change | stable completed ledger; no acceleration or transient reassignment moment |
| reduced motion | same eligibility and command | full completed ledger in one discrete composition | same completion flag | same static completed ledger |
| trace erased | unavailable on fresh root | none | all v2 state, including `response-attached`, removed | none |

Legacy version-1 migration never imports `response-attached`; that event did not
exist in v1 and must be earned under the current occupied-Operator contract.
Existing valid version-2 state may retain and replay the flag normally even if
it was earned under the older first-probe rule.

## Visible-state matrix

| Source | Precision used | Example role in ledger |
| --- | --- | --- |
| `id` | existing eight-character random trace designation | response source and final assignment |
| `order`, `seen` | first eight allowlisted routes; counts remain capped at `3+` | response-sector paths and access evidence |
| `answers` | five fixed-choice values | compatibility checksum sectors |
| integrity flags | membership only | matched, drift retained, or unverified |
| `heard`, `returns` | event membership and capped `7+` return count | carrier/return sector |
| `obs.commands` | five existing category bits | recovered operation classes; no raw command |
| `obs.refused` | existing `0`, `1`, `2`, `3+` band | refusal boundary |
| `obs.mode` | existing five-value enum | input surface |
| `obs.held` | existing allowlisted room membership | retention threshold evidence |
| `witness` | existing sanitized token, when present | unresolved fictional ownership relation |
| `response-attached` | one allowlisted completion bit | root and archive post-operation interpretation |

The event never stores its visual line order, animation timing, scroll position,
raw command, keystrokes, or additional behavioral observations.

## Accessibility and motion contract

- The input and quick action both trigger the same reconciliation operation and retain visible
  keyboard focus before and after completion.
- Rapid visual lines live in an `aria-hidden` ledger so the existing polite log
  does not announce every transient mutation.
- A separate polite status reports only operation start/review and the final
  response-sector assignment.
- Reduced motion appends the completed evidence in one discrete composition and
  performs no accelerating scroll.
- Leaving before the final operation cancels completion; history restoration
  returns enabled controls and the original eligible state.

## Privacy implications

The milestone adds no observation field. It allows one new progression value in
the existing `flags` collection, retains it under the same 2,048-byte and
30-day logical-expiry contract, transmits it to no request, and removes it with
complete trace erasure. All visible evidence is reconstructed locally from
already accepted state.

## Rollback

Before merge or deployment, close or revert the Milestone 8 branch.

After deployment, first disable the trigger and archive mutation while keeping
`response-attached` allowlisted until ordinary expiry or erasure. This avoids
silently deleting a completed event during a behavioral rollback.

A full code revert to Milestone 7 drops the unknown flag during normalization
and restores the earlier root/archive interpretation. No other version-2 field
requires conversion and no higher-precision value can be exposed. Cloudflare,
nginx, tunnel routing, ports, and unrelated services remain untouched.
