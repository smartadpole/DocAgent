---
type: registry
id: VIEWS-LENS-REGISTRY-001
scope: shared
status: active
source_of_truth: true
updated: 2026-06-12
tags: [views, lens, registry]
---

# Lens Registry

本页登记 `views/` 下的持久 lens。

每条记录至少写清：`lens_id`、`path`、`lens_type`、`focus_object`、`judgement_purpose`、`source_pages`、`generated_at`、`source_revision`、`evidence_boundary`、`output_mode`、`visual_structure`、`export_profile`、`print_profile`、`equivalence_profile`、`default_auto_exports`、`conversation_png_preview`、`canonical_policy`、`snapshot_policy`、`staleness_policy` 和 `refresh_trigger`。

每条记录还要能回到 source pack，并用中文写清证据边界、未读来源和不能上推范围。PDF / PNG / SVG 导出缓存必须进入 gitignore 忽略目录，不作为 registry 的事实源。

## Current

当前暂无登记。

## Snapshots

当前暂无登记。

## 维护规则

- current lens 更新时，登记项应指向最新 canonical HTML / source / manifest。
- snapshot lens 不覆盖旧记录；按时间新增登记。
- PDF / PNG / SVG 导出缓存不在本页作为事实源登记，只记录导出状态和可再生成方式。
