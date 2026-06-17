# Loop Engineering Governance

Loop Engineering is a governance control plane for continuous agent loops. It sits above Goal Contract, Run Capsule, harness feedback, and repo-local sensors. It does not create a parallel project state, issue board, release flow, or unattended automation permission.

## Maturity Contract

A loop is mature only when all of the following are explicit:

- discovery source: where new findings come from and how noisy inputs are filtered
- run queue: how findings move through queued, running, passed, partial, blocked, failed, or skipped
- worker ownership: which agent owns which files, evidence, and stop conditions
- evaluator oracle: which sensor, reviewer, or readback decides the result
- persistent state: where durable outcomes are written back
- quality gate: what acceptance criteria must pass before a loop result can be called closed
- benchmark: what baseline, previous run, or best practice the loop is compared against
- next-run decision: continue, narrow, promote, stop, or ask for human review

## Quality Gate

The quality gate for this repo is:

- `python3 scripts/check_all.py --only loop-engineering` must pass after any loop wiring change.
- A worker result without evaluator evidence is partial, not passed.
- A loop result cannot close project status, publish a release, or rewrite governance rules unless the owning page and human confirmation allow it.
- The final response must name the files changed, checks run, unresolved blockers, and next-run decision.

## Benchmark

The local benchmark is AcknowledgeBase Loop Engineering: skill body, TRANSFER boundary, Loop Contract, Run Capsule, orchestration governance, and sensor wiring. This repo adapts that benchmark to wiki governance without copying source project facts.

## Anti-Patterns

- Do not create a new `loop/` board when an existing project, issue, log, or governance page owns the state.
- Do not treat repeated agent activity as maturity without a quality gate.
- Do not use Loop Engineering to bypass manual approval, merge, release, production writes, or policy changes.
- Do not copy AcknowledgeBase paths, scores, project facts, run IDs, or handoff examples into this repo.

## Persistence

Durable results land in the owning page: governance, skill, template, log, issue, report, or sensor. The loop contract only records the control plane; it is not the source of truth for project facts.
