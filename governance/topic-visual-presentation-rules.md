---
type: governance
id: GOV-TOPIC-VISUAL-PRESENTATION-001
status: active
source_of_truth: true
updated: 2026-07-31
---

# Topic Visual Presentation Rules

```yaml
topic_presentation_profile:
  repository: wiki
  need: required
  existing_skill: skills/topic-visual-presentation/SKILL.md
  local_owner_roots: [skills/, concepts/, templates/, governance/, views/, scripts/]
  renderer: Google Chrome headless with same-source PDF/PNG readback
  design_system: semantic-static HTML, accessibility-first hierarchy, single visual purpose
  evidence_layers: [contract-schema, semantic-content, visual-quality, delivery-findability, reader-utility]
  views_layer: views/current/, views/snapshots/, views/lens-registry.md
  publication: skills/public-html-publish/SKILL.md and views/publication.md
  local_deltas: canonical-only cutover, all-runtime residual scan, mutation fixtures
  compatibility: v1 writer frozen; grandfather legacy local HTML/lens_id via baseline manifest
  sample_set: real single-page owner plus real four-owner page tree
  validation: portable-structure without exports, runtime artifact readback, negative suite, v1 zero-write, public live/deny, check_all, git diff --check
```

[[skills/topic-visual-presentation/SKILL]] 是唯一运行入口。先做 presentation eligibility，再冻结 subject_package、source_pack、reader contract 和三轴；`admit` 默认 HTML，inline/ephemeral/current/snapshot 默认同源 PDF/PNG 到临时或 ignored exports。

主题、项目 owner 和独立知识不可混同：`projects/` 维护项目事实，`articles/` / `concepts/` 维护独立知识；视图和导出不成为 truth source。problem-focus 仅是 content_scope。

五门 evaluator（contract-schema、semantic-content、visual-quality、delivery-findability、reader-utility）独立且不得上推。semantic-content 必须同时有确定性 sensor、builder-independent model judge 与版本化 rubric/calibration/trace；无真实 reader oracle 则 reader-utility=unproven。没有通用人工 veto。

`views/` 仅承接 canonical current/snapshot；registry 记录 source、refresh 和五门边界。旧 artifact 仅按 legacy baseline grandfather；同路径刷新须 pre/post hash、reason 和 compatibility readback。公开发布遵守 [[governance/public-html-publish-rules]]；本仓当前没有已发布页面，其他工程的发布读回不能作为本仓证据。

## page-bundle v2 活动口径

- `governance/topic-presentation-active-profile.v2.json` 是本仓活动 consumer pointer；当前 `active_consumer_pointer=v2`，v1 writer 禁止写入，也禁止 v1/v2 dual-write。
- `single-page | page-tree` 由内聚性、独立模块边界、拆分收益与导航成本裁决。页面树只保留一份 canonical edges；所有 parent、children 和 breadcrumb 派生生成。
- 每页只链接当前页 Markdown owner，并以 `unit_id + claim_id + source_fragment_id + rendered_section_id` 做细粒度 binding。
- 每页本地下载包含 PDF、桌面 PNG、移动 PNG；生成时间必须带时区且精确到分钟。public surface 没有受控 endpoint 时保持 blocked。
- `portable-structure` 不依赖 `views/.exports/`；`runtime-artifact-readback` 才显式生成 ignored immutable bundle 并校验。
- v1 grandfather 只读合同由 baseline manifest 校验；显式 v1 compatibility 必须零写入。
