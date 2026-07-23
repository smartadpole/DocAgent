---
type: template
id: TEMPLATE-IMPLEMENTATION-PROJECT-PROFILE-001
status: active
updated: 2026-07-23
tags: [template, implementation, project, agent-system, harness]
---

# 实现类工程 Profile 模板

用于把任意主控、子工程、服务、知识库、数据 / 模型工程、文档治理工程、运维 agent 或 hybrid 工程接入 wiki 的实现类工程模板系统。它不是项目状态页，也不替代 TASK / issue / report / service registry。

本模板不要求目标工程复制 wiki 整套结构。它把 wiki 作为“Template Kernel + Project Profile Overlay + Capability Pack”的模板母体来使用：先声明工程画像，再选择能力包，最后写清不能上推的项目事实和 closeout proof。

## 基本信息

- **project_name**：
- **project_role**：controller / subproject / runtime-service / knowledge-base / documentation-governance / data-model / ops-agent / hybrid
- **primary_profile**：
- **secondary_profiles**：
- **profile_overlay**：controller-profile / subproject-profile / runtime-service-profile / knowledge-base-profile / ops-agent-profile / data-model-profile / lightweight-repo-profile / hybrid-profile
- **required_capability_packs**：
- **optional_capability_packs**：
- **forbidden_capability_packs**：
- **required_packs**：
- **optional_packs**：
- **forbidden_packs**：
- **repo_path / owner**：
- **source_of_truth**：
- **current_branch_policy**：
- **remote capability boundary**：

## Template-Facing Boundary

- **template_identity**：Template Kernel + Project Profile Overlay + Capability Pack。
- **source_provenance_location**：内部 registry / 审计报告 / 上游 topic / 历史 log。
- **source_deidentification_rule**：模板正文使用工程角色、能力包和证据边界；不使用来源工程名作为 profile、capability 或默认事实。
- **project_bound_facts**：路径、服务、数据、模型、运行 ID、业务事实、机器、端口、账号、一次性 handoff。

## Template Kernel

| Kernel area | Use / adapt / defer / reject | Local owner | Boundary |
| --- | --- | --- | --- |
| agent entry / AGENTS |  |  |  |
| governance / workflow |  |  |  |
| harness / Goal / Run Capsule |  |  |  |
| memory / trace / log |  |  |  |
| skill / templates |  |  |  |
| evaluation / sensor |  |  |  |
| migration / handback |  |  |  |

## Project Profile Overlay

| Profile overlay | Decision | Local defaults enabled | Disabled / forbidden defaults |
| --- | --- | --- | --- |
| controller-profile | use / adapt / defer / reject |  |  |
| subproject-profile | use / adapt / defer / reject |  |  |
| runtime-service-profile | use / adapt / defer / reject |  |  |
| knowledge-base-profile | use / adapt / defer / reject |  |  |
| data-model-profile | use / adapt / defer / reject |  |  |
| ops-agent-profile | use / adapt / defer / reject |  |  |
| lightweight-repo-profile | use / adapt / defer / reject |  |  |
| hybrid-profile | use / adapt / defer / reject |  |  |

## Capability Packs

| Capability Pack | Decision | Local landing | Boundary |
| --- | --- | --- | --- |
| work-item-control-pack | required / optional / forbidden |  |  |
| runtime-control-plane-pack | required / optional / forbidden |  |  |
| research-intelligence-pack | required / optional / forbidden |  |  |
| visual-publication-pack | required / optional / forbidden |  |  |
| acceptance-governance-pack | required / optional / forbidden |  |  |
| memory-trace-log-pack | required / optional / forbidden |  |  |
| subproject-handoff-pack | required / optional / forbidden |  |  |
| ops-diagnostics-pack | required / optional / forbidden |  |  |

## Adoption Matrix

| Field | Value |
| --- | --- |
| `project_role` |  |
| `primary_profile` |  |
| `secondary_profiles` |  |
| `required_packs` |  |
| `optional_packs` |  |
| `forbidden_packs` |  |
| `project_bound_facts` |  |
| `closeout_proof` |  |

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
