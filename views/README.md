---
type: entry
id: VIEWS-README-001
scope: shared
status: active
source_of_truth: true
updated: 2026-06-25
tags: [views, lens, presentation]
---

# 图文呈现层

`views/` 承接问题聚焦式图文 lens 的持久呈现入口。

它不是事实源，也不是第二份项目状态。事实仍然回到 `projects/`、`articles/`、`concepts/`、`skills/`、`templates/`、`log.md` 或原始来源；`views/` 只负责把已经读取的来源按当前问题重组为可读、可追溯、可打印或可导出的视图。

## 职责

- `views/current/`：当前有效的 canonical lens。
- `views/snapshots/`：阶段、会议、验收、复盘或外部分发节点的 snapshot lens。
- [[views/lens-registry]]：登记持久 lens 的来源、类型、证据边界、视觉策略、导出状态和刷新条件。
- [[views/publication]]：登记 public-html-publish 发布 profile、public_url 公式、HTML-only 边界、host / prefix 分离和 blocked / live readback 状态。
- `views/.exports/`、`views/exports/`、`views/**/.exports/`：PDF / PNG / SVG 等可再生成导出缓存，必须被 `.gitignore` 忽略。

## 写入规则

- 只有用户要求 HTML / 图文文件 / 打印 / PDF / PNG / 持久页面，或本轮明确需要 current / snapshot lens 时，才写入 `views/`。
- 每个持久 lens 必须能回到 source pack、证据边界和原始入口。
- 每个新复杂或持久呈现必须声明 eligibility、subject/source、关系图、三轴、五门 evaluator 与 versioned trace；旧 grandfather artifact 不追补新 schema。
- current lens 不记录历史快照结论；snapshot lens 不冒充当前事实。
- PDF / PNG / SVG 只作为导出、打印、预览或分发产物，不作为事实源提交。
- 生成或刷新持久 HTML / print view 时，必须说明是否已生成同源 PDF / PNG；如果没有实际导出，只能写“具备导出配置”或“待导出”。
- 生成或刷新持久 HTML / print view 时，必须从同一 HTML / source manifest 生成 PDF 和至少一张 PNG 到忽略目录，并在最终回复展示 PNG 预览；导出失败时只能写失败原因。
- 复杂或持久 lens 必须在 HTML meta、JSON script 或等价机器可读块中保留 `static_visual_qa`，字段覆盖 layout、type、spacing、palette、component roles、accessibility、export render、finish grade、视觉强度、层级幅度、组件多样性、颜色预算、调整循环、渲染审阅、review artifact 和视觉验收结果。
- 生成或刷新 canonical HTML 后，还必须按 [[skills/public-html-publish/SKILL]] 和 [[views/publication]] 给出 public_url；没有真实 host / live readback 时写明 blocked 原因，不能声称公网完成。

## Lens 完成合同

持久 HTML lens 至少包含：

- `focus_object`、`lens_type`、`judgement_purpose`、`source_pack`、`evidence_boundary`、`output_mode`、`persistent_or_temporary`、`export_required`。
- `art_direction_brief`、`information_topology`、`layout_morphology_plan`、`topic_visual_language`、`primary_visual_metaphor`、`theme_specific_elements`、`anti_information_listing_strategy`、`page_paradigm`、`component_semantic_manifest`、`human_rubric`、`result_cluster_diagnosis`。
- `static_visual_qa`，覆盖 layout、type、spacing、palette、component、accessibility、export、finish grade、视觉强度、层级幅度、组件变化、色彩预算、调整循环、渲染审阅、review artifact 和视觉验收结果。
- source pack、未读但相关来源、不可上推范围和 owner 页面回写守卫。

## 相关入口

- [[skills/topic-visual-presentation/SKILL]]
- [[skills/public-html-publish/SKILL]]
- [[templates/topic-presentation-template]]
- [[views/lens-registry]]
- [[views/publication]]
- `views/publication.md`: public-html-publish profile and public_url contract.
- `current/public-html-publish-status.html`: stable public-html-publish live readback sample.
- `current/markdown-owner-viewer.html`: shared current HTML owner-page viewer; current lens links to repository Markdown owners must go through this rendered viewer instead of raw `.md` files.
- `current/topic-visual-presentation-system.html`: canonical topic presentation representative sample; older problem-focused sample is grandfathered legacy only.
- HTML-only public sharing excludes `.exports`, Markdown, PDF / PNG / SVG, logs, raw assets, and local secrets.
