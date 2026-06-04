---
type: article
id: ARTICLE-KNOWLEDGE-LINKING-MECHANISM-RESEARCH-2026-06-04
scope: shared
status: active
source_of_truth: false
updated: 2026-06-04
tags: [knowledge, linking, obsidian, zettelkasten, evergreen-notes, harness]
---

# 新增知识关联机制调研

## 来源

- [Obsidian Internal links](https://obsidian.md/help/links)
- [Obsidian Backlinks](https://obsidian.md/help/plugins/backlinks)
- [Obsidian Graph view](https://obsidian.md/help/plugins/graph)
- [Andy Matuschak: Evergreen notes](https://notes.andymatuschak.org/Evergreen_notes)
- [Andy Matuschak: Evergreen notes should be densely linked](https://notes.andymatuschak.org/Evergreen_notes_should_be_densely_linked)
- [Zettelkasten.de: Getting Started](https://zettelkasten.de/overview/)

## 一句话总结

新增知识的关联不应被理解成“工具自动生成语义网络”，而应被设计成“agent 做调研和语义判断，知识库用入口、上位、邻接、反向链接和 sensor 检查结构漏项”的 [[harness-engineering]] 机制。

## 关键结论

1. Obsidian 的 internal links、backlinks 和 graph view 负责展示已经存在的 `[[wikilink]]` 关系；它能帮助发现入链、出链和孤岛，但不会替维护者决定一个新知识点的上位概念、邻接案例或规则归属。
2. Evergreen notes 强调笔记要随时间演化、面向概念、保持原子化并形成密集连接。这里的“密集”不是堆链接，而是迫使写作者解释概念之间如何相关。
3. Zettelkasten 方法强调通过链接形成结构层：内容笔记、结构笔记和主结构笔记共同工作。对应到本库，就是 `articles/`、`concepts/`、`indexes/`、`governance/` 和 `skills/` 需要分工明确。
4. 对本库来说，最稳方案是把“调研、沉淀、总结、关联、验证”拆成可执行工作流：[[knowledge-linking-rules]] 管规则，[[skills/knowledge-linking/SKILL]] 管执行，`scripts/check_knowledge_linking.py` 管最小结构检查。

## 对本库的机制设计

这次采用四层机制：

1. **规则层**：[[knowledge-linking-rules]] 定义新增知识的最小关系画像，包括层级、主入口、上位关系、邻接关系、反向承接和 `[[log]]` 边界。
2. **技能层**：[[skills/knowledge-linking/SKILL]] 把调研、内部历史分析、分层落位、关系画像、验证命令和最终回复要求做成可复用 agent 技能。
3. **模板层**：[[templates/concept-template]] 和 [[templates/article-template]] 要求新增概念页 / 摘要卡片显式做知识关联自检。
4. **sensor 层**：`scripts/check_knowledge_linking.py` 通过 `python3 scripts/check_all.py --only knowledge-linking` 检查 `concepts/` 和 `articles/` 的出链、非 `[[log]]` 入链和入口 / 知识页回链。

## 历史知识库分析

本轮机制落地前，已用现有 `concepts/` 和 `articles/` 页面校准过阈值：现有概念页和摘要卡片均能满足最小关联标准，即有出链、非 `[[log]]` 入链和入口或知识页回链。

随后用临时孤岛页做负向测试：临时创建 `concepts/__tmp_orphan_check.md` 后，`python3 scripts/check_all.py --only knowledge-linking` 会失败，并指出缺出链、缺非 `[[log]]` 入链、缺入口 / 知识页回链。删除测试页后检查恢复通过。

## 方案边界

- 不自动生成语义链接：语义归属仍由 agent 基于 [[INDEX]]、入口页、上位概念和调研材料判断。
- 不把 `[[log]]` 当作入口：历史记录只证明这件事发生过，不证明读者能从知识网络找到它。
- 不让调研变成仪式：用户明确要求调研、事实不稳定或外部工具约定会影响方案时必须查；纯内部补链可只做轻量历史分析和 sensor 验证。
- 不复制正文：入口页、上位概念页和规则页只写短说明和链接，正文留在单一信息源。

## 关联概念

- [[knowledge-linking-rules]]
- [[skills/knowledge-linking/SKILL]]
- [[concepts/harness-engineering]]
- [[concepts/agent-governance]]
- [[concepts/agent-instruction-sharing]]
