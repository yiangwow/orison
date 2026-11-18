# Current project state

Last updated: 2026-09-11

## Current change: /elias/ rebuilt with two seals

`/elias/` is replaced rather than extended. The original page released its
audio on one retrieval key decoded from two fragments; it now carries two
seals on the `/mihai/` template, both in English, on subjects its addressee —
a computer-science student — answers on sight: a segmentation fault, then the
halting problem. The brief was recognition rather than difficulty, so the work
is in the wording and in the near-miss table, which answers the wrong guesses
a student actually reaches for (bus error, null pointer, core dump, the name
the other operating system uses; Turing rather than his question, the
Entscheidungsproblem, Gödel, P vs NP). Near misses get their own nudge and do
not advance the attempt counter; hints appear after the second and fourth
wrong attempt of a seal. The payload's file name is assembled from the two
fragments the digests unlock, so it is unreachable until both seals are named,
and no answer appears in the page. The route, page name (`held`), privacy
behaviour and Dockerfile line are unchanged; the previous single-key payload
is replaced by one new recording. The claim field keeps the visible green
border and glow added after the addressee could not find the input the first
time.

Verification: a headless Chromium pass on a local static server ran 103 checks
— the wrong-answer note ladder and both hint reveals on each seal, all twelve
first-seal and ten second-seal near misses (each asserted against its exact
nudge, and asserted not to open the next stage), every accepted spelling of
both answers, the assembled payload URL at HTTP 200 with its full byte count,
both single-fragment guesses returning 404, a 390×844 pass with no horizontal
overflow, and the computed border colour, width and glow of the claim field.
Zero console errors. `deploy/verify_asset_versions.py` passes for all 17
documents. As recorded below for `/mihai/`, Playwright's `click` never reports
these claim buttons stable in this WSL environment; `press(…, "Enter")`
submits the same form and was used throughout.

## Prior change: a second held object at /mihai/

`/mihai/` follows `/elias/` with two seals for a non-technical addressee: an
inventory riddle whose answer is a monster from the games he plays, and,
once accepted, one whose answer is a car, each with a two-step hint ladder
and near-miss nudges. Both seals are in English now. The questions were
rewritten three times on 2026-09-11: an engineer's name was too hard, an
engine and a rifle were subjects the owner had already used, and the
Romanian second seal was dropped at his request. The payload is the message
that was left for the addressee, its second sentence processed harder than
its first.
Digest comparison after normalisation; the payload name is assembled from two
unlocked fragments; page name `held-second`; nothing persisted beyond the
visit lifecycle. `/elias/` was deployed on 2026-09-08 (its claim field gained
a visible green border after the addressee could not find it) and is public.

Verification: a headless Chromium pass on a local static server drove both
seals through wrong answers, near misses, the hint reveals and the accepted
spellings; the payload resolved with HTTP 200 and the full byte count; no
console errors. Note for this environment: Playwright's `click` on the
claim buttons never reports the element stable (the same environment issue
recorded for the `#commandHint` click below); pressing Enter in the field
submits the same form and was used instead. Deployment note: the first
release of `/elias/` wedged the container recreate on tt-server and left the
site answering 502 until the Docker daemon was restarted; releases since
have been clean.

## Prior change: held object at /elias/

