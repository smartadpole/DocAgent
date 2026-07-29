---
template_type: topic-presentation-contract
contract_revision: topic-presentation-contract.v1
---

# Topic Presentation Contract

```yaml
presentation_eligibility: admit | reject | clarify | abstain
intent_routing_contract:
  speech_acts: []
  reader_tasks: []
  content_scope: topic | problem-focus | not-applicable
  materialization_need: inline | ephemeral | canonical-current | snapshot | not-applicable
  confidence: {value: , calibration_revision: }
  ambiguity: {type: none | multi-intent | missing-context | conflict | out-of-scope, unresolved_axes: []}
  decision: route | clarify | abstain
  reason_codes: []
subject_package: {subject_id: , user_goal: , subject_boundary: , known_facts: [], unknowns: [], owner_refs: []}
source_pack: {sources: [], source_revision: , freshness: , contradictions: [], evidence_bindings: []}
information_graph: {units: [], typed_relations: []}
organization_plan: {plan_revision: , reader_task: , topic_shape: , selected_units: [], omitted_units: [], section_graph: [], primary_visual: {paradigm: , encoded_relations: []}, alternatives: [], decision_rationale: , uncertainty: [], provenance_refs: []}
reader_adaptation_profile: {reader_task: , prior_knowledge: unknown | novice | working | expert, time_budget: , device: , accessibility_needs: [], interaction_need: , density_preference: , language_complexity: , evidence_depth: , explicit_preferences: [], preference_provenance: [], confidence: , expires_at: }
runtime_axes: {task_state: understand | compare | decide | act | verify | review, content_scope: topic | problem-focus, materialization: inline | ephemeral | current | snapshot}
representation: {primary_format: html, html_profile: semantic-static | interactive, same_source_exports: [pdf, png], export_policy: required-by-default, export_workspace_kind: runtime-temporary | gitignored-exports, export_readback: {html: , pdf: , png: }, fallback_reason: }
evaluation:
  contract-schema: {deterministic_sensor: }
  semantic-content: {deterministic_sensor: , independent_model_judge: , rubric_revision: , calibration_revision: , trace_ref: }
  visual-quality: {independent_reviewer: , review_artifact: }
  delivery-findability: {canonical_ref: , export_refs: [], findability_readback: }
  reader-utility: {task_oracle: , result_ref: }
artifact_compatibility: {legacy_artifact_baseline_manifest: , legacy_policy: grandfather-unmodified, refresh_policy: same-path-upgrade, public_html_publish: independent}
```

结构、fixture 与 canonical check key 通过的上限是 `structure-ready`；没有真实 artifact/readback、独立 judge trace 或 reader oracle 不能上推。
