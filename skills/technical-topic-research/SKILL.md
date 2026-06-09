---
name: technical-topic-research
description: 调研技术类专题或概念时，用于把资料、原理、生态、对比、场景、PoC、风险和决策建议沉淀成可复用知识资产。
---

# 技术专题调研技能

## 定位

本技能把“技术专题 / 技术概念调研”从资料搜集收敛成一套面向判断和行动的研究流程。

目标不是把资料搜全，而是生成可支撑判断、选型、落地和复用的 [[concepts/technical-research-knowledge-asset|技术研究型知识资产]]。

## 触发场景

- 用户要求“调研某个技术专题 / 技术概念 / 技术路线”。
- 用户要求判断某个技术“值不值得做、能不能落地、怎么选型、怎么 PoC”。
- 用户给出技术资料、文章、论文、GitHub 项目或产品链接，要求沉淀到知识库。
- 需要把技术热点从聊天摘要升级成 `articles/`、`concepts/`、选型矩阵或 PoC 方案。

如果用户给的是具体 GitHub / Hugging Face / 论文代码 / 开源产品仓库，并且问题是“能不能用、怎么接、是否值得引入”，优先切到 [[skills/open-source-project-research/SKILL]]。

## 边界

- 不追求资料穷尽；优先构建判断链。
- 不把最新事实凭记忆写死。涉及近期生态、产品、版本、价格、license、benchmark、论文或 GitHub 活跃度时，必须查证来源。
- 不把调研结论直接变成采用决策；没有 PoC 或本地约束验证时，只能给推荐等级和验证建议。
- 不把项目事实、运行状态或工程任务写进本技能；具体项目执行仍回到目标项目的单一信息源。
- 不替代 [[skills/knowledge-linking/SKILL]]；本技能负责调研判断，知识关联技能负责落位、补链和 sensor 验证。

## 读取顺序

1. [[articles/2026-06-09-technical-topic-research-methodology]]：确认本库对技术专题调研的目标、主线和产物标准。
2. [[concepts/technical-research-knowledge-asset]]：确认调研资产的概念边界。
3. [[templates/technical-topic-research-template]]：需要写正式调研页时使用。
4. [[skills/knowledge-linking/SKILL]]：确认新增 article / concept / template / skill 的入口、上位、邻接和反向链接要求。
5. 目标专题已有页面：先搜 `INDEX.md`、`articles/`、`concepts/`、`skills/`、`governance/`，避免重复新建。
6. 外部来源：优先官方文档、论文原文、作者原文、项目仓库、release / issue / license、产品文档，再用二级文章辅助理解。

具体开源工程调研读取 [[articles/2026-06-09-open-source-project-due-diligence-methodology]]、[[concepts/open-source-project-due-diligence]] 和 [[templates/open-source-project-research-template]]。

## 工作流

### 1. 固定调研问题

先把专题从“名词”改写成问题：

- 它试图解决什么问题？
- 旧方案为什么不够？
- 如果没有它，会有什么损失？
- 这次调研需要支持什么决策：关注、实验、产品化、替换、采购、集成还是只做储备？

如果用户只给一个新名词，先给一个轻量问题假设，再继续调研。

### 2. 建立概念边界

输出技术谱系和边界：

- 上游技术。
- 下游应用。
- 平行概念。
- 替代路线。
- 容易混淆的名词。
- 这个概念真正不同的地方。

必要时用树状结构、表格或 Mermaid 图。

### 3. 拆核心机制

至少说明输入、过程、输出、关键模块、关键算法 / 模型 / 工程组件、瓶颈和效果决定因素。

如果机制不清，不要急着给采用建议；先标记为 `blocked by mechanism understanding` 或 `needs deeper source review`。

### 4. 扫描生态

按四层扫描：

- 学术层：论文、benchmark、关键路线、可复现性。
- 开源层：仓库活跃度、issue、commit、release、文档、license、真实案例。
- 产品层：API、SaaS、平台能力、付费点、代表公司。
- 工程层：部署、成本、延迟、稳定性、安全和维护复杂度。

如果事实会随时间变化，最终页要写明查询日期和来源。

### 5. 做对比评估

至少比较：

- 与传统方案相比。
- 与同类新方案相比。
- 与我们现有方案或可用基础相比。

没有现有方案信息时，明确写 `待补：本地现状 / 目标系统约束`，不要假装已经完成选型。

### 6. 映射场景

用结构化方式输出：

`技术能力 -> 可用场景 -> 所需条件 -> 预期收益 -> 落地难度 -> 优先级`

这一步要明确不适合场景和收益边界。

### 7. 设计 PoC

只有值得 A / B 级推进的技术才需要 PoC。PoC 至少包含：

- 验证目标。
- 数据或样本。
- 技术栈。
- 评估指标。
- 时间安排。
- 成功标准。
- 失败退出条件。

PoC 不是“试试看”，而是为了减少哪个不确定性。

### 8. 给分级结论

使用四级结论：

- A：立即试点。
- B：短期验证。
- C：持续观察。
- D：暂不投入。

结论必须带下一步动作，例如“建 20 条评估集做 1 周 PoC”“只保留概念页并季度复查”“暂不接入，等待生态成熟”。

### 9. 沉淀知识资产

按层级写入：

- `articles/`：本次调研正文、来源、对比、PoC、结论。
- `concepts/`：稳定概念、边界、适用场景和常见误区。
- `templates/`：只有跨专题高频复用的骨架才进入模板层。
- `skills/`：只有 agent 可重复执行的调研流程才进入技能层。
- `log.md`：记录本次对话意图、关键动作和影响页面。

写完后使用 [[skills/knowledge-linking/SKILL]] 做知识关联自检。

## 输出要求

正式调研页优先使用 [[templates/technical-topic-research-template]]，并至少包含：

1. 一句话结论。
2. 背景与问题。
3. 概念定义与边界。
4. 技术原理。
5. 技术路线与生态。
6. 方案对比。
7. 应用场景。
8. 落地路径。
9. 风险与限制。
10. 结论与建议。

## 验证

新增或大改知识页后运行：

```bash
python3 scripts/check_all.py --only knowledge-linking
```

如果新增或大改技能、模板、入口或治理页，收尾前运行：

```bash
python3 scripts/check_all.py
```

## 自检清单

- 是否从问题切入，而不是只解释名词。
- 是否建立了谱系和边界。
- 是否拆了核心机制。
- 是否覆盖学术、开源、产品、工程四层生态。
- 是否做了传统方案、同类方案和现有方案对比。
- 是否映射到自身场景。
- 是否给出 PoC、风险和投入等级。
- 是否区分已验证事实、推论和待确认项。
- 是否补齐 article / concept / entrypoint / backlink。
- 是否运行知识关联检查。
