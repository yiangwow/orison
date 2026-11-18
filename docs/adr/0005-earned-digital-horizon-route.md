# ADR 0005: Place the Digital Horizon on an earned interstitial route

Date: 2026-07-17

Status: Accepted

## Context

ORISON needs a first major change of visual scale without turning the recovered
directory, Operator, or another established document into a reusable scenic
background. The scene must follow earned progression, remain compatible with
native browser history, and stay separate from the one-time mechanical aperture
manifestation.

A temporary replacement of the recovered directory would couple the scene to
Living Archive state, first-opened hierarchy, and aperture timing. A permanent
archive object would make the scene an ordinary replayable feature rather than
a rupture in the visitor's mental map.

## Decision

Add `/.lost+found/00000000/extent/` as a state-earned interstitial route. The
route is earned by opening Operator and then selecting its existing “return to
recovered directory” action. On the first eligible selection, that action leads
to the extent instead of directly to the archive. The Operator scene itself is
unchanged.

Direct access before `operator-probe` replaces the route with the recovered
directory and does not record an extent visit. An earned entry uses the unique
page state name `extent`; the existing `seen`, `order`, and `last` fields record
the visit. No new flag or cookie version is required.

The first entry contains extremely slow depth drift. History or direct revisits
remain possible after earning but render the same composition as a deliberate
still. Once `seen.extent` exists, Operator's return action again leads directly
to the archive. The immediate extent-to-archive transition suppresses the
aperture slip for that one archive entry; aperture eligibility is preserved for
a later return.

## Consequences

- The horizon has a genuine hidden URL and participates in native Back/Forward
  history without becoming a recovered directory object.
- The unexpected first detour cannot be replayed from Operator. Replay loses
  motion and displacement, not the spatial composition.
- Existing version-1 traces remain valid. `seen.extent` is ordinary route state
  and contributes to existing awareness calculations.
- The route adds no permission, external request, dependency, stored machine
  profile, or privacy-boundary change.
- Tests must cover unearned direct access, first detour, replay stillness,
  Operator restoration, browser Back, and aperture separation.
- Before deployment, rollback is to remove the route and restore the two route
  conditions. After deployment, a revert may temporarily ignore `extent` in
  awareness and ledger presentation until existing 30-day traces expire.
