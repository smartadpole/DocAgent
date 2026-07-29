---
type: governance
id: GOV-TOPIC-VISUAL-PRESENTATION-001
status: active
source_of_truth: true
updated: 2026-07-29
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
  compatibility: grandfather legacy HTML/lens_id/public URL via baseline manifest
  sample_set: topic current sample plus canonical problem-focus fixture
  validation: check_topic_visual_presentation, runtime export readback, public live/deny, check_all, git diff --check
```

[[skills/topic-visual-presentation/SKILL]] 是唯一运行入口。先做 presentation eligibility，再冻结 subject_package、source_pack、reader contract 和三轴；`admit` 默认 HTML，inline/ephemeral/current/snapshot 默认同源 PDF/PNG 到临时或 ignored exports。

主题、项目 owner 和独立知识不可混同：`projects/` 维护项目事实，`articles/` / `concepts/` 维护独立知识；视图和导出不成为 truth source。problem-focus 仅是 content_scope。

五门 evaluator（contract-schema、semantic-content、visual-quality、delivery-findability、reader-utility）独立且不得上推。semantic-content 必须同时有确定性 sensor、builder-independent model judge 与版本化 rubric/calibration/trace；无真实 reader oracle 则 reader-utility=unproven。没有通用人工 veto。

`views/` 仅承接 canonical current/snapshot；registry 记录 source、refresh 和五门边界。旧 artifact 仅按 legacy baseline grandfather；同路径刷新须 pre/post hash、reason 和 compatibility readback。公开发布遵守 [[governance/public-html-publish-rules]]，独立进行 new/legacy/deny live readback。
