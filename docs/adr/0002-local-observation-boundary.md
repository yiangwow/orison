# ADR 0002: Keep observation local, coarse, and technically honest

Date: 2026-07-16

Status: Accepted

## Context

The central horror premise is that ORISON has noticed the visitor. Browser APIs
can expose coarse environmental details, and a server could collect IP-derived
or fingerprinting data. More invasive collection could make the effect stronger
in the moment but would violate the intended trust and privacy boundary.

The experience must not claim capabilities it does not possess or create actual
compromise to simulate fictional compromise.

## Decision

Use only first-party local narrative state and coarse browser-provided values
rendered on the operator page. Do not persist the machine profile. Do not use
analytics, advertising, third-party scripts, fingerprinting services, IP
lookups, or an application backend.

Do not request camera, microphone input, geolocation, clipboard, local files,
contacts, credentials, payment, or USB access. User-initiated Web Audio output
is allowed because it neither records input nor transmits data.

Provide a plain-language processing record and an explicit local trace erasure
route.

## Consequences

- The operator scene remains invasive in tone without being invasive in fact.
- The site cannot determine exact identity or correlate separate browsers.
- Invitations contain only a random prior trace token.
- The current privacy design is simple and auditable.
- Adding server storage, analytics, external services, or more identifying
  signals requires a new decision and consent/legal review.
- Writing and timing must carry much of the horror instead of relying on hidden
  data collection.
