# Milestone 8 review captures

Status: Merged through pull request 27 and deployed at `abb011c`; trigger later amended by ADR 0009

These captures exercise the accepted post-Operator response attachment, its
reduced-motion composition, and the resulting recovered-directory record.

## Captures

| Capture | Viewport | State |
| --- | --- | --- |
| [`root-transfer-desktop-2560x1319.png`](root-transfer-desktop-2560x1319.png) | 2560 × 1319 | completed accelerating response ledger |
| [`root-transfer-mobile-375x812.png`](root-transfer-mobile-375x812.png) | 375 × 812 | contained mobile ledger and final assignment |
| [`root-transfer-reduced-1440x1000.png`](root-transfer-reduced-1440x1000.png) | 1440 × 1000 | discrete reduced-motion composition |
| [`archive-response-1440x1000.png`](archive-response-1440x1000.png) | 1440 × 1000 | response-source record with hierarchy and Operator interrupt preserved |

## Accepted contract

The complete trigger/state/replay and visible-state matrices are in
[`docs/APPARENT_TRANSFER_LOG.md`](../../APPARENT_TRANSFER_LOG.md). ADR 0008
originally accepted a standalone attachment in the late root terminal after
Operator access and five answers. ADR 0009 folds it into earned unpack while
preserving the final operation and `response-attached` state;
legacy version-1 migration cannot import that later event.

The visual ledger reconstructs bounded route, answer, progression, command,
modality, refusal, hold, return, and optional witness evidence. It never stores
the transcript, raw command, keystrokes, exact timing, or scroll position.

## Validation evidence

- Unearned typed operation, earned typed and quick activation, real
  state-derived lines, final flag timing, later root boot, condensed replay,
  interrupted navigation, reduced motion, archive mutation, v1 exclusion,
  2,048-byte budget, no narrative cookie, and complete erasure passed in
  Chromium.
- The complete established journey passed: original root terminal/commands and
  steady warning; five questions and command-driven mount; first-opened
  hierarchy; Camera/Weather browser Back; Integrity; native Carrier
  teardown/re-entry; Dead Letter; Operator/Horizon/replay; one-time aperture;
  post-Horizon interrupt; authority state; invitation; degradation; and trace
  erasure.
- Milestone 7's fresh, migrated, malformed, oversized, expired,
  storage-unavailable, fragment/legacy invitation, and two-tab-erasure matrix
  remains passing.
- Root and archive passed at 2560×1319, 960×900, stacked 700×900, 375×812,
  and reduced motion with enabled controls, restored input focus, and no
  horizontal overflow.
- The transient ledger is `aria-hidden`; a separate visually hidden polite
  status exposes only start/review and final assignment.
- Fourteen local HTML documents and assets resolve. Browser validation reported
  zero console/page errors and zero unintended external requests.
- `node --check assets/orison.js` and `git diff --check` pass.
- The nginx image builds; `nginx -t` passes; root/archive return HTTP 200;
  unrelated dot paths return HTTP 403; the custom missing route returns HTTP
  404; restrictive response headers remain; and the isolated container is
  healthy with zero restarts. The focused M8 browser suite also passes against
  that production image.

## Privacy and rollback

The milestone adds one coarse completion flag under the accepted browser-only
retention, size, request-exposure, and erasure contract. It adds no observation,
permission, backend, analytics, external request, or durable machine profile.

Before deployment, close or revert this branch. After deployment, prefer
disabling the trigger and archive mutation while continuing to allowlist
`response-attached` until expiry or erasure. A full Milestone 7 revert drops the
unknown flag and restores the earlier interpretation without converting any
other state. No rollback changes Cloudflare, tunnel routing, ports, or unrelated
services.
