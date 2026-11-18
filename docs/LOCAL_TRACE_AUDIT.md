# Milestone 7: Local Trace and Observation Audit

Date: 2026-07-17

Status: Accepted, merged through pull request 26, and deployed at `abb011c`

## Current operational-spine amendment

ADRs 0013 and 0014 change only how existing version-2 values are earned and
rendered. `response-attached` now completes only after the explicit local
`reconcile response 00000000` operation; repeated unpack does not write it.
The three existing `fragment-probe-*` flags are independent cumulative
receipts: zero to two flags are partial progress and all three are completion.
Existing valid v2 records require no conversion. Version-1 migration still
excludes response attachment, Parent completion, every fragment flag, and the
fragment route; complete erasure still removes the one storage key.

The three fragment requests remain fixed same-origin paths without trace ID,
answer, witness, classification, or arbitrary visitor input. Ordinary HTTP
infrastructure can observe which fixed path was requested, exactly as already
disclosed. No durable field, precision, size ceiling, cookie fallback, request
payload, backend, or infrastructure change is introduced.

These earning and rendering amendments are merged through pull request 41 on
`main` at `3ddfa99a17df7061b219a517463f30acc5b5da5c` and publicly deployed from
application source `3a9bfa28d2e6d438f5838606b1371d293807aa49`.

The unnumbered Operational Spine merged through pull request 37 and deployed
from `main` at `1895f6c` does not change this accepted version-2 storage,
migration, privacy, or erasure contract. The archive's one
unresolved-operation register and receiver phases (occupied, attached, parent)
are derived from existing state. Letter eligibility uses existing Weather,
Integrity, and Staff outcomes. New attachment consumes existing
`operator-occupied` and five-answer state; existing `response-attached` records
remain grandfathered. No new durable value, route, request exposure, backend,
or mobile validation is implied.

The version-1 cookie inventory below is historical baseline material. It is not
the current steady-state store.

## Baseline verified before planning

| Surface | Verified state |
| --- | --- |
| Local checkout | `main` at `da58a3e6e24ed668dd84aa7e40b34a295ee16d56`; only unrelated untracked `.serena/` present |
| GitHub | `main` at `da58a3e6e24ed668dd84aa7e40b34a295ee16d56`; no open pull requests; pull request 25 merged |
| Server checkout | clean `main` at `b085671cfcf223a3993705f3824b305a6708ef83` |
| Running container | `orison` running and healthy; zero restarts; nginx configuration valid |
| Public deployment | root, archive, and Camera documents match the server checkout and running container byte-for-byte, not GitHub `main` |
| Public browser behavior | complete retained-state regression passed with zero console/page errors and zero off-origin requests |

Pull request 25 is therefore accepted on GitHub but intentionally absent from
the server and public deployment. Milestone 7 branches from GitHub `main`; it
does not deploy pull request 25.

## Scope and non-goals

This is a Level 3 persistence and privacy decision. It may replace the durable
state store, coarsen existing observations, and retain a small number of new
interaction outcomes produced inside ORISON. It does not add analytics, a
backend, identity collection, third-party code, permissions, or durable machine
profile fields.

Raw commands, arbitrary keystrokes, pointer paths, exact event times, activity
outside ORISON, IP-derived location, credentials, exact identity, and the
ephemeral Operator machine profile remain out of scope and prohibited.

## Current version-1 cookie inventory

The complete record is URI-encoded JSON in `orison_trace`. Normal writes use a
30-day sliding `Max-Age`, `Path=/`, `SameSite=Lax`, and `Secure` on HTTPS. The
application has no encoded-size limit; the practical limit is the browser's
per-cookie limit, commonly about 4 KiB for the complete cookie. Current parsing
checks only JSON syntax and `v === 1`, then shallow-merges the result into a
fresh object. The normal maxima below are conventions, not enforced validation.

