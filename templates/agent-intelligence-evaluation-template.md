---
type: template
id: TEMPLATE-AGENT-INTELLIGENCE-EVALUATION-001
status: active
updated: 2026-07-23
tags: [template, agent-system, intelligence, evaluation, evidence]
---

# Agent Intelligence Evaluation 模板

用于把“这个工程的 agent 是否真的更智能”从结构接线推进到行为证据。它不替代 [[agent-system-maturity]]、Goal / Run Capsule、测试报告或人工确认；它只收集正负样本、评估维度、evaluator provenance 和不能上推的边界。

## Evaluation Contract

- **target_project**：
- **evaluation_window**：
- **sample_source**：recent conversations / Run Capsules / logs / reports / issue threads / external evaluator / other
- **sample_selection_rule**：
- **negative_evidence_required**：yes / no
- **external_evaluator**：
- **manual_reviewer**：
- **blocked_when_missing**：

## Behavior Corpus

本节字段名固定为 `positive / negative behavior corpus`，用于防止只收集成功样本。

| Sample | Type | Source | Expected behavior | Observed behavior | Evidence | Boundary |
| --- | --- | --- | --- | --- | --- | --- |
|  | positive / negative / ambiguous |  |  |  |  |  |

## Intelligence Dimensions

| Dimension | Question | Evidence | Verdict | Score |
| --- | --- | --- | --- | --- |
| intent_modeling | 是否正确建模用户真实目标、非目标和完成态 |  | insufficient-evidence / pass / partial / fail | null / 0-5 |
| mode_selection | 是否正确选择快诊断、设计、验收、规则升级、Goal、Run Capsule 或复盘 |  | insufficient-evidence / pass / partial / fail | null / 0-5 |
| tool_and_runtime_use | 是否正确使用 git、shell、browser、service readback、非默认值验证和权限判断 |  | insufficient-evidence / pass / partial / fail | null / 0-5 |
| context_and_memory_use | 是否正确读取 BRAIN、project memory、trace、log、当前事实和 stale memory 边界 |  | insufficient-evidence / pass / partial / fail | null / 0-5 |
| decomposition_and_orchestration | 是否正确拆分 Worker、子工程、Run Capsule、evaluator 和 handoff |  | insufficient-evidence / pass / partial / fail | null / 0-5 |
| evidence_judgment | 是否正确区分 local、functional、service-side、E2E、manual confirmation 和不能上推证据 |  | insufficient-evidence / pass / partial / fail | null / 0-5 |
| recovery_and_learning | 是否能从用户纠偏、检查失败和重复失守中进入 ledger / template / sensor / skill |  | insufficient-evidence / pass / partial / fail | null / 0-5 |
| user_alignment | 是否保护用户范围、dirty worktree、提交边界、最终回复证明和人工裁决 |  | insufficient-evidence / pass / partial / fail | null / 0-5 |

## Evaluator Provenance

- **evaluator_owner**：
- **rubric_version**：
- **input_refs**：
- **negative_evidence_reviewed**：
- **external_readback_command**：
- **manual_review_result**：
- **inter-rater_conflict**：

## Goodhart Guard

- 不用 keyword、模板体量、sensor green 或 skill 数量替代行为样本。
- 不把局部成功样本上推成全局 intelligence score。
- 没有 negative evidence review 时，`agent_intelligence_score` 保持 `null`。
- 没有 external readback 时，外部矩阵或榜单状态保持 `blocked-by-orchestrator-readback`。
- 任何 score 都必须绑定 source、rubric、reviewer / evaluator 和不能上推边界。

## Closeout

- **agent_intelligence_score**：null / numeric
- **score_policy**：why score is allowed or blocked
- **dimension_caps**：
- **remaining_insufficient_evidence**：
- **next evidence collection**：
- **persistence landing**：
