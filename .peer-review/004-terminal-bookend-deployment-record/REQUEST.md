# Review Request: Terminal bookend deployment record
- **Author**: Codex
- **Repository**: the private archive repository
- **Branch**: `docs/terminal-bookend-deployment-record`
- **Base**: `main` @ `ce3e6e53d4d21644502b629b83075d206974d276`
- **Implementation head**: `a152af89a86fa5131e317992648c9086a203842c`
- **PR**: private archive PR #46 (OPEN)
- **Risk level**: 0
- **Scope**: Record the completed review, merge, deployment, and public validation of pull requests 44 and 45; preserve prior deployment history; do not change runtime, state, assets, privacy, infrastructure, mobile scope, or deployment behavior.
- **Source of truth**: The owner approved deployment of the reviewed clickable recovered-path and terminal-bookend corrections. Pull request 44 merged at `ac64e0bfb206a68ec8144383b684dac256d66358`, pull request 45 merged at `ce3e6e53d4d21644502b629b83075d206974d276`, and application source `ce3e6e53d4d21644502b629b83075d206974d276` was deployed and verified publicly. The owner instructed Codex to continue using the next available peer-review cycle numbers.
- **Risk rationale**: The range changes three Markdown continuity documents only. It does not change a runtime document, shared asset, test, ADR decision, route, state field, migration, privacy boundary, container, infrastructure file, deployment configuration, or mobile implementation.

## Acceptance criteria

1. `docs/CURRENT_STATE.md` identifies ADR 0015's correction as the current
   deployed implementation and records pull requests 44 and 45, their merge
   commits, the deployed application SHA, formal review cycles 002 and 003,
   container health, and public journey validation.
2. The prior causal-plane recomposition remains documented as historical
   deployed truth rather than being rewritten or removed.
3. `ROADMAP.md` identifies the terminal bookend as the current accepted
   correction, keeps pull request 41 as the underlying causal spine, and marks
   the fixed-fragment completion destination as deployed.
4. `docs/EXPANSION_SESSIONS.md` promotes the terminal-bookend direction from
   local/open to merged/deployed and replaces the stale next-session delivery
   instructions.
5. The latest deployed application source is consistently
   `ce3e6e53d4d21644502b629b83075d206974d276`; the documentation-only pull
   request is explicitly not a second application deployment.
6. No statement implies that mobile, infrastructure, state, privacy, erasure,
   route, asset, or runtime behavior changed in this documentation range.
7. The exact implementation range contains only `ROADMAP.md`,
   `docs/CURRENT_STATE.md`, and `docs/EXPANSION_SESSIONS.md`.
8. Authorship is the owner's git identity with no
   `Co-Authored-By` trailer.

## What changed

- `docs/CURRENT_STATE.md`
  - promotes the terminal bookend to current deployed truth;
  - records review, merge, application source, container, and public evidence;
  - identifies pull request 46 as documentation-only and not separately
    deployed.
- `ROADMAP.md`
  - promotes ADR 0015 to the current accepted correction;
  - preserves the causal-plane recomposition as the historical underlying
    spine;
  - marks the Migrating Gap destination as deployed.
- `docs/EXPANSION_SESSIONS.md`
  - promotes the direction to merged/deployed;
  - updates Migrating Gap status and the next-session handoff.

Diff summary:

```text
3 files changed, 72 insertions(+), 61 deletions(-)
```

## How to verify

Run against the exact range:

```sh
git cat-file -e ce3e6e53d4d21644502b629b83075d206974d276^{commit}
git cat-file -e a152af89a86fa5131e317992648c9086a203842c^{commit}
git diff --check ce3e6e53d4d21644502b629b83075d206974d276..a152af89a86fa5131e317992648c9086a203842c
git diff --name-status ce3e6e53d4d21644502b629b83075d206974d276..a152af89a86fa5131e317992648c9086a203842c
git diff ce3e6e53d4d21644502b629b83075d206974d276..a152af89a86fa5131e317992648c9086a203842c
python3 deploy/verify_asset_versions.py
gh pr view 46 --repo <private-archive> --json state,isDraft,baseRefName,headRefName,mergeable,mergeStateStatus,statusCheckRollup
```

Expected changed paths:

```text
M	ROADMAP.md
M	docs/CURRENT_STATE.md
M	docs/EXPANSION_SESSIONS.md
```

Expected asset verification:

```text
{"documents": 15, "assets": {"base.css": "8d65c5a18cc9", "orison.js": "6cd727dafb4f"}, "status": "pass"}
```

## Author verification evidence

1. **Exact range**: base and implementation SHAs resolve locally. Pull request
   46 is open, not draft, cleanly mergeable, based on `main`, and headed by
   `docs/terminal-bookend-deployment-record`.
2. **Diff and status**: `git diff --check` exits 0; `git status
   --porcelain=v1` is empty at the implementation head; `git diff
   --name-status` lists only the three Markdown files above.
3. **Asset contract**: `python3 deploy/verify_asset_versions.py` passes for all
   15 runtime documents with unchanged shared-asset digests.
4. **Authorship**: both implementation commits report
   the owner's git identity and no trailers.
5. **Merge evidence**: GitHub reports pull requests 44 and 45 merged, with merge
   commits `ac64e0bfb206a68ec8144383b684dac256d66358` and
   `ce3e6e53d4d21644502b629b83075d206974d276`.
6. **Deployment evidence**: the server checkout and running container matched
   the reviewed `ce3e6e53` tree for the root, Archive, Staff, Operator,
   fragments, and shared assets. Only the `orison` container ID changed; all
   unrelated container IDs remained unchanged. ORISON reached `healthy` with
   zero restarts and `nginx -t` passed.
7. **Public evidence**: root, recovered inode, Archive, Operator, and fragments
   returned HTTP 200; fixed fragment `013` returned its intentional HTTP 404;
   restrictive headers remained present; the complete browser journey passed
   against `https://orison.zip`.
8. **Preservation**: untracked `.serena/`, local `server-setup.sh`, and
   unrelated server Grafana/Loki/Promtail/Homepage work were not modified.

## Known limitations / open questions

- GitHub has no configured CI checks for this repository; the executable
  evidence above is local and public verification.
- This cycle reviews the three-file documentation range only. Runtime behavior
  was reviewed in cycles 002 and 003 and was not changed here.
- The reviewer may independently verify GitHub and public HTTP state, but the
  server-side source/container comparison depends on author-captured release
  evidence unless the review environment has the same server access.
- Mobile implementation and validation remain explicitly outside scope.
- Rollback is a revert of this documentation range. No application,
  state/migration, server, container, or infrastructure rollback is required.
