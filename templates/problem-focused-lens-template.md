---
type: template
id: TEMPLATE-PROBLEM-FOCUSED-LENS
status: active
updated: 2026-06-10
tags: [template, lens, presentation, problem-focused]
---

# {{lens_title}}

## Metadata

| Field | Value |
| --- | --- |
| lens_id | {{stable lens id}} |
| focus_object | {{status / plan / decision / risk / issue / acceptance / knowledge / resource / owner / timeline}} |
| lens_type | {{status / plan / decision / risk / issue / acceptance / knowledge / resource / owner / timeline}} |
| judgement_purpose | {{understand / compare / act / accept / account / review / learn / sediment}} |
| source_pages | {{source wikilinks or paths}} |
| source_scope | {{single-page / topic / project / incident / asset-set / runtime / time-range}} |
| generated_at | {{YYYY-MM-DD HH:MM timezone}} |
| source_revision | {{commit / source date / data snapshot / not applicable}} |
| evidence_boundary | {{confirmed / likely / possible / blocked, plus local project terms if needed}} |
| context_frame | {{see Context Frame}} |
| output_mode | {{short_markdown / markdown_source / lens_page / html_report / notebook / dashboard / print_view / slide}} |
| visual_structure | {{status_card / table / matrix / mind_map / block_diagram / flowchart / relation_graph / timeline / evidence_chain}} |
| photo_layout_strategy | {{if photo-heavy: aspect-family layout, landscape evidence grid, portrait feature row/column, main-plus-secondary, text-note placement, no-crop policy}} |
| export_profile | {{targets, page size, orientation, margins, pagination, export dir}} |
| print_profile | {{@page, @media print, headers, repeated table headers, chart clipping, readability}} |
| equivalence_profile | {{HTML / PDF / PNG / slide same-source and semantic equivalence policy}} |
| canonical_policy | {{when this current lens is refreshed}} |
| snapshot_policy | {{when to freeze a snapshot}} |
| staleness_policy | {{what source changes make this lens stale}} |
| refresh_trigger | {{user question / source update / status change / incident update / external verification}} |
| snapshot_of | {{only for snapshot lenses; otherwise omit}} |

## One Screen View

首屏只放用户当前判断需要的信息，不把 metadata 当主体。

- 当前判断：
- 下一步：
- 关键风险 / 缺口：
- 不能上推：

## Context Frame

- 上位背景：
- 来源背景：
- 历史背景：
- 关系背景：
- 使用边界：

## Evidence Boundary

| Claim | Boundary | Source | Cannot Prove |
| --- | --- | --- | --- |
| {{claim}} | {{confirmed / likely / possible / blocked}} | {{source}} | {{boundary}} |

## Lens Body

按主 `lens_type` 填写：

- `status`：当前态、阶段、阻塞、下一步、状态来源、更新时间。
- `plan`：目标、约束、依赖、可执行动作、blocked 条件、时间窗、资源。
- `decision`：候选方案、取舍维度、已确认、待确认、当前倾向、裁决入口。
- `risk`：触发条件、影响对象、概率 / 影响、缓解动作、剩余风险、监控点。
- `issue`：原始现象、影响范围、证据链、根因候选、验证边界、下一步。
- `acceptance`：验收对象、关闭标准、证据层级、缺口、人工确认边界、回归范围。
- `knowledge`：结论、来源、上位概念、邻接关系、适用边界、禁用场景。
- `resource`：位置、版本、权限、用途、owner、归档入口、追溯入口。
- `owner`：owner、协同方、确认状态、责任边界、依赖对象、升级条件。
- `timeline`：关键节点、转折点、状态变化、证据回链、未闭合影响。

## Visual Structure

- 主视觉结构：
- 辅助视觉结构：
- 如果包含照片 / 视觉证据：
  - 扫读路径：
  - 画幅家族：
  - 排版模式：
  - 证据图裁切策略：默认 `object-fit: contain`，不裁切证据图。
  - 判断卡位置：

## Output / Export Profile

- output_mode：
- export_profile：
- print_profile：
- equivalence_profile：
- default_auto_exports：
- conversation_png_preview：
- ignored export 目录：
- A4 / A3 适配说明：
- canonical / export 边界：提交 canonical HTML / source / manifest；PDF / PNG / SVG 放 ignored export 目录，不和真相源重复提交。
- 未实际导出或展示的阻塞声明：

## Refresh Notes

- 本轮刷新：
- 未读取但邻接相关：
- 下次必须刷新条件：
