---
name: topic-visual-presentation
description: 主题级图文呈现的唯一运行入口；把即时 subject_package 与 source_pack 组织为默认 HTML，并生成同源 PDF/PNG。
maturity: adopted
evidence_signals: [skill, concept, template, governance, sensor, fixtures, legacy-baseline, current-sample]
transfer_ready: true
sensor: python3 scripts/check_all.py --only topic-visual-presentation
---

# Topic Visual Presentation

## 定位

这是本仓主题信息呈现的唯一活动入口。调用不要求已有 Topic 文档：对话、文件、页面和临时材料可即时规范化为 `subject_package` 与 `source_pack`。项目事实仍由 `projects/` owner 保存，独立知识仍由 `articles/`、`concepts/` 保存；本技能只生成派生呈现。

## 成熟度与证据信号

`evidence_signals` 覆盖 skill、concept、template、governance、sensor、fixtures、legacy baseline 和 current sample；`evidence boundary` 是 structure/readback 不能上推为独立语义、视觉或 reader-utility 通过。

## 准入与输入

先裁决 `presentation_eligibility: admit | reject | clarify | abstain`。普通短答、显式 text-only 或信息不足以改变结构时不强制呈现；`admit` 后 `primary_format=html`，非 HTML 或缺少 PDF/PNG 必须记录 fallback reason。

```yaml
subject_package: {subject_id: , user_goal: , subject_boundary: , known_facts: [], unknowns: [], owner_refs: []}
source_pack: {sources: [], source_revision: , freshness: , contradictions: [], evidence_bindings: []}
intent_routing_contract:
  content_scope: topic | problem-focus | not-applicable
  materialization_need: inline | ephemeral | canonical-current | snapshot | not-applicable
  confidence: {value: , calibration_revision: }
  decision: route | clarify | abstain
```

`content_scope=topic` 是默认；`content_scope=problem-focus` 只是内容子范围。`canonical-current` 进入运行时唯一规范化为 `current`。confidence 必须来自版本化 calibration，而不是模型自报。

## 运行合同

`information_graph` 保留带来源和生命周期的 units 与 typed_relations；`organization_plan` 记录选取、遗漏、主视觉和理由；`reader_adaptation_profile` 只使用显式任务与偏好证据。

```yaml
runtime_axes: {task_state: understand|compare|decide|act|verify|review, content_scope: topic|problem-focus, materialization: inline|ephemeral|current|snapshot}
representation:
  primary_format: html
  html_profile: semantic-static | interactive
  same_source_exports: [pdf, png]
  export_policy: required-by-default
  export_workspace_kind: runtime-temporary | gitignored-exports
```

inline、ephemeral、current、snapshot 都默认生成并读回同源 PDF/PNG。仓内导出进入 Git-ignored `views/.exports/`；不提交为第二事实源。

## 五门 evaluator

| 门 | 证明 | 不能上推 |
| --- | --- | --- |
| contract-schema | package、枚举、revision、representation | 内容正确 |
| semantic-content | 来源绑定、未知项、独立模型 judge、版本化 rubric/trace | 视觉、发布或效用 |
| visual-quality | 独立 reviewer、可访问性、PDF/PNG readback | 语义正确 |
| delivery-findability | canonical、registry、exports、public live/deny | 读者任务成功 |
| reader-utility | 真实读者任务 oracle | 业务状态关闭 |

五门独立，任一 pass 都不能提升其他门。没有 builder-independent judge 或真实 reader task 时分别保持 `unproven`；不存在通用人工 veto。业务授权和验收仍回到 owner。

## 兼容与边界

旧 HTML、current、snapshot、lens_id 与 registry entry 由 `scripts/fixtures/topic-visual-presentation/legacy_artifact_baseline_manifest.v1.json` grandfather。未修改旧 artifact 不追补新 schema；同路径刷新必须记录 pre/post hash、reason 和 compatibility readback。`public-html-publish` 是独立能力，本仓当前没有已发布页面。

相关入口：[[concepts/topic-information-presentation]]、[[templates/topic-presentation-template]]、[[governance/topic-visual-presentation-rules]]、[[skills/public-html-publish/SKILL]]。

## 工作流

按 eligibility → packages → information graph → organization/adaptation → HTML → same-source exports → five gates 执行；拒绝、澄清和 abstain 不 materialize artifact。

## 输出格式

输出 eligibility、subject/source、三轴、canonical/export refs、五门状态、cannot-promote 与 persistence decision。

## 禁止项

不把 builder 自评当 independent judge；不以导出件替代 truth；不把历史 legacy artifact 变成 alias 或重写其文本；不以任一 gate 通过关闭业务 owner。
