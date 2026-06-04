---
type: guide
id: GUIDE-KNOWLEDGE-LINKING-001
scope: shared
status: active
source_of_truth: true
updated: 2026-06-04
tags: [knowledge, linking, wikilink, graph]
---

# 知识关联规则

这页定义新增知识怎样进入网状结构。它服务 `articles/`、`concepts/`、`indexes/` 和相关入口页，不替代 [[WORKFLOW]]、[[POLICY]] 或 [[log-writing-rules]]。

实际执行时优先使用 [[skills/knowledge-linking/SKILL]]。本页回答“新增知识最少要形成哪些关系”，技能页回答“agent 本轮怎样完成调研、沉淀、总结方案、补链和验证”。

核心目标不是让每篇笔记有很多链接，而是让新增知识至少回答：

- 它属于哪一层？
- 它的上位概念或 owning page 是谁？
- 它和哪些邻接概念、案例、模板、技能或规则互相说明？
- 读者从入口页能不能找到它？
- 未来从上位概念回看时，能不能回到它？

## 新增知识关联自检

新增或大幅改写一篇长期知识页时，先做一次轻量关系判断：

1. **层级归属**：判断它是证据、摘要卡片、概念 / 方法、入口索引、治理规则、项目运行页还是历史记录。
2. **主入口**：确认它应该从哪个入口被找到，例如 [[concepts/README]]、[[articles/README]]、[[INDEX]]、[[governance/README]]、[[skills/README]] 或项目入口。
3. **上位关系**：至少连到一个上位概念、方法页、治理页或 owning page。
4. **邻接关系**：如果它是对既有主题的扩展，至少连到一个同主题案例、概念、模板、技能或规则页。
5. **反向承接**：必要时更新上位页或入口页，让新页不只从自己出链，也能被旧网络发现。
6. **历史边界**：如果本轮有长期价值，按 [[log-writing-rules]] 写入 [[log]]；但 `[[log]]` 入链不能替代真正的知识网络入链。

## 最小通过标准

### 概念页

`concepts/*.md` 新增或大改时，至少满足：

- 页面正文有一个以上指向既有知识页的 `[[wikilink]]`。
- 至少有一个非 `[[log]]` 页面反向链接到它。
- 入口或上位页可发现它：优先从 [[concepts/README]]、[[INDEX]]、上位概念页或专题页进入。
- 如果它补充了某个 Harness / Agent / 项目方法主题，上位概念页要有一句短说明或反模式回链。

### 摘要卡片

`articles/*.md` 新增或大改时，至少满足：

- 页面正文有一个以上指向概念、专题、治理页或相关案例的 `[[wikilink]]`。
- 至少有一个非 `[[log]]` 页面反向链接到它；可以是 [[articles/README]]、[[INDEX]]、相关概念页或同主题文章。
- 如果文章稳定抽象出概念，应回链到 `concepts/`；如果只是案例，应回链到承接该案例的上位概念或治理页。

### 治理 / 模板 / 技能页

这类页面不强制套用 `concepts/` / `articles/` 标准，但必须遵守单一信息源：

- 规则写进 owning governance page，不散落在多个入口。
- 模板变化回链到 [[templates/README]] 和相关规则页。
- 技能变化回链到 [[skills/README]] 和相关 `TRANSFER.md` / 模板。
- 能被检查的约束优先进入 sensor，而不是只写自然语言。

## 自动检查

本库用 `scripts/check_knowledge_linking.py` 做最小网状关联检查，并通过 `python3 scripts/check_all.py --only knowledge-linking` 运行。

它只检查结构性信号：

- `concepts/` 和 `articles/` 页面是否有出链。
- 这些页面是否有非 `log.md` 的入链。
- 概念页是否能从 [[concepts/README]]、[[INDEX]] 或其他知识页被发现。
- 摘要卡片是否能从 [[articles/README]]、[[INDEX]] 或相关知识页被发现。

它不会自动生成语义链接，也不会判断某条链接是不是最佳上位概念。agent 仍要按本页做语义判断；sensor 只负责抓明显孤岛和入口漏挂。

如果用户明确要求调研，或本轮事实依赖外部工具、官方约定、近期变化、可花钱 / 花时间决策，应按 [[skills/knowledge-linking/SKILL]] 先完成外部来源校准，再写入摘要卡片、概念、规则或技能。

## 禁止项

- 不为了通过检查而随便堆链接。
- 不把 `[[log]]` 当作唯一入链；历史记录不是知识入口。
- 不把同一段正文复制到多个入口页；入口只写短说明和链接。
- 不把候选规则直接写入 [[POLICY]]，除非本轮已进入规则升级并完成冲突检查。
- 不把新概念只挂在最终回复里，文件内没有上位链接、入口链接或反向承接。
