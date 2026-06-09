---
name: technology-research-router
description: 面对技术调研、AI/IT 行业调研、开源工程调研、产品/公司/PoC 研究时，用于先判对象、证据等级、成熟度、风险和输出形态，再路由到正确调研技能。
---

# 技术调研总控技能

## 定位

本技能是技术调研的总入口。它不替代具体调研技能，而是在开始前完成对象识别、证据分级、成熟度判断、风险初筛和产物选择。

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

- 已验证事实。
- 高权重分析。
- 产业信号。
- 媒体 / 社区线索。
- 推论。
- 待确认项。

没有一手事实时，不给强采用建议。

### 4. 判成熟度

至少给：

- 技术成熟度：TRL 或等价阶段。
- 采用建议：Adopt / Trial / Assess / Hold 或 A/B/C/D。
- 证据置信度：high / medium / low。

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

### 6. 路由到分支

按对象和目标选择技能：

| 对象 | 技能 |
| --- | --- |
| 行业 / AI 赛道 / 公司群体 | [[skills/industry-ai-research/SKILL]] |
| 技术概念 / 方法 / 架构 | [[skills/technical-topic-research/SKILL]] |
| GitHub / Hugging Face / 开源产品 | [[skills/open-source-project-research/SKILL]] |
| 本地源码工程 | [[projects/codebase/source-code-audit-workflow]] |

如果一个任务跨多个对象，先做行业/赛道判断，再下钻到技术专题和开源工程。

## 输出要求

初始 intake 至少输出：

- 调研对象类型。
- 决策目标。
- 必须回答的问题。
- 证据来源计划。
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
- 是否写明刷新触发条件。
