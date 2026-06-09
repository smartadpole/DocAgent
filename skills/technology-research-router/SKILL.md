---
name: technology-research-router
description: 面对技术调研、AI/IT 行业调研、开源工程调研、产品/公司/PoC 研究时，用于先判对象、证据等级、成熟度、风险、输出形态和知识沉淀路径，再路由到正确调研技能。
---

# 技术调研总控技能

## 定位

本技能是技术调研的总入口。它不替代具体调研技能，而是在开始前完成对象识别、证据分级、成熟度判断、风险初筛和产物选择。

本技能要把当前工程的调研知识储备转成执行合同：每次调研先生成对象路由、证据计划、决策目标、成熟度假设、风险门和沉淀路径，再进入行业 / 技术专题 / 开源工程 / 源码审计 / PoC 分支。

## 触发场景

- 用户要求“全面补全技术调研体系”“做好完整技术调研储备”。
- 用户给出模糊对象，例如“调研 AI 方向”“调研一个项目”“看看这个技术有没有价值”。
- 用户同时关心行业、技术、开源、产品、公司和落地机会。
- 不确定应该走行业调研、技术专题调研、开源工程调研还是源码审计。

## 读取顺序

1. [[articles/2026-06-09-technology-research-capability-system]]：总控体系。
2. [[concepts/technology-research-system]]：概念边界。
3. [[templates/technology-research-intake-template]]：初始 intake。
4. 根据对象分流：
   - 行业 / AI 赛道：[[skills/industry-ai-research/SKILL]]
   - 技术专题 / 概念：[[skills/technical-topic-research/SKILL]]
   - 开源工程：[[skills/open-source-project-research/SKILL]]
   - 本地源码工程：[[projects/codebase/source-code-audit-workflow]]
5. [[skills/knowledge-linking/SKILL]]：沉淀和补链。

## 工作流

### 0. 固定本轮调研合同

先用 [[templates/technology-research-intake-template]] 固定：

- 对象类型和分流理由。
- 决策目标：学习、选型、PoC、引入、产品化、创业、采购、治理或观察。
- 当前要回答的 3-7 个关键问题。
- 证据来源计划和必须查证的近期事实。
- 本轮输出形态：短答、article、concept、选型矩阵、PoC、源码审计、公司/产品卡、图表或后续任务。
- 不做项：本轮不展开的对象、不会给出的强结论、缺少证据时不能越界的部分。

没有这一步，不要直接进入长篇调研。

### 1. 判对象

先回答：

- 这是行业 / AI 赛道吗？
- 是技术概念 / 技术路线吗？
- 是具体开源仓库吗？
- 是本地源码工程吗？
- 是公司 / 产品 / 商业机会吗？
- 是 PoC / 实验设计吗？

对象不明时，先写假设和分流理由，不直接铺完整报告。

### 2. 判决策目标

调研是为了：

- 学习。
- 选型。
- 投入研发。
- 引入开源。
- 产品化。
- 创业判断。
- 采购 / 合作。
- 风险治理。
- 持续观察。

不同目标决定读取深度和输出形态。

### 3. 建证据框架

把材料分成：

- L1 一手事实：官方文档、论文、标准、法规、repo、release、产品文档、运行日志、自测数据。
- L2 权威分析：标准组织、监管机构、AI Index、Gartner、McKinsey、NIST、OECD 等报告。
- L3 产业信号：招聘、客户案例、融资、会议、社区活跃、产品更新。
- L4 媒体 / 社区线索：新闻、博客、社交媒体、论坛，只能作为线索。
- L5 推论：必须说明依据和不确定性。
- L6 建议：必须连接证据、成熟度、风险和行动。

没有一手事实时，不给强采用建议。

### 4. 判成熟度

至少给：

- 技术成熟度：TRL 或等价阶段。
- 采用建议：Adopt / Trial / Assess / Hold 或 A/B/C/D。
- 证据置信度：high / medium / low。
- 刷新触发：哪些 release、法规、价格、benchmark、CVE、融资、产品变化或 PoC 结果会推翻当前判断。

### 5. 判风险

快速扫描：

- 安全。
- license。
- 供应链。
- 隐私。
- 合规。
- AI 幻觉和评测。
- 成本。
- 维护。
- 组织落地。

高风险项要前置，不等 PoC 后再补。

风险扫描必须区分“阻断项”和“观察项”。阻断项会阻止采用或 PoC，观察项进入复查条件。

### 6. 路由到分支

按对象和目标选择技能：

| 对象 | 技能 |
| --- | --- |
| 行业 / AI 赛道 / 公司群体 | [[skills/industry-ai-research/SKILL]] |
| 技术概念 / 方法 / 架构 | [[skills/technical-topic-research/SKILL]] |
| GitHub / Hugging Face / 开源产品 | [[skills/open-source-project-research/SKILL]] |
| 本地源码工程 | [[projects/codebase/source-code-audit-workflow]] |

如果一个任务跨多个对象，先做行业/赛道判断，再下钻到技术专题和开源工程。

### 7. 形成沉淀计划

按长期价值选择落位：

- `articles/`：本次调研正文、证据包、对比、结论和刷新条件。
- `concepts/`：稳定概念、边界、常见误区和适用场景。
- `skills/`：可重复执行的调研流程或判断套路。
- `templates/`：跨对象高频复用的报告骨架或 intake 骨架。
- `projects/`：只在对象已经进入当前项目运行层时承接任务、决策、风险或验收。

知识沉淀要配合 [[skills/knowledge-linking/SKILL]]，不能只在最终回复里留下结论。

## 输出要求

初始 intake 至少输出：

- 调研对象类型。
- 决策目标。
- 必须回答的问题。
- 证据来源计划。
- 成熟度和置信度。
- 风险门和阻断项。
- 推荐分支技能。
- 预计产物。
- 不做项。
- 验证和刷新条件。

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

- 是否先判对象，而不是直接套模板。
- 是否说明为什么选这个调研分支。
- 是否建立证据等级。
- 是否给成熟度和置信度。
- 是否前置安全、license、供应链、AI 风险和合规。
- 是否定义 PoC 或下一步行动的成功/退出条件。
- 是否说明本轮成果落到 article / concept / skill / template / project 的哪一层。
- 是否写明刷新触发条件。
