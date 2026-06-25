---
type: governance
id: GOV-PROBLEM-FOCUSED-VISUAL-PRESENTATION-001
scope: shared
status: active
source_of_truth: true
updated: 2026-06-25
tags: [governance, problem-focused-visual-presentation, problem-focused-lens, visual-presentation, lens]
---

# Problem-Focused Visual Presentation Rules

本页是 `problem-focused-visual-presentation` 的治理合同。[[skills/problem-focused-visual-presentation/SKILL]] 负责执行图文 lens；[[templates/problem-focused-lens-template]] 负责字段骨架；[[views/README]] 和 [[views/lens-registry]] 负责持久呈现层。本页定义什么时候可以生成 lens、什么时候必须回到真相源、哪些导出件不能成为事实源。

## 核心原则

问题聚焦式图文呈现不是“把页面变漂亮”，而是把读者当前要判断的问题压缩成可见结构：

- 先固定关注问题，再选择图形。
- 先固定 source pack，再组织视觉层。
- 先说明证据边界，再给一眼判断。
- 先确认持久性，再写入 `views/`。
- 先保护单一信息源，再谈导出。
- 先通过静态视觉 QA 和同源导出，再声称 HTML / PDF / PNG 完成。

如果没有明确问题，lens 只能是装饰图；如果没有 source pack，lens 会变成第二份不可靠事实源。

持久 HTML、print view、PDF 或 PNG 还必须完成这条流水线：

`Source truth -> Content contract -> Visual strategy -> Page paradigm / slot schema -> Component semantic manifest -> Renderer implementation -> Export / accessibility / regression QA -> Human rubric`

字段齐全、token 合规、卡片整齐或文件存在都不能单独证明完成；它们只是可检查的结构信号。

## 启动条件

以下场景可以启动 problem-focused lens：

- 用户明确要“图文”“HTML”“一图胜千言”“更直观”“直观看”“图文混排”“矩阵”“导出 PNG / PDF”“current / snapshot”。
- 多个文档、报告、issue、风险、决策或状态需要压缩成一个可读视图。
- 复杂主题需要呈现“当前判断 + 背景框 + 证据链 + 缺口 + 下一步”。
- 需要给用户看矩阵、热力图、任务地图、时间线、关系图、状态看板或验收缺口。
- 本轮形成稳定 current lens 或阶段 snapshot，且后续会复看。

以下场景不启动持久 lens：

- 用户只问一个简单事实、只查一个路径或只要一句结论。
- source pack 不稳定，尚未确认主入口。
- 结论会在几分钟内被一次命令刷新替代。
- 正式状态、验收或规则裁决还没有写回主入口。
- 只是为了通过矩阵成熟度而制造页面。

如果用户明确要求“HTML”“PDF”“PNG”“打印”“一图胜千言”“图文混排”“状态页”“风险页”“验收页”“决策页”“主题梳理”，默认进入本技能；只有用户明确说只要口头结论、只分析不落文件或先看路径，才降级为聊天内 lens。

## Source Pack 合同

每个 lens 必须列出 source pack。source pack 不只是“引用列表”，而是证据合同：

- `source_pages`：已读且直接支撑 lens 的页面。
- `source_scope`：本轮覆盖范围和未读但相关范围。
- `source_revision`：使用的 commit、生成时间或文件版本。
- `evidence_boundary`：confirmed / likely / possible / blocked。
- `refresh_trigger`：哪些源变化后必须刷新 lens。
- `single_source_guard`：哪些页面仍是真相源，lens 不能替代它们。

如果 source pack 里存在未读关键页面，lens 必须把相关判断降级，不允许写成 confirmed。

## Focus Contract

每个 lens 必须先冻结：

- `focus_object`
- `lens_type`
- `judgement_purpose`
- `source_pack`
- `evidence_boundary`
- `output_mode`
- `persistent_or_temporary`
- `export_required`

`lens_type` 至少覆盖 `status / plan / decision / risk / issue / acceptance / knowledge / resource / owner / timeline`。自动生成时，不能用一个通用 `html` 类型替代真实关注对象。

## 背景框

成熟 lens 至少给出四层背景：

- `上位背景`：属于哪个项目、治理主题、技能、模板、验收或知识体系。
- `来源背景`：哪些文档、截图、数据、诊断或人工确认支撑了当前视图。
- `历史背景`：这是 current、snapshot、旧结论修正、阶段对比还是一次性观察。
- `关系背景`：连接哪些 owner、任务、风险、issue、报告、规则或资产。

背景框的目标是让读者知道“这张图在回答哪个问题”，而不是把所有文档摘要塞进首屏。

## 视觉结构选择

| 关注问题 | 推荐结构 | 关键边界 |
| --- | --- | --- |
| 当前状态是什么 | 状态卡、红黄绿看板、矩阵 | 状态源必须写清 |
| 哪些能力缺口最重要 | 热力矩阵、缺口表、优先级图 | 分数不能替代诊断 |
| 哪条链路断了 | 流程图、泳道图、证据链 | 不能把候选根因写成事实 |
| 多方案怎么比较 | 对比矩阵、雷达图、排序表 | 评分口径必须显式 |
| 任务怎么推进 | 行动地图、依赖图、时间线 | owner 和验收层级分开 |
| 知识如何组织 | 关系图、入口图、层级图 | 链接要有关系类型 |
| 验收能否关闭 | 证据层级表、缺口矩阵 | 局部通过不能上推 |

