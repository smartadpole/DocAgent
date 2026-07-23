---
type: template
id: TEMPLATE-IMPLEMENTATION-PROJECT-PROFILE-001
status: active
updated: 2026-07-23
tags: [template, implementation, project, agent-system, harness]
---

# 实现类工程 Profile 模板

用于把任意主控、子工程、服务、数据 / 模型工程或文档治理工程接入 wiki 的实现类工程模板系统。它不是项目状态页，也不替代 TASK / issue / report / service registry。

## 基本信息

- **project_name**：
- **project_role**：controller / subproject / runtime-service / data-model / documentation-governance / hybrid
- **repo_path / owner**：
- **source_of_truth**：
- **current_branch_policy**：
- **remote capability boundary**：

## Owner Surfaces

| Surface | Path / owner | Status | Boundary |
| --- | --- | --- | --- |
| AGENTS / local adapter |  |  |  |
| project homepage |  |  |  |
| service registry |  |  |  |
| work-item chain | Gate / FP / EP / TASK / todo |  |  |
| memory / trace / log |  |  |  |
| reports / acceptance |  |  |  |
| handoff / engineering feedback |  |  |  |

## Agent System Layers

| Layer | Local owner | Evidence | Verdict |
| --- | --- | --- | --- |
| skill |  |  | complete / partial / blocked |
| runtime |  |  | complete / partial / blocked |
| harness |  |  | complete / partial / blocked |
| memory |  |  | complete / partial / blocked |
| evaluation |  |  | complete / partial / blocked |
| governance |  |  | complete / partial / blocked |
| migration |  |  | complete / partial / blocked |

## Control Plane

- **Goal Contract**：
- **Loop policy**：
- **Run Capsule policy**：
- **Orchestrator role**：
- **Worker / subproject dispatch**：
- **Evaluator owner**：
- **Issue policy**：
- **Persistence Decision**：
- **Monitoring / heartbeat / lease**：

## Implementation Boundaries

- **Allowed writes**：
- **Forbidden writes**：
- **Subproject Git Preflight**：
- **Dirty / diverged / local-only decision**：
- **Generated artifacts boundary**：
- **Secrets / credentials boundary**：
- **Rollback / recovery path**：

## Evidence Contract

| Evidence layer | Required proof | Not enough to prove |
| --- | --- | --- |
| code-level / unit |  |  |
| functional / business-flow |  |  |
| service-side |  |  |
| end-to-end |  |  |
| non-default / boundary |  |  |
| related regression |  |  |
| manual-confirmation |  |  |

## Template Adoption

| Wiki capability | Decision | Local landing | Boundary |
| --- | --- | --- | --- |
| response-mode-routing | use / adapt / defer / reject |  |  |
| goal-contract | use / adapt / defer / reject |  |  |
| loop-engineering | use / adapt / defer / reject |  |  |
| agent-orchestration | use / adapt / defer / reject |  |  |
| research-capability | use / adapt / defer / reject |  |  |
| issue-analysis | use / adapt / defer / reject |  |  |
| documentation-maintenance | use / adapt / defer / reject |  |  |
| problem-focused-visual-presentation | use / adapt / defer / reject |  |  |
| public-html-publish | use / adapt / defer / reject |  |  |
| retrospective-capability | use / adapt / defer / reject |  |  |
| work-item-auto-decomposition | use / adapt / project-bound / reject |  |  |

## Closeout Proof

- **local validation**：
- **service-side validation**：
- **end-to-end validation**：
- **manual confirmation boundary**：
- **blocked_for_done**：
- **not_blocked_for_implementation**：
- **handoff / report path**：
- **next action**：stop / split / retry-after / wait-human / schedule-next
