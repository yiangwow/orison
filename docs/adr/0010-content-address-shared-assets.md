# ADR 0010: Content-address shared browser assets

Date: 2026-07-18

Status: Accepted

## Context

ORISON serves HTML with immediate revalidation, but Cloudflare currently gives
the unversioned shared CSS and JavaScript URLs a four-hour browser cache
lifetime. After a deployment, a returning browser can therefore combine new
HTML with an older `base.css` or `orison.js`. The shared-field deployment made
that mismatch visible: old JavaScript does not export `renderRecoveryField`, so
the new unpack sequence can stop before its final text, archive URL, and restored
input. The same mismatch can leave the shared scanner absent until a hard
refresh.

## Decision

Reference `base.css` and `orison.js` from every HTML document with a query value
derived from the first twelve characters of that file's SHA-256 digest. All
documents in one release use the same URL for a given shared asset. Whenever a
shared asset changes, update its digest query in every HTML reference before
deployment.

Keep the existing filenames, Cloudflare route, nginx headers, CSP, and static
container design. Do not add a build system or change browser-retained narrative
state for this correction.

## Consequences

- A browser requests a new URL when either shared asset changes, preventing a
  new HTML document from executing against an older cached runtime or stylesheet.
- History navigation can still reuse one internally consistent release of each
  asset; normal reloads no longer require a hard refresh after deployment.
- The query values are operational release metadata only. They contain no trace,
  identity, observation, or invitation data and do not change erasure behavior.
- Future shared-asset edits must include a mechanical reference update across
  all HTML surfaces. `deploy/verify_asset_versions.py` checks that every HTML
  document references both shared assets with the current digest queries; run it
  before any deployment that changes a shared asset or an HTML reference.
- The mechanism depends on Cloudflare keying its cache on the full URL including
  the query string (the zone's default Standard caching level, confirmed by the
  post-deployment cache miss on the new URLs). Configuring the zone or a cache
  rule to ignore query strings would silently disable versioning and serve stale
  asset bodies for new queries; such a configuration change must be treated as a
  breaking change to this decision.
- Rollback is to restore the prior asset queries or the unversioned references.
  Both underlying files remain ordinary same-origin static assets, so no state or
  infrastructure migration is required.
