# Milestone 7 review captures

Status: Merged through pull request 26 and deployed at `abb011c`

These captures exercise the accepted browser-only trace architecture and the
bounded retained-intervention reading on repeat Operator access.

## Captures

| Capture | Viewport | State |
| --- | --- | --- |
| [`operator-desktop-2560x1319.png`](operator-desktop-2560x1319.png) | 2560 × 1319 | retained Operator intervention reading |
| [`operator-stacked-960x900.png`](operator-stacked-960x900.png) | 960 × 900 | stacked retained reading |
| [`operator-mobile-375x812.png`](operator-mobile-375x812.png) | 375 × 812 | mobile retained reading |
| [`operator-reduced-1440x1000.png`](operator-reduced-1440x1000.png) | 1440 × 1000 | reduced-motion completed composition |

## Accepted contract

The complete field/storage, migration, and route-consumer matrices are in
[`docs/LOCAL_TRACE_AUDIT.md`](../../LOCAL_TRACE_AUDIT.md). ADR 0007 accepts a
one-way migration from the request-bearing version-1 cookie to a normalized,
2,048-byte browser-only version-2 record. Retained observations are limited to
five coarse command-category bits, a refused-command band, activation modality,
and the allowlisted recovered objects that crossed the existing hold threshold.

The implementation retains no raw command, keystroke, pointer path, exact
event time, activity outside ORISON, identity, or durable machine profile. New
witness tokens use URL fragments; legacy query tokens remain compatible and
are scrubbed after capture. Complete erasure removes both stores and prevents
another open tab from restoring the deleted trace.

## Validation evidence

- Fresh v2, valid v1 migration with trace-ID rotation and coarsening, malformed
  JSON and nested state, oversized state, expired state, unavailable storage,
  fragment and legacy-query invitations, two-tab erasure, and the 2,048-byte
  limit passed in Chromium.
- The complete established journey passed: restrained root terminal and steady
  warning, five-question examination and command-driven mount, first-opened
  hierarchy, Camera/Weather browser-Back precedence, Integrity, native Carrier
  teardown and re-entry, Dead Letter, Operator, Digital Horizon, one-time
  aperture, post-Horizon return interrupt, later Camera state, root
  degradation, invitation, and trace erasure.
- Desktop 2560×1319, stacked 960×900 and 700×900, mobile 375×812, and
  reduced-motion layouts passed across thirteen routes without horizontal
  overflow. Keyboard/focus behavior and all fourteen local HTML documents and
  assets passed.
- Browser validation reported zero console/page errors and zero unintended
  external requests.
- The nginx image builds; `nginx -t` passes; root and archive return HTTP 200;
  unrelated dot paths return HTTP 403; the custom missing route returns HTTP
  404; restrictive response headers remain; and the isolated container runs
  with zero restarts.

## Privacy and rollback

Steady-state narrative data is no longer attached to matching HTTP requests.
Cloudflare/nginx request metadata and already-copied witness links remain
outside ORISON-controlled erasure, as disclosed in `privacy.txt`.

Before deployment, close or revert this branch. After deployment, prefer a
behavioral rollback that keeps the v2 adapter and erasure contract. Reverting
the storage architecture requires an explicit v2-to-v1 converter; a plain code
revert would make migrated traces appear fresh. No rollback changes Cloudflare,
tunnel routing, ports, or unrelated services.