| Field | Type and current precision | Normal / accepted maximum | Narrative consumers | Retention and transmission | Erasure and current migration |
| --- | --- | --- | --- | --- | --- |
| `v` | number; exact integer | created as and required to equal `1` | runtime schema gate | refreshed with the whole cookie and sent on matching requests | deleted with the cookie; any other version resets the whole trace |
| `id` | string; trace designation made from four random hex characters plus the low four hex characters of `Date.now()` | normally 8 uppercase hexadecimal characters; malformed v1 is unbounded | shared trace labels, root, inode, Carrier, Staff, Weather, Camera, Operator, invitations | 30-day sliding; sent to Cloudflare and nginx on matching requests | deleted with the cookie; no field validation; generation retains a fragment of creation timing |
| `first` | number; epoch milliseconds | exact creation time; malformed v1 is unbounded | Dead Letter derives a date 19 days earlier | 30-day sliding; sent on matching requests | deleted with the cookie; no coarsening |
| `visits` | number; one-page-entry precision | unbounded counter | shared footer count, 404 late-state threshold | 30-day sliding; sent on matching requests | deleted with the cookie; no saturation or validation |
| `seen` | object of page name to count; one-entry precision | normally 13 known route names; keys and counts are not validated | awareness, all revisit states, archive hierarchy, Horizon replay, Operator occupation | 30-day sliding; sent on matching requests | deleted with the cookie; malformed nested values may break consumers |
| `order` | string array; exact first-entry order | normally up to 13 distinct route names; malformed v1 is unbounded | archive first-source hierarchy, Camera ledger, Operator authority path | 30-day sliding; sent on matching requests | deleted with the cookie; no allowlist or length cap |
| `last` | string; exact prior page name | normally one known route name; malformed v1 is unbounded | route context and Weather/Camera Back precedence | 30-day sliding; sent on matching requests | deleted with the cookie; no allowlist |
| `returns` | number; one-return precision | unbounded counter | awareness, Camera ledger, Operator authority path | 30-day sliding; sent on matching requests | deleted with the cookie; no saturation or validation |
| `focus` | number; one delayed visibility loss | unbounded counter after a 750 ms in-page threshold | awareness and Camera behavioral reconstruction | 30-day sliding; sent on matching requests | deleted with the cookie; no saturation or validation |
| `seconds` | number; one-second accumulated precision | unbounded total; each page hide adds at most 120 seconds | shared observation interval and root `dmesg` residue | 30-day sliding; sent on matching requests | deleted with the cookie; no coarse migration |
| `answers` | string array; exact forced choices | normally 5 distinct values from 15 allowed answers; malformed v1 is unbounded | examination resume, Integrity, Camera answer count, Operator vector and hypotheses | 30-day sliding; sent on matching requests | deleted with the cookie; no allowlist or per-question validation |
| `flags` | string array; exact event membership | normally up to 16 known flags; malformed v1 is unbounded | progression and mutations across every established route | 30-day sliding; sent on matching requests | deleted with the cookie; unknown flags survive |
| `invited` | string; prior witness token | query value sliced to 16 characters on normal capture; malformed v1 is unbounded | inode ownership and pre-occupation Operator residue | 30-day sliding; token is also exposed in the initial query request | deleted with the cookie; no character allowlist |

Known flags are `unpacked`, `invited`, `examined`, `mirror-route`, `forecast`,
`forecast-returned`, `forecast-held`, `warning-armed`, `checksum-match`,
`checksum-drift`, `aperture-slip`, `heard`, `letter`, `operator-probe`,
`operator-occupied`, and `probed`.

## Candidate observation decisions

| Candidate | Decision | Precision ceiling and maximum | Concrete consumer | Reason |
| --- | --- | --- | --- | --- |
| recognized command categories | retain | five-bit membership mask; no order, count, spelling, arguments, or raw text | repeat/occupied Operator composition; later available to Milestone 8 | distinguishes recovery, inspection, process, mount, and utility intervention without retaining commands |
| refused commands | retain | saturating band `0`, `1`, `2`, `3+` | repeat/occupied Operator composition; later available to Milestone 8 | records persistence at the command boundary without text or timing |
| activation modality | retain | one enum: `unknown`, `keyboard`, `pointer`, `touch`, or `mixed`; no counts | repeat/occupied Operator composition | expresses how ORISON controls were operated without recording movement or arbitrary input |
| recovered-object hold | retain | presence only after the existing 850 ms archive focus/hover threshold; allowlisted maximum of five object names; no duration | repeat/occupied Operator composition | preserves a meaningful existing ORISON interaction while discarding exact dwell time and pointer path |
| exact command text and keystrokes | reject | not stored | none | raw input can contain arbitrary personal or sensitive content |
| pointer coordinates, paths, and counts | reject | session-only receiver rendering remains | none | high-resolution behavior is unnecessary and fingerprint-like |
| exact focus, dwell, page, return, or absence timing | reject | ephemeral timers may only promote a documented band | none | exact timing exceeds the narrative need |
| ignored controls, parallel tabs, and open-in-parallel inference | defer | not stored | none | intent cannot be inferred reliably from current browser events without broader instrumentation |
| browser/platform/language/timezone/screen/viewport/CPU/memory/touch/preferences | keep ephemeral | rendered only during the current Operator document | first Operator composition only | the combined profile would become a durable fingerprint |
| invitation progression | retain existing coarse contract | allowlisted witness token plus existing `invited` event; no identity lookup | inode and Operator | preserves invitations while moving new tokens out of the request URL |

