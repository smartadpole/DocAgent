---
name: problem-focused-visual-presentation
description: 问题聚焦式图文呈现技能；用于把复杂文档、主题、状态、风险、计划、验收、知识或证据链重组为可读、可追溯、带视觉主角和证据边界的 HTML / 图文 lens。
maturity: leading
evidence_signals: [skill, README entry, template, governance, sensor, TRANSFER, views, reference, exported-sample]
transfer_ready: true
sensor: python3 scripts/check_all.py --only problem-focused-visual-presentation,skill-maturity
---

# Problem-Focused Visual Presentation

## 定位

本技能把复杂文字、文档、专题或项目状态重组为面向当前关注问题的图文 lens。

它吸收 AcknowledgeBase 和下游工程中成熟的问题聚焦呈现方法，并在本库绑定既有 `views/` 持久呈现层。默认仍先产出聊天内 Markdown / 表格 / Mermaid / 结构化图文方案；只有用户明确要求 HTML、持久页面、打印、导出，或本轮已经形成可长期复用的 current / snapshot lens 时，才写入 [[views/README]]。

统一流水线固定为：

`Source truth -> Content contract -> Visual strategy -> Page paradigm / slot schema -> Component semantic manifest -> Renderer implementation -> Export / accessibility / regression QA -> Human rubric`

## 适用场景

- 用户说“信息乱”“阅读不方便”“一图胜千言”“直观看”“做成图文”“图文混排”“HTML 呈现”。
- 用户要看一个文档、主题、状态页、风险页、计划页、决策页、验收页、issue、知识材料、资源、owner 或时间线。
- 用户需要比较多个对象、看证据链、看缺口、看行动地图或把材料转成可分发视图。
- 用户要求 HTML / PDF / PNG / 打印 / snapshot / current lens。

## 不适用场景

- 简单问答、只查一个路径、只要一句结论时，不启动完整 lens。
- 正式验收关闭、状态推进、issue 关闭、发布准出或规则裁决不能被 lens 替代。
- 测试报告、项目状态、Issue、风险、决策、handoff、log 和 memory 仍回到自己的 owner 页面。
- 不为了视觉好看牺牲证据边界；必须写清来源、更新时间、未读来源和不可上推范围。
- 不默认创建持久 HTML；只有用户要求或仓库已有持久呈现层时才落文件。

## 成熟度与证据信号

- `maturity`：`leading`。本技能已具备技能正文、README 入口、迁移边界、治理接线、模板、`views/` 持久呈现层、参考范式、导出样本和专项 sensor。
- `template`：持久 lens 模板见 [[templates/problem-focused-lens-template]]，只承接字段骨架，不替代 source pack 或事实源。
- `views`：持久 lens 入口见 [[views/README]]，current / snapshot 登记见 [[views/lens-registry]]；持久 lens 必须声明 `export_profile`、`print_profile`、`equivalence_profile`、`default_auto_exports`、`conversation_png_preview`、视觉策略字段和 `static_visual_qa`，导出缓存必须落在 `.gitignore` 忽略目录。
- `reference`：页面范式、组件语义和视觉完成度口径见 `skills/problem-focused-visual-presentation/reference/`，用于指导 renderer 和 sensor，不承接项目事实。
- `governance`：持久化、证据边界、项目状态和验收不上推回到 [[governance/problem-focused-visual-presentation-rules]]、[[response-mode-routing]]、[[POLICY]] 和目标单一信息源。
- `TRANSFER`：迁移边界见 [[skills/problem-focused-visual-presentation/TRANSFER]]；迁移时吸收 lens 合同、source pack、背景框、证据边界、视觉流水线、同源导出和 QA 守卫，不复制具体视图。
- `sensor`：`python3 scripts/check_all.py --only problem-focused-visual-presentation` 检查技能、模板、`views/` registry、参考文件、HTML meta、`static_visual_qa`、导出缓存忽略规则和总门禁接线。
- `evidence boundary`：本技能证明的是呈现质量和追溯边界，不证明原事实完整或验收完成。

