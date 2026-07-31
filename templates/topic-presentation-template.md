---
template_type: topic-presentation-contract
contract_revision: topic-presentation-contract.v2
---

# Topic Presentation Contract v2

```yaml
contract_revision: topic-presentation-contract.v2
presentation_bundle_decision:
  bundle_shape: single-page | page-tree
  materialization: inline | ephemeral | current | snapshot
  cohesion: low | medium | high
  independent_module_boundaries: []
  split_benefit: low | medium | high
  navigation_cost: low | medium | high
  split_guard: pass | fail
  root_responsibility:
  navigation_depth_budget: 1
  page_count_budget: 1
  decision_rationale:
presentation_bundle:
  bundle_id:
  bundle_revision:
  source_snapshot_id:
  build_id:
  root_page_id:
  page_catalog:
    - page_id:
      responsibility:
      canonical_path:
      lifecycle_status: active | redirected | merged | retired
      includes: []
      excludes: []
      local_section_graph: []
  canonical_tree:
    edge_source: edges
    edges: []
  discovery_paths: []
coverage_manifest:
  information_units: []
  claims: []
  source_fragments:
    - source_fragment_id:
      owner_ref:
      selector:
      rendered_text:
  rendered_sections: []
  page_bindings:
    - page_id:
      unit_id:
      claim_id:
      source_fragment_id:
      rendered_section_id:
  structural_coverage: {expected_unit_ids: [], bound_unit_ids: [], uncovered_unit_ids: [], invalid_bindings: [], acceptance: }
  semantic_coverage: {oracle_revision: , reviewer: , unsupported_claim_ids: [], contradicted_claim_ids: [], acceptance: not-evaluated}
page_download_contracts:
  - page_id:
    artifacts:
      - {format: pdf, artifact_id: }
      - {format: png-desktop, artifact_id: }
      - {format: png-mobile, artifact_id: }
    surfaces:
      local: {delivery_adapter: local-export-resolver, availability: blocked, target_readback: not-evaluated}
      public: {delivery_adapter: none, availability: blocked, target_readback: not-evaluated}
    controls: {placement: shared-footer, labels: [下载 PDF, 下载桌面 PNG, 下载移动 PNG]}
generation_metadata:
  - page_id:
    generated_at:
    display_text:
    precision: minute
    source_revision:
    bundle_revision:
    build_id:
evaluation:
  contract-schema: {status: }
  semantic-content: {status: not-evaluated, independent_evaluator: }
  visual-quality: {status: not-evaluated, independent_evaluator: }
  delivery-findability: {status: not-evaluated}
  reader-utility: {status: unproven, task_oracle: }
```

## 使用边界

- 单页适合一个稳定信息边界；页面树必须由独立模块边界与净拆分收益证明，复杂度本身不构成拆页理由。
- 每页只提供当前页 owner 的信息源链接；逐 claim binding 保留完整证据关系，不把多个 Markdown 文件堆成链接列表。
- HTML、PDF、桌面 PNG 与移动 PNG 来自同一 `source_snapshot_id + bundle_revision + build_id`。
- portable 检查不读取 `.exports`；runtime gate 才生成和校验本地下载件。
- local 与 public surface 独立；没有受控 published endpoint 时 public 必须 blocked。
- 任何本地 gate 通过都不能上推独立语义、视觉、公开交付或 reader utility 已通过。
