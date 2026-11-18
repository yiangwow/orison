# Milestone 6 visual review

Milestone 6 was reviewed as a stack on Digital Horizon, then retargeted to
`main` after Milestone 5 merged. Both milestones are deployed. Review the
Operator transition after the Horizon before reviewing the later Camera state.

Review pull request: `private archive PR #23`

## Accepted route and state matrix

| State | Operator | Camera 06 | Durable effect | Revisit / Back |
| --- | --- | --- | --- | --- |
| before Horizon | neutral `0 / operator not found` | existing states | existing `operator-probe` | archive return detours through extent |
| repeat before Horizon | neutral `1 / operator inferred` topology | existing states | none | preserves earlier traces |
| first post-Horizon Operator entry | `1 / operator occupied`; `SHE` authority reference | unchanged until entered | `operator-occupied` | later Operator entries retain authority state |
| immediate Weather Back | — | retained two-subject frame | existing forecast flags | Back precedence remains protected |
| later Camera entry | occupied Operator state retained | feminine authority reconstruction | none | stable on later reconstruction |
| trace erased | fresh `0` | fresh Camera | all local state removed | earning sequence resets |

## Screenshot apertures

- `operator-desktop.png`: 1440 × 1000
- `operator-2560.png`: 2560 × 1319
- `operator-stacked.png`: 700 × 900
- `operator-mobile.png`: 375 × 812
- `operator-reduced.png`: 1440 × 1000 with reduced motion
- `camera-authority.png`: 1440 × 1000 later Camera reconstruction

## Review questions

- Does the central `1` read as role, count, and possible entity without settling
  which interpretation is correct?
- Is `SHE` unmistakable but subordinate to the authority relationship rather
  than presented as a character introduction?
- Does Camera feel like a second system converging on the same classification,
  rather than a repeated announcement?
- Do the neutral root, inode, examination, and dead-letter eras remain legible
  as incompatible older records?

## Validation evidence

- Unchanged root → five questions → command mount → Operator `0` → extent →
  native Back baseline passed before implementation.
- Fresh `0`, legacy neutral `1`, post-Horizon occupation, stable replay, Camera
  convergence, and Weather Back precedence passed.
- The complete stateful journey passed through first-opened hierarchy,
  Integrity match/locked replay, Carrier teardown/re-entry with a replacement
  AudioContext, aperture separation and suppression, invitation, root warning
  and degradation, and trace erasure.
- Operator and Camera passed at 1440×1000, 2560×1319, 960×900, stacked
  700×900, 375×812, and reduced motion with no horizontal overflow.
- Keyboard focus order, all fourteen local documents and assets, zero external
  requests, and zero browser console/page errors passed.
- The nginx image built successfully; Operator and Camera returned HTTP 200,
  unrelated dot paths returned HTTP 403, nginx configuration passed, and the
  review container reached `running/healthy` with zero restarts.

## Rollback

Revert Milestone 6 before Milestone 5 if both must be removed, then rebuild only
the `orison` container. Earlier code ignores `operator-occupied`; the unknown
flag expires with the existing cookie or is removed by trace erasure.