## Architecture approaches

### Approach A: retain the version-1 cookie

Add only bounded values to the existing object and correct the processing
record. This is the smallest code diff and preserves browser-managed expiry,
but all retained behavior—including new fields—continues to accompany matching
HTML and asset requests. It also leaves shallow validation and the practical
cookie-size ceiling as architectural constraints.

### Approach B: migrate to a validated version-2 cookie

Introduce explicit migration, allowlists, saturation, and a 2 KiB application
budget while continuing to use one cookie. This fixes malformed-state and
storage-exhaustion behavior and preserves automatic expiry. It does not fix the
central exposure: Cloudflare and nginx still receive the complete narrative
trace on matching requests even though neither consumes it.

### Approach C: one-way migration to browser-only version-2 storage

Read a valid legacy cookie once, normalize it into a bounded version-2 record
in `localStorage`, verify the write, and then delete the cookie. New invitations
place the witness token in the URL fragment rather than the query. Legacy query
invitations remain readable for compatibility and are removed from the visible
URL with `history.replaceState` immediately after capture.

If `localStorage` is unavailable or a bounded write fails, fail closed: do not
silently recreate a request-bearing trace. The current document may render from
an ephemeral fresh state, but durable cross-route progression is unavailable
until browser storage is available. This limitation is preferable to an
undisclosed privacy fallback.

Approach C is recommended. A static server has no narrative consumer for a
request-bearing cookie. Moving the record removes unnecessary repeated
transmission, gives the state an explicit size and validation contract, and
allows Milestone 7 observations without converting the cookie into a larger
request header. Its cost is that browser-only storage cannot physically
self-delete while ORISON is closed; an expired record is deleted before use on
the next ORISON load, and the processing record must say so plainly.

## Recommended version-2 field and storage matrix

Storage key: `orison_trace_v2`. Maximum serialized UTF-8 size: 2,048 bytes.
Every read is normalized through allowlists and saturation before a consumer
receives it. No value is copied into a cookie.

