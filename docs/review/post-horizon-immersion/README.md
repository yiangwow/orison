# Post-Horizon immersion correction review

Status: Awaiting visual review

This corrective branch makes the missing causal step visible without changing
the accepted Milestone 5 or 6 state contract. After `extent` and before
`operator-occupied`, the existing Operator archive record becomes an interrupt:
`operator return / authority unresolved`. Reopening Operator writes the already
accepted occupation event, after which the row returns to `already open`.

Camera 06 also conceals its baseline document until the stateful renderer has
selected the current trace composition. The gate is restored on `pagehide`, so
initial load, reload, and browser-history restoration cannot expose the old
optical frame before the authority reconstruction.

## State contract

| Existing state | Archive result | Operator result | Revisit result |
| --- | --- | --- | --- |
| no `seen.extent` | ordinary Operator row | existing first or legacy state | unchanged |
| `seen.extent`, no `operator-occupied` | full-width return interrupt; authority unresolved | next entry records occupation under ADR 0006 | interrupt remains until Operator is reopened |
| `operator-occupied` | ordinary `already open` row | occupied authority topology | stable; no replay announcement |
| trace erased | fresh gated progression | fresh `0` | correction leaves no state to clean up |

No new route, flag, cookie field, schema version, migration, permission,
dependency, external request, audio behavior, or privacy behavior is added.

## Captures

- `archive-operator-return-desktop.png` — 1440×900
- `archive-operator-return-mobile.png` — 375×812

## Validation

- archive cue at 1440×900, 2560×1319, 700×1000, and 375×812;
- deliberate still presentation under reduced motion;
- keyboard focus on the Operator interrupt;
- extent-earned cue, occupation write, and resolved archive revisit;
- first-opened archive hierarchy remains dominant;
- Camera 06 initial load, reload, and browser Back expose only the selected
  retained composition;
- no horizontal overflow, browser console/page errors, or external requests.
- Docker image build, isolated nginx configuration test, corrected-route
  serving, and zero container restarts.

## Rollback

Remove the derived archive interrupt styling/render branch and the Camera 06
render-visibility gate. Existing traces require no migration or cleanup because
the correction writes no state.
