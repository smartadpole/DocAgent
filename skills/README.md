# 技能层

这里放当前文档项目内可复用的 agent 技能。

## 边界

- `skills/` 承接面向 agent 的分析流程、判断框架和执行套路。
- `templates/` 承接可复制的文档骨架和页面模板。
- `governance/` 承接规则、流程、背景和裁定边界。
- [[response-mode-routing]] 先判断本轮是否需要调用完整技能流程；快速诊断不应默认触发完整沉淀链。
- [[harness-evolution]] 用来判断技能执行中的重复偏差是否应先记录为 episode，再升级为技能规则、模板字段或 sensor。

技能可以带当前项目的业务语境，但不直接承担项目状态、需求、设计、TODO 或测试报告的单一信息源职责。涉及项目事实时，技能只提示应该回到哪些主页面取证和回写。

## 当前技能

- [[skills/issue-analysis/SKILL]]：主控侧 issue / incident 分析技能。用于把模糊问题拆成权威事实源、最小根因链、责任边界、跨工程分工、联测方案和主控文档回写。
- [[skills/historical-dialogue-retrospective/SKILL]]：历史对话与 Agent 工作流复盘技能。用于从当前上下文、[[log]]、[[harness-feedback-ledger]]、原始 session / rollout、git diff / commit 和检查输出中复盘 agent 偏差、效率质量和 workflow 改进候选。
- [[skills/cross-project-governance-audit/SKILL]]：跨工程治理审计技能。定期或按需读取各工程关键治理文件，对照 [[governance/platform-standards]] 评估成熟度，生成漂移报告和 handoff 包；支持全量审计和单工程审计两种模式。

## 维护原则

- 新技能先写最小可用版本，不铺无关资源目录。
- 技能正文只写可复用流程，不复制项目主页、设计页或 TODO 的长正文。
- 如果技能引入新的项目事实判断口径，同轮检查是否需要回写 [[BRAIN]]、[[POLICY]]、[[WORKFLOW]] 或项目主页面。