| Field | Type | Precision ceiling / maximum | Narrative consumer | Retention | Transmission exposure | Erasure | v1 migration |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `v` | integer | exactly `2` | runtime | logical 30-day sliding window | browser JavaScript only | remove key | set to `2` |
| `id` | string | exactly 8 uppercase hex characters from `crypto.getRandomValues`; no timestamp component | existing trace labels and invitation creation | same | browser JavaScript; shared only when a visitor intentionally sends an invitation | remove key | rotate once on migration because the v1 generator includes timestamp bits; accepted progression remains |
| `firstDay` | integer | UTC calendar-day bucket | Dead Letter relative date | same | browser JavaScript only | remove key | floor valid `first` milliseconds to a UTC day |
| `expiresDay` | integer | UTC calendar-day bucket, 30 days after last successful write | runtime only | record is rejected and deleted before use after expiry | browser JavaScript only | remove key | initialize from migration day plus 30 |
| `visits` | integer | `0..31`, saturating at `31+` | shared entry display and 404 threshold | same | browser JavaScript only | remove key | clamp valid nonnegative `visits` |
| `seen` | object | allowlisted route keys; each count `0..3`, saturating at `3+`; maximum 14 keys | existing revisit, hierarchy, Horizon, occupation, and detached-fragment contracts | same | browser JavaScript only | remove key | keep known keys and clamp counts; explicitly discard the version-2-only `fragments` route |
| `order` | string array | deduplicated allowlisted routes; maximum 14 | archive, Camera, Operator, detached fragments | same | browser JavaScript only | remove key | filter and deduplicate in original order; explicitly discard `fragments` |
| `last` | string | one allowlisted route or empty | existing Back/route context | same | browser JavaScript only | remove key | keep only a known route |
| `returns` | integer | `0..7`, saturating at `7+` | awareness, Camera, Operator | same | browser JavaScript only | remove key | clamp valid nonnegative `returns` |
| `attention` | integer | visibility-loss band `0`, `1`, `2`, `3+`; no timestamps | awareness and Camera language | same | browser JavaScript only | remove key | map valid `focus` into the four bands |
| `activity` | integer | accumulated 30-second units `0..31`, saturating at `15m30s+`; sub-30-second remainder and exact elapsed value are discarded | shared interval language and root residue | same | browser JavaScript only | remove key | floor valid aggregate `seconds` to 30-second units and clamp |
| `answers` | string array | one allowlisted answer per five forced questions; maximum 5 | examination, Integrity, Camera, Operator | same | browser JavaScript only | remove key | retain the first valid value per question |
| `flags` | string array | allowlisted event membership; maximum 21 current flags | existing progression contracts, response attachment, Parent Process completion, and up to three cumulative fixed fragment receipts | same | browser JavaScript only | remove key | filter unknown values and deduplicate; exclude version-2-only `response-attached`, `orphan-released`, and all `fragment-probe-*` values during legacy migration |
| `witness` | string | allowlisted ASCII token, maximum 16 characters | inode and pre-occupation Operator | same | browser JavaScript after capture; legacy query is exposed once | remove key | sanitize valid `invited` value |
| `obs.mode` | enum | `unknown`, `keyboard`, `pointer`, `touch`, `mixed`; no counts | repeat/occupied Operator | same | browser JavaScript only | remove key | initialize `unknown` |
| `obs.commands` | integer bit mask | five category bits; no order, frequency, spelling, arguments, or raw text | repeat/occupied Operator and future Milestone 8 | same | browser JavaScript only | remove key | initialize `0` |
| `obs.refused` | integer | `0`, `1`, `2`, `3+` | repeat/occupied Operator and future Milestone 8 | same | browser JavaScript only | remove key | initialize `0` |
| `obs.held` | string array | allowlisted recovered objects that crossed the existing hold threshold; presence only; maximum 5 | repeat/occupied Operator and future Milestone 8 | same | browser JavaScript only | remove key | initialize empty |

The runtime may use exact elapsed time, current pointer coordinates, and the
current command string transiently to perform the interaction. Those values
must be discarded after classification and never enter a durable store.

## Migration matrix

| Input condition | Result | Loss and user-visible effect |
| --- | --- | --- |
| no v2 record and no v1 cookie | create a fresh normalized v2 record | fresh journey |
| valid normal v1 cookie | write normalized v2 with a new time-independent random trace ID, read it back, then delete v1 cookie | the visible trace designation rotates once; exact `first`, `seconds`, focus count, high counts, and unknown values are intentionally coarsened or discarded; accepted progression, answers, route order, witness, and known v1 flags remain; version-2-only `response-attached`, `orphan-released`, `fragment-probe-*`, and `fragments` route values are excluded |
| valid v2 and valid v1 | normalized v2 is authoritative; delete v1 | prevents an older cookie from overwriting a completed migration |
| malformed/expired v2 and valid v1 | delete invalid v2, migrate valid v1, then delete v1 | valid legacy progression is recovered |
| valid v2 and malformed v1 | keep normalized v2; delete malformed v1 | no accepted state loss |
| malformed v2 and malformed/absent v1 | delete both and create fresh v2 | explicit reset rather than partial hostile state |
| v1 version other than `1` | do not interpret it; delete after a successful fresh v2 write | unknown schemas are not shallow-merged |
| v2 exceeds 2,048 bytes or contains unknown/deep structure | normalize allowlisted bounded fields; reject and reset if still oversized | no attacker-controlled key growth or storage exhaustion |
| v2 write/read-back fails | do not delete or add fields to a valid v1 source; otherwise use ephemeral fresh state and expose no cookie fallback | an existing legacy cookie remains request-bearing until later migration or erasure; no new observation is written to it |
| legacy `?witness=` invitation | capture a sanitized token, replace the current URL without query/fragment, continue normally | initial request may already exist in Cloudflare/nginx access data |
| new `#witness=` invitation | capture sanitized token, replace the current URL without query/fragment, continue normally | fragment is not included in the HTTP request |

Migration is idempotent. The legacy cookie is deleted only after a bounded v2
write is read back successfully. Normal code never dual-writes the two stores.

## Route-consumer matrix

