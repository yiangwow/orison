# Milestone 5 visual review

Status: Merged and deployed

Deployed baseline: `5c5ff1ac492bdce1adf1c260bd39d9668b1e2d5d`

Pull request: `private archive PR #22`

Milestone 5 was merged before Milestone 6 and deployed with it. The accepted
trigger, route, state, and revisit matrix is recorded in
[`docs/EXPANSION_SESSIONS.md`](../../EXPANSION_SESSIONS.md#selected-route-and-replay-contract)
and ADR 0005.

## Review apertures

| Capture | Aperture | Motion condition |
| --- | --- | --- |
| [`extent-desktop.png`](extent-desktop.png) | 1440 × 1000 | first entry / 214-second drift |
| [`extent-2560.png`](extent-2560.png) | 2560 × 1319 | first entry / 214-second drift |
| [`extent-stacked.png`](extent-stacked.png) | 960 × 900 | first entry / 214-second drift |
| [`extent-mobile.png`](extent-mobile.png) | 375 × 812 | first entry / 214-second drift |
| [`extent-reduced.png`](extent-reduced.png) | 1440 × 1000 | reduced-motion deliberate still |

## Validation evidence

- Static depth remains legible at every aperture through occlusion, perspective
  convergence, luminance falloff, and process-text density.
- The maintenance rail, hatch, ladder, and fault lamp remain visible as
  human-scale cues without introducing a person or body.
- Unearned access is gated; first Operator return detours once; Back and direct
  replay are still; later Operator return restores the archive destination.
- Immediate aperture overlap is deferred while later one-time eligibility is
  retained.
- Every aperture has zero horizontal overflow, one keyboard target, zero browser
  errors, and zero unintended external requests.
- The complete existing state, sound, warning, Carrier lifecycle, and journey
  regression suites remain valid.
- The nginx feature image served the hidden route, denied unrelated dot paths,
  and reported healthy with zero failures or restarts.

## Rollback

Revert Milestone 6 first if both milestones must be removed, then revert
Milestone 5 and rebuild only the `orison` container. Do not change Cloudflare,
tunnel, or unrelated services.