A new unlinked route, `/elias/`: an orphaned audio delivery addressed to one
person, released by a retrieval key. Two fragments on the page decode to the
key (a rot-13 sentence naming it, and its ASCII octets); the page hashes the
stated key with Web Crypto and derives the payload's file name from the digest,
so the file is unreachable without the key and no network request is made
(the CSP's `connect-src 'none'` holds). Nothing is persisted beyond the shared
page-visit lifecycle; wrong attempts are counted in page memory only. The
payload is a 453 KB MP3 committed under `elias/`, copied into the image by a
new `COPY elias` line in the Dockerfile. Page name `held`.

Verification: a headless Chromium pass on a local static server: a wrong key
produced the administrative note and left the release hidden; the right key
(with trailing punctuation and capitals, normalised) revealed the release, the
download link resolved to the payload with HTTP 200 and the full byte count,
and the console logged no errors. `deploy/verify_asset_versions.py` passed for
all 16 documents.

## Prior change: presence-relay ingress

Root now recognizes `?via=presence.<clause>` (refusal, molt, release,
terminal) — the ingress marker carried by the owner's Discord presence-card
buttons. A known clause renders one transient pair of dim boot lines before the
index pass and the address is normalized with `history.replaceState`. The
clause is consumed on first render (a `clear` re-boot does not repeat it),
unknown values are ignored, and nothing is persisted — no state field, schema,
route, request, asset, or dependency change. Runtime delta is under 1.5 KB.

Verification: a targeted Chromium pass covered all four clauses (residue
rendered, address scrubbed, no repeat after clear), a plain visit (no residue,
boot intact), an unknown clause (ignored), and zero console errors. The full
`tests/verify.py` journey could not be used as the gate for this change: it
fails identically on the unmodified checkout in the WSL environment used for
this session (a `#commandHint` click never becomes "stable"), so it records an
environment problem, not a regression from this change. Re-running the full
suite in a known-good environment remains advisable.

## Prior deployed correction: response reconciliation hierarchy

The Level 1 root hierarchy correction merged through pull request 53 at
`f0bcd969f77d7c71e728ab4077b8f36a83123177` and is publicly deployed from that
application source. Once occupied Operator and five retained answers make
response reconciliation available, root no longer presents the recovered-inode
path as a competing next action. The existing executable
`run: reconcile response 00000000` control becomes the sole dominant
continuation. Reconciliation still writes `response-attached` only at its final
boundary; afterward the visible path and quick action both lead directly to
ordered Archive.

The first unpack still exposes the inode, direct route access and native history
remain meaningful, typed commands retain their behavior, and reload, repeated
unpack, or interruption cannot restore the inode anchor while reconciliation is
pending. The correction adds no route, state field, schema, migration,
dependency, shared asset, request, backend, privacy behavior, or infrastructure
change. Root grows from 34,060 to 35,125 uncompressed bytes, a 1,065-byte
runtime delta.

The complete local and public Chromium journeys pass, including the canonical
occupied-Operator return, direct pending state, keyboard focus, repeated unpack,
interrupted reconciliation and reload, mobile layouts, reduced motion, erasure,
and the retained terminal ending. Focused visual checks pass at 2560×1319,
1440×700, 390×844, 375×812, and constrained 390×650 without horizontal
overflow, browser errors, or off-origin requests. Local `main`, the clean server
checkout, running container, and public root, Archive, Operator, `base.css`, and
`orison.js` bytes agree at `f0bcd969...`. The ORISON-only container is healthy
with zero restarts; nginx configuration, restrictive headers, public 200s,
intentional fixed and generic 404s, and asset-version validation pass. Formal
cross-agent review was not requested.

## Current deployed correction: static Foreground Account

ADR 0017 amends ADR 0016's Controlling Source presentation without changing its
eligibility or state boundary. The revision merged through pull request 51 at
`e8b6622602a87dd0e6612c804897127a58e5e5f5` and was first publicly deployed
from that application source. On the first canonical Letter → unresolved
Operator arrival, the existing `operator-probe` is still spent immediately, but
one static, user-paced foreground account replaces the former timed prelude.
The observer trace is its dominant process value; the ordinary unresolved `0`
is withheld for that document lifetime, while the adjacent record and actions
remain present and usable. Nothing settles automatically, and reduced motion
receives the same composition.

Direct entry, reload, interruption, persisted restore, Back/Forward, revisit,
and prior migrated probes continue to skip the account. The revision adds no
route, durable state, schema, migration, dependency, shared asset, request,
backend, or privacy behavior. The complete 15-document Chromium journey passes
locally and against production, including static persistence beyond the former
timing boundary, mobile containment, reduced motion, focus, migration, erasure,
and replay paths with no browser errors or off-origin requests. The Operator
document grows from 29,652 to 33,585 uncompressed bytes, a 3,933-byte delta;
shared assets and their content-addressed references remain unchanged.

At that release, the server checkout, running container, and public root,
Archive, Operator, `base.css`, and `orison.js` bytes matched `e8b6622...`. The
revision remains included in current application source `f0bcd969...`. Formal
cross-agent review was not requested. The timed pull request 49 presentation at
`805cb391...` is superseded.

## Current deployed correction: mobile aperture containment

The Level 1 responsive correction from `fix/mobile-aperture-containment`
merged through pull request 48 at
`a8a0d63531d9e41b38bcc4de168d1a0659a941d3`. It keeps the one-time Archive
aperture inside the narrow visual viewport by replacing its mobile
`right: -0.8rem` offset with `right: 0`. The aperture remains state-earned,
non-interactive, transient, and unchanged at desktop widths. Repository-native
coverage asserts containment while the aperture is visible and again after it
is hidden at 375×812, 390×844, and a reduced-motion 390×640 viewport.

Post-change validation passes for all 15 runtime documents and the complete
repository journey. A production-image replay covers 116 mobile states and 31
focus audits across fresh, returning, migrated, interrupted, reduced-motion,
Back/Forward, fragment, retained-terminal, and cross-tab erasure contexts with
no browser errors, off-origin requests, or horizontal-overflow states.
The complete 1440×700 journey and focused 1440×1000 and 2560×1319 Archive
checks also pass. The image preserves restrictive headers, intentional fixed
and generic 404 responses, healthy zero-restart operation, and source-identical
root bytes.

No route, state field, schema, migration, privacy, erasure, native Back,
keyboard, touch, asset, dependency, backend, or infrastructure behavior
changes. Shared `base.css` and `orison.js` bytes and their content-addressed
references remain unchanged. Mobile Chromium is directly verified; physical
OS virtual-keyboard behavior and non-Chromium engines remain unverified.
`privacy.txt` retains its browser-native plain-text mobile presentation because
changing its delivery contract is outside this correction. Peer-review cycle
006 approved the implementation with no findings. The correction is included
in deployed application source `e8b6622...`.

## Deployed foundation: terminal bookend and custody hinge

The Level 2 desktop coherence correction governed by ADR 0015 is merged through
pull request 45 on `main` at
`ce3e6e53d4d21644502b629b83075d206974d276` and publicly deployed from that
application source. It keeps occupied Operator as the dramatic climax,
condenses Parent Process into a left-column custody control and receipt, keeps
all three fixed fragment requests cumulative, and sends their complete receipt
forward to a state-derived retained condition on the existing root terminal.

The final root condition is derived from existing `response-attached`,
`orphan-released`, and three `fragment-probe-*` flags. It adds no completion
flag, route, schema version, migration, backend, request, asset type, privacy,
erasure, or infrastructure behavior. Reconciliation now points directly to
ordered Archive; the first unpack still points to inode and remains the sole
full recovery operation. The completed terminal intentionally provides no
forward late-route link, closing the Archive loop while native Back retains the
completion receipt in the finishing history. Staff remains pending until
Weather and Integrity resolve and its first route position or capped revisit
count makes insertion visible. Aperture timing is restricted to the early
Camera/Weather return so it cannot collide with late operations.

Repository-native validation passes for all 15 runtime documents and the
complete journey, including all six request orders, keyboard, pointer, native
Back/Forward, reload, interruption, migration, reduced motion, partial and
completed revisit, fixed and generic 404 behavior, record size, invitation
isolation, and cross-tab erasure. Local visual validation at 2560×1319,
1440×1000, and 1440×700 reports no horizontal overflow, browser errors, or
off-origin requests; the required Operator, Parent, fragment, Staff, and final
terminal consequences remain visible in the constrained desktop viewport.

Claude formally approved the exact implementation ranges in peer-review cycles
002 and 003. The clickable recovered-path predecessor is merged through pull
request 44 at `ac64e0bfb206a68ec8144383b684dac256d66358`; the terminal bookend is
merged through pull request 45 at `ce3e6e53d4d21644502b629b83075d206974d276`.
The targeted ORISON-only deployment passed source/container hash comparison,
nginx configuration, restrictive-header checks, container health with zero
restarts, and the complete public browser journey. Untracked `.serena/`, local
`server-setup.sh`, and unrelated server monitoring work remained outside the
release. Pull request 46 carries only that post-deployment documentation record
and was not separately deployed. Its historical GitHub/server difference was
superseded by the 2026-07-24 ORISON-only deployment from application source
`805cb39119eadb45dd809aa009e3b7c5a8ab39e6`.

## Previous deployed truth: causal-plane recomposition

The approved Level 3 coherence correction is merged through pull request 41 on
`main` at `3ddfa99a17df7061b219a517463f30acc5b5da5c` and was publicly deployed on
2026-07-23 from application source
`3a9bfa28d2e6d438f5838606b1371d293807aa49`.

The deployed source makes the first unpack the sole full recovery operation,
routes Extent directly back to the same visibly transformed Operator, and
introduces explicit `reconcile response 00000000` as the only new trigger for
the existing `response-attached` completion flag. Archive now keeps current
interpretation, Parent Process, and fragment continuation in its left
operational column while its right column contains only Camera, Weather,
Integrity, Carrier, Staff, Letter, and Operator in fixed order. Fixed fragment
requests are cumulative and all of `013`, `027`, and `058` can be retained in
one continuous forward run.

No route, schema version, durable field, migration, privacy, erasure, backend,
asset type, or infrastructure contract changes. Existing valid v2 attachment
and partial-fragment records replay without conversion. Repository-native
validation passes for 15 runtime documents, all six fragment request orders,
interrupted operations, grandfathered state, keyboard, Back, reduced motion,
revisit, migration, erasure, and request boundaries. Desktop visual review
passes at 1440×1000, 2560×1319, and 960×900 with no browser errors or off-origin
requests. The rebuilt nginx production image passes `nginx -t`, preserves
strict CSP and intentional fragment HTTP 404 behavior, and passes the same
complete journey against `https://orison.zip`. Mobile implementation and
deployment remain out of scope.

## Previous deployed truth: Consequential Handoff Pass

The previous public application source at
`ece7fc63f46a251c4e39ad92f570d870f94c762a` served the accepted whole-site
canonical spine: root unpack → inode →
examination/mount → Camera → Weather outcome
(Camera-derived Back or held) → Integrity match/drift → Staff → Letter →
Operator → Extent → occupied Operator → repeat root unpack/response attachment
→ inode direct archive return → Parent Process → detached child request.

The archive now exposes exactly one state-derived unresolved-operation register.
While it is active, prior first-access hierarchy remains retained but no longer
outweighs the current fault; Parent eligibility restores that historical scale.
Letter requires Weather outcome, Integrity outcome, and Staff. New response
attachment requires occupied Operator plus all five answers; existing
response-attached replays remain grandfathered. Shared receiver status reflects
occupied, attached, and parent phases. Parent Process and Migrating Gap
semantics are unchanged. Pull requests 37 and 39 are merged and that release
was deployed on 2026-07-22. Desktop, keyboard, browser-Back,
reduced-motion, revisit,
erasure, migration, fresh-context, Parent Process, and Migrating Gap behavior
passed against the public hostname. Mobile remains deferred as a separate
scope and is not claimed by this release.

## Deployed coherence correction: Consequential Handoff Pass

The approved whole-site coherence correction is merged through pull request 39,
deployed, and validated against the public hostname. It keeps the existing
route graph and version-2 state contract. Completed Camera, Weather,
Integrity, Carrier, and Staff surfaces expose one shared retained-consequence
handoff; the archive makes the current consequence visually dominant and uses
semantic object outcomes instead of access counts; Parent completion promotes
the detached-child entry; fragment finality no longer advertises an impossible
second request; and the root keyboard sequence contains no invisible tab stop.

Operator now treats a utility-only privacy round-trip as part of the same
observation interval while preserving genuine pre-Horizon revisit and
post-Extent occupation behavior. Parent Process, Migrating Gap, Weather and
Extent native Back, schema, migration, privacy, erasure, invitation, and
infrastructure semantics remain unchanged. Repository-native validation passes
with 15 runtime documents. Mobile remains explicitly outside this change.

## Summary

The first complete ORISON journey is public at `https://orison.zip`. V1.1
ambient observation, the operator-copy cleanup, Milestone 1: Living Archive,
Milestone 2: Deeper Mutations, and Milestone 3: New Recovered Object are merged
and deployed. Milestones 1, 2, and 3 were published together from `main` at
`f8d8010acc1bf748b6d2b53df83cdc2214f4edd3` on 2026-07-17.
The post-deployment Milestones 1–3 visual revision is also merged and deployed
from `main` at `08af964b3a3b190031c3257b4dd166b0ce0258c5`.

Milestone 4: Restrained Sound Language is merged and deployed from `main`. The
approved post-deployment warning, alignment, and Carrier re-entry corrections
were followed by a processing-record copy revision.

Milestone 5: Digital Horizon and Milestone 6: Feminine System Presence are
merged and publicly deployed from `main`.

The post-Horizon correction, Milestone 7 browser-only trace, Milestone 8
response attachment, the shared recovery/history correction, content-addressed
shared assets, Milestone 9: Parent Process, the unnumbered Migrating Gap
direction, and causal-plane recomposition are merged and publicly deployed. The
latest served application source is
`f0bcd969f77d7c71e728ab4077b8f36a83123177`, including the Operational Spine,
Consequential Handoff Pass, causal-plane recomposition merged through pull
request 41, clickable recovered path merged through pull request 44, terminal
bookend merged through pull request 45, mobile aperture containment merged
through pull request 48, Controlling Source merged through pull request 49, and
the static Foreground Account revision merged through pull request 51, and the
response reconciliation hierarchy correction merged through pull request 53.

Repository-native static-reference and Playwright journey validation is merged
through pull request 33 on `main` at `065c1eb3ff8624d8a182c8bbaf88167985f16a83`.
It did not change or redeploy the public experience.

Milestone 9: Parent Process is merged through pull request 34 on `main` at
`faf1dcccd03a4292c7332afd54abbed6ca03f428` and publicly deployed as part of
`94ffb657`.

The approved, unnumbered Migrating Gap direction is implemented, validated,
merged through pull request 35, and publicly deployed from `94ffb657`.

The manifestation is a brief pair of green mechanical apertures in the
recovered directory, available only after forecast/return behavior and
suppressed permanently for that local trace.

## Website repository

- Local path: `/home/unix/signal-null`
- Canonical future repository name: `yiangwow/orison`
- Current stable branch: `main`
- Initial implementation commit: `b67bbb0`
- Continuity and aperture commit: `981d16e`
- Living Archive implementation commit: `43967a9`
- Git author: the owner's git identity
- Remote: `git@github-alt:yiangwow/orison.git` (history restarted 2026-11-18; older history is a private archive)
- Initial pull request: `private archive PR #1`
- Initial pull request state: merged
- Living Archive pull request: `private archive PR #5`
- Living Archive pull request state: merged
- Living Archive merge commit: `868b92805a502ef524b4272afe7d66a8ab8da185`
- Living Archive pull request checks: none configured or reported
- Deeper Mutations implementation commit: `6470b458966a7438e2ce220b373f6f3d2724a40b`
- Deeper Mutations pull request: `private archive PR #6`
- Deeper Mutations pull request state: merged
- Deeper Mutations merge commit: `45f2e1c5028f0c6245181c4c975c1a521d28f72e`
- Deeper Mutations pull request checks: none configured or reported
- Integrity Manifest implementation commit: `159c049f86b979ee4bbcb36a9c4c6f934f63355f`
- Integrity Manifest pull request: `private archive PR #7`
- Integrity Manifest pull request state: merged
- Integrity Manifest merge commit: `9d025b2eafc92ff1d023f850f1c851da692ecd3b`
- Integrity Manifest pull request checks: none configured or reported
- Visual revision implementation commit: `e2cf8a7374bfa9b96e320eb71550fbdaf2a2c65d`
- Visual revision pull request: `private archive PR #11`
- Visual revision pull request state: merged
- Visual revision merge commit: `08af964b3a3b190031c3257b4dd166b0ce0258c5`
- Visual revision pull request checks: none configured or reported
- Restrained Sound Language implementation commit: `d3ae5f7745b7c6791d27f18ba8d9bbef6c7f4c62`
- Restrained Sound Language pull request: `private archive PR #14`
- Restrained Sound Language pull request state: merged
- Restrained Sound Language merge commit: `6ead00311a5451e1949733d67de9af228a110e0f`
- Restrained Sound Language pull request checks: none configured or reported
- Warning visibility implementation commit: `9273737c9f6e596a0dc30c0c92eb9fffd192da9d`
- Warning visibility pull request: `private archive PR #15`
- Warning visibility pull request state: merged
- Warning visibility merge commit: `7ab4b87931bc813c3417ee37921350e6a381c6bb`
- Warning visibility pull request checks: none configured or reported
- Warning alignment implementation commit: `02165065843b8ea98c500e8ee7845bd16e3025cd`
- Warning alignment pull request: `private archive PR #17`
- Warning alignment pull request state: merged
- Warning alignment merge commit: `285cae61087aa34d1a34694949652f965eae63f8`
- Warning alignment pull request checks: none configured or reported
- Steady warning implementation commit: `e9f4dd994b63bd1700133eac957f37f317389c97`
- Carrier re-entry implementation commit: `5183919ad8fc93bd7da4884d4e57b97b0c6f0ed9`
- Final warning and Carrier pull request: `private archive PR #19`
- Final warning and Carrier pull request state: merged
- Final warning and Carrier merge commit: `f5d8ae5df3c7e0221989818ec852c3956f30699c`
- Final warning and Carrier pull request checks: none configured or reported
- Deployment-record pull request: `private archive PR #21`
- Deployment-record merge commit: `5426e09bc282be6898cb76021099908131570721`
- Processing-record copy pull request: `private archive PR #20`
- Processing-record copy merge commit: `e3a2036d947e92aeb6838334a939a570c0752f33`
- Digital Horizon implementation commit: `f1395be21ce1c648ca49210117bac8874e4d46e0`
- Digital Horizon pull request: `private archive PR #22`
- Digital Horizon pull request state: merged
- Digital Horizon merge commit: `6a0db930dd9fd58d4dac319627c8b2191fc8e3c7`
- Digital Horizon pull request checks: none configured or reported
- Feminine System Presence implementation commit: `9c85ca945fb453de2a60fbf78d0a7f703ea219c6`
- Feminine System Presence pull request: `private archive PR #23`
- Feminine System Presence pull request state: merged after retargeting from
  Digital Horizon to `main`
- Feminine System Presence merge commit: `5c5ff1ac492bdce1adf1c260bd39d9668b1e2d5d`
- Feminine System Presence pull request checks: none configured or reported
- Milestone 7 audit commit: `e05155a1af152c634a9b9f26f11fa6553abee212`
- Milestone 7 implementation commit: `086486260f69263e8e683b4a5c6325f5fd62fef0`
- Milestone 7 pull request: `private archive PR #26`
- Milestone 7 pull request state: merged; no checks configured or reported
- Milestone 7 merge commit: `16380094e71cbcb919ca14d4f3cf19451048780e`
- Milestone 8 implementation commit: `6904a6ea33e6aca4328918a5864e8025a305b764`
- Milestone 8 pull request: `private archive PR #27`
- Milestone 8 pull request state: merged; no checks configured or reported
- Milestone 8 merge commit: `abb011cae4f7b75b6c5be854f5edcd1236e4a2de`
- Shared recovery/history implementation commit: `ff61c74404f5b254d08f932b70559c9de1113bfa`
- Shared recovery/history pull request: `private archive PR #28`
- Shared recovery/history pull request state: merged; no checks configured or reported
- Shared recovery/history merge commit: `e79878ff4787e9c8ec861a058e8df080e52f9e1b`
- Shared-asset version implementation commit: `6c11cac3ca8770f426e524e12d36f83302cf21bd`
- Shared-asset version pull request: `private archive PR #30`
- Shared-asset version pull request state: merged; no checks configured or reported
- Shared-asset version merge commit: `0e7574cb65f5c4a9a011f41fdbada4e9297a59b7`
- Repository-native validation pull request: `private archive PR #33`
- Repository-native validation pull request state: merged; no checks configured or reported
- Repository-native validation merge commit: `065c1eb3ff8624d8a182c8bbaf88167985f16a83`
- Parent Process pull request: `private archive PR #34`
- Parent Process pull request state: merged; no checks configured or reported
- Parent Process merge commit: `faf1dcccd03a4292c7332afd54abbed6ca03f428`
- Migrating Gap implementation commit: `12460e59e342b5ca3be68a1a26c7299c7d3b49ba`
- Migrating Gap pull request: `private archive PR #35`
- Migrating Gap pull request state: merged; no checks configured or reported
- Operational Spine implementation commit:
  `a1319200e03aad843565484011bef7d6d915cb94`
- Operational Spine hierarchy refinement commit:
  `462327315d3cfa5e94a242c7ad21cdb46a953330`
- Operational Spine pull request: `private archive PR #37`
- Operational Spine pull request state: merged; no checks configured or reported
- Operational Spine merge commit:
  `1895f6c9bcdc4b1804b63f08efaa5e3fa6259ea8`
- Consequential Handoff implementation commit:
  `b2fd201e322fab63b252afa0447262d36030f694`
- Consequential Handoff pull request: `private archive PR #39`
- Consequential Handoff pull request state: merged; no checks configured or reported
- Consequential Handoff merge commit:
  `ece7fc63f46a251c4e39ad92f570d870f94c762a`

The local directory name `signal-null` is historical. Product naming is ORISON;
do not rename narrative references to SIGNAL NULL unless a future creative
decision explicitly introduces that phrase.

## Infrastructure repository

- Local path: `/home/unix/is-infra`
- Infrastructure pull request: `private infrastructure PR #2`
- Infrastructure pull request state: merged
- Service name: `orison`
- Expected server source path: `/home/tt/orison`
- Latest deployed website commit: `f0bcd969f77d7c71e728ab4077b8f36a83123177`
- Latest website deployment date: 2026-07-24
- Container state after deployment: running and healthy
- Container restarts after deployment: zero
- Public root, recovered archive, and fragment index: verified HTTP 200 through
  Cloudflare
- Public fixed fragment address `013`: verified intentional HTTP 404 through
  Cloudflare
- Public restrictive CSP, permissions, referrer, framing, and content-type
  headers: verified on the deployed root, archive, and missing fragment
- The complete desktop Playwright journey: passed against `https://orison.zip`
  after the terminal-bookend deployment; all six fragment request orders,
  interrupted operations, grandfathered state, fresh keyboard navigation,
  native Back/Forward, reduced motion, revisit/reload, erasure, migration,
  fresh context, Parent Process, Migrating Gap finality, and the retained root
  terminal remained intact, with zero browser errors and zero external requests
- Public root, recovered archive, Digital Horizon, Camera 06, Operator,
  warning, Carrier re-entry, and feminine-authority states: verified after
  the previous deployment
- Infrastructure checkout: `main` at
  `680d746f3bb00da964e9eb350e313f2e1047e3ae`
- Unrelated local Grafana, Loki, and Promtail work: preserved without modification
- Existing unrelated untracked file: `server-setup.sh` — preserve it

The infrastructure commit adds the Compose service, Homepage entry,
documentation, service registry entry, and Cloudflare Tunnel ADR.

## Cloudflare state

Confirmed in the Cloudflare dashboard:

- Domain: `orison.zip`
- Zone: active/protected by Cloudflare
- Old GoDaddy parking `A` records were deleted
- DNS record type shown by Cloudflare: `Tunnel`
- Tunnel target: `homelab`
- Proxy: enabled
- Published application route:
  - hostname: `orison.zip`
  - path: all
  - service: `http://orison:80`

Do not add an apex `A` or `AAAA` record. Do not expose the home IP. Cloudflare
manages the tunnel DNS record.

## Delivery status

GitHub access is restored. The Codex network allowlist includes `github.com`,
`api.github.com`, and `release-assets.githubusercontent.com`; the GitHub API
returns successfully and the CLI is authenticated as the owner's account.

The private repository was created without putting the implementation directly
on the default branch. A temporary `bootstrap` branch containing only the
repository baseline was pushed and renamed to `main` through the GitHub API.
The implementation history was then rebased onto that baseline and pushed as
`feat/initial-experience`.

The public hostname progressed from GoDaddy parking to the expected Cloudflare
502, then served ORISON after the container was deployed. On 2026-07-22 the
server checkout was fast-forwarded to `94ffb657`, only the `orison` Compose
service was rebuilt, and the replacement container reached healthy with zero
restarts. The tunnel, other services, and host-port exposure were unchanged.
Later that day, after pull request 37 merged, the website checkout was
fast-forwarded to `1895f6c`, the same targeted service-only build was repeated,
and the new container again reached healthy with zero restarts. The complete
browser journey then passed through the public Cloudflare hostname. The
infrastructure checkout, its unrelated monitoring work, the tunnel, and all
other services remained untouched. After pull request 39 merged, the website
checkout was fast-forwarded to `ece7fc6`; only the `orison` image and container
were rebuilt. The replacement reached healthy with zero restarts, public files
matched the merged source, and the complete desktop journey passed again with
no browser errors or external requests. Unrelated monitoring files and all
other services remained untouched.

## Ambient-observation revision

The current revision adds:

- a second command boundary requiring `mount directory` after compatibility;
- blinking block cursors at both terminal command prompts;
- quiet generated mechanical key clicks after keyboard interaction;
- real-system commands and residue such as `ps`, `dmesg`, watchdog, orphan,
  mount, interrupt, dwell, and process attachment;
- a shared peripheral receiver field on interior pages;
- pointer acquisition on the recovered inode;
- low-opacity process scale behind the recovered directory;
- state-aware dwell and return-event recognition.

No cookie fields, routes, third-party requests, permissions, or privacy
boundaries changed.

## Living Archive milestone

The recovered directory now behaves as active infrastructure:

- seven scheduler rows advance at unequal intervals through meaningful process
  states without visitor input;
- each recovered object reroutes or suppresses a different pair of processes;
- hover and keyboard focus share the same semantic response;
- sustained dwell temporarily reclassifies the selected object as retained;
- pointer or focus departure leaves a brief decaying process residue;
- tab return adds a retained interrupt to the visible watchdog log;
- reduced-motion mode preserves discrete state changes and reactions while
  removing continuous column drift;
- no durable state, cookie schema, route, permission, dependency, or privacy
  behavior changed.

## Deeper Mutations milestone

Existing version-1 cookie fields now produce larger, deterministic changes to
the same routes:

- the compatibility examination asks five questions, and the response channel
  becomes the final command-driven mount terminal;
- traces that already contain the original three answers resume at question
  four without migration or data loss;
- the first recovered room becomes the dominant source record on archive
  revisits, materially changing grouping and hierarchy according to visit order;
- after operator access, Camera 06 reconstructs the retained route and behavior
  counts instead of treating an optical frame as the dominant record;
- the first operator visit retains the temporary browser/environment profile;
- later operator visits invert `0 / operator absent` to `1 / operator inferred`,
  replace the profile with a route ledger, and display deterministic fictional
  interpretations of the five forced choices;
- those interpretations are visibly marked as non-diagnostic archive
  hypotheses; they make no medical or identity claim;
- no cookie field, schema version, route, dependency, permission, third-party
  request, or privacy behavior changed.

No ADR was added because the accepted stateful-static and local-observation
contracts are unchanged.

## New Recovered Object milestone

Integrity Manifest 32 is the fifth recovered archive object:

- it appears only after five complete examination answers and a later archive
  entry;
- it asks the visitor to reconstruct those five earlier choices with native
  radio groups;
- a live path connects the reconstructed copy, while verification reveals the
  retained-source path for direct visual comparison;
- exact attempted choices remain session-only;
- a complete agreement writes `checksum-match`; any contradiction writes
  `checksum-drift`;
- on revisit, controls and the attempted path are removed, and the retained
  answer path is presented as the authoritative copy;
- direct access from an incomplete trace produces an unavailable state and a
  route back to compatibility;
- the object counts toward archive progression and has distinct hover, focus,
  dwell, and process-residue behavior;
- Camera 06 and the operator ledger recognize the new route in retained order;
- no cookie schema field, permission, dependency, audio, external request, or
  privacy behavior changed.

No ADR was added because the route follows the accepted stateful-static design
and the two durable outcomes fit the existing explicit version-1 `flags` field.

## Milestones 1–3 visual-review revision

The post-deployment visual review produced a bounded corrective revision without
changing routes, persistence, permissions, or the privacy boundary:

- Integrity Manifest 32 uses a smaller container-safe heading and stacks before
  the reconstructed-copy title can cross its vertical divider;
- Camera 06 first presents a pre-exposed Weather 19 return event instead of an
  undifferentiated signal, while the forecast-return and later behavioral
  reconstruction states remain distinct;
- Weather 19 now renders a live fourteen-second navigation front tied to the
  predicted browser Back event and changes to retained-after-passage on revisit;
- the operator exposes an explicit return to the recovered directory without
  replacing browser Back behavior;
- all visitor-facing HTML copy avoids direct second-person address, including
  the five existing examination questions, while answer values and stored
  response vectors remain unchanged;
- the archive's first-opened-room hierarchy remains intentional and continues
  to identify the enlarged object as `first access` and the recovered source;
- no cookie field, schema version, route, dependency, permission, external
  request, or privacy behavior changed.

Milestone 8 originally reserved an explanatory inversion sentence for the
post-Operator response attachment. ADR 0009 removes it in favor of operational
reassignment and the final recovered URL.

## Restrained Sound Language milestone

Milestone 4 is merged and deployed:

- the root scan stages discovery without delaying terminal input;
- accepted archive operations arm a persistent accessible warning beside the
  discovered `orison.zip` object;
- the warning, Weather monitor, and Carrier 44 share the generated 41.2 / 61.8 /
  82.4 relationship, with deterministic state-dependent cadence and phase;
- hiding a tab suspends sound without cue accumulation and navigation closes
  the context; the warning remains steadily bright at every motion preference;
- root background degradation is selected from retained archive outcomes and
  expressed as scanner, buffer, retained-process, and missing-region state;
- Weather writes `forecast-held` when the predicted departure is missed, while
  Camera writes `forecast-returned` when browser Back fulfills the prediction;
- the immediate Weather → Back Camera frame now wins over later Operator state,
  and subsequent Camera access may still show the behavioral ledger;
- all Integrity result titles remain inside their copy pane at the documented
  apertures;
- first Operator access centers the missing `0`, subordinates temporary
  environment readings, and withholds hypotheses; later `1 / operator inferred`
  behavior is preserved;
- Carrier revisits and the later Operator ledger reflect coarse carrier and
  Weather state without persisting audio-device information or claiming audio
  continued across navigation; each explicit Carrier activation replaces any
  stale stopped graph, including after shared audio teardown and history return.
- The final visual-review correction keeps the triangle steadily bright red
  from discovery, removes its decorative flashing and state-dependent color,
  and preserves the corrected text baseline. The quiet relay cadence remains
  command-gated and state-dependent.

The milestone adds `warning-armed`, `forecast-returned`, and `forecast-held` to
the existing version-1 `flags` vocabulary. It adds no cookie field, migration,
route, dependency, permission, third-party request, or privacy change. No ADR
was required because the accepted stateful-static and local-observation
decisions remain unchanged.

## Digital Horizon milestone

Milestone 5 is merged and publicly deployed:

- the first eligible “return to recovered directory” action after Operator
  detours through `/.lost+found/00000000/extent/`;
- unearned direct access returns to the archive without recording an extent
  visit;
- a finite machine-city and maintenance gantry sit against receding green
  process and address fields, with a hatch, rail, ladder, and fault lamp as
  human-scale cues;
- the first entry has only extremely slow depth drift, while reduced motion and
  earned replay are deliberate still compositions;
- Operator restores its ordinary archive destination after `seen.extent`
  exists, so the forced detour cannot replay;
- an immediate extent-to-archive transition defers an eligible aperture slip
  until a later archive return;
- ordinary `seen`, `order`, and `last` route state express the contract without
  a new flag, schema version, permission, dependency, sound, external request,
  or privacy change;
- ADR 0005 records the accepted trigger, route, replay, and rollback contract.

## Feminine System Presence milestone

Milestone 6 is merged and publicly deployed after Digital Horizon:

- first Operator access remains the neutral `0 / operator not found`
  environmental instrument;
- a repeat Operator access before the Horizon remains neutral for compatibility
  with existing version-1 traces;
- the first post-Horizon Operator entry writes the coarse
  `operator-occupied` flag and changes `1` into an occupied authority topology;
- behavioral source, inherited privilege, operator role, and `SHE` authority
  reference are spatially related without identifying which entity `1` names;
- the repeat raw table is removed, while the five deterministic non-diagnostic
  archive hypotheses remain subordinate evidence;
- a later Camera 06 behavioral reconstruction becomes the second converging
  feminine record, while immediate Weather-to-Camera Back retains precedence;
- root, inode, examination, and dead letter remain neutral as incompatible
  older interface eras;
- generated sound remains nonverbal and unchanged;
- ADR 0006 records the trigger, durable state, route mutation, compatibility,
  and rollback contract.

The milestone adds no route, cookie field, schema version, migration,
dependency, permission, stored machine profile, audio behavior, external
request, portrait, voice, or privacy-boundary change.

## Post-Horizon immersion correction

The Level 1 correction is merged through pull request 25 and deployed:

- after the Horizon and before `operator-occupied`, the archive reclassifies
  Operator as a full-width `interrupt / operator return` record with
  `authority unresolved`, providing visible causal evidence for reopening it;
- the interrupt disappears after the accepted Operator occupation event and
  the ordinary `already open` row returns;
- the cue derives only from existing `seen.extent`, `operator-probe`, and
  `operator-occupied` state, so it adds no route, flag, schema, migration, or
  privacy change;
- Camera 06 now keeps its baseline frame concealed until the current trace has
  been rendered on initial load, reload, or history restoration, preventing a
  superseded optical state from flashing before the authority reconstruction;
- no ADR was added because the accepted trigger, route, replay, durable-state,
  and privacy contracts remain unchanged.

## Local Trace and Observation Audit milestone

Milestone 7 is accepted, merged through pull request 26, and deployed:

- a valid request-bearing version-1 cookie migrates once into a normalized,
  read-back-verified version-2 `localStorage` record and is then deleted;
- the record is limited to 2,048 UTF-8 bytes, a 30-day UTC-day logical expiry,
  allowlisted values, saturated counters, and capped collections;
- legacy trace IDs rotate because their generator included time bits;
- retained ORISON-only observations are limited to five command-category bits,
  a refused-command band, activation modality, and allowlisted recovered-object
  holds; raw text, keystrokes, pointer paths, exact timing, external activity,
  identity, and the ephemeral machine profile remain unstored;
- new witness invitations use a URL fragment, legacy query invitations remain
  compatible, and either form is scrubbed from the current history entry;
- erasure removes v2 and the legacy cookie, stops runtime activity, and prevents
  another open ORISON tab from resurrecting the deleted trace;
- Operator converts the four new bounded observations into one authored
  retained-intervention reading rather than a diagnostics table;
- ADR 0007 and `docs/LOCAL_TRACE_AUDIT.md` record the accepted field/storage,
  migration, route-consumer, privacy, erasure, and rollback contracts.

Local validation covers fresh, migrated, malformed, oversized, expired,
storage-unavailable, invitation, and two-tab-erasure states; the complete
existing journey; desktop, stacked, 375×812 mobile, and reduced motion; focus
and browser Back; Carrier lifecycle; local links; horizontal overflow; browser
errors and external requests; and an isolated nginx container.

## Apparent Transfer Log milestone

Milestone 8 is accepted, merged through pull request 27, and deployed:

- Operator access plus five retained answers earns a response-attachment phase
  inside `unpack orison.zip` without changing the restrained opening;
- ordinary recovery, inode, permission, checksum, and ownership lines expand
  into response sectors derived from the current trace ID, route order/counts,
  answers, command categories, refusal band, modality, held rooms, progression,
  returns, and optional witness;
- raw input, the visual transcript, line timing, and scroll position are never
  persisted;
- completion alone adds the coarse `response-attached` flag, changes later root
  boot language, and exposes a response-source record in the archive without
  replacing first-opened hierarchy or the post-Horizon Operator interrupt;
- replay is a condensed completed ledger and does not repeat the transition;
- reduced motion receives one discrete completed composition, while a separate
  polite status prevents transient lines from flooding screen readers;
- interrupted navigation writes no completion flag and history restoration
  returns enabled controls;
- ADR 0008 records the original placement; ADR 0009 and
  `docs/APPARENT_TRANSFER_LOG.md` record the amended trigger, privacy,
  accessibility, and rollback contract.

## Shared recovery field and unpack-attachment correction

The accepted post-deployment correction is merged through pull request 28 and
publicly deployed at `e79878f`:

- the root scanner, retained-process rows, and missing-region pressure now run
  as one state-derived background behind every HTML experience surface;
- the runtime explicitly restarts recovery and receiver scans on `pageshow`,
  including browser-history restoration, so a hard refresh is not required;
- the examination clears a disabled mount snapshot on departure and rebuilds
  the enabled command channel on return;
- Operator renders from the current result of its flag writes, preserving the
  deployed occupied authority and `SHE` state through migration and history;
- the detached inode uses a wider, larger signal composition at wide apertures;
- response attachment remains earned but is now an internal phase of unpack,
  and the recovered URL is the final output;
- the explanatory examination sentence is removed from visitor copy and canon;
- ADR 0009 records the accepted presentation, lifecycle, progression, privacy,
  and rollback contract.

The change adds no route, state field, flag, migration, permission, dependency,
external request, or privacy-boundary change. Post-deployment validation passed
the history, mount, SHE, M8, privacy, layout, and critical-journey matrices.

## Content-addressed shared assets

The Level 2 cache-consistency correction is merged through pull request 30 and
publicly deployed at `0e7574c`:

- Cloudflare continues to give shared assets a four-hour browser lifetime, but
  all fourteen HTML documents now request CSS and JavaScript with query values
  derived from the first twelve SHA-256 characters of each file;
- the deployed URLs are `base.css?v=c0081e9230da` and
  `orison.js?v=04aee4c1c272`;
- a new HTML release can no longer reuse an incompatible unversioned runtime or
  stylesheet from the browser cache;
- the first public requests returned a Cloudflare cache miss, and the complete
  unpack ending, scanner history restart, enabled mount, SHE, mobile/reduced
  layout, local links, and zero-external-request matrices passed publicly;
- ADR 0010 records the maintenance, privacy, and rollback contract;
- `deploy/verify_asset_versions.py` mechanically enforces the reference
  contract offline with the standard library only. Run it before deploying any
  change to `assets/` or to HTML asset references; it exits nonzero with
  file-and-line violations when a digest query is stale or missing.

The correction changes no runtime logic, narrative, retained state, erasure,
permission, dependency, nginx rule, Cloudflare route, or external request.

## Repository-native validation

The Level 1 testing improvement is merged through pull request 33:

- `tests/verify.py` starts and stops an ephemeral loopback server, validates all
  fourteen runtime HTML documents and their local references, and runs the
  retained-state journey in headless Chromium;
- the browser journey covers typed unpack, five answers, command-driven mount,
  Camera 06 → Weather 19 → native Back, Integrity reveal, Letter and first
  Operator access, invitation isolation, Digital Horizon, occupied feminine
  authority, response attachment, Parent Process eligibility/persistence, and
  cross-tab trace erasure;
- browser console/page errors and unintended external requests fail the run;
- `tests/requirements.txt` pins the test-only Playwright version, and
  `python3 tests/verify.py` is the documented single validation command;
- the new runner passed locally together with JavaScript syntax, asset-version,
  whitespace, and Python compilation checks.

The change added no runtime asset, route, narrative, state, migration,
permission, production dependency, deployment behavior, or privacy change. It
required no public deployment.

## Milestone 9: Parent Process

The Level 1 milestone is merged on `main` through pull request 34 and publicly
deployed from `94ffb657`:

- after both `operator-occupied` and `response-attached`, the archive exposes
  one parent-process interlock with the action `release orphan 00000000`;
- completion writes only the allowlisted `orphan-released` flag, changes all
  seven scheduler lanes and recovered-record states to an inherited parent
  relationship, and replaces the action with a persistent receipt;
- reload and later archive visits keep the completed composition without
  replaying the handoff; object names, links, first-room hierarchy, Operator,
  Horizon, Camera/Weather Back, audio, and response evidence remain intact;
- legacy-v1 migration excludes the version-2-only event, while existing
  storage-unavailable and cross-tab erasure contracts remain unchanged;
- ready/completed 1440×1000 and 375×812 captures are retained under
  `docs/review/milestone-9/`;
- the expanded local and strict-CSP production-image journeys passed together
  with reduced motion, mobile containment, asset digests, local references,
  JavaScript/Python syntax, browser errors, external requests, nginx
  configuration, `.lost+found` access, unrelated-dot-path denial, and healthy
  zero-restart container state.

The milestone adds no route, schema version, permission, sound, dependency,
backend, external request, portrait, manifestation, deployment configuration,
or privacy-boundary change.

## Post-program direction: Migrating Gap

The approved Level 2 direction is merged through pull request 35 without a
milestone number:

- `orphan-released` reveals one detached-child sequence link adjacent to the
  unchanged completed Parent Process receipt;
- the new sequence route exposes fixed missing addresses `013`, `027`, and
  `058`, each served through the existing custom HTTP 404 surface;
- the first eligible request writes exactly one allowlisted version-2 flag and
  native Back reveals that address assigned to the trace while its next child
  becomes absent;
- later requests preserve the first selection, generic 404 behavior remains
  unchanged, and the recovered-object hierarchy is not reordered;
- legacy migration excludes the three version-2-only flags, erasure removes
  them, and fixed request paths contain no trace, witness, answer, or local
  classification;
- the repository-native journey covers unearned access, all three branches,
  intentional HTTP 404 status, mutual exclusion, keyboard activation, native
  Back, stable replay, 375×812 containment, generic 404 preservation, migration,
  invitation isolation, cross-tab erasure, browser errors, and external
  requests.
- the production nginx image serves the fragment index as HTTP 200 and all three
  deliberate addresses as HTTP 404 with the accepted restrictive headers;
  unrelated dot paths remain HTTP 403, `nginx -t` passes, the complete browser
  journey passes against the container, and health reaches `healthy` with zero
  restarts.

The direction adds one route name and three allowlisted flags without changing
the version-2 record shape or size ceiling. It adds no motion, sound, permission,
dependency, backend, external request, manifestation, credential surface,
nginx rule, Cloudflare configuration, or server-side narrative state.

## Accepted future creative and state directions

- Milestones 7 and 8, their shared-field correction, and the asset-version fix
  are present in the public deployment at `0e7574c`.
- ADR 0015 accepts a state-derived terminal bookend for the current complete v2
  run. A finite end to ORISON or complete explanation remains unaccepted.

## Validation already completed

The following passed locally after the terminal entry was added:

- JavaScript syntax check for `assets/orison.js`;
- whitespace/error check with `git diff --check`;
- all local HTML links and assets resolve;
- terminal fresh state;
- typed `file` and `unpack` commands;
- delayed extraction and hidden-path reveal;
- `unpacked` cookie flag persistence;
- transition to the inode;
- changed terminal on return;
- mobile terminal layout;
- complete desktop route journey;
- examination answers and directory mount;
- mirror → weather → browser Back mutation;
- choir user-initiated audio state;
- staff observer insertion;
- dead-letter reveal;
- operator profile and invitation;
- invitation behavior in a fresh browser context;
- local trace erasure and fresh trace generation;
- mobile inode layout;
- no desktop or mobile browser console errors.
- one-time aperture slip after forecast/return behavior;
- aperture suppression on later archive visits;
- reduced-motion and narrow-mobile aperture presentation.
- V1.1 root terminal command and block-cursor behavior;
- compatibility answers followed by the `mount directory` command;
- incorrect mount commands leaving the receiver waiting;
- interior receiver field and pointer acquisition;
- archive dwell-retention state;
- desktop and narrow-mobile ambient presentation;
- reduced-motion receiver presentation;
- no browser console or page errors in the revised journey.
- 20-second unattended scheduler progression;
- object-specific hover and keyboard-focus process reactions;
- dwell retention, focus/pointer departure residue, and tab-return interrupts;
- archive cleanup after navigation and browser-history restoration;
- Living Archive desktop and narrow-mobile layouts;
- Living Archive reduced-motion behavior;
- full root → examination → archive → operator regression after the milestone;
- local-only requests and no browser console or page errors after the milestone.
- five-question fresh progression and command-driven mount continuity;
- legacy version-1 traces with three answers resuming at question four;
- all four possible first-room archive source branches through deterministic
  `order` state;
- distinct first and repeat operator compositions and answer-derived inference;
- post-operator Camera 06 behavioral reconstruction;
- Deeper Mutations desktop and narrow-mobile layouts without horizontal
  overflow;
- keyboard focus, dwell retention, and pointer-departure residue after archive
  recomposition;
- reduced-motion behavior for the archive and Camera 06 mutations;
- one-time aperture manifestation and permanent suppression after revisit;
- full fresh root-to-operator progression with no browser console/page errors
  and no non-local network requests.
- Integrity Manifest reveal after complete examination and archive return;
- exact-match and one-sector-drift comparisons;
- visible divergence between reconstructed and retained paths;
- locked match and drift revisit states;
- incomplete direct-route handling without writing an outcome flag;
- native radio keyboard traversal and object-specific archive focus reaction;
- Integrity Manifest desktop, narrow-mobile, and reduced-motion behavior;
- no horizontal overflow, browser console/page errors, new permissions, or
  non-local requests in the new object matrix;
- the complete Milestone 2 regression matrix after adding Object 32.

The home-server Docker image was rebuilt from merged `main`, the `orison`
container was recreated without restarting dependencies, and its healthcheck
reported `healthy` with a zero failure streak. The served container filesystem
and the public Cloudflare route both contained Integrity Manifest 32.

The complete Milestone 2 and Milestone 3 Playwright matrices also passed against
`https://orison.zip`, covering the stateful critical journey, Living Archive,
Deeper Mutations, Integrity Manifest match/drift/locked revisit states, desktop,
narrow mobile, keyboard behavior, reduced motion, overflow, browser errors, and
third-party requests.

The Milestones 1–3 visual-review revision additionally passed locally across:

- first, forecast-return, and post-operator Camera 06 states;
- first and confirmed Weather 19 navigation-front states;
- Integrity Manifest layouts at 2560×1319, 1336×910, 960×900, and 375×812 with
  measured title/divider separation;
- operator-to-archive keyboard focus and route resolution;
- desktop, narrow mobile, and reduced-motion presentation;
- the complete Milestone 2 and Milestone 3 regression matrices;
- no horizontal overflow, browser console/page errors, or non-local requests.

After deployment at `08af964`, the complete Milestone 2 and Milestone 3
Playwright matrices passed again against `https://orison.zip`. The public root
and Integrity Manifest routes returned HTTP 200, the served Camera 06 and
Weather 19 documents contained their new operational compositions, and the
recreated `orison` container reported `running/healthy`.

Milestone 4 local validation passed:

- original root commands, staged discovery, unpack, hidden-path reveal, five
  questions, refused and accepted mount commands, and fresh, existing,
  malformed, and erased version-1 cookie behavior;
- root warning activation, synchronized relay frequencies, persistent visual
  state, hidden-tab suspension without queued cues, clean return cadence,
  navigation teardown, reduced-motion steady warning, and trace erasure;
- Weather source-remains completion and retained event, native browser Back,
  protected immediate Camera frame with existing Operator state, and later
  Camera behavioral reconstruction;
- first-opened archive hierarchy, keyboard focus, Integrity radio traversal,
  Carrier activation and reactivation after audio teardown and browser-history
  return, staff, dead letter, Operator `0 → 1`, invitation in a fresh context,
  one-time aperture, and permanent suppression;
- all five Integrity outcomes at 2560×1319, 1336×910, 960×900, and 375×812;
- root, archive, Camera, Weather, Integrity, Carrier, and Operator layouts at
  desktop, stacked, and narrow-mobile apertures without horizontal overflow;
- reduced-motion root and Carrier behavior, no browser console/page errors, all
  local HTML links and assets, and no external browser requests.

After deployment at `f5d8ae5`, the server checkout matched merged `main` and the
recreated `orison` container reported `running/healthy` with a zero failure
streak. Live Playwright assertions confirmed the warning remains steadily
bright from discovery at normal and reduced-motion preferences, its 4.4-second
relay remains command-gated, alignment and narrow-mobile containment remain
correct, and the public site makes zero external requests and emits zero browser
errors. Carrier validation confirmed native AudioContext teardown closes the
first graph and explicit reactivation creates a new running three-oscillator
graph. Back → Forward and Back → reopen both reset and reopen Carrier correctly.

Milestone 5 local and container validation passed:

- unearned direct extent access returned to the archive without writing
  `seen.extent`;
- first Operator access remained `0 / operator not found`, wrote the existing
  `operator-probe`, and routed its first archive-return action through extent;
- first extent entry wrote ordinary route state, exposed only one keyboard
  target, and retained native Back through extent to Operator;
- extent replay and reduced motion were still while the first-view process
  field retained a 214-second drift;
- immediate extent-to-archive entry suppressed aperture overlap without writing
  `aperture-slip`, while a later archive return still presented and retained the
  one-time manifestation;
- desktop 1440×1000, 2560×1319, stacked 960×900, narrow 375×812, and reduced
  motion layouts had zero horizontal overflow and kept the egress in view;
- static screenshots at all five apertures retained the finite structure,
  foreground gantry, human-scale maintenance details, and unbounded text field;
- the complete root, five-question examination, command mount, first-opened
  hierarchy, Camera/Weather Back, Integrity, Carrier, Staff, letter, Operator,
  invitation, aperture, erasure, and root-degradation journey remained valid;
- Milestone 2, Milestone 3, Milestone 4, root-warning, native Carrier, and
  Carrier teardown/re-entry regressions remained valid;
- all fourteen local HTML documents and assets resolved with no external links;
- the nginx image built successfully, served the extent with the existing CSP,
  denied unrelated dot paths, passed `nginx -t`, and reported healthy with zero
  failures or restarts;
- all targeted and full-browser runs reported zero console/page errors and zero
  unintended external requests.

Milestone 6 local and container validation passed:

- unchanged stacked baseline from root extraction through five questions,
  command mount, first Operator `0`, Horizon, and native Back to Operator `1`;
- fresh `0`, legacy neutral `1`, first post-Horizon occupation, one-time
  `operator-occupied` writing, and stable occupied replay;
- later Camera authority reconstruction and protected immediate Weather Back
  precedence;
- desktop 1440×1000, 2560×1319, intermediate 960×900, stacked 700×900, narrow
  375×812, and reduced motion Operator layouts without horizontal overflow;
- Camera authority layouts at the same aperture matrix without horizontal
  overflow;
- keyboard focus order through Operator return, leave, and invitation actions;
- original terminal commands and steady warning, five-question examination,
  command-driven mount, first-opened archive hierarchy, Integrity match and
  locked replay, native Carrier teardown/re-entry with a new AudioContext,
  Digital Horizon/aperture separation, one-time aperture, invitation, root
  degradation, and trace erasure;
- fourteen local HTML documents and assets resolve with no external links;
- all browser runs reported zero console/page errors and zero unintended
  external requests;
- nginx image build, configuration test, Operator and Camera HTTP 200, unrelated
  dot-path HTTP 403, and container `running/healthy` with zero restarts.

Before implementation, local `main`, GitHub `main`, the clean server checkout,
the running server container, and the public site were verified at
`e3a2036d947e92aeb6838334a939a570c0752f33`. The public processing record matched
the server checkout and running container byte-for-byte.

After approval, pull request 22 was merged first. Pull request 23 was then
retargeted from the Milestone 5 branch to `main`, verified to contain only the
Milestone 6 layer, and merged. The server checkout fast-forwarded cleanly to
`5c5ff1ac492bdce1adf1c260bd39d9668b1e2d5d`; only the `orison` service was
rebuilt and recreated.

Post-deployment validation confirmed:

- the server checkout and running container match merged `main` for the extent
  and Operator documents;
- the container is `running/healthy` with zero restarts and valid nginx
  configuration;
- public root, extent, Operator, and Camera routes return HTTP 200, unrelated
  dot paths return HTTP 403, and the extent and Operator documents match the
  server/container byte-for-byte;
- restrictive CSP, Permissions Policy, and framing headers remain present;
- the complete fresh public journey, Camera/Weather Back, first-opened
  hierarchy, Integrity, native Carrier teardown/re-entry, extent/aperture
  separation, Operator occupation, later Camera authority, invitation, root
  warning/degradation, and trace erasure pass;
- public 1440×1000, 2560×1319, 960×900, stacked 700×900, 375×812, and reduced
  motion layouts have no horizontal overflow;
- public validation reports zero console/page errors and zero unintended
  external requests.

The post-Horizon immersion correction passed locally at 1440×900, 2560×1319,
stacked 700×1000, and 375×812, plus reduced motion. Validation covered the
extent-earned archive interrupt, keyboard focus, Operator occupation, resolved
archive revisit, Mirror initial load and reload, Mirror browser Back after the
occupation event, horizontal overflow, local-only requests, and zero console or
page errors. The Docker image also built successfully; an isolated container
served both corrected documents, passed `nginx -t`, remained running with zero
restarts, and was removed after validation. Review captures live in
`docs/review/post-horizon-immersion/`.

Milestone 8 local and production-image validation passed:

- unearned typed refusal, earned typed and quick activation, real trace-derived
  sectors, completion-only flag writing, later root state, condensed replay,
  interrupted navigation, reduced motion, archive response record, legacy-v1
  flag exclusion, 2,048-byte storage budget, no narrative cookie, and complete
  erasure;
- the complete existing root, examination/mount, archive hierarchy,
  Camera/Weather Back, Integrity, Carrier lifecycle, Letter, Operator, Horizon,
  aperture, authority, invitation, degradation, and erasure journey;
- Milestone 7's fresh, migrated, malformed, oversized, expired,
  storage-unavailable, invitation, and two-tab-erasure matrix;
- 2560×1319, 960×900, stacked 700×900, 375×812, and reduced-motion root/archive
  layouts with restored input focus and no horizontal overflow;
- concise accessibility status, fourteen local documents/assets, zero browser
  errors, and zero unintended external requests;
- nginx build/configuration, root/archive HTTP 200, unrelated dot-path HTTP 403,
  custom HTTP 404, restrictive headers, and isolated container
  `running/healthy` with zero restarts. The focused browser suite also passed
  against the production image.

The infrastructure repository's full `docker-compose config` is blocked locally
by a pre-existing legacy Compose interpolation issue in the unrelated
`docker-cleanup` command. The ORISON service block itself is structurally
straightforward and was reviewed independently. Do not silently fix that
unrelated command as part of ORISON delivery.

## Next exact sequence

1. Keep the deployed Controlling Source → unresolved Operator → Extent →
   occupied Operator sequence as the accepted current baseline.
2. Preserve the terminal bookend, cumulative fragments, local-only state,
   native Back, invitation isolation, erasure, and verified mobile aperture.
3. Reassess speculative expansion only after stabilization; no new post-ending
   operation or site-wide fault effect is accepted.

Rollback:

- rebuild only `orison` from
  `ce3e6e53d4d21644502b629b83075d206974d276` to remove both the mobile aperture
  containment and Controlling Source deployment;
- restore the prior unversioned asset references if the cache-key contract must
  be removed; no state or infrastructure migration is required;
- after deployment, restore the root-only field and standalone attachment
  behavior while keeping `response-attached` allowlisted;
- rebuild only `orison` from the selected last accepted commit;
- no state conversion or trace cleanup is required;
- leave Cloudflare, tunnel routes, ports, and unrelated services untouched.
- for the testing-only review branch, revert its single logical commit; no
  production rollback or state action is required.
- for Milestone 9, restore the prior shared-runtime query and archive document
  while leaving `orphan-released` allowlisted until expiry or erasure; no state
  conversion, service dependency, or infrastructure rollback is required.
- for Migrating Gap, remove the fragment route, archive entry, and specialized
  404 branch while leaving its three flags allowlisted but inert until expiry or
  erasure; no state conversion or infrastructure rollback is required.
- for the Operational Spine, rebuild only `orison` from the last accepted
  public source `94ffb657`; existing version-2 state remains readable and no
  state, infrastructure, tunnel, or privacy migration is required.
- for the Consequential Handoff Pass, rebuild only `orison` from the prior
  accepted public source `1895f6c`; no route, state, migration, infrastructure,
  tunnel, or privacy rollback is required.
