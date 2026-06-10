# Lens Registry

本页登记问题聚焦式持久 lens。临时对话内 lens 不需要登记；稳定 current lens 和需要冻结的 snapshot lens 应登记最小 provenance。

## Registry Fields

| Field | Meaning |
| --- | --- |
| lens_id | 稳定视图 id。 |
| focus_object | 状态、计划、决策、风险、issue、验收、知识、资源、owner 或时间线。 |
| lens_type | status / plan / decision / risk / issue / acceptance / knowledge / resource / owner / timeline。 |
| source_pages | 主源页面。 |
| source_scope | 单页、主题、项目、incident、资产集、运行实例或时间范围。 |
| generated_at | 生成或刷新时间。 |
| source_revision | commit、源日期、数据快照或不适用说明。 |
| evidence_boundary | confirmed / likely / possible / blocked 或本仓库补充边界。 |
| context_frame | 上位背景、来源背景、历史背景、关系背景和使用边界。 |
| output_mode | 短 Markdown、Markdown 真相源、lens page、HTML report、Notebook、dashboard、print view 或 slide。 |
| visual_structure | 状态卡、表格、矩阵、脑图、框图、流程图、关系图、时间线或证据链。 |
| photo_layout_strategy | 照片密集型 lens 的画幅家族、证据网格、竖图专题、no-crop 和判断卡策略。 |
| export_profile | PDF / PNG / print view / slide、A4 / A3 / custom、横排 / 竖排、边距、分页策略和导出目录。 |
| print_profile | `@page`、`@media print`、页眉页脚、重复表头、图表裁切和打印可读性。 |
| equivalence_profile | HTML / PDF / PNG / slide 是否同源生成，以及信息、结论、证据边界和版式语义如何保持一致。 |
| default_auto_exports | 持久 HTML lens / print view 是否默认同轮生成 PDF / PNG，以及生成工具或命令。 |
| conversation_png_preview | 最终回复是否展示 PNG 预览；无法展示时的阻塞说明。 |
| canonical_policy | 什么时候覆盖 current lens。 |
| snapshot_policy | 什么时候冻结 snapshot。 |
| staleness_policy | 哪些源变化会让 current lens 过期。 |
| refresh_trigger | 用户追问、源页面更新、状态变化、incident 更新或外部核验。 |

## Current Lenses

| lens_id | focus_object | lens_type | current_view | source_pages | updated | staleness_policy |
| --- | --- | --- | --- | --- | --- | --- |
| `lens-skill-maturity-matrix-current` | 所有工程动态发现技能项的成熟度排名、领先工程和反哺候选 | knowledge | [[views/current/governance/skill-maturity-matrix.html]] | [[skills/README]], [[projects/governance/registry]], `scripts/update_skill_maturity_matrix.py` | 2026-06-10 | 任一工程 skill / TRANSFER / governance / sensor / views / template 路径、跨工程治理注册表或三天刷新任务发生变化时刷新。 |
| `lens-xinzhi-ruisheng-company-current` | 北京芯智睿声科技有限公司企业调研 | knowledge | [[views/current/knowledge/xinzhi-ruisheng-company.html]] | [[articles/2026-06-09-xinzhi-ruisheng-company-research]], [[concepts/beijing-xinzhi-ruisheng]] | 2026-06-09 | 企业公开进展、医疗器械注册、临床 / 取证阶段、商业化上市节奏或核心来源变化时刷新。 |

## Snapshot Lenses

当前没有需要登记的 snapshot lens。