## 工作流

### 1. 冻结关注合同

每次生成 lens 前先冻结 focus contract：

- `focus_object`：本轮聚焦的文档、主题、状态、风险、决策、计划、验收、issue、知识或资源。
- `lens_type`：`status / plan / decision / risk / issue / acceptance / knowledge / resource / owner / timeline`。
- `judgement_purpose`：看懂、比较、行动、验收、追责、回顾、学习或沉淀。
- `source_pack`：已读来源、未读但相关来源、更新时间、证据和推断。
- `evidence_boundary`：`confirmed / likely / possible / blocked`。
- `output_mode`：短答、Markdown、Mermaid、HTML、HTML + assets、PDF / PNG、slide、临时 artifact、持久 current 或 snapshot。
- `persistent_or_temporary`：聊天内临时、`views/current/` 或 `views/snapshots/`。
- `export_required`：是否必须导出 PDF / PNG / print view / slide。

简单问答不启动完整 lens。显式要求 HTML、图文文件、打印、PDF / PNG 或持久页面时，默认进入持久 lens 路径。

### 2. 组装 source pack

按对象读取最小必要源：

- 单文档：目标文档、frontmatter、出链 / 入链、相关入口。
- 主题：主题入口、概念页、相关文章、报告、决策、log、raw / assets。
- 状态 / 验收 / issue：状态页、事项页、报告、issue、风险、服务台账或运行证据。
- 运行 / 代码事实：代码位置、日志、测试、artifact、服务状态和相关文档。

source pack 必须标明已读、未读但相关、更新时间、哪些结论来自证据、哪些只是推断。

### 3. 建背景框和证据边界

每个 lens 都要包含：

- 上位背景：属于哪个项目、主题、概念、计划或事件。
- 来源背景：读了哪些文档，哪些只是邻接未读。
- 历史背景：新结论、旧结论修正、阶段快照还是历史证据。
- 关系背景：连接哪些文档、owner、任务、风险、决策或资产。
- 使用边界：适合用于什么判断，不能上推到哪里。

证据边界使用：

- `confirmed`：已由源页面、记录、截图、票据、决策、人工确认、脚本检查或可靠数据支撑。
- `likely`：证据较强，但缺少关键确认、最新核验或完整闭环。
- `possible`：合理候选或推断，不能写成当前结论。
- `blocked`：缺少权限、核验、人工确认、数据快照或源页面。

### 4. 设计视觉策略

复杂或持久 lens 必须先填写视觉策略，再开始写 HTML：

- `art_direction_brief`：这张 lens 的视觉主角和阅读气质。
- `information_topology`：信息之间是层级、网络、路径、矩阵、时间线还是边界结构。
- `layout_morphology_plan`：首屏、主图、证据区、追溯区和行动区如何分布。
- `topic_visual_language`：该主题专属图形、颜色、线条、标签、网格或图标语义。
- `primary_visual_metaphor`：主视觉隐喻，例如地图、控制台、证据链、边界图或分层脑图。
- `theme_specific_elements`：只属于本主题的视觉元素，避免通用卡片堆叠。
- `anti_information_listing_strategy`：哪些长列表下沉，哪些信息前置为图形结构。
- `page_paradigm`：选用 `current-status-dashboard / decision-comparison / evidence-chain / concept-map / timeline / matrix / boundary-map / resource-map` 等范式。
- `component_semantic_manifest`：本页组件角色清单，例如 verdict strip、evidence rail、matrix cell、timeline node、boundary block、trace link。
- `human_rubric`：完成前由人读时用来判断是否真的直观的标准。
- `result_cluster_diagnosis`：如果页面退化成标题 + 卡片 + 表格，要指出并调整。

### 5. 选择图文结构

