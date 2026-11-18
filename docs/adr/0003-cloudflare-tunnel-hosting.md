# ADR 0003: Host ORISON through the existing Cloudflare Tunnel

Date: 2026-07-16

Status: Accepted

## Context

`orison.zip` requires HTTPS in normal browsers because `.zip` is HSTS-preloaded.
The site will run on a home server. Publishing the origin address or forwarding
router ports would expose unnecessary home-network surface. The server already
runs the remotely managed `homelab` Cloudflare Tunnel on the `self-hosted`
Docker network.

## Decision

Run ORISON as a dedicated nginx container named `orison` with no published host
ports. Route the Cloudflare public hostname `orison.zip` through the existing
`homelab` tunnel to `http://orison:80` over the private Docker network.

Keep website source in its own repository, expected at `/home/tt/orison` on the
server. Keep Compose wiring in the separate `is-infra` repository.

## Consequences

- Cloudflare provides public HTTPS without exposing the home IP.
- No router port forwarding or origin TLS certificate management is required.
- The existing tunnel is a dependency for availability.
- Website updates require updating the source and rebuilding the container.
- Cloudflare DNS should show a tunnel-managed proxied record, not an apex origin
  `A` record.
- Rollback is to remove/disable the published hostname and stop the `orison`
  container; other tunnel routes remain unchanged.
