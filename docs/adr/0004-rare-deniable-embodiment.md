# ADR 0004: Keep ORISON's embodiment rare, transient, and deniable

Date: 2026-07-16

Status: Accepted; scheduling narrowed by ADR 0015

## Context

The experience needs visual horror strong enough to make accumulated
observation emotionally undeniable. A persistent pair of watching eyes would
communicate surveillance clearly, but it would also define ORISON as a visible
character, explain too much, and turn a disturbing image into a repeatable
interface feature.

Interpretation is a central requirement. Visitors should be able to construct
different stories from the same evidence.

## Decision

ORISON will not have a stable body, face, avatar, or repeatedly accessible
appearance.

The first apparent embodiment will be two green mechanical apertures that appear
in the recovered directory only after the visitor has activated the forecast
and returned. The interface will expose them briefly without sound, text, or
interaction, then repair itself. A local `aperture-slip` flag prevents replay
for that browser trace.

The form will remain ambiguous enough to read as eyes, optical machinery,
damaged video, interface residue, or pareidolia. No later page will confirm what
was seen.

## Consequences

- The moment can be visually memorable without becoming ORISON's official face.
- Many visitors may miss it or doubt it; that uncertainty is intentional.
- Automated tests must force the eligible state and verify both appearance and
  permanent suppression.
- Future manifestations must be rarer or meaningfully different, not a series of
  recurring eye effects.
- Documentation may describe implementation mechanics, but visitor-facing copy
  must not explain the event.
- Accessibility requires a motion-reduced presentation, not removal of the
  narrative event.
