---
type: template
id: TEMPLATE-PROBLEM-FOCUSED-LENS-001
scope: shared
status: active
source_of_truth: false
updated: 2026-06-25
tags: [template, lens, problem-focused, visual-presentation, html-lens]
---

# Problem-Focused Lens Template

> 用于生成或维护 `views/current/`、`views/snapshots/` 或一次性图文 lens。复制后删除提示文字，并保留证据边界。lens 只负责呈现，不替代 owner 页面。

## Metadata

- `lens_id`:
- `focus_object`:
- `lens_type`: status / plan / decision / risk / issue / acceptance / knowledge / resource / owner / timeline
- `judgement_purpose`: 看懂 / 比较 / 行动 / 验收 / 追责 / 回顾 / 学习 / 沉淀
- `source_pages`:
- `source_scope`:
- `generated_at`:
- `source_revision`:
- `evidence_boundary`: confirmed / likely / possible / blocked
- `context_frame`:
- `output_mode`: markdown / html_report / print_view / snapshot / current
- `persistent_or_temporary`:
- `export_required`: none / pdf / png / pdf+png / slide
- `visual_structure`: status-card / matrix / timeline / relation-map / evidence-chain / action-map / concept-map / boundary-map / mixed
- `export_profile`:
- `print_profile`:
- `equivalence_profile`:
- `default_auto_exports`:
- `conversation_png_preview`:
- `canonical_policy`:
- `snapshot_policy`:
- `staleness_policy`:
- `refresh_trigger`:

## Focus Contract

- `focus_object`：
- `lens_type`：
- `judgement_purpose`：
- `source_pack`：
- `evidence_boundary`：
- `output_mode`：
- `persistent_or_temporary`：
- `export_required`：

## 一眼判断

- 当前结论：
- 下一步 / 当前动作：
- 风险或缺口：
- 不能上推：

## 背景框

- 上位背景：
- 来源背景：
- 历史背景：
- 关系背景：
- 使用边界：

## Source Pack

- 已读来源：
- 未读但相关：
- 最新性 / 更新时间：
- 关键证据：
- 推断：

## 证据边界

- `confirmed`：
- `likely`：
- `possible`：
- `blocked`：

## 视觉策略

- `art_direction_brief`：
- `information_topology`：
- `layout_morphology_plan`：
- `topic_visual_language`：
- `primary_visual_metaphor`：
- `theme_specific_elements`：
- `anti_information_listing_strategy`：
- `page_paradigm`：
- `component_semantic_manifest`：
- `human_rubric`：
- `result_cluster_diagnosis`：

## Page Paradigm / Slot Schema

- 首屏判断区：
- 背景框：
- 主视觉：
- 证据边界：
- 追溯入口：
- 行动分流或 owner 回写：
- 导出和刷新说明：

## 图文主体

优先选择一种主视觉结构，不要把所有内容都堆成长文。

- 主结构：
- 图 / 表：
- 详情卡：
- 追溯入口：

按 lens 类型选择：

- `status`：状态总览、变化点、阻塞、下一步。
- `plan`：阶段、路径、依赖、owner、验收点。
- `decision`：选项、标准、取舍、待确认。
- `risk`：风险源、影响面、触发条件、缓解动作。
- `issue`：原始现象、证据层、修复层、复验层、不可关闭边界。
- `acceptance`：验收对象、证据分层、缺口矩阵、人工确认边界。
- `knowledge`：概念图、脑图、关系图或分层地图。
- `resource`：资源类型、可用性、权限、更新条件。
- `owner`：职责边界、协作接口、交接点。
- `timeline`：事件顺序、版本、转折点、未确认段。

## Static Visual QA

复杂或持久 HTML / PDF / PNG 输出必须在产物自身 meta 或等价机器可读块里留下 `static_visual_qa`：

- `layout_frame`：
- `type_scale`：
- `spacing_rhythm`：
- `semantic_palette`：
- `component_roles`：
- `accessibility_checks`：
- `export_render_check`：
- `finish_grade`：
- `visual_strength_gate`：
- `hierarchy_amplitude_gate`：
- `component_variety_gate`：
- `color_budget_single_hero_gate`：
- `adjustment_loop`：
- `rendered_visual_review`：
- `review_artifact`：
- `visual_acceptance_result`：

## 导出与持久化

- 是否持久：
- current / snapshot：
- canonical 文件：
- registry：
- PDF 导出：
- PNG 预览：
- 导出缓存目录：
- 同源一致性：
- final reply preview：

## 回写守卫

- owner 页面：
- 需要分流的 issue / risk / decision / report / memory / trace：
- lens 不能替代：
- 不可上推范围：

## 未覆盖边界

- 未读来源：
- 待人工确认：
- 不适用场景：
- 下次刷新触发：
