# ORISON project continuity

This file is the entry point for every future development session in this
repository. ORISON is intended to be a long-running project. Do not rely on chat
history as the source of truth.

## Required reading order

Before changing the experience, read:

1. `VISION.md` for the creative contract and narrative boundaries.
2. `ARCHITECTURE.md` for the current route graph, state model, privacy boundary,
   and deployment design.
3. `docs/CURRENT_STATE.md` for current delivery status and known blockers.
4. `docs/EXPANSION_SESSIONS.md` for the ordered multi-session expansion program.
5. `ROADMAP.md` for additional possible work. Roadmap items are not accepted
   canon.
6. Relevant records in `docs/adr/` before changing an accepted decision.

The repository-level instructions inherited from `/home/unix/AGENTS.md` still
apply.

## Vision authority and amendments

`VISION.md` is the strong default, not an infallible authority. The owner's
standing rule (2026-07-25): canon authority can be minimal when project
cohesion can be improved.

- Any agent may propose a change that contradicts accepted canon when it
  strongly believes the piece becomes more coherent. The proposal must argue
  cohesion on merit; "it is in VISION.md" is not by itself a sufficient defense
  of the status quo, and novelty is not by itself a sufficient case for change.
- Cohesion is measured against the experienced whole — the emotional
  progression, the honesty contract, scarcity discipline, and the
  administrative register — not against the letter of any single passage.
- Peer reviewers evaluate canon-breaking proposals on cohesion merit.
  Rejecting a proposal solely because it contradicts `VISION.md` is not a
  valid finding.
- An accepted discovery is written into `VISION.md` (or an ADR) in the same
  change that adopts it: deliberate amendment, never drift. Unrecorded
  divergence from canon remains a defect.
- This rule rescues creative disagreements only. Factual errors, privacy
  regressions, and technical-honesty violations are never justified by it.
- The owner remains the arbiter for contested amendments.

## Durable project contracts

- The canonical name is **ORISON** and the canonical domain is `orison.zip`.
- The visitor believes they are investigating ORISON. The deeper truth is that
  ORISON constructed a curiosity trap and is examining the visitor.
- This realization must emerge gradually. The first page must not explain the
  premise.
- Horror comes from hostile intelligence, anticipation, implication, changed
  context, and loss of interpretive control.
- Do not use gore, jumpscares, shock images, scream audio, or cheap glitch spam.
- Leave ORISON's origin, body, exact purpose, and ultimate capability unresolved.
- Interpretation takes priority over revelation. Never confirm one explanation
  when several disturbing explanations can remain viable.
- ORISON's future presence is intentionally feminine, but she must remain
  nonhuman and difficult to localize. Establish femininity through language,
  authority, and conflicting system records rather than a stable female avatar,
  sexualization, or a copied character voice.
- ORISON must not become a consistently visible character. Any apparent body,
  face, voice, or direct presence should be rare, transient, and deniable—as if
  the interface failed to conceal something rather than chose to introduce it.
- The project needs occasional changes of visual scale. Not every route should
  feel like a flat terminal or document. A rare horizon-scale scene may use a
  finite foreground structure against an effectively unbounded field of system
  text, while preserving ambiguity about whether the space is literal.
- Returning and backward navigation are first-class interactions. Previously
  visited pages should be allowed to change.
- Observation must remain theatrical and privacy-respecting: first-party local
  state only, no analytics, no server-side visitor profile, and no camera,
  microphone, geolocation, clipboard, local-file, credential, or contact access.
- Never expose the home-server IP or open router ports for this project.
- Preserve the hidden-path fiction. New routes should feel recovered,
  misaddressed, orphaned, or operational rather than like normal website pages.
- Influences include *Serial Experiments Lain*, SHODAN, *System Shock*, and
  early-web experimental sites, but implementation and writing must be original.
  Do not reproduce another site's code, copy, layout, imagery, or exact devices.

## Documentation discipline

After a meaningful session:

- Update `docs/CURRENT_STATE.md` with what exists, what was verified, and what is
  blocked.
- Update `ARCHITECTURE.md` when routes, state fields, privacy behavior, runtime,
  or deployment structure change.
- Update `VISION.md` only when the creative contract changes.
- Add an ADR when a decision is difficult to reverse or constrains future work.
- Update `ROADMAP.md` when an idea is accepted, rejected, completed, or replaced.
- Update `docs/EXPANSION_SESSIONS.md` when a planned milestone begins, changes
  scope, completes, or is superseded.
- Keep accepted facts out of the speculative sections and speculative ideas out
  of the accepted architecture.

## Implementation rules

- Prefer plain HTML, CSS, and browser JavaScript unless a concrete need justifies
  a build system.
- Prefer one strong interaction per page over a collection of decorative effects.
- Keep pages usable with keyboard navigation and respect reduced-motion settings.
- New state must be versioned and documented. Do not silently repurpose existing
  cookie fields or flags.
- A new page should define:
  - what the visitor thinks the page is;
  - what ORISON learns or causes;
  - what changes on revisit;
  - what state it reads and writes;
  - where it leads;
  - why it could not be replaced by an existing page.
- Do not add external dependencies or third-party requests without an explicit
  architectural decision and privacy review.

## Validation contract

At minimum, changes should preserve:

- root terminal boot and extraction;
- extraction revealing `/.lost+found/00000000/`;
- cookie persistence across routes;
- changed root and archive pages after progression;
- browser Back behavior between Camera 06 and the weather log;
- invitation URLs in a fresh browser context;
- local trace erasure;
- all local links and assets;
- desktop and narrow mobile layouts;
- no browser console errors;
- nginx access to `.lost+found` while denying unrelated dot paths.
