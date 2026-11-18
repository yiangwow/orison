# ORISON

An original multi-page browser horror experience built as a forbidden archive.
The visitor appears to investigate a damaged system while bounded, first-party
browser state lets the archive observe and react to their behavior.

There is no gore, no jumpscare, no camera or microphone access, and no external
tracking.

## Project documentation

ORISON is a long-running project. Durable creative and technical context lives
in the repository:

- [`AGENTS.md`](AGENTS.md) — required reading order and session rules
- [`VISION.md`](VISION.md) — creative thesis, canon, tone, and boundaries
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — routes, state, privacy, runtime, and hosting
- [`ROADMAP.md`](ROADMAP.md) — future possibilities and rejected directions
- [`docs/CURRENT_STATE.md`](docs/CURRENT_STATE.md) — delivery state and exact next steps
- [`docs/EXPANSION_SESSIONS.md`](docs/EXPANSION_SESSIONS.md) — ordered expansion milestones and session contracts
- [`docs/adr/`](docs/adr/) — accepted architectural decisions

## Run locally

The experience expects to be hosted at the root of a domain:

```bash
cd /home/unix/signal-null
python3 -m http.server 4173
```

Open `http://localhost:4173/`.

The public page is a black-and-green recovery terminal built around the
`orison.zip` domain name. Running `unpack orison.zip` reveals the first hidden
route as a raw URL:

```text
/.lost+found/00000000/
```

## Release

The site is a Compose service on the home server; a release updates the
separate checkout there and rebuilds only `orison` (steps in
`is-infra/projects/self-hosted/README.md`).

**Remove the running container before bringing the new one up.** Twice on
2026-09-08 `docker compose up -d --build --no-deps orison` wedged partway:
the old container would not stop, a half-made twin sat in `Created`, the
tunnel resolved to the dead twin and the whole site answered 502 until the
container was removed by hand (once the Docker daemon itself had to be
restarted, which bounced every service on the host for about a minute).
Building first and swapping after shortens the outage but does not prevent
the wedge: on 2026-09-11 `docker rm -f orison` hung again after a clean
build. The only step that has worked every time is restarting the daemon,
which costs every service on the host about fifteen seconds:

```bash
git -C /home/tt/orison fetch origin main && git -C /home/tt/orison merge --ff-only origin/main
cd /home/tt/is-infra/projects/self-hosted
docker compose build orison                           # site still serving
docker rm -f orison && docker compose up -d --no-deps --no-build orison   # try this first
# if the remove or the recreate hangs (it has, three times out of four):
sudo systemctl restart docker && sleep 15
for c in $(docker ps -a --format '{{.Names}}' | grep -i orison); do docker rm -f "$c"; done
docker compose up -d --no-deps --no-build orison
curl -sI https://orison.zip/ | head -1
```

Always check for a stray `<hash>_orison` container afterwards and remove
it; a leftover twin is what the tunnel hits on the next release. The root
cause is not diagnosed: the container's own process stops responding to
`docker kill`, and only this service has shown it.

## Validate locally

Install the pinned browser-test dependency and Chromium once:

```bash
python3 -m pip install -r tests/requirements.txt
python3 -m playwright install chromium
```

Then run the static-reference and critical-journey checks with one command:

```bash
python3 tests/verify.py
```

The test starts and stops its own loopback HTTP server. Its fresh canonical path
uses keyboard activation through unpack and mount, Camera 06 → Weather 19 →
browser Back, Integrity, Staff, Letter, late Operator and Horizon state,
response attachment, Parent Process, and the detached-fragment request. It also
covers completed-state replay, invitation isolation, cross-tab erasure,
intentional 404 responses, browser errors, and unintended external requests.

## State and privacy

Version 2 stores the bounded narrative record in first-party `localStorage`
under `orison_trace_v2` for up to 30 days. The legacy version-1
`orison_trace` cookie is read only as a one-way migration source and is then
removed; normal v2 operation does not use a request-bearing cookie.

The operator page reads coarse browser characteristics locally for theatrical
effect. It does not save those characteristics. There is no backend, analytics,
IP lookup, or third-party request.

See `/privacy.txt` for the visitor-facing processing record and `/erase/` for
the reset control.

## Hosting

Upload the complete directory—including `.lost+found`—to a static web root.
Configure the host to:

- serve `index.html` as the directory index
- preserve dot-prefixed directories
- use `404.html` as the custom not-found page
- serve over HTTPS
- avoid adding third-party analytics scripts

Some upload tools ignore dot-prefixed directories by default. Verify that
`.lost+found/00000000/` exists on the deployed host.

## Container deployment

Build and run the included nginx image:

```bash
docker build -t orison .
docker run --rm -p 8080:80 orison
```

For the home-server deployment, the container is not published on a host port.
The existing Cloudflare Tunnel connects to `http://orison:80` over the private
Docker network.
