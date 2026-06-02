---
type: concept
id: CONCEPT-AGENT-GOVERNANCE-001
status: active
updated: 2026-05-29
tags: [agent, governance, harness, knowledge-base]
---

# Agent 治理

相关：[[concepts/harness-engineering]]、[[concepts/agent-work-retrospective]]、[[skills/historical-dialogue-retrospective/SKILL]]、[[agent-governance-strategy]]、[[response-mode-routing]]、[[proactive-dialogue-system]]、[[instruction-adherence]]、[[execution-contract-semantics]]、[[harness-evolution]]、[[harness-feedback-ledger]]

Agent 治理是把 agent 的规则、上下文、工具、技能、模板、验证、复盘和自演进机制组织成一套可维护系统的方法。它关注的不是“写更多提示词”，而是让 agent 在不同任务里能正确判断响应模式、保留事实边界、遵守执行合同、生成证据、回写知识，并从真实失误中改进。

## 核心问题

- Agent 本轮应该快速诊断、知识沉淀、引导式设计、验收关闭、规则升级、子工程实现还是批处理？
- 哪些内容是硬约束，哪些只是候选经验、专题方法或单次用户偏好？
- 规则已经存在但没有执行时，应该补更强文字、模板字段、sensor、门禁还是最终证明？
- 用户纠偏、检查失败、模式切换和重复返工怎样进入 episode，而不是直接堆成新规则？
- Agent 的工作质量如何复盘，怎样区分单次表现问题和 Harness 机制缺口？

## 治理对象

| 对象 | 关注点 | 当前入口 |
| --- | --- | --- |
| 治理策略 | 硬约束、语义门、流程、建议和 backlog 如何分级 | [[agent-governance-strategy]] |
| 响应模式 | 本轮先轻还是重，是否需要切换模式 | [[response-mode-routing]] |
| 主动对话 | 目标不完整时如何少问、假设推进并产物化 | [[proactive-dialogue-system]] |
| 指令遵循 | 已有规则怎样进入触发器、模板字段、sensor、门禁和最终证明 | [[instruction-adherence]] |
| 执行合同 | 防止参考规则、非目标和证据说明漂移成隐形待办 | [[execution-contract-semantics]] |
| H5 自演进 | episode 怎样观察、晋升、降级或删除 | [[harness-evolution]]、[[harness-feedback-ledger]] |
| 工作复盘 | 回看目标理解、读取预算、工具使用、验证质量和沟通节奏 | [[concepts/agent-work-retrospective]]、[[skills/historical-dialogue-retrospective/SKILL]] |

## 分层模型

- **治理策略层**：[[agent-governance-strategy]]。回答哪些防线保留为 P0 硬约束，哪些降成 P1 语义门、P2 流程或 P3 backlog。
- **硬约束层**：[[AGENTS]]、[[POLICY]]。回答 agent 必须怎么做、什么可以自动写入、冲突时谁优先。
- **执行路由层**：[[response-mode-routing]]、[[WORKFLOW]]。回答本轮该用什么模式、按什么顺序推进。
- **任务语义层**：[[instruction-adherence]]、[[execution-contract-semantics]]。回答规则如何落到执行，以及执行页怎样保持单值裁决。
- **能力复用层**：`skills/`、`templates/`、`scripts/`。承接可复用流程、页面骨架和可检查约束。
- **反馈学习层**：[[harness-evolution]]、[[harness-feedback-ledger]]、[[concepts/agent-work-retrospective]]。承接纠偏、失败、复盘、晋升和降级。

## 当前基线

当前知识库已经有一组 Agent Harness 基线：

- 治理瘦身和分级策略：[[agent-governance-strategy]]
- 响应效率治理：[[response-mode-routing]]
- 引导式设计和产物化：[[proactive-dialogue-system]]、[[templates/guided-discovery-session-template]]
- 计划型问题状态推演：[[state-constraint-reasoning]]
- 规则执行和合同语义：[[instruction-adherence]]、[[execution-contract-semantics]]
- H5 反馈闭环：[[harness-evolution]]、[[harness-feedback-ledger]]
- 接入与复盘模板：[[templates/harness-adoption-template]]、[[templates/harness-episode-package-template]]、[[templates/harness-evolution-review-template]]、[[templates/goal-contract-template]]
- 复盘专题：[[concepts/agent-work-retrospective]]
- 复盘技能：[[skills/historical-dialogue-retrospective/SKILL]]
- 检查入口：`python3 scripts/check_all.py --list`

这说明 Agent 治理专题不是新建项目开发任务，而是对既有知识库方法、治理页和 Harness 机制的总览与继续沉淀。

## 使用口径

当后续对话涉及“agent 更智能 / 更稳定 / 更会遵守规则 / 更会复盘 / 更会自我进化”时，先用本页判断问题属于哪一层，再回到对应单一信息源修改。

候选能力只有在跨场景稳定、能模板化或能 sensor 化时，才考虑升级为规则、模板或门禁。单次纠偏优先进入 [[harness-feedback-ledger]] 观察，不直接变成全局硬规则。

## 常见反模式

- 把 agent 治理误写成某个项目开发专题，导致知识库方法被塞进 `projects/`。
- 把每次纠偏都升级成 [[AGENTS]] 硬规则，最后入口页变成百科全书。
- 把防漏规则写成无条件仪式，导致 `[[log]]`、完整检查、二阶反思或产物化变成低价值固定动作。
- 把降低读取成本误写成删除信息结构，例如压缩 Gate / FP / EP / TASK / risk / issue / AP / report 体系，或把分层验收压成一个“已验证”结论。
- 把日志、报告、handoff 或模型自述当作验收闭环。
- 把“更智能”理解成无限扩读、长问卷或一次铺满结构。
- 只做复盘不改模板、sensor 或技能，导致同类问题反复靠人工提醒。

## 典型案例

- [[articles/2026-06-02-issue-original-evidence-asset-intake]]：用户上传截图生成 issue 时，旧 issue skill / AGENTS / issue README 已有“先保存图片、再 Markdown 引用”规则，但场景分流没有把 `用户上传图 + 创建 issue` 识别为独立场景，导致 Evidence Persistence Gate 未进入第一执行槽位；该案例不是缺少复现。
- [[articles/2026-05-29-finalizer-write-scope-case]]：finalizer 只证明 working tree clean / external residual 明示，却没有证明本轮提交仍符合用户最新写入范围；该案例把问题归类为 Scope Lock / Scope Proof 缺口，而不是业务 issue。
