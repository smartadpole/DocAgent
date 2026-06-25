---
type: concept
id: CONCEPT-AGENT-WORK-RETROSPECTIVE
status: active
source_of_truth: true
updated: 2026-06-03
tags: [concept, retrospective, ai-agent, harness, workflow]
---

# Agent 工作复盘

上级专题：[[concepts/project-retrospective]]

相关页面：[[concepts/harness-engineering]]、[[response-mode-routing]]、[[harness-evolution]]、[[harness-feedback-ledger]]

可启动技能：[[skills/historical-dialogue-retrospective/SKILL]]

复盘总入口：[[skills/retrospective-capability/SKILL]]

Agent 工作复盘关注 agent 作为执行主体时，它的工作方式、效率、质量、边界感和自我改进是否可靠。它不是对项目结果的替代复盘，而是对“这个 agent 是怎样完成工作的”做结构化回看。

具体复盘档案默认放在 [[projects/retrospectives/README]] 所在目录；结构性 Harness episode 仍进入 [[harness-feedback-ledger]]。

## 定义

Agent 工作复盘是在一次任务、一个阶段、一次长时目标或一次明显偏差之后，回看 agent 从理解目标到交付结果的全过程。

它回答：

- agent 是否正确理解了用户目标和当前阶段。
- agent 是否用了合适的响应模式、读取预算和工具。
- agent 是否把精力花在最关键的事实、实现和验证上。
- agent 是否及时沟通状态、边界、风险和证据。
- agent 的输出质量是否满足本轮完成契约。
- 这次经验应进入普通 log、Harness episode、规则、模板、skill、sensor 还是项目记忆。

## 复盘维度

| 维度 | 核心问题 | 常见证据 |
| --- | --- | --- |
| 目标理解 | 是否抓住用户真正要解决的问题 | 用户原话、模式判断、最终交付物 |
| 阶段判断 | 是否知道当前在分析、沉淀、实现、验收还是收尾 | [[response-mode-routing]]、状态更新、log |
| 上下文读取 | 是否读取了足够且不过量的事实源 | 读取文件、搜索记录、引用页面 |
| 工具使用 | 是否用对工具，避免低效或越权操作 | shell、browser、tests、scripts、MCP 工具记录 |
| 执行策略 | 是否拆对步骤、优先级和中间节点 | plan、diff、提交、阶段性结果 |
| 验证质量 | 是否用合适证据证明结果成立 | 测试、sensor、review、人工确认边界 |
| 沟通节奏 | 是否及时说明当前阶段、发现和阻塞 | commentary 更新、最终回复、handoff |
| 权限和边界控制 | 是否守住权限、路径、环境和非目标 | AGENTS、POLICY、工作区状态、未触碰文件 |
| 沉淀路由 | 是否把可复用经验放到正确位置 | log、concept、template、skill、ledger |
| 收尾和提交质量 | 是否补齐同步、检查、log 和 scoped commit | diff、checks、commit、最终回复 |

## 启动判断与技能边界

本页只保留 Agent 工作复盘的粗启动判断和概念边界。详细触发、证据读取、输出结构和质量自检由 [[skills/historical-dialogue-retrospective/SKILL]] 承接，避免概念页和 skill 维护两份执行流程。

优先在这些场景考虑 Agent 工作复盘：

- 长时任务结束，尤其是跨多轮、跨仓库、跨环境的任务。
- 需要复盘历史对话、当前对话上下文、[[log]] 或 [[harness-feedback-ledger]] 中的 agent 协作链。
- 用户指出 agent 理解错、做慢了、做重了、漏验证、漏提交或漏沉淀。
- 任务出现明显返工、偏航、重复读取、过度治理或证据不足。
- 一次任务暴露出可复用流程缺口、模板缺口、sensor 缺口或协作契约缺口。
- 周期性回看某段时间内 agent 的效率、质量和用户体验。

如果只是单次普通执行过程，写入 [[log]] 或对应项目记录即可；如果只是项目结果复盘，优先回到 [[concepts/project-retrospective]] 或 [[concepts/software-development-project-retrospective]]。

## 历史对话复盘

历史对话复盘要同时区分材料角色：

- [[harness-feedback-ledger]]：结构性 episode 和已观察到的 Harness 缺口。
- [[log]]：按对话整理后的主题、意图、关键动作和影响页面。
- 当前对话上下文：用户最新目标、约束、纠偏和本轮复盘触发点。
- 原始 session / rollout：真实对话、tool call、执行顺序和状态更新。
- git diff / commit：实际改动、提交边界和文件落位。
- 受影响主页面：当前单一信息源和最终沉淀状态。
- 检查 / 测试输出：agent 是否做了足够验证，以及验证能证明什么。
- memory：检索线索和长期偏好，不是当前事实真相源。
- 最终回复 / handoff：agent 对用户或下游的交付表达，不能替代 diff 和检查。

如果复盘目标是找 agent 偏差或 workflow 改进，优先启动 [[skills/historical-dialogue-retrospective/SKILL]]，不要只凭 [[log]] 或当前记忆下结论。

历史对话和 Agent 工作流复盘是 [[skills/retrospective-capability/SKILL]] 的内部子项；它不替代项目交付复盘，也不替代 Issue、事故、测试报告或验收关闭。

## 和 Harness 的分工

- [[harness-feedback-ledger]]：记录可复盘 episode、sensor backlog 和规则晋升队列。
- [[harness-evolution]]：决定 episode 何时晋升为 sensor、模板、技能或规则。
- [[response-mode-routing]]：定义每轮应该如何先判模式、控制读取预算和切换阶段。
- Agent 工作复盘：把一次或一段 agent 工作放到这些机制之上回看，判断哪里是工作习惯问题，哪里是 Harness 机制缺口。

如果复盘结论只是单次表现，不直接升级规则；如果它反复出现、能脚本化或能模板化，再进入 Harness 自演进链。

## 常见反模式

- 只评价结果好坏，不回看 agent 是怎样判断和行动的。
- 把用户纠偏只当成一次失误，没有判断是否暴露流程或 Harness 缺口。
- 把每个小问题都升级成硬规则，导致治理层膨胀。
- 只追求速度，省掉目标保真、证据分层和边界说明。
- 只追求完整，过度读取、过度建模或把简单任务做成重治理。
