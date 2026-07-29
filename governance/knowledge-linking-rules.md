---
type: governance
id: GOV-KNOWLEDGE-LINKING-001
scope: shared
status: active
source_of_truth: true
updated: 2026-06-12
tags: [governance, knowledge-linking, knowledge]
---

# Knowledge Linking Rules

本页是 `knowledge-linking` 的治理裁定页。[[skills/knowledge-linking/SKILL]] 负责执行知识落位、入口和回链；本页负责判断“什么时候必须做知识关联、做到什么程度、哪些链接不能算有效关联”。Markdown 方言、显示名、转义、frontmatter、资产和渲染由 [[markdown-document-governance-profile.v1]] 承接。

## 必须做 knowledge-linking 的场景

- 新增或大改 `articles/`、`concepts/`、`indexes/`、`skills/`、`templates/`、`governance/`、`views/`。
- 用户要求“沉淀”“复用”“形成参考”“做成 wiki”“以后别再忘”。
- 外部资料、项目经验、迁移方法或复盘结论从聊天进入长期知识库。
- 本轮新增了规则、模板、技能、sensor 或呈现层，可能影响后续 agent 的读取路径。
- 发现某个知识只存在于 [[log]]、最终回复或孤立页面。

## 有效链接标准

有效知识关联必须说明关系类型，而不是堆链接：

- `上位`：本页属于哪个入口、治理页、概念或项目主线。
- `邻接`：哪些页面和本页共同回答同一主题的不同侧面。
- `来源`：原始材料、文章、诊断、报告或用户纠偏来自哪里。
- `应用`：哪个技能、模板、sensor 或项目流程会使用它。
- `反向`：上位入口或 owning page 是否回链到新页。

只有“参见若干链接”但不说明关系的，不能算完成 knowledge-linking。

链接是否符合本地 profile、能否在表格中安全解析以及是否需要 renderer readback，由 `python3 scripts/check_all.py --only markdown-document-governance` 和 [[markdown-document-governance-profile.v1]] 判断。knowledge-linking 通过不能上推为 Markdown 渲染通过。

## 单一信息源守卫

知识关联不是复制正文。维护时按以下规则：

- 规则裁定留在 `governance/`。
- 执行流程留在 `skills/`。
- 可复制字段留在 `templates/`。
- 视图呈现留在 `views/`。
- 稳定概念留在 `concepts/`。
- 单篇材料摘要留在 `articles/`。
- 过程记录留在 [[log]]。

入口页只保留导航、职责和短说明。若需要详细正文，链接到单一信息源。

## 关系画像

每次新增或大改长期知识页，至少在工作记录或最终回复中确认：

- 主落位。
- 主入口。
- 上位页面。
- 邻接页面。
- 是否需要反向回链。
- 是否需要 source / evidence block。
- 是否需要 sensor 或模板字段。
- 是否需要记录到 [[log]]。

对于轻量修补，可以在最终回复简写；对于结构变化，必须写进对应入口或 [[log]]。

## 禁止项

- 不让 [[log]] 成为唯一入口。
- 不把项目事实抽象成通用概念。
- 不把外部事实写成永久事实而不写刷新条件。
- 不用空泛“相关链接”代替关系说明。
- 不为了通过 sensor 添加无意义链接。
