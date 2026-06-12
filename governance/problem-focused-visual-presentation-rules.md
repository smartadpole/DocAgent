---
type: governance
id: GOV-PROBLEM-FOCUSED-VISUAL-PRESENTATION-001
scope: shared
status: active
source_of_truth: true
updated: 2026-06-12
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

如果没有明确问题，lens 只能是装饰图；如果没有 source pack，lens 会变成第二份不可靠事实源。

## 启动条件

以下场景可以启动 problem-focused lens：

- 用户明确要“图文”“HTML”“一图胜千言”“更直观”“矩阵”“导出 PNG / PDF”“current / snapshot”。
- 多个文档、报告、issue、风险、决策或状态需要压缩成一个可读视图。
- 复杂主题需要呈现“当前判断 + 背景框 + 证据链 + 缺口 + 下一步”。
- 需要给用户看矩阵、热力图、任务地图、时间线、关系图、状态看板或验收缺口。
- 本轮形成稳定 current lens 或阶段 snapshot，且后续会复看。

以下场景不启动持久 lens：

- 用户只问一个简单事实。
- source pack 不稳定，尚未确认主入口。
- 结论会在几分钟内被一次命令刷新替代。
- 正式状态、验收或规则裁决还没有写回主入口。
- 只是为了通过矩阵成熟度而制造页面。

## Source Pack 合同

每个 lens 必须列出 source pack。source pack 不只是“引用列表”，而是证据合同：

- `source_pages`：已读且直接支撑 lens 的页面。
- `source_scope`：本轮覆盖范围和未读但相关范围。
- `source_revision`：使用的 commit、生成时间或文件版本。
- `evidence_boundary`：confirmed / likely / possible / blocked。
- `refresh_trigger`：哪些源变化后必须刷新 lens。
- `single_source_guard`：哪些页面仍是真相源，lens 不能替代它们。

如果 source pack 里存在未读关键页面，lens 必须把相关判断降级，不允许写成 confirmed。

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

如果导出失败，最终回复只能说“未导出”或“导出未验证”；不能因为 HTML 存在就声称 PNG / PDF 已生成。

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
- 是否运行 `python3 scripts/check_all.py --only problem-focused-visual-presentation`。

## 失败模式

- `装饰化`：图很漂亮，但没有关注问题和证据边界。
- `二次事实源`：lens 复制主页面正文并开始承接状态维护。
- `快照冒充 current`：历史页面没有标记生成时间和刷新条件。
- `导出冒充完成`：PNG / PDF 没生成或没验证，却写成已交付。
- `矩阵替代诊断`：颜色和分数替代了原因、缺口和下一步。
- `图文替代验收`：把看板绿灯当成 Gate / TASK 关闭证据。
- `registry 漏登`：HTML 存在，但没有 registry、source pack 和刷新触发。

这些失败模式出现时，优先补合同和入口，不扩大成无关视觉重做。
