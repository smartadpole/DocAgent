# 技能层

这里放当前文档项目内可复用的 agent 技能。

## 边界

- `skills/` 承接面向 agent 的分析流程、判断框架和执行套路。
- `templates/` 承接可复制的文档骨架和页面模板。
- `governance/` 承接规则、流程、背景和裁定边界。
- [[response-mode-routing]] 先判断本轮是否需要调用完整技能流程；快速诊断不应默认触发完整沉淀链。
- [[harness-evolution]] 用来判断技能执行中的重复偏差是否应先记录为 episode，再升级为技能规则、模板字段或 sensor。

技能可以带当前项目的业务语境，但不直接承担项目状态、需求、设计、TODO 或测试报告的单一信息源职责。涉及项目事实时，技能只提示应该回到哪些主页面取证和回写。

## 技能成熟度模型

判断一个技能是否成熟，不能只看有没有 `SKILL.md` 文件。优先看它是否同时具备这些证据信号：

- `skill`：技能页存在，frontmatter 写清 `name`、`description`，正文有定位、触发 / 适用场景、工作流、输出格式、回写守卫或禁止项。
- `README entry`：技能在本页有入口，读者不用猜路径。
- `template`：如果技能会反复产出同类文档、报告、任务或回传包，已有对应模板；如果不需要模板，要在技能边界里说明。
- `governance`：技能会改变响应模式、写入边界、验收口径或规则升级时，已回到 [[response-mode-routing]]、[[WORKFLOW]]、[[POLICY]] 或 [[AGENTS]] 等主入口，而不是只写在技能里。
- `sensor`：能脚本化检查的结构、字段、入口或禁止项，已接入 `scripts/check_all.py` 的专项 sensor；技能层当前用 `python3 scripts/check_all.py --only skill-maturity` 检查。
- `TRANSFER`：准备跨工程迁移的技能，必须先形成迁移边界或等价说明，写清吸收什么、不复制什么、目标工程如何自检。
- `evidence boundary`：任何成熟度比较、能力排行或迁移建议都只代表本轮信号强弱，不代表运行验收、项目状态或可从下游原样复制。

状态词建议只作治理提示：`领先` 表示证据信号最完整且可反哺；`成熟` 表示本地可稳定使用；`接入` 表示有入口但仍缺模板、sensor 或迁移边界；`局部` 表示只有零散信号；`未见` 表示未发现等价能力；`阻塞` 表示路径不可读或证据不足。状态不能替代验收、关闭或项目裁决。

## 当前技能

- [[skills/issue-analysis/SKILL]]：主控侧 issue / incident 分析技能。用于把模糊问题拆成权威事实源、最小根因链、责任边界、跨工程分工、联测方案和主控文档回写。
- [[skills/historical-dialogue-retrospective/SKILL]]：历史对话与 Agent 工作流复盘技能。用于复盘当前上下文、log、Harness ledger、原始 session / rollout、git diff / commit、检查输出、memory 和最终回复里的 agent 协作质量、偏差和改进路由。

## 维护原则

- 新技能先写最小可用版本，不铺无关资源目录。
- 技能正文只写可复用流程，不复制项目主页、设计页或 TODO 的长正文。
- 如果技能引入新的项目事实判断口径，同轮检查是否需要回写 [[BRAIN]]、[[POLICY]]、[[WORKFLOW]] 或项目主页面。
