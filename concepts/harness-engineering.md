---
type: concept
updated: 2026-06-22
tags: [ai-agent, software-engineering]
---

# Harness Engineering

## 定义

Harness Engineering 是围绕 AI 模型构建工程化运行环境的实践。它把模型之外的上下文、工具、规则、权限、工作流、验证、日志、记忆和人类干预组织成一套可约束、可观测、可校验、可持续演化的系统。

最短公式是：

`Agent = Model + Harness`

模型负责推理，Harness 负责让推理发生在正确上下文、正确权限、正确流程和正确反馈闭环里。

## 边界

Harness Engineering 包含 Prompt Engineering 和 Context Engineering，但不止于二者。

- Prompt Engineering：当前请求怎么表达。
- Context Engineering：当前请求需要哪些信息。
- Harness Engineering：请求、上下文、工具、反馈、权限、流程、记录和演化如何一起组成稳定工程系统。

## 常见组件

- 规格：SPEC、任务说明、验收标准、非目标、人工确认点。
- 上下文：AGENTS / CLAUDE、README、架构文档、dev-map、任务看板、接口文档。
- 规则：底线、禁止项、路径边界、提交要求、验证要求。
- Skill：编译、测试、审查、源码审计、发布等高频动作的 SOP。
- Workflow：计划、实现、验证、审查、打回、提交、回写的接力规则。
- Sub Agent：按阶段或专业分工的 agent 角色。
- Scripts / Sensors：lint、测试、CI、静态分析、架构检查、trace、日志、SLO。
- MCP / Tools：外部系统、宿主环境和受控工具能力。
- Goal Contract：像 [[concepts/codex-goals]] 这样的线程级完成契约，用来让长时任务在多轮之间保留终点线和证据审计面。
- Run Capsule：把一次多 agent / 子工程运行中的 Orchestrator、Worker、Evaluator、Subproject Git Preflight、证据层级和沉淀路由固定下来。
- State Constraint Reasoning：把权限、远程、dirty 状态、预算和人工确认传播到可执行动作，避免把 blocked 写成 plan。
- Memory：会话延续和偏好辅助；团队真相源应优先文件化。
- Observability：运行记录、失败归因、干预记录和 harness 变更证据。

## 在本库的落地

当前 wiki 把自己定位成模板级 Agent Harness，而不是某个具体业务项目的第二真相源。

- [[response-mode-routing]] 承接响应效率治理：每轮先判快速诊断、知识沉淀、Issue 分析、验收关闭、规则升级、子工程实现或批处理。
- [[agent-governance-strategy]] 承接治理强度分级：P0 / P1 / P2 / P3，避免把普通流程默认升级成硬规则。
- [[state-constraint-reasoning]] 承接状态约束推理：权限、远程、dirty / diverged、预算、证据和人工确认会限制当前可执行动作。
- [[agent-orchestration]] 承接多 agent 和子工程编排：Run Capsule、Orchestrator、Worker、Evaluator、Subproject Git Preflight 和沉淀路由。
- [[harness-evolution]] 和 [[harness-feedback-ledger]] 承接 H5 自演进：把真实 episode、用户纠偏、检查失败和重复失守先沉淀成数据，再决定是否晋升为 sensor、模板、技能或规则。
- [[AGENTS]] 保持硬约束和短入口，不承担百科全书式正文。
- [[WORKFLOW]] 承接执行顺序，[[POLICY]] 承接自动写入边界和优先级。
- [[skills/issue-analysis/SKILL]] 承接高频问题分析方法，并区分快速根因链和完整沉淀链。
- [[templates/harness-adoption-template]] 承接新系统接入时的主控关系、单一信息源、写权限、验证层级、handoff 和 feedback sensor。
- [[templates/goal-contract-template]] 承接长时任务的期望最终状态、完成判定、验证面 / 证据边界、约束、预算、探索边界和阻塞停止条件。
- [[templates/run-capsule-template]] 和 [[templates/loop-contract-template]] 承接单轮编排与持续循环控制面。
- [[templates/harness-episode-package-template]] 和 [[templates/harness-evolution-review-template]] 承接单次 episode 和周期复盘。
- `scripts/check_all.py` 是本库本地门禁入口，`scripts/check_harness_governance.py` 先覆盖 Harness wiring。

## 适用场景

- AI coding agent 在真实代码仓库中持续工作。
- 多轮需求、设计、实现、验证、交付需要稳定接力。
- 团队希望减少 AI 重复犯错，并把错题沉淀成规则、脚本或流程。
- 需要把 AI 从“会写代码”推进到“能在工程约束里交付可验证结果”。

## 常见误区

- 把 Harness 简化成提示词模板。
- 把所有规则塞进一个巨大的 AGENTS / CLAUDE 文件。
- 只增加工具，不分析工具补的是哪个行为缺口。
- 只有自然语言规则，没有脚本、测试或 CI 反馈。
- 把隐藏 memory 当团队单一信息源。
- 多 Agent 没有交接材料、打回规则和完成定义。
- Worker 自述、health、handoff 或 local pass 被上推成整体完成。

## 相关页面

- [[articles/2026-05-25-harness-engineering-research]]
- [[concepts/codex-goals]]
- [[AGENTS]]
- [[WORKFLOW]]
- [[response-mode-routing]]
- [[agent-governance-strategy]]
- [[state-constraint-reasoning]]
- [[agent-orchestration]]
- [[harness-evolution]]
- [[harness-feedback-ledger]]
- [[POLICY]]
- [[BRAIN]]
- [[skills/README]]
- [[templates/README]]
