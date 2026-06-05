---
type: concept
id: CONCEPT-AI-ERA-INFORMATION-PRESENTATION-001
status: active
updated: 2026-06-05
tags: [ai, information-architecture, presentation, markdown, html, rag]
---

# AI 时代信息记录、处理与呈现方式

AI 时代信息记录、处理与呈现方式，是指在 LLM、agent、RAG 和可交互前端共同参与后，信息从“静态给人阅读”转向“同时服务保存、检索、推理、协作、操作和决策”的组织方式。

核心判断是：信息不再只有一个最终版页面，而应先区分三种基础职能：

- **记录**：事实、来源、版本和责任保存在哪里。
- **处理**：模型怎样找到、理解、组合和生成。
- **呈现**：人怎样快速理解、比较、决策和行动。

如果要做完整信息架构，这三种职能还应展开成五层：记录、组织、处理、呈现、归档 / 分发。

## 分层

| 层级 | 典型形态 | 主要职责 | 职能 |
| --- | --- | --- | --- |
| 源 | Markdown、CSV、代码、原始资料、语义静态 HTML | 保存事实、版本、来源和审计路径 | 记录 |
| 索引 | chunk、embedding、vector store、搜索索引、HTML-aware retrieval | 帮助模型和人快速召回候选内容 | 处理 |
| 关系 | wikilink、backlink、目录、上位概念、邻接页面 | 让知识结构、依赖、冲突和演进显式可见 | 记录 + 处理 |
| 界面 | HTML、Artifact、Notebook、dashboard、slide deck | 支持实时呈现、筛选、比较、复现和决策 | 呈现 |
| 归档 | PDF、PPTX、WARC、MHTML、静态 HTML package | 保存发布结果、交付材料或网页快照 | 分发 + 记录 |

## 基本原则

- Markdown 更适合作为长期轻量真相源；HTML 要区分记录型和呈现型。
- 向量库是派生索引，不是知识主库。
- 超链接和入口页是语义结构的一部分，不能完全交给 embedding 代替。
- 面向复杂系统的呈现不应只做固定总览；应按读者当前关注的问题生成 [[concepts/problem-focused-information-presentation|问题聚焦式信息呈现]] lens，并回链到源、证据和关系层。
- 语义静态 HTML 可以成为记录格式；动态 HTML / SPA / dashboard 默认只是运行时呈现界面，除非补齐源、数据快照、构建方式和归档。
- PPT / PDF 适合作为正式分发和归档格式，但不应反向定义调研、分析和 agent 协作的主链。
- 面向 agent 的信息应保留可执行命令、路径、API、预期输出和权限边界。

## 判断标准

判断一种信息格式或工具是否适合某一层，不看后缀名，而看它提供哪些保证：

| 保证 | 问题 |
| --- | --- |
| 可读性 | 人和模型能否低噪声读懂 |
| 可寻址性 | 能否稳定引用到段落、版本或对象 |
| 可关系化 | 能否表达上位、邻接、来源、依赖和冲突 |
| 可计算性 | 能否被检索、抽取、执行和重组 |
| 可呈现性 | 能否帮助人比较、探索、决策 |
| 可复现性 | 能否重新生成同一结果 |
| 可归档性 | 能否长期保存发布状态和证据 |
| 可治理性 | 权限、审计、安全和责任是否清楚 |

因此，Markdown 的价值不是 `.md`，而是可读、可 diff、可链接、模型友好；HTML 的价值也不只是 `.html`，而是它在语义静态形态下可记录，在动态交互形态下可呈现，在 WARC / MHTML / static package 形态下可归档。

## 适用场景

- 设计 AI agent 可读的知识库、项目文档和规则系统。
- 判断一份研究、报告、方案或评审材料应该用 Markdown、RAG、HTML 还是 PPT。
- 设计从资料收集到实时呈现的工作流。
- 判断 HTML 产物是记录型、呈现型还是归档型。
- 把静态文档升级成可交互 dashboard、Notebook、Artifact 或 HTML report，同时保留记录层。

## 和本库的关系

本概念是 [[concepts/document-os]] 在 AI 时代的信息界面侧扩展：

- [[knowledge-linking-rules]] 负责让 Markdown 知识源形成关系网。
- [[skills/knowledge-linking/SKILL]] 负责调研、沉淀、补链和验证。
- [[articles/2026-06-05-ai-era-information-presentation-research]] 记录本专题调研结论。
- [[concepts/problem-focused-information-presentation]] 承接本专题在“每次关注某个具体问题时怎样选择展示 lens”的方案化延伸。
- [[articles/2026-06-04-knowledge-linking-mechanism-research]] 是邻接研究，说明为什么语义关联不能只依赖自动图谱或最终回复。

## 常见误区

- 把 RAG 当成知识库本身，忽略源文件和版本。
- 把 Markdown + 链接当成 UI，忽略交互和数据探索需求。
- 把 HTML report 当成唯一交付物，缺少源、数据快照和审计链。
- 把所有 HTML 都当成长期记录，忽略动态运行态、远程资源、权限和归档问题。
- 把 PPT 完全否定；实际更稳的做法是把 PPT 降级为导出和分发格式。

## 相关页面

- [[articles/2026-06-05-ai-era-information-presentation-research]]
- [[concepts/problem-focused-information-presentation]]
- [[concepts/document-os]]
- [[concepts/harness-engineering]]
- [[knowledge-linking-rules]]
- [[skills/knowledge-linking/SKILL]]
- [[articles/2026-06-04-knowledge-linking-mechanism-research]]
