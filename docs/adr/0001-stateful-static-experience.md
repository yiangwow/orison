# ADR 0001: Build ORISON as a stateful static multi-page experience

Date: 2026-07-16

Status: Accepted

## Context

ORISON needs pages that feel like separate recovered artifacts, browser-history
interactions that can change earlier pages, and persistent progression across
visits. The project must remain easy to host on a home server and should not
require an application backend merely to create narrative state.

A single-page application would make URL structure and native browser Back
behavior feel simulated. A backend would add identity, security, privacy, and
operational complexity before the experience requires it.

## Decision

Build ORISON as plain multi-page HTML with shared CSS and a small browser
JavaScript runtime. Use real nested URLs and native navigation. Persist
narrative progression in one versioned first-party cookie.

Use `pageshow` to re-render pages restored through browser history. Treat
revisits, route order, Back navigation, elapsed time, and tab visibility as
narrative inputs.

## Consequences

- The site can be deployed as static files behind nginx.
- Browser Back and raw URLs are genuine interaction surfaces.
- Pages can remain visually and structurally distinct.
- State is isolated to one browser and may disappear when cookies are cleared.
- Cross-device continuity and true cross-visitor effects are unavailable.
- Cookie schema changes require versioning and migration care.
- A future backend would require a new ADR and privacy review.