| 目的 | 优先结构 |
| --- | --- |
| 一眼看状态 | 状态卡、看板、红黄绿矩阵 |
| 比较方案 / 版本 / 缺口 | 表格、评分矩阵、差异热力表 |
| 理解主题结构 | 脑图、树图、主题地图 |
| 理解系统或边界 | 框图、架构图、边界图 |
| 推进计划或排障 | 流程图、泳道图、行动地图 |
| 回看演进 | 时间线、里程碑图 |
| 看多文档关系 | 关系图、引用地图、证据链图 |
| 验收或关闭 | 证据层级表、缺口矩阵、不可上推边界 |

矩阵和热力图优先用整格状态表达，不把长证据塞进格子；详情放到卡片或追溯区。知识型内容优先考虑脑图、概念图、关系图或分层地图；流程用路径图 / 泳道图；系统边界用结构边界图；验收和对比用矩阵。不要让所有页面退化成标题 + 卡片 + 表格。

页面范式和组件语义参考：

- `skills/problem-focused-visual-presentation/reference/page-paradigm-library.md`
- `skills/problem-focused-visual-presentation/reference/component-semantic-manifest.md`
- `skills/problem-focused-visual-presentation/reference/visual-finish-rubric.md`

### 6. 输出、持久化和同源导出

默认聊天内输出即可。只有满足以下条件才写文件：

- 用户明确要求 HTML / 图文文件 / 下载 / 打印 / PDF / PNG / 持久页面。
- 当前主题稳定，适合作为 canonical current lens。
- 本轮形成决策、验收、发布、事故、阶段复盘或外部分发 snapshot。
- 当前仓库已有 `views/`、`reports/` 或等价呈现层。

本库的持久呈现层固定为 [[views/README]]。新增 current lens 放 `views/current/` 并同步 [[views/lens-registry]]；阶段性 snapshot 放 `views/snapshots/` 并同步 registry。导出 PDF / PNG / SVG 缓存放 `views/.exports/`、`views/exports/`、`views/**/.exports/` 或等价忽略目录，不提交为第二份事实源。

只要本轮生成或更新持久 HTML lens，就必须同轮从同一 source manifest / render pipeline 生成 PDF 和至少一张 PNG，并在最终回复里展示 PNG 预览。禁止为了聊天展示另画一张不同源 PNG。

### 7. 静态视觉 QA

复杂或持久 HTML / PDF / PNG 输出必须在产物自身 meta 或等价机器可读块里留下 `static_visual_qa`，至少覆盖：

- `layout_frame`
- `type_scale`
- `spacing_rhythm`
- `semantic_palette`
- `component_roles`
- `accessibility_checks`
- `export_render_check`
- `finish_grade`
- `visual_strength_gate`
- `hierarchy_amplitude_gate`
- `component_variety_gate`
- `color_budget_single_hero_gate`
- `adjustment_loop`
- `rendered_visual_review`
- `review_artifact`
- `visual_acceptance_result`

sensor 只能检查字段、导出留痕和同源约束，不能替代人审或视觉模型判断美感。

## 输出格式

```markdown
**一眼判断**
- 当前结论：
- 下一步 / 当前动作：
- 风险或缺口：

**背景框**
- 上位背景：
- 来源背景：
- 历史背景：
- 关系背景：
- 使用边界：

**图文主体**
- 结构：
- 图 / 表：

**证据边界**
- confirmed：
- likely：
- possible：
- blocked：

**证据与追溯**
- 已读来源：
- 关键证据：
- 原始入口：

**导出和持久化**
- 是否持久：
- 导出需求：
- PDF / PNG：
- static_visual_qa：
- 未覆盖边界：
```

## 禁止项

- 不把图文 lens 当作项目状态、验收、准出、关闭或规则裁决。
- 不让 metadata 抢占首屏；首屏先回答用户现在该看什么。
- 不把历史快照当 current。
- 不在未生成和检查导出件时声称“已导出”。
- 不提交同一 lens 的 HTML、PDF、PNG、SVG 等重复渲染物作为多个事实源。
- 不绕开 [[templates/problem-focused-lens-template]] 和 [[views/lens-registry]] 生成孤立持久 HTML。
