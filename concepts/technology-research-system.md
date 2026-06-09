---
type: concept
id: CONCEPT-TECHNOLOGY-RESEARCH-SYSTEM-001
status: active
updated: 2026-06-09
tags: [research, technology-research, evidence, decision-system]
---

# 技术调研体系

技术调研体系，是把行业、技术、开源工程、产品、公司和 PoC 调研组织成可复用决策资产的方法系统。

它的目标不是“搜全资料”，而是让每次调研都能回答：对象是什么、证据是否可靠、成熟度到哪、价值是否成立、能否落地、风险是否可控、下一步该做什么。

相关：[[articles/2026-06-09-technology-research-capability-system]]、[[skills/technology-research-router/SKILL]]、[[templates/technology-research-intake-template]]、[[concepts/technical-research-knowledge-asset]]、[[concepts/it-ai-industry-research-asset]]、[[concepts/open-source-project-due-diligence]]

## 分层

| 层级 | 主问题 | 对应方法 |
| --- | --- | --- |
| 行业 / AI 赛道 | 趋势、玩家、产品机会、治理风险 | [[skills/industry-ai-research/SKILL]] |
| 技术专题 / 概念 | 原理、路线、适用、PoC、决策 | [[skills/technical-topic-research/SKILL]] |
| 开源工程 | 仓库健康度、跑通、代码、集成 | [[skills/open-source-project-research/SKILL]] |
| 本地源码工程 | 已读深度、复用边界、生产接入 | [[projects/codebase/source-code-audit-workflow]] |
| PoC / 实验 | 验证假设、成功标准、退出条件 | 由上面分支派生 |

## 总控原则

- 先判对象，再套模板。
- 先列证据，再下结论。
- 先区分事实、信号、推论、建议。
- 先判断成熟度和风险，再建议采用。
- 先定义 PoC 要证伪什么，再安排实验。
- 结论必须能落到行动：学习、观察、PoC、引入、产品化、创业、放弃。
- 每个长期调研资产都要写查询日期和复查触发条件。

## 必备判断轴

一个完整技术调研至少有八条判断轴：

1. 对象层级。
2. 问题和价值。
3. 技术机制。
4. 产业 / 生态位置。
5. 成熟度。
6. 经济性。
7. 安全合规和供应链。
8. 行动建议和更新机制。

## 在本库中的用法

- 用户说“补全技术调研体系”“全面调研方法”“技术调研怎么做”时，优先读 [[articles/2026-06-09-technology-research-capability-system]] 和 [[skills/technology-research-router/SKILL]]。
- 用户给出具体对象时，先用 [[templates/technology-research-intake-template]] 做 intake，再分流到行业、技术专题、开源工程或源码审计。
- 总控页面只管体系和分流；具体调研正文仍放在对应 `articles/`，稳定概念放 `concepts/`，执行流程放 `skills/`，骨架放 `templates/`。

## 常见误区

- 还没判对象，就直接写长篇报告。
- 只有资料摘要，没有证据等级和决策门。
- 把成熟度、热度、价值、可落地性混成一句“值得关注”。
- 没有 PoC 成功标准和退出条件。
- 忽略 license、供应链、隐私、AI 安全和合规。
- 没有刷新机制，导致旧调研看起来像当前事实。

## 知识关联自检

- 上位概念 / owning page：[[concepts/technical-research-knowledge-asset]]
- 邻接概念 / 案例：[[articles/2026-06-09-technology-research-capability-system]]、[[concepts/it-ai-industry-research-asset]]、[[concepts/open-source-project-due-diligence]]
- 入口回链：[[concepts/README]]、[[INDEX]]
- 不进入的层级：不替代具体行业、技术专题或开源工程调研正文。

## 相关页面

- [[articles/2026-06-09-technology-research-capability-system]]
- [[skills/technology-research-router/SKILL]]
- [[templates/technology-research-intake-template]]
- [[concepts/technical-research-knowledge-asset]]
- [[concepts/it-ai-industry-research-asset]]
- [[concepts/open-source-project-due-diligence]]
- [[articles/2026-06-09-technical-topic-research-methodology]]
- [[articles/2026-06-09-open-source-project-due-diligence-methodology]]
- [[articles/2026-06-09-it-ai-industry-research-methodology]]