| Route / subsystem | Existing retained input preserved or coarsened | New retained input | Required result |
| --- | --- | --- | --- |
| shared runtime and receiver | `id`, visits, activity, `seen`, returns, attention, flags | activation modality classification only on ORISON controls | all reads normalized; no pointer path or arbitrary key capture |
| root terminal | `seen`, `id`, activity band, answers/progression flags | command-category mask, refused band, activation modality | original commands and warning remain; raw command is discarded after classification |
| recovered inode | `id`, witness, `seen`, awareness | none | query and fragment invitations remain compatible; captured token is scrubbed from the visible URL |
| examination | answers, `examined`, `id` | mount/utility command category, refused band, activation modality | five questions and command-driven mount remain unchanged |
| recovered directory | `seen`, `order`, `id`, flags, awareness | held-object membership, activation modality, and explicit `orphan-released` completion | existing hover/focus hold threshold supplies a durable yes/no outcome; Parent Process retains only its completed action; hierarchy and PR 25 interrupt remain intact |
| detached fragments | `id`, `orphan-released`, `seen.fragments` | independent membership of `fragment-probe-013`, `fragment-probe-027`, and `fragment-probe-058` | Parent Process alone earns the route; every fixed missing path remains actionable until its local receipt exists; no arbitrary pathname, retry count, order, or timing field is stored |
| Camera 06 | forecast and authority flags, `seen`, `order`, returns, answer count, attention, `id` | none directly | attention is rendered as a band; Weather Back precedence and state-flash prevention remain intact |
| Weather 19 | forecast flags, `id`, awareness, prior route | none | native Back contract remains intact |
| Integrity Manifest 32 | answers and checksum flags | activation modality on verification only | attempted reconstruction remains session-only |
| Carrier 44 | `id` and carrier/forecast flags | activation modality on explicit listen only | audio-device data and lifecycle remain ephemeral |
| Staff Register 71 | `id` and awareness | none | existing insertion contract remains |
| Dead Letter | `id`, `firstDay`, `letter` | none | relative date uses day precision, not milliseconds |
| Operator | all retained route, answer, carrier, return, authority, and witness evidence; machine profile remains ephemeral | modality, command categories, refused band, held objects | replace raw-count emphasis with a bounded intervention reading; every new field changes this authored composition |
| Digital Horizon | `seen.extent` and `operator-probe` | none | one-time detour and still replay remain unchanged |
| missing path | visits and `probed` | one allowlisted fragment-probe flag only for the three fixed, earned child paths | generic 404 behavior remains unchanged; later fragment requests cannot replace the first selection |
| trace erasure | all v2 state and legacy cookie | all new observations | remove every ORISON-controlled durable store and prevent another open tab from resurrecting it |

Existing state is sufficient to show where the visitor went and which fixed
events completed. It cannot distinguish required recovery from exploratory
commands, a refused command boundary, the input surface used to activate ORISON
controls, or which recovered objects crossed the archive's existing hold
threshold. Those four bounded outcomes are why the Operator composition may
consume the proposed fields.

## Threat and privacy review

### Browser

The browser profile is the privacy boundary, not an identity boundary. Anyone
with access to the same browser profile can inspect or clear the record.
Same-origin JavaScript can read both the current cookie and proposed
`localStorage`; neither protects against a same-origin script injection. ORISON
is static and dependency-free, but its CSP permits existing inline scripts, so
code review and local-only assets remain essential. Private browsing, user
settings, or storage eviction can remove continuity at any time.

### Matching HTTP requests

The current cookie accompanies matching document and asset requests. `Secure`
protects browser-to-edge transport but does not hide the value from the HTTPS
terminator. `SameSite=Lax` limits some cross-site cookie contexts; it does not
provide confidentiality. The proposed steady state sends no narrative cookie.

### Cloudflare

Cloudflare terminates public HTTPS and can observe the visitor IP, user agent,
requested URL, and current cookie header. ORISON does not create a Cloudflare
visitor profile or call an analytics API, but the edge remains an infrastructure
processor. A new fragment invitation is not present in the HTTP request; a
legacy query invitation is. Current browser validation observed no off-origin
requests, although Cloudflare adds its own response reporting headers.

### nginx

nginx receives the current cookie through the tunnel even though the static
site does not consume it. The running container's default `main` access-log
format records request URL, status, referrer, user agent, and forwarded address;
it does not include the Cookie header. A legacy witness query can appear in the
logged request URL. New fragment invitations avoid that exposure. No
application backend or server-side narrative store exists.

