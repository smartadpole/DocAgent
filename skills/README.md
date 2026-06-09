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

- [[skills/problem-focused-visual-presentation/SKILL]]：问题聚焦式图文呈现技能。用于把一份文档、跨文档主题、状态、风险、决策、计划、验收或知识材料重组为带背景框、证据边界、图文主体、同源一致性和 ignored PDF / PNG 导出配置的 lens。
- [[skills/cross-project-skill-adoption-prompt/SKILL]]：跨工程技能升级提示词生成技能。用于把已沉淀的 skill / 能力转换成可交给目标工程 agent 的升级提示词、附件资料清单、吸收边界、落地步骤和验证要求。
- [[skills/knowledge-linking/SKILL]]：知识关联技能。用于把调研、沉淀知识、总结方案、入口 / 上位 / 邻接 / 反向链接和 `knowledge-linking` sensor 验证收敛成可复用流程，避免新增知识成为孤岛。
- [[skills/technical-topic-research/SKILL]]：技术专题调研技能。用于把技术类专题 / 概念调研组织成问题牵引、谱系边界、机制拆解、生态扫描、对比评估、场景映射、PoC、风险和分级决策的可复用研究包。
- [[skills/open-source-project-research/SKILL]]：开源工程调研技能。用于把 GitHub / Hugging Face / 论文代码 / 开源产品调研组织成项目画像、健康度、运行验证、代码结构、效果性能、集成成本、风险和使用策略的工程尽调卡。
- [[skills/industry-ai-research/SKILL]]：IT / AI 行业调研技能。用于把 IT 行业、AI 领域、AI 赛道、产品机会、公司群体和落地场景调研组织成宏观趋势、技术路线、产品应用、竞争格局、开源生态、治理风险和行动建议。
- [[skills/issue-analysis/SKILL]]：主控侧 issue / incident 分析技能。用于把模糊问题拆成权威事实源、最小根因链、责任边界、跨工程分工、联测方案和主控文档回写。
- [[skills/historical-dialogue-retrospective/SKILL]]：历史对话与 Agent 工作流复盘技能。用于从当前上下文、[[log]]、[[harness-feedback-ledger]]、原始 session / rollout、git diff / commit 和检查输出中复盘 agent 偏差、效率质量和 workflow 改进候选。
- [[skills/cross-project-governance-audit/SKILL]]：跨工程治理审计技能。定期或按需读取各工程关键治理文件，对照 [[governance/platform-standards]] 评估成熟度，生成漂移报告和 handoff 包；支持全量审计和单工程审计两种模式。

## 维护原则

- 新技能先写最小可用版本，不铺无关资源目录。
- 技能正文只写可复用流程，不复制项目主页、设计页或 TODO 的长正文。
- 高价值技能如果需要被其他工程吸收，可以补 `TRANSFER.md` 作为迁移资料清单；完整提示词按需由 [[skills/cross-project-skill-adoption-prompt/SKILL]] 生成，不把每次提示词长期写死。
- 如果技能引入新的项目事实判断口径，同轮检查是否需要回写 [[BRAIN]]、[[POLICY]]、[[WORKFLOW]] 或项目主页面。
- 复盘类技能必须保留证据分层、对象边界、质量自检和行动分流，不只凭 [[log]] 或当前上下文判断完整历史。
