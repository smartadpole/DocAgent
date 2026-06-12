---
type: concept
updated: 2026-06-09
tags: [ai-agent, skills, harness-engineering, workflow]
---

# Agent Skills

相关：[[concepts/harness-engineering]]、[[concepts/agent-governance]]、[[concepts/agent-instruction-sharing]]、[[concepts/technical-research-knowledge-asset]]、[[skills/knowledge-linking/SKILL]]、[[skills/technical-topic-research/SKILL]]、[[articles/2026-06-09-scientific-agent-skills-research]]

Agent Skills 是把某类可重复工作打包成 agent 可发现、可加载、可执行和可审计的能力单元。它通常以一个目录承接，核心文件是 `SKILL.md`，并可配合 `scripts/`、`references/`、`assets/` 等资源。

它解决的问题不是“让模型知道更多事实”，而是让 agent 在遇到高频任务时少一点临场发挥，多一点可复用流程、事实源分层、工具边界、输出格式和验证守卫。

## 基本结构

一个成熟 skill 至少要回答：

- **什么时候用**：触发条件、任务关键词、适用场景和禁用场景。
- **读什么**：入口文档、事实源、参考资料、外部 API、数据库或项目文件。
- **怎么做**：步骤、分支、打回条件、失败处理和人工确认点。
- **用什么工具**：命令、脚本、依赖、权限、联网和文件写入边界。
- **交付什么**：输出格式、证据边界、验证命令和最终回复口径。
- **怎样维护**：版本、来源、迁移边界、安全扫描和过期信号。

## 和 Harness Engineering 的关系

在 [[concepts/harness-engineering]] 里，Skill 层承接高频动作标准化。它位于 prompt / context 之后，script / sensor 之前：

1. Prompt 表达当前目标。
2. Context 给出当前任务必须知道的事实。
3. Skill 告诉 agent 这一类任务应该按什么流程行动。
4. Script / Sensor 用可执行反馈证明结果是否达标。

因此，Skill 不应替代项目事实单一信息源，也不应替代测试、lint、CI、安全扫描或人工审查。它更像“可加载的任务合同”。

## 和工具 / MCP 的区别

| 类型 | 回答的问题 | 典型内容 |
| --- | --- | --- |
| Tool / MCP | agent 可以调用什么外部能力 | API、浏览器、数据库、CI、文件系统、GitHub |
| Skill | agent 应该如何完成某类任务 | 读取顺序、流程、范式、例子、验证、禁止项 |
| Template | 人或 agent 创建页面 / 报告时复制什么骨架 | frontmatter、字段、章节、默认结构 |
| Rule | 哪些底线必须遵守 | 权限、边界、提交、验收、敏感数据 |

Skill 可以调用工具，也可以引用模板和规则，但不能把四者混成一页。混在一起后，agent 会不知道当前是在执行流程、调用工具、填模板，还是遵守硬约束。

## 好 skill 的特征

- 描述字段具体，能帮助 agent 区分何时触发，而不是泛泛写“帮助研究 / 帮助开发”。
- 主体短而可执行；长参考拆到 `references/`，脚本放到 `scripts/`。
- 明确输入、输出、验证和失败处理。
- 保留事实边界：项目状态、业务事实、服务地址和运行 ID 不写成通用 skill 正文。
- 支持 progressive disclosure：先给触发摘要，真正需要时再加载完整流程和支撑文件。
- 对高风险动作写明权限、联网、文件写入、凭据和人工确认点。
- 可迁移时提供 `TRANSFER.md` 或等价资料清单，说明可吸收项和禁止复制项。

## 技能归类和迁移策略

跨工程看 skill 时，不能只问“有没有 `SKILL.md`”或“哪个工程得分高”，还要先判断它的项目绑定强度。

| 类别 | 典型对象 | 迁移口径 |
| --- | --- | --- |
| 通用 / 可迁移技能 | 调研、复盘、图文呈现、Issue 分析、知识关联、跨工程治理审计 | 可迁移的是触发条件、事实源分层、流程、输出格式、验证命令和禁止项。 |
| 治理能力 / 协作契约 | Goal Contract、执行合同语义、状态约束推演 | 可迁移的是协作契约和裁决边界；不能把它误写成普通业务 skill，也不能替代验收关闭。 |
| 项目 / 领域绑定技能 | 客群 DB 读回、项目上下文入口、LifeOS 管理、特定 backlog 批处理 | 只能抽象方法；不能复制业务表、服务名、运行 ID、本地路径、项目状态、一次性 handoff 或领域事实。 |

“客群 DB 读回”这类能力表面上是 skill，实质上绑定了业务对象、数据库写入合同、字段含义、验收窗口和项目运行边界。它可以在成熟度矩阵里展示，但应和通用技能分表呈现；否则读者会误以为它像“复盘”或“调研”一样可以跨工程直接吸收。

因此，跨项目反哺时默认先做两步判断：

1. 判断 skill 是否强绑定项目、业务、数据合同、服务环境或领域语义。
2. 如果绑定强，只提取任务触发、读回方法、证据分层、输出格式和验证守卫；项目事实仍回到项目页、报告、issue、service registry 或原工程文档，不进入通用 skill 正文。

## 常见误区

- 把 skill 当 prompt 集合，只写几句泛化指令。
- 把项目事实、当前状态或一次性 handoff 写进通用 skill，导致跨项目污染。
- 一次性安装大量 community skill，让 agent 触发空间变得更混乱。
- 只写自然语言流程，没有验证命令、sensor 或输出边界。
- 把 skill 当成安全边界；实际上 skill 可以影响 agent 行为，本身也需要审查。
- 为了复用而复用，把低频、模糊、还没跑稳的流程提前技能化。

## Scientific Agent Skills 案例

[[articles/2026-06-09-scientific-agent-skills-research]] 记录了 K-Dense-AI/scientific-agent-skills 的调研。该项目把科研场景中的数据库、Python 包、文献综述、科学写作、医学影像、材料科学、单细胞分析、实验室自动化等流程打包成约 140+ 个 skill。

它说明 Agent Skills 的价值不在“模型变懂科研”，而在“科研流程、工具链和方法规范被版本化成 agent 可加载资产”。同时它也暴露出安全边界：skill 会影响 agent 选择、信任和执行，不能无脑全装。

## 在本库的使用口径

本库已有 `skills/` 层。后续新增或升级 skill 时，优先保持这个口径：

- 技能页写触发、事实源、流程、输出、验证和禁止项。
- 业务事实回到项目页、报告、issue、service registry 或 `articles/` / `concepts/`，不要塞进技能。
- 高价值跨项目能力补 `TRANSFER.md`，说明迁移资料、吸收边界和目标工程落地步骤。
- 如果同类失守重复出现，先判断是 skill 缺触发、模板缺字段、sensor 缺检查，还是规则本身需要升级。

## 相关页面

- [[articles/2026-06-09-scientific-agent-skills-research]]
- [[concepts/harness-engineering]]
- [[concepts/agent-governance]]
- [[concepts/agent-instruction-sharing]]
- [[concepts/technical-research-knowledge-asset]]
- [[skills/knowledge-linking/SKILL]]
- [[skills/technical-topic-research/SKILL]]
- [[skills/cross-project-skill-adoption-prompt/SKILL]]
- [[templates/skill-template]]
- [[articles/2026-05-25-harness-engineering-research]]
- [[articles/2026-06-04-knowledge-linking-mechanism-research]]
