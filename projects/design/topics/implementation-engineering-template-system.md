---
type: design-topic
id: DES-TOPIC-IMPLEMENTATION-TEMPLATE-001
project: PROJ-WIKI-001
status: accepted-design
stage: implementation-template
updated: 2026-07-23
tags: [design, implementation, template, agent-system, harness]
---

# 实现类工程合集与模板系统

上游：[[projects/design/topics/README]]、[[agent-system-maturity]]

相关：[[agent-system-cross-project-alignment.v1]]、[[projects/development/plan/work-item-system-model]]、[[agent-orchestration]]、[[templates/implementation-project-profile-template]]

## 定位

当前 wiki 不再只是一套普通知识库模板。它的目标角色是**所有实现类工程的合集与模板**：主控仓库、子工程、运行服务、数据 / 模型工程、文档治理工程、前端 / 后端 / CLI / worker / scheduler 都要能在这里找到最小可复制的 owner、合同、技能、模板、sensor 和验收边界。

这页是实现类工程模板系统的设计 owner。它不保存任何具体工程的运行 ID、端口、业务表、服务状态或一次性 handoff；具体项目事实仍留在各项目自己的 owner、service registry、TASK / issue / report 或 handoff 中。

## 工程类型覆盖

| 工程类型 | wiki 必须提供的模板能力 | 本仓落位 |
| --- | --- | --- |
| 主控 / controller | Goal、Run Capsule、事项主链、验收裁决、子工程回传、不上推边界 | [[agent-orchestration]]、[[templates/run-capsule-template]]、[[projects/development/plan/work-item-system-model]] |
| 子工程 / implementation repo | Subproject Git Preflight、allowed writes、handoff、代码 / runtime 证据 | [[templates/harness-adoption-template]]、[[templates/code-handoff-template]]、[[templates/implementation-project-profile-template]] |
| runtime-service | service registry、health / smoke / config profile、blocked readback | [[projects/service-registry]]、[[state-constraint-reasoning]] |
| 数据 / 模型工程 | source freshness、non-default / boundary evidence、readback、evaluation correction | [[agent-system-maturity]]、[[projects/development/reports/README]] |
| 文档 / 知识工程 | owner-first、trace、memory、log、topic placement、documentation maintenance | [[projects/memory/README]]、[[projects/trace]]、[[documentation-maintenance-rules]] |
| 调研 / 选型工程 | Research Contract、Source Ledger、evidence matrix、adoption contract | [[skills/research-capability/SKILL]]、[[templates/research-intake-template]] |

## Implementation Project Profile

任何新实现类工程接入 wiki 模板时，先建立或填写 [[templates/implementation-project-profile-template]]，至少裁决：

- `project_role`：controller / subproject / runtime-service / data-model / documentation-governance / hybrid。
- `owner_surfaces`：项目主页、AGENTS、service registry、work-item chain、memory、trace、report、handoff。
- `agent_system_layers`：skill、runtime、harness、memory、evaluation、governance、migration 七层是否有本地 owner。
- `control_plane`：Goal / Loop / Run Capsule / Worker / Evaluator / Issue policy / persistence policy 的落点。
- `implementation_boundaries`：allowed writes、forbidden writes、Git preflight、dirty / diverged / local-only 处理。
- `evidence_contract`：code-level、functional、service-side、end-to-end、non-default / boundary、manual confirmation。
- `template_adoption`：直接使用、局部适配、项目绑定、拒绝或延后。

## Topic 到系统层落地

AcknowledgeBase 的 design topics 进入 wiki 时，不按原目录复制；按系统层吸收：

| AcknowledgeBase 方案族 | wiki 系统层 | 本仓落地 |
| --- | --- | --- |
| Universal Agent Harness Baseline | harness + governance + template | [[agent-system-maturity]]、[[templates/harness-adoption-template]] |
| Agent Harness / Memory / Evaluation / Migration | agent-system 七层对象 | [[agent-system-cross-project-alignment.v1]]、[[projects/design/topics/agent-workflow-memory-harness-skill-landing]] |
| Goal Orchestration / Run Capsule | workflow + harness | [[agent-orchestration]]、[[templates/run-capsule-template]] |
| Process Knowledge Persistence / Dialogue Persistence | memory + persistence | [[projects/memory/README]]、[[log]]、[[harness-feedback-ledger]] |
| Research Operating System / Technical Research | skill + template + sensor | [[skills/research-capability/SKILL]]、[[skills/technology-research/SKILL]] |
| topic placement / Design Topic Governance | topic owner + project docs sensor | [[projects/design/topics/README]]、本页 |
| Cross-project Log Architecture | memory + log + generated view boundary | [[log-writing-rules]]、[[projects/memory/README]] |
| Public / Lens / Visual Presentation | views + skill + publication boundary | [[skills/problem-focused-visual-presentation/SKILL]]、[[skills/public-html-publish/SKILL]] |

## 不能上推边界

## 完成边界

本页达成的是结构和模板能力，不自动证明任何具体工程已经上线、验收或达到智能化行为分数。完整实现类工程接入必须另有：

- 本地 profile 或等价 owner。
- 目标工程自己的 `python3 scripts/check_all.py` 或等价验证。
- 子工程 Git preflight 和 handoff。
- 主控侧 evaluator 关闭裁决。
- 缺 runtime / live readback / 人工确认时明确 `blocked / partial / review`。

## 验证

- `python3 scripts/check_all.py --only implementation-template-system`
- `python3 scripts/check_all.py --only agent-system-maturity`
- 收尾前 `python3 scripts/check_all.py`
