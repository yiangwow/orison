# ORISON architecture

## System summary

ORISON is a static multi-page website implemented with HTML, CSS, and browser
JavaScript. It has no application backend, database, package manager, or build
step. Narrative continuity is stored in one bounded, versioned browser-only
`localStorage` record. A legacy version-1 cookie is only a migration source.

Production topology:

```text
visitor
  → Cloudflare HTTPS edge
  → remotely managed Cloudflare Tunnel "homelab"
  → Docker network "self-hosted"
  → nginx container "orison" on port 80
  → static files
```

The container publishes no host port. No router port forwarding or public origin
address is required.

## Repository structure

```text
/
├── AGENTS.md                 session continuity and project rules
├── VISION.md                 creative canon and boundaries
├── ARCHITECTURE.md           implementation and deployment truth
├── ROADMAP.md                possible future work
├── docs/
│   ├── CURRENT_STATE.md      delivery status and active blockers
│   ├── EXPANSION_SESSIONS.md ordered multi-session expansion program
│   ├── LOCAL_TRACE_AUDIT.md  accepted field, migration, privacy, and erasure contract
│   ├── APPARENT_TRANSFER_LOG.md accepted trigger, state, replay, and rollback contract
│   ├── review/               milestone review captures and validation evidence
│   └── adr/                  accepted architectural decisions
├── index.html                public extraction terminal
├── 404.html                  stateful missing-path response
├── privacy.txt               visitor-facing processing record
├── robots.txt                crawler clue and hidden-route exclusions
├── erase/index.html          local trace reset
├── assets/
│   ├── base.css              shared visual system
│   └── orison.js             state, observation, profile, and signal runtime
├── .lost+found/00000000/     hidden experience root
├── deploy/nginx.conf         production web-server configuration
└── Dockerfile                static nginx image
```

## Route graph

```text
/
└── unpack orison.zip
    └── /.lost+found/00000000/                  inode / recovered signal
        └── examination/                        five behavioral questions
            └── archive/                        mutable recovered directory
                ├── mirror/                     Camera 06
                │   └── weather/                Camera-derived Back or held outcome
                ├── weather/                    recovered weather log
                ├── integrity/                  match or drift from recalled answers
                ├── choir/                      user-initiated generated audio
                ├── staff/                      inserts current observer
                ├── ../dead-letter/             requires Weather, Integrity, and Staff outcomes
                │   └── ../operator/             local machine observations
                ├── ../operator/                becomes occupied after Extent
                │   └── ../extent/               first eligible archive return detour
                └── ../fragments/               appears after Parent Process completion
                    ├── 013/                     intentional missing-path request
                    ├── 027/                     intentional missing-path request
                    └── 058/                     intentional missing-path request

/.lost+found/00000000/extent/ ──→ operator/      one egress; compares the same Operator endpoint
all three fragment receipts     ──→ /             retained current-run terminal condition

/elias/                                        held object, two seals in English: a fault, then a question
/mihai/                                        held object, two seals in English: a monster, then a car
/erase/                                        delete local trace
/privacy.txt                                   processing disclosure
unknown path                                   custom stateful 404
```

The accepted, unnumbered whole-site operational spine is root unpack → inode →
examination/mount → Camera 06 → Weather outcome → Integrity outcome → Staff →
Letter → Controlling Source → unresolved Operator → Extent → occupied Operator → root response reconciliation
→ ordered Archive → Parent Process → cumulative detached-child
requests → retained root terminal. Weather outcome is Camera-derived and
resolves through native Back or the held condition. Extent returns directly to
Operator; response attachment is a separate
`reconcile response 00000000` operation and never a repeated unpack phase.
Parent Process retains its eligibility and replay semantics. Carrier remains an
existing optional recovered object and does not alter the spine.

## Page responsibilities