Mermaid 只适合小流程和短链路。大型架构图、复杂拓扑或需要持续编辑的图，遵守本库 Excalidraw / Diagrams.Net 规则，不用 Mermaid 硬撑。

## 视觉策略必填项

复杂或持久 lens 必须在 metadata、模板正文或 HTML manifest 中写清：

- `art_direction_brief`
- `information_topology`
- `layout_morphology_plan`
- `topic_visual_language`
- `primary_visual_metaphor`
- `theme_specific_elements`
- `anti_information_listing_strategy`
- `page_paradigm`
- `component_semantic_manifest`
- `human_rubric`
- `result_cluster_diagnosis`

知识型内容优先考虑脑图、概念图、关系图或分层地图；流程用路径图 / 泳道图；系统边界用结构边界图；验收和对比用矩阵。不要把所有页面都退化成标题 + 卡片 + 表格。

## 持久化规则

本库持久呈现层固定为 `views/`：

- `views/current/`：当前版本的 canonical lens。
- `views/snapshots/`：阶段性快照、会议快照、验收快照或历史对比。
- `views/lens-registry.md`：登记 lens id、主题、source pack、刷新触发、导出状态和人工边界。
- `views/.exports/`、`views/exports/`、`views/**/.exports/`：PDF / PNG / SVG 导出缓存，默认不提交。

持久 lens 写入时必须同步 registry。没有 registry 的孤立 HTML 不算完成。

## 导出与同源一致性

HTML、print view、PNG、PDF、SVG 之间必须保持同源：

- canonical HTML 或 Markdown 是主呈现。
- print view 只调整打印样式和分页，不改变事实。
- PNG 用于聊天预览和快速复看，不成为第二份真相源。
- PDF 用于分发和归档，不承接后续编辑。
- SVG 只在图形源需要时保留，不能和 HTML 产生独立事实。

只要本轮生成或刷新持久 HTML lens，就必须同轮生成同源 PDF 和至少一张 PNG 截图 / 长图到 `.gitignore` 忽略目录，并在最终回复用 Markdown 图片语法展示 PNG 预览。HTML / PDF / PNG 必须来自同一 source manifest 或 render pipeline；禁止为了聊天展示另画一张不同源 PNG。

如果导出失败，最终回复只能说“未导出”或“导出未验证”；不能因为 HTML 存在就声称 PNG / PDF 已生成。

## Static Visual QA

复杂或持久 HTML / PDF / PNG 输出必须在产物自身 meta、JSON script 或等价机器可读块里留下 `static_visual_qa`，至少覆盖：

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

Sensor 只检查字段、入口、导出路径和不上推边界；它不能替代人审、截图审阅或视觉模型判断美感。

## 验收、状态和规则不上推

Lens 只能帮助看懂，不自动完成裁决：

- 验收关闭回到 acceptance plan、test report、issue、TASK、EP、FP、Gate。
- 项目状态回到 `projects/README.md` 或 owning status page。
- 服务运行事实回到 `projects/service-registry.md`。
- 规则裁定回到 `governance/`。
- 技能成熟度回到 skill、TRANSFER、sensor、template、views 和专项检查。

如果 lens 发现缺口，只能把缺口路由到对应主入口，不能让图本身成为修复完成证明。

## 质量自检

完成 lens 前至少检查：

- 首屏是否回答当前关注问题。
- 是否列出 source pack 和 evidence boundary。
- 是否避免 metadata 抢占读者注意。
- 是否有 current / snapshot 边界。
- 是否写清 refresh_trigger。
- 是否更新 `views/lens-registry.md`。
- 是否没有提交 PDF / PNG / SVG 缓存作为事实源。
- 是否在持久 HTML 中留下 `static_visual_qa` 和 `component_semantic_manifest`。
- 是否为本轮更新的持久 HTML 实际生成同源 PDF / PNG，或明确写出失败原因。
- 是否运行 `python3 scripts/check_all.py --only problem-focused-visual-presentation`。

## 失败模式

- `装饰化`：图很漂亮，但没有关注问题和证据边界。
- `二次事实源`：lens 复制主页面正文并开始承接状态维护。
- `快照冒充 current`：历史页面没有标记生成时间和刷新条件。
- `导出冒充完成`：PNG / PDF 没生成或没验证，却写成已交付。
- `矩阵替代诊断`：颜色和分数替代了原因、缺口和下一步。
- `图文替代验收`：把看板绿灯当成 Gate / TASK 关闭证据。
- `registry 漏登`：HTML 存在，但没有 registry、source pack 和刷新触发。
- `视觉弱完成`：只有卡片和表格，没有主视觉、层级幅度、组件语义或 human rubric。
- `不同源预览`：HTML、PDF、PNG 来自不同内容或临时重画截图。

这些失败模式出现时，优先补合同和入口，不扩大成无关视觉重做。
