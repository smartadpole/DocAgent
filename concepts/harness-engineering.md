---
type: concept
updated: 2026-05-25
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
- Memory：会话延续和偏好辅助；团队真相源应优先文件化。
- Observability：运行记录、失败归因、干预记录和 harness 变更证据。

## 在本库的落地

当前 wiki 把自己定位成模板级 Agent Harness，而不是某个具体业务项目的第二真相源。

- [[response-mode-routing]] 承接响应效率治理：每轮先判快速诊断、知识沉淀、Issue 分析、验收关闭、规则升级、子工程实现或批处理。
- [[AGENTS]] 保持硬约束和短入口，不承担百科全书式正文。
- [[WORKFLOW]] 承接执行顺序，[[POLICY]] 承接自动写入边界和优先级。
- [[skills/issue-analysis/SKILL]] 承接高频问题分析方法，并区分快速根因链和完整沉淀链。
- [[templates/harness-adoption-template]] 承接新系统接入时的主控关系、单一信息源、写权限、验证层级、handoff 和 feedback sensor。

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

## 相关页面

- [[articles/2026-05-25-harness-engineering-research]]
- [[concepts/codex-goals]]
- [[AGENTS]]
- [[WORKFLOW]]
- [[response-mode-routing]]
- [[POLICY]]
- [[BRAIN]]
- [[skills/README]]
- [[templates/README]]