| State name | Route | Visitor-facing role | Narrative/state role |
| --- | --- | --- | --- |
| `root` | `/` | archive recovery terminal | performs the sole four-phase unpack and sets `unpacked` only at completion; the first recovered path enters inode; after occupied Operator and five answers, exposes explicit response reconciliation, sets `response-attached` only at completion, and points directly to ordered Archive; when response, Parent, and all three fragment receipts are present, renders a commandless retained terminal condition from existing state without a forward late-route link |
| `inode` | `/.lost+found/00000000/` | recovered signal object | introduces ownership; resolves invitation token; after archive access or response attachment, returns directly to the still-mounted directory |
| `exam` | `examination/` | compatibility questions and mount prompt | stores forced-choice answers and coarse command outcomes; sets `examined`; exposes an explicit `mount directory` control and returns completed revisits to the mounted archive |
| `archive` | `archive/` | recovered directory | keeps interpretation, response evidence, compact Parent custody control/receipt, and fragment continuation in its left operational column; keeps only stable recovered records in the right index; marks first-room history in place without reordering; retains which recovered objects cross the existing hold threshold; permits one transient early aperture slip; after occupied authority and response attachment, exposes the one-time parent-process interlock and retains its completion |
| `mirror` | `archive/mirror/` | pre-exposed optical retention record | sets `mirror-route` and `forecast-returned`; protects the immediate Weather Back frame before later behavioral or authority reconstruction; after a returned or held Weather outcome, promotes the retained frame handoff and demotes comparison replay; conceals its baseline until stateful render completes |
| `weather` | `archive/weather/` | predictive event log and navigation front | sets `forecast` and, after a missed departure, `forecast-held`; visualizes and instructs browser Back; completed revisits expose the retained front as the dominant archive handoff |
| `integrity` | `archive/integrity/` | retained-response checksum | compares reconstructed examination choices; sets match or drift; returns the retained integrity decision through a completed-state handoff |
| `choir` | `archive/choir/` | carrier sample | user starts local Web Audio; sets `heard`; reflects root and Weather carrier outcomes on return; combines heard and Weather-derived state in one retained-carrier handoff |
| `staff` | `archive/staff/` | personnel register | renders an early source as pending; after Weather and Integrity resolve, inserts the observer row when Staff first follows Integrity or has been opened more than once; returns the indexed source through a completed-state handoff |
| `letter` | `dead-letter/` | message addressed to trace | becomes eligible only after Weather outcome, Integrity outcome, and Staff; sets `letter`; its first canonical continuation opens the existing unresolved Operator ingress as Controlling Source |
| `operator` | `operator/` | observation and authority report | its first canonical Letter ingress spends `operator-probe` and presents a static foreground account inside the existing left search-instrument for that document lifetime; direct access, reload, interruption, Back/Forward, revisits, and prior migrated probes skip the account and render the ordinary unresolved `0`; it then follows the existing unresolved/Extent/occupied behavior, including local-only ephemeral readings, invitations, and root reconciliation |
| `extent` | `extent/` | unexpected spatial extent inside an attempted archive return | reads `operator-probe`; records ordinary route visit state; first entry drifts, revisit is still; its sole egress returns to Operator |
| `fragments` | `fragments/` | detached child-address sequence | requires `orphan-released`; exposes three independent fixed missing addresses; retains every completed request while leaving the others actionable; communicates completion only after all three are retained, then returns forward to the retained root terminal |
| `missing` | any 404 | missing-path response | sets `probed`; later admits generic paths were recorded; each earned fixed fragment address idempotently retains its own request and returns forward to the child sequence |

**`/elias/` (page name `held`).** An orphaned delivery addressed to one named
person: a single sealed audio object released by two seals, in the shape of
`/mihai/`. Both seals are in English, on subjects a computer-science student
names on sight: a fault, where a process was stopped for reading an address
that was never assigned to it, and then, once the first is named, the 1936
question of whether any program can decide that another program ever finishes.
The visitor states each answer; the page compares its SHA-256 digest in the
browser (Web Crypto, no network) and each seal unlocks one eight-character
fragment of the payload's file name, so the object is unreachable until both
are named and no answer appears in the page. Answers are normalised before
hashing — case, diacritics, trailing punctuation, hyphens, a leading article
for the first seal, token splitting for the second. A wrong answer is answered
in the administrative register with an escalating attempt note; the adjacent
answers a student reaches for first (the neighbouring signal, the cause rather
than the fault, the name the other operating system uses, the man rather than
his question, the theorem beside it) receive their own nudge and do not advance
the counter. Hints appear after the second and fourth wrong attempt of a seal.
Visits are recorded through the shared `ORISON.page` lifecycle like any other
route (`seen`, `order`, `last`), and nothing else is written; attempt counts
live in page memory only. First visit and revisit render identically; neither
opened seal is persisted, so a return shows the sealed object again. The route
is reachable only by its address; nothing links to it, and it is excluded from
indexing. The payload lives under `elias/` in the image, named by the two
fragments the digests unlock.