The detached-fragment interaction deliberately uses three fixed request paths.
Cloudflare and nginx can therefore observe which of `013`, `027`, or `058` was
requested in ordinary access data. The paths contain no trace ID, witness,
answer, classification, or local-state value, and neither system joins the
request to ORISON's browser-only probe flag. This is route exposure, not
narrative-record transmission, and remains inside the processing record's
existing request boundary.

### JavaScript and malformed state

Current shallow merging allows hostile nested types and unbounded strings,
arrays, keys, and numbers to reach consumers. Version 2 accepts only a plain
object with allowlisted scalar/array/object members, finite integers, known
route names, known answers, known flags, and capped lengths. Unknown data is
discarded. A state that cannot be normalized within the size budget resets
rather than being partially trusted. DOM insertion continues to use
`textContent` for retained values.

### Storage exhaustion

The current cookie can silently exceed browser limits as unbounded malformed or
future fields grow, and its bytes are repeated on requests. Version 2 has an
application budget of 2,048 serialized UTF-8 bytes even though browser storage
quotas are larger. All arrays, maps, counters, strings, and enum values have
fixed maxima. Write exceptions and failed read-back do not trigger a cookie
fallback. ORISON does not evict unrelated origin storage.

### Invitation tokens

The token is a random ORISON trace designation, not verified identity, but it
can correlate an inviter and invitee inside the fiction. Current query URLs
expose it to network infrastructure, access logs, copied URLs, and browser
history. New invitations use a fragment, which is available to page JavaScript
but omitted from HTTP requests. Both forms are scrubbed from the current history
entry after capture. ORISON cannot retract a token already shared or erase it
from another browser.

### Trace erasure

Erasure can remove ORISON-controlled browser state; it cannot erase ordinary
Cloudflare/nginx request logs, another person's copied invitation, browser
history outside the current entry, screenshots, backups, or data retained by
the browser itself. The interface and processing record must not claim those
capabilities.

## Trace-erasure contract

1. The erase action removes `orison_trace_v2` from `localStorage`.
2. It expires the legacy `orison_trace` cookie at `Path=/` for compatibility,
   whether or not migration completed.
3. It clears in-memory state, stops generated audio and timers, and replaces
   navigation with `/` without witness query or fragment data.
4. A `storage` deletion event marks every other open ORISON tab erased before
   it can write again; those tabs stop audio/timers and replace to a fresh root.
5. A fresh root creates a new trace only after confirming both durable stores
   are absent. No accepted answer, flag, order, count, witness, observation, or
   prior random trace ID may reappear.
6. Erasure is tested from fresh v2, migrated v1, malformed v1/v2, both stores,
   an invitation trace, and two open tabs.
7. The visitor-facing text states the boundary: ORISON-controlled local state
   is removed; network access records and copies outside this browser are not.

## Rollback strategy

Before merge or deployment, close or revert the Milestone 7 branch; no stored
state changes exist publicly.

After deployment, prefer a behavioral rollback that disables the new Operator
reading while retaining the v2 storage adapter and erasure logic. This
preserves migrated continuity and the stronger request boundary.

If the storage architecture itself must roll back, ship an explicit v2-to-v1
converter before restoring the older runtime. Preserve route order, known
flags, answers, witness, and saturated counts; discard Milestone 7 observations
that v1 cannot represent. Coarsened day, attention, and activity values cannot
be expanded back into exact historical values and must not be fabricated. A
plain revert without conversion would make migrated visitors appear fresh.

No rollback changes Cloudflare, tunnel routing, ports, or unrelated services.

A behavioral rollback of the detached-fragment interaction removes its archive
entry, route, and specialized 404 branch while leaving the three probe flags
allowlisted but inert until logical expiry or erasure. No state conversion,
Cloudflare rule, nginx change, or infrastructure rollback is required.

## Accepted implementation

The user approved the contract on 2026-07-17 before implementation began. The
review branch implements:

- Approach C and one-way v1 cookie to v2 `localStorage` migration;
- the version-2 field, precision, size, retention, and malformed-state contract;
- the four new retained observation outcomes;
- fragment-based invitations with legacy query compatibility; and
- the trace-erasure and rollback contracts above.

The implementation is merged on `main` through pull request 26 and deployed at
`abb011c`. Milestone 8 uses this accepted state architecture.