**`/mihai/` (page name `held-second`).** The same shape as `/elias/` with two
seals, both in English: an inventory riddle whose answer is a monster from
the games he plays, then, once it is accepted, one whose answer is a car.
Both answers are words the addressee says himself; the wrong-but-adjacent
ones (the monster's mate, a later game, the maker, the successor) get their
own nudges. Answers are
compared by SHA-256 digest after normalisation (case, diacritics, hyphens,
articles, a few tolerated misspellings); near misses get a nudge in the same
register instead of the attempt note, and hints appear after the second and
fourth wrong attempt of a seal. The payload's file name is assembled from two
fragments the digests unlock, so it is unreachable without both answers.
Nothing is persisted beyond the shared page-visit lifecycle; attempt counts
live in page memory only. Unlinked and excluded from indexing.

### Consequence handoffs and eligibility

The archive's left column contains its state-derived unresolved-operation
register and all current operations. It is rendered from existing bounded state
rather than stored as a route, flag, schema version, or separate progression
system. The right index has one fixed semantic order: Camera, Weather,
Integrity, Carrier, Staff, Letter, Operator. State can reveal records, annotate
semantic outcomes, and mark the first-access source in place; it cannot move
Parent or fragment controls into that index or reorder recovered evidence.

Camera, completed Weather, Integrity, Carrier, and Staff use one shared visual
handoff grammar: retained result, explicit consequence, and one primary return
action. Replay and utility controls remain secondary. These handoffs are
rendered entirely from existing route context and allowlisted state. They do not
form a second progression system or preview unearned operations. The shared
receiver status continues to reflect occupied, attached, and parent phases from
the same derived state.

Letter eligibility is the conjunction of a Weather outcome (Camera-derived
Back or held), an Integrity outcome (`checksum-match` or `checksum-drift`), and
a visible Staff insertion. Staff opened before Integrity remains pending until
Integrity resolves and either Staff has been opened more than once or its first
recorded position follows Integrity. Staff and Archive evaluate this same rule
from existing visit order and capped visit count.
A new response attachment requires `operator-occupied` and five retained
answers, then the explicit root reconciliation operation. Existing v2 traces
with `response-attached` remain replayable as grandfathered completed traces.
The three existing fragment flags are independent cumulative receipts; one or
two flags represent valid partial progress and all three represent completion.
Together with `response-attached` and `orphan-released`, all three also derive
the retained root terminal. No route, schema field, migration, backend, or
privacy behavior is introduced by these rules.

Controlling Source is a rendered ingress, not a new progression state: the
first canonical Letter → Operator transition spends the existing
`operator-probe` event before presenting a static foreground account with
concise status. The ordinary unresolved Operator `0` is withheld for that
document lifetime; nothing resolves or transforms automatically. The account
is available to assistive technology, leaves focus unchanged, and keeps the
existing record actions usable. All noncanonical entry and replay paths render
the ordinary state directly. It adds no route, durable state, schema,
migration, request, dependency, asset, backend, or privacy behavior; invite and
erasure behavior remain isolated, and focus, actions, and history retain their
existing contracts.

## State model

Browser-only record:

- Storage: `localStorage`
- Key: `orison_trace_v2`
- Version: `2`
- Application size ceiling: 2,048 serialized UTF-8 bytes
- Logical lifetime: 30 days after the last successful ORISON write
- Expiry precision: UTC calendar day; expired state is deleted before use on
  the next ORISON load
- Request exposure: none; `localStorage` is not attached to HTTP requests
- Validation: allowlisted fields and values, capped collections, saturated
  counters, and read-back verification

Current schema:

| Field | Type | Meaning |
| --- | --- | --- |
| `v` | number | state schema version |
| `id` | string | eight uppercase hexadecimal characters generated with `crypto.getRandomValues`; contains no timestamp component |
| `firstDay` | number | first-state creation day as a UTC day bucket |
| `expiresDay` | number | logical expiry as a UTC day bucket |
| `visits` | number | page entries capped at `31+` |
| `seen` | object | allowlisted visit counts keyed by page state name and capped at `3+` |
| `order` | string array | first-seen order of distinct page names |
| `last` | string | most recently entered page name |
| `returns` | number | revisits and browser back/forward navigation events capped at `7+` |
| `attention` | number | delayed tab-visibility losses capped at `3+`; no event time |
| `activity` | number | accumulated 30-second units capped at `15m30s+`; sub-unit remainder is discarded |
| `answers` | string array | one allowlisted forced-choice value for each of five questions |
| `flags` | string array | allowlisted narrative events |
| `witness` | string | allowlisted invitation token, maximum 16 characters |
| `obs.mode` | string | `unknown`, `keyboard`, `pointer`, `touch`, or `mixed`; no counts |
| `obs.commands` | number | five-bit membership mask for recovery, inspection, process, mount, and utility commands; no text, order, or count |
| `obs.refused` | number | refused-command band `0`, `1`, `2`, or `3+` |
| `obs.held` | string array | up to five recovered-object names that crossed the existing 850 ms hold threshold; no duration |

On first access after Milestone 7, the runtime accepts a valid
`orison_trace` version-1 cookie as a one-way migration source. It preserves
known progression, answers, route order, flags, and witness state; caps counts;
maps exact creation, focus, and seconds fields into day/attention/activity
bands; rotates the time-derived legacy trace ID; verifies the version-2 write;
excludes the version-2-only `response-attached`, `orphan-released`, and
`fragment-probe-*` events plus the `fragments` route state;
and then deletes the cookie. Normal operation never dual-writes the stores. If
browser-only storage is unavailable, the document uses ephemeral state and
does not add observations to or recreate a request-bearing cookie.

Known flags:

| Flag | Set by | Meaning |
| --- | --- | --- |
| `unpacked` | root terminal | visitor extracted the archive |
| `invited` | runtime | route included a witness token |
| `examined` | examination | five-question sequence completed and mount channel exposed |
| `mirror-route` | Camera 06 link | visitor was directed from mirror to weather |
| `forecast` | weather | backward-navigation prediction activated |
| `forecast-returned` | Camera 06 | browser Back fulfilled the Weather prediction and was retained |
| `forecast-held` | weather | the predicted departure passed while the input source remained |
| `warning-armed` | root terminal | an accepted archive operation armed the persistent recovery warning |
| `checksum-match` | integrity manifest | reconstructed answers matched all retained answers |
| `checksum-drift` | integrity manifest | at least one reconstructed answer differed from the retained source |
| `aperture-slip` | recovered directory | one-time ambiguous visual manifestation was shown |
| `heard` | choir | visitor started the generated carrier |
| `letter` | dead letter | addressed message opened |
| `operator-probe` | operator | local observation report opened |
| `operator-occupied` | post-Horizon Operator revisit | inherited operator authority resolved to a feminine reference |
| `response-attached` | earned root recovery operation | response sector `00000000` completed reassignment to the current trace |
| `orphan-released` | earned archive parent-process interlock | explicit release completed and recovery children were re-parented to the current trace |
| `fragment-probe-013` | earned fragment missing response | address `013` was the first detached child requested after Parent Process completion |
| `fragment-probe-027` | earned fragment missing response | address `027` was the first detached child requested after Parent Process completion |
| `fragment-probe-058` | earned fragment missing response | address `058` was the first detached child requested after Parent Process completion |
| `probed` | 404 | visitor requested an unknown path |

### Awareness

`ORISON.awareness(state)` compresses progression into levels 0–5:

```text
floor(distinct pages seen / 2)
+ 1 if return events > 1
+ 1 if attention losses > 2
+ 1 if the letter has been opened
capped at 5
```

Awareness is a presentation heuristic, not a complete story state. Explicit
flags should be used for events whose meaning must remain stable.

### Navigation lifecycle

`ORISON.page()` registers a page configuration. On `pageshow`, the runtime:

1. reads or creates state;
2. records the page visit and previous page;
3. detects revisit or back/forward navigation;
4. consumes a new fragment or legacy query `witness` token when present and
   removes it from the current visible URL;
5. writes the bounded browser-only record;
6. updates shared trace/activity fields;
7. calls the page-specific renderer.

Using `pageshow` rather than only initial script execution is important because
pages restored from the browser's back-forward cache must re-evaluate state.

On `pagehide`, exact elapsed time exists only transiently. The runtime adds
complete 30-second units with a per-page cap of 120 seconds and discards the
remainder. A tab hidden for at least 750 ms increments the saturated
`attention` band without retaining a timestamp.

## Local observation boundary

The operator page reads:

- browser family;
- platform family;
- language;
- timezone;
- screen and viewport dimensions;
- logical processor count;
- approximate device memory when exposed;
- touch points;
- dark/light preference;
- reduced-motion preference.

These values are rendered locally and are not persisted. The site
does not request camera, microphone, geolocation, clipboard, contacts, local
files, credentials, or exact identity. The choir uses Web Audio only after the
visitor activates its control; it does not use microphone input or load audio.

The version-2 record retains only four additional interaction outcomes produced
inside ORISON: recognized command-category membership, a saturated refused
command band, activation modality on ORISON controls, and membership of
recovered objects that crossed the existing hold threshold. Raw command text,
keystrokes, pointer paths, coordinates, exact event times, external activity,
and the temporary machine profile never enter durable storage. Operator turns
the four bounded outcomes into one authored retained-intervention reading.
Milestone 8 reconstructs an apparent response-sector ledger from those accepted
values and existing progression, then retains only the coarse
`response-attached` completion flag. It does not persist the transcript,
animation timing, raw triggering command, or another observation.

There are no third-party scripts, analytics requests, advertising requests,
external fonts, IP lookups, or application-backend calls.

Root additionally recognizes a `via` query parameter carrying one of four fixed
`presence.*` clauses, used by the owner's Discord presence-card buttons as an
external ingress marker. A known clause adds one transient pair of dim boot
lines ("ingress / external presence relay" plus a clause-specific line) and the
parameter is immediately removed from the address with `history.replaceState`.
The clause is consumed on first render, never persisted, and unknown values are
ignored. No state field, route, request, or storage is involved.

The current no-banner approach depends on browser-only state remaining
first-party, functional, local to the experience, and unshared except for an
intentionally copied witness token. If analytics, server storage,
fingerprinting, advertising, or third-party services are introduced, privacy
and consent requirements must be reassessed before implementation.

## Visual and interaction architecture

`assets/base.css` defines the archive interior:

- near-black foundation;
- luminous terminal green for ORISON, system activity, and actions;
- ambient green for nonessential process residue;
- bone for recovered records and interpretation;
- dim green-grey metadata;
- bright red only for faults, absence, and unresolved work;
- violet and blue secondary tones;
- paper mode for recovered documents;
- mono, serif, and utility roles;
- subtle noise and scanline layers;
- shared machine header/footer and frame primitives;
- reduced-motion overrides.

The shared receiver field adds sparse phosphor registration rails, acquisition
status, coordinates, and a low-opacity pointer reticle to interior routes.
Pointer coordinates remain session-only. Its language reacts to existing trace
awareness, pointer interruption, tab return, and dwell over recovered objects.

The root terminal performs one full four-phase unpack derived only from archive
evidence and writes `unpacked` after the recovered path is complete. Operator
occupation plus five answers later earns the separate
`reconcile response 00000000` command. That operation accelerates through an
`aria-hidden` response-sector ledger reconstructed from bounded state; a
separate polite status reports only start and completion. Reduced motion and
replay use completed static compositions. The final reconciliation line adds
`response-attached`, changes later root boot language, exposes the
archive's response-source record, and makes ordered Archive the direct next
surface. Leaving either operation before its final boundary writes no
completion flag. After Parent release and all three fixed fragment receipts,
the same root renders the current run's retained terminal condition without
adding a flag, route, command, or completion label.

Controlling Source reuses the existing left search-instrument on the first
canonical Letter → unresolved Operator ingress. Its static foreground account
makes the local observer trace the dominant process value, with an absent
terminal and leader plus an impossible relative chronology. Eligibility is
spent immediately through the existing `operator-probe`; the account remains
until navigation or reload and does not alter the later occupied `1`/`SHE`
authority climax or the retained root ending. It is available to assistive
technology, introduces no motion, and preserves the adjacent record actions.
Direct entry, reload, interruption, browser history, revisit, and migrated
prior probes skip the account. Only the Operator document changes at runtime;
shared assets are unchanged.

The root recovery scanner, retained-process rows, and missing-region pressure
are a shared background layer on every HTML experience surface. Route-specific
foreground compositions remain distinct while the shared role palette connects
them. The runtime reconstructs
the layer from bounded state and explicitly restarts both it and the receiver
scan on every `pageshow`, including browser-history restoration. Reduced motion
receives the same stateful depth as a still composition.

After both occupied Operator authority and response attachment, the recovered
directory exposes one compact parent-process custody interlock.
`release orphan 00000000` briefly hands the seven scheduler lanes from an
unresolved wait to the current trace, then writes only `orphan-released`.
Completion reclassifies the existing record states as inherited children
without changing their names, links, first-room hierarchy, or route behavior.
The left-column receipt states that custody changed and makes fragment egress
primary; it does not become a route or second climax. Revisit renders the
completed receipt immediately and does not restore the control or replay the
handoff. Reduced motion resolves directly to the same receipt, and
storage-unavailable contexts retain only the runtime's existing ephemeral
result.

After Parent Process completion, a separate child-sequence entry appears next
to the unchanged receipt. It leads to `fragments` instead of joining the
recovered-object hierarchy. The fixed addresses `013`, `027`, and `058`
deliberately return the custom HTTP 404 document. Each eligible request
writes its corresponding existing `fragment-probe-*` flag. Forward continuation
re-renders every retained receipt while leaving unrequested addresses
actionable; native Back remains valid. Completion appears only after all three
flags are present, then the existing footer returns forward to the state-derived
root terminal. Native Back from that terminal returns to the completed fragment
receipt. The
fixed paths contain no trace, witness, answer, or classification; Cloudflare and
nginx can still observe the requested URL as ordinary network infrastructure.
Generic missing paths retain their existing response and `probed` behavior.

The recovered directory adds an archive-local scheduler fabric behind its
document hierarchy. Process rows advance at unequal intervals through running,
waiting, sleeping, and uninterruptible states. Hover and keyboard focus route
the selected object's attention into related rows; sustained dwell reclassifies
the object temporarily; pointer or focus departure leaves short-lived residue;
and tab return records a retained watchdog interrupt in the visible process
log. Process motion and residue remain session-only; crossing the established
850 ms hold threshold retains only the allowlisted recovered-object name.
Reduced-motion mode removes continuous column drift while preserving discrete
process changes and interaction responses.

On a later archive visit, the first recovered room in `order` is marked in
place as the source record without moving the stable index. After the Horizon but
before `operator-occupied`, the existing Operator link becomes a full-width
interrupt labeled `operator return / authority unresolved`; reopening Operator
resolves the accepted Milestone 6 event and restores the ordinary archive row.
This cue is derived from existing state and does not add a flag or change the
first-room hierarchy. An immediate Weather 19 browser-Back return always
retains Camera 06's two-subject forecast frame, even after `operator-probe`;
only a subsequent Camera entry replaces it with the retained route and behavior
counts. Camera 06 keeps its frame concealed until its `pageshow` renderer has
resolved the current trace, including after browser-history restoration, so a
superseded optical composition cannot flash before the authority state. On
first operator access, temporary machine readings are arranged as subordinate
bounds around the dominant absent `0` and are not persisted. A repeat access
before the Digital Horizon presents a neutral `1 / operator inferred`
authority topology for compatibility with older traces. The first post-Horizon
repeat writes `operator-occupied` and resolves the same topology to an occupied
role, inherited privilege, and `SHE` authority reference. Five deterministic,
non-diagnostic archive hypotheses remain mapped directly from the five forced
choices; they are fictional interpretation, not persisted machine profile or
psychological diagnosis. These branches add no schema field or privacy change.

After `operator-occupied`, a later Camera 06 behavioral reconstruction changes
from optical-source classification to an authority field and feminine
reference. The immediate Weather-to-Camera browser-Back frame still wins over
both Operator states. Root, inode, examination, and dead letter remain neutral
as older interface eras.

Integrity Manifest 32 appears after a complete examination and a later archive
entry. Its only interaction asks the visitor to reconstruct the five retained
choices. A live path follows the reconstructed copy; verification reveals the
retained path and records one coarse explicit flag, `checksum-match` or
`checksum-drift`. On revisit, inputs are locked and only the retained source is
shown. The detailed attempted reconstruction is not persisted. Direct access
with an incomplete examination produces a stable unavailable state.

The root and examination terminals use generated Web Audio key clicks after
keyboard interaction. Root discovery is staged without delaying input. An
accepted `file orison.zip` or unpack operation arms a visible warning beside the
discovered object; unpack aliases and the quick action are equivalent fallback
activation paths. Its 4.4-second base cadence uses a quiet fragment of Carrier
44 and changes deterministically after Weather or Operator state. Tab hiding
suspends the scheduler without queuing cues, and navigation closes the page's
audio context. No audio file is loaded, nothing autoplays, and no input device
is accessed. Both terminals expose a blinking block cursor while waiting for an
empty command.

The root has a phosphor-green terminal foreground. The lure remains a
comprehensible utility while recovered routes keep their stranger document
foregrounds, but both now occupy the same recovery infrastructure. Completed
rooms, Weather outcomes, checksum state, the letter, and Operator access select
three deterministic background-depth levels. Scanner passes, retained process
rows, buffer pressure, and missing regions remain behind fixed, legible route
content; reduced motion presents the same degradation as a still condition.
Mono carries system state and action, serif carries one interpretive claim per
surface, and narrow sans is reserved for institutional records. Recovered
titles are bounded at ordinary record scale; only Operator's `0` and `1` retain
monumental single-glyph scale. Required causal actions and their earned
consequences fit the initial 1440×700 desktop viewport.

`ORISON.drawSignal()` renders the inode and mirror visuals with Canvas. Shared
audio helpers generate the 41.2 / 61.8 / 82.4 Carrier 44 relationship for the
root relay, Weather's explicitly monitored phase-shifted interval, and the
Carrier room. Weather completion writes `forecast-held`; a native Back return
writes `forecast-returned` from Camera. Carrier and the repeat Operator topology
read those outcomes without claiming audio continued across documents. All
output remains explicitly activated and the silent path remains complete.

The archive contains a hidden pair of CSS-built mechanical apertures. The
manifestation is eligible only after the `forecast` event and a safe early
return from Camera or Weather, before Operator has been probed. Eligibility is
checked again when its delayed reveal fires. It appears briefly, sets
`aperture-slip`, and cannot be replayed in the same trace or overlap
reconciliation, Parent, or fragments. It has no text, sound, link, semantic
label, or canonical explanation. Reduced-motion mode removes twitching/flicker
but preserves one brief static appearance.

The Digital Horizon is a separate full-viewport route named `extent`. The first
eligible “return to recovered directory” action after Operator opens it once.
Direct access before `operator-probe` returns to the archive without recording
the route. The first view uses extremely slow process-field depth drift; a
history or direct revisit is a deliberate still. Its only control returns
directly to the same Operator endpoint, it does not install the shared receiver
overlay, and it adds no sound. `seen.extent` supplies the durable replay
condition without a new flag. The aperture window has already closed by this
late confrontation.

## Production server

The Docker image uses `nginx:alpine` and copies only runtime files. The nginx
configuration:

- serves static directory indexes;
- preserves access to `.lost+found`;
- denies other dot-prefixed paths;
- provides a custom internal 404 page;
- disables server version tokens;
- sends no-cache headers;
- prohibits framing;
- denies browser permissions for camera, microphone, geolocation, payment, and
  USB;
- blocks all network connections from page code with CSP `connect-src 'none'`;
- permits only same-origin assets plus inline page-specific CSS/JS and data-image
  noise;
- uses a health check against `/robots.txt`.

## Infrastructure integration

The infrastructure repository is `/home/unix/is-infra`.

Accepted service design:

- Compose service: `orison`
- Build context on server: `${ORISON_BUILD_CONTEXT:-/home/tt/orison}`
- Container port: internal `80`
- Docker network: `self-hosted`
- Public hostname: `orison.zip`
- Cloudflare tunnel: `homelab`
- Tunnel service target: `http://orison:80`
- Host ports: none

Every HTML surface references the shared stylesheet and runtime with the first
twelve characters of each file's SHA-256 digest as a query value. This keeps a
new HTML release from loading a four-hour browser-cached asset from an earlier
deployment. Any change to `assets/base.css` or `assets/orison.js` must update the
corresponding query in all HTML documents. ADR 0010 records this delivery
contract.

The corresponding infrastructure change is merged on `is-infra/main` through
pull request 2 at `7c1d90f`. Its accepted decision record is also mirrored in
this repository under `docs/adr/`.

## Change rules

When adding state:

1. Add a new explicit field or flag rather than overloading unrelated state.
2. Document it in this file.
3. If the schema shape changes, increment `v` and define migration behavior.
4. Preserve the 2,048-byte budget and define v2 migration behavior.
5. Verify fresh, migrated, expired, oversized, malformed, storage-unavailable,
   multi-tab, and erased state.

When adding a route:

1. Give it a unique `ORISON.page({ name })`.
2. Add it to the route graph and page table.
3. Define first-visit and revisit behavior.
4. Define links and browser-history expectations.
5. Keep privacy behavior within the accepted boundary.

When changing deployment or security headers, add or supersede an ADR because
those choices affect the threat model and rollback path.
