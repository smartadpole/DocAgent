---
type: skill-maturity-diagnostics
lens_id: lens-skill-maturity-diagnostics-current
focus_object: per-project action diagnostics for cross-project skill maturity gaps
lens_type: knowledge
source_pages: skills/README.md; projects/governance/registry.md; scripts/update_skill_maturity_matrix.py
source_scope: same scan context as skill-maturity-matrix.html and skill-maturity-matrix.data.json
source_of_truth: false
generated_at: 2026-06-12 16:24
source_revision: aa12a0d
evidence_boundary: local skill/governance/sensor/view/template discovery and content-volume signals only; no runtime validation
context_frame: action-oriented companion to the HTML matrix; groups diagnostics by project so each project can see missing signals and recommended modification directions
output_mode: generated_markdown_diagnostics
export_profile: none; HTML matrix owns PDF/PNG exports
print_profile: not optimized for print; use HTML matrix for print-oriented output
equivalence_profile: generated from the same build_context as HTML and JSON outputs
canonical_policy: overwritten by scripts/update_skill_maturity_matrix.py on every matrix refresh
snapshot_policy: freeze separately only when a dated audit snapshot is needed
staleness_policy: stale when any scanned skill/governance/sensor/view/template path, ranking rule, action diagnostic rule, project registry, or data schema changes
refresh_trigger: rerun scripts/update_skill_maturity_matrix.py
tags: [views, governance, skill-maturity, diagnostics]
---

# 跨工程技能成熟度行动诊断

本页由 `scripts/update_skill_maturity_matrix.py` 生成，和 [[views/current/governance/skill-maturity-matrix.html]]、`views/current/governance/skill-maturity-matrix.data.json` 使用同一轮扫描上下文。它不是手写真相源；每次刷新矩阵时应同步重写。

## 使用边界

- `领先 / 成熟 / 接入 / 局部 / 未见` 只表示本地文件证据信号强弱，不代表运行时验收。
- `领先` 要求该工程覆盖同一技能下全体工程已经出现的独特证据信号；如果多个工程各有特色但没有任何一个覆盖并集，只能标为成熟或接入，并在诊断里提示互补对齐方向。
- `建议修改方向` 只指出下一步补证据或补能力的方向；项目 / 领域绑定技能只能抽象方法，不复制业务表、路径、运行 ID、状态或一次性 handoff。
- HTML 负责鸟瞰，JSON 负责结构化数据，本页负责每个工程可读的行动诊断。

## 输出互链

- HTML 总览：[[views/current/governance/skill-maturity-matrix.html]]
- HTML 详情：[[views/current/governance/skill-maturity-diagnostics.html]]
- JSON 数据：`views/current/governance/skill-maturity-matrix.data.json`

## AcknowledgeBase

- **工程路径**：`/Users/hai/Documents/Docs/AcknowledgeBase`
- **成熟概览**：领先 1；成熟 7；接入 0；局部 2；未见 4；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 4/16 | 12 | DocCustomeranalysis | body、governance | large-body、sensor、skill | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 局部 5/16 | 11 | fetch-adapter | governance、large-body | TRANSFER、sensor、skill | 追齐领先信号：优先补 TRANSFER, sensor, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 成熟 12/16 | 4 | Software/wiki | TRANSFER、skill、small-body | body、sensor | 追齐领先信号：优先补 body, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 成熟 10/13 | 3 | Software/wiki | skill、small-body、template | TRANSFER、body、governance | 追齐领先信号：优先补 TRANSFER, body, governance；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 成熟 17/20 | 3 | Software/wiki | governance、large-body、sensor、skill、template | TRANSFER | 追齐领先信号：优先补 TRANSFER；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 成熟 14/15 | 1 | Software/wiki | governance、sensor、skill、small-body | TRANSFER | 追齐领先信号：优先补 TRANSFER；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 成熟 10/11 | 1 | Software/wiki | body、skill | TRANSFER | 追齐领先信号：优先补 TRANSFER；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 成熟 20/21 | 1 | DocCustomeranalysis | TRANSFER、body、sensor、skill、template、views | governance、large-body | 追齐领先信号：优先补 governance, large-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 成熟 14/14 | 0 | AcknowledgeBase、Software/wiki | governance、large-body、skill、template | TRANSFER | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 TRANSFER；覆盖证据信号并集后，才可重新评为领先。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 领先 10/10 | 0 | AcknowledgeBase、Software/wiki、DocCustomeranalysis、DocFilmCommunity、LifeOS | goal-contract、governance、large-body、template | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **客群 DB 读回**：`AcknowledgeBase:governance/harness-feedback-ledger.md`、`AcknowledgeBase:governance/template-feedback-rules.md`、`AcknowledgeBase:projects/development/execution/engineering-feedback-loop.md`
- **文档与 Agent 规则维护**：`AcknowledgeBase:AGENTS.md`、`AcknowledgeBase:governance/agent-governance-strategy.md`
- **复盘 / 回顾改进**：`AcknowledgeBase:skills/historical-dialogue-retrospective/SKILL.md`
- **Issue / 事故分析**：`AcknowledgeBase:skills/issue-analysis/SKILL.md`、`AcknowledgeBase:templates/development-issue-template.md`
- **跨工程治理审计**：`AcknowledgeBase:governance/BRAIN.md`、`AcknowledgeBase:governance/POLICY.md`、`AcknowledgeBase:governance/README.md`、`AcknowledgeBase:governance/WORKFLOW.md`、`AcknowledgeBase:governance/agent-governance-strategy.md`
- **知识关联**：`AcknowledgeBase:governance/knowledge-linking-rules.md`、`AcknowledgeBase:scripts/check_knowledge_linking.py`、`AcknowledgeBase:skills/knowledge-linking/SKILL.md`
- **跨工程技能迁移提示词**：`AcknowledgeBase:skills/cross-project-skill-adoption-prompt/SKILL.md`
- **问题聚焦式图文呈现**：`AcknowledgeBase:scripts/check_problem_focused_visual_presentation.py`、`AcknowledgeBase:skills/problem-focused-visual-presentation/SKILL.md`、`AcknowledgeBase:templates/problem-focused-lens-template.md`、`AcknowledgeBase:views/lens-registry.md`
- **调研 / 研究能力**：`AcknowledgeBase:governance/BRAIN.md`、`AcknowledgeBase:governance/state-constraint-reasoning.md`、`AcknowledgeBase:skills/industry-ai-research/SKILL.md`、`AcknowledgeBase:skills/open-source-project-research/SKILL.md`、`AcknowledgeBase:skills/technical-topic-research/SKILL.md`
- **Goal Contract / 长时任务完成契约**：`AcknowledgeBase:AGENTS.md`、`AcknowledgeBase:INDEX.md`、`AcknowledgeBase:README.md`、`AcknowledgeBase:articles/2026-05-25-codex-goals-research.md`、`AcknowledgeBase:articles/2026-06-12-codex-goal-mode-public-guide.md`

## Software/wiki

- **工程路径**：`/Users/hai/Documents/Software/wiki`
- **成熟概览**：领先 3；成熟 6；接入 0；局部 1；未见 4；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 7/16 | 9 | DocCustomeranalysis | body、governance、sensor | large-body、skill | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 成熟 14/16 | 2 | fetch-adapter | TRANSFER、large-body、skill | governance、sensor | 追齐领先信号：优先补 governance, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 成熟 19/21 | 2 | DocCustomeranalysis | TRANSFER、sensor、skill、small-body、template、views | body、governance、large-body | 追齐领先信号：优先补 body, governance, large-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 成熟 13/13 | 0 | Software/wiki | TRANSFER、skill、small-body、template | body、governance | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 body, governance；覆盖证据信号并集后，才可重新评为领先。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 成熟 15/15 | 0 | Software/wiki | TRANSFER、sensor、skill、small-body | governance | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 governance；覆盖证据信号并集后，才可重新评为领先。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 成熟 14/14 | 0 | AcknowledgeBase、Software/wiki | TRANSFER、governance、skill、small-body | body、large-body、template | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 body, large-body, template；覆盖证据信号并集后，才可重新评为领先。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 成熟 11/11 | 0 | Software/wiki | TRANSFER、skill | body | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 body；覆盖证据信号并集后，才可重新评为领先。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 领先 10/10 | 0 | AcknowledgeBase、Software/wiki、DocCustomeranalysis、DocFilmCommunity、LifeOS | goal-contract、governance、large-body、template | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 领先 16/16 | 0 | Software/wiki | TRANSFER、body、sensor、skill | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 领先 20/20 | 0 | Software/wiki | TRANSFER、governance、large-body、sensor、skill、template | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **客群 DB 读回**：`Software/wiki:governance/harness-feedback-ledger.md`、`Software/wiki:governance/template-feedback-rules.md`、`Software/wiki:projects/development/execution/engineering-feedback-loop.md`、`Software/wiki:scripts/check_harness_feedback_ledger.py`
- **文档与 Agent 规则维护**：`Software/wiki:AGENTS.md`、`Software/wiki:skills/documentation-maintenance/SKILL.md`
- **问题聚焦式图文呈现**：`Software/wiki:scripts/check_problem_focused_visual_presentation.py`、`Software/wiki:skills/problem-focused-visual-presentation/SKILL.md`、`Software/wiki:templates/problem-focused-lens-template.md`、`Software/wiki:views/lens-registry.md`
- **Issue / 事故分析**：`Software/wiki:skills/issue-analysis/SKILL.md`、`Software/wiki:templates/development-issue-template.md`
- **知识关联**：`Software/wiki:scripts/check_knowledge_linking.py`、`Software/wiki:skills/knowledge-linking/SKILL.md`
- **调研 / 研究能力**：`Software/wiki:governance/BRAIN.md`、`Software/wiki:skills/documentation-maintenance/SKILL.md`、`Software/wiki:skills/technology-research/SKILL.md`
- **跨工程技能迁移提示词**：`Software/wiki:skills/cross-project-skill-adoption-prompt/SKILL.md`
- **Goal Contract / 长时任务完成契约**：`Software/wiki:AGENTS.md`、`Software/wiki:INDEX.md`、`Software/wiki:README.md`、`Software/wiki:articles/2026-05-25-codex-goals-research.md`、`Software/wiki:concepts/codex-goals.md`
- **复盘 / 回顾改进**：`Software/wiki:scripts/check_retrospective_system.py`、`Software/wiki:skills/historical-dialogue-retrospective/SKILL.md`
- **跨工程治理审计**：`Software/wiki:governance/BRAIN.md`、`Software/wiki:governance/POLICY.md`、`Software/wiki:governance/README.md`、`Software/wiki:governance/WORKFLOW.md`、`Software/wiki:governance/execution-contract-semantics.md`

## DocCustomeranalysis

- **工程路径**：`/Users/hai/Documents/Code/DocCustomeranalysis`
- **成熟概览**：领先 3；成熟 2；接入 2；局部 2；未见 5；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 未见 0/15 | 15 | Software/wiki | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 未见 0/11 | 11 | Software/wiki | 无 | TRANSFER、body、skill | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 局部 3/16 | 13 | fetch-adapter | large-body | TRANSFER、governance、sensor、skill | 追齐领先信号：优先补 TRANSFER, governance, sensor, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 局部 2/14 | 12 | AcknowledgeBase、Software/wiki | governance | TRANSFER、body、large-body、skill、small-body、template | 追齐领先信号：优先补 TRANSFER, body, large-body, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 接入 9/20 | 11 | Software/wiki | governance、large-body、sensor、template | TRANSFER、skill | 追齐领先信号：优先补 TRANSFER, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 接入 10/16 | 6 | Software/wiki | body、skill | TRANSFER、sensor | 追齐领先信号：优先补 TRANSFER, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 成熟 10/13 | 3 | Software/wiki | body、skill | TRANSFER、governance、template | 追齐领先信号：优先补 TRANSFER, governance, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 成熟 21/21 | 0 | DocCustomeranalysis | TRANSFER、large-body、sensor、skill、template、views | governance | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 governance；覆盖证据信号并集后，才可重新评为领先。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 领先 10/10 | 0 | AcknowledgeBase、Software/wiki、DocCustomeranalysis、DocFilmCommunity、LifeOS | goal-contract、governance、large-body、template | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 领先 9/9 | 0 | DocCustomeranalysis | skill、small-body | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 领先 16/16 | 0 | DocCustomeranalysis | governance、large-body、sensor、skill | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **文档与 Agent 规则维护**：`DocCustomeranalysis:AGENTS.md`
- **调研 / 研究能力**：`DocCustomeranalysis:governance/BRAIN.md`
- **跨工程治理审计**：`DocCustomeranalysis:governance/BRAIN.md`、`DocCustomeranalysis:governance/POLICY.md`、`DocCustomeranalysis:governance/README.md`、`DocCustomeranalysis:governance/WORKFLOW.md`、`DocCustomeranalysis:governance/execution-contract-semantics.md`
- **复盘 / 回顾改进**：`DocCustomeranalysis:skills/historical-dialogue-retrospective/SKILL.md`、`DocCustomeranalysis:skills/retrospective/SKILL.md`
- **Issue / 事故分析**：`DocCustomeranalysis:skills/issue-analysis/SKILL.md`
- **问题聚焦式图文呈现**：`DocCustomeranalysis:scripts/check_problem_focused_visual_presentation.py`、`DocCustomeranalysis:skills/problem-focused-visual-presentation/SKILL.md`、`DocCustomeranalysis:templates/problem-focused-lens-template.md`、`DocCustomeranalysis:views/current/task-080-status-acceptance-lens.html`、`DocCustomeranalysis:views/lens-registry.md`
- **Goal Contract / 长时任务完成契约**：`DocCustomeranalysis:AGENTS.md`、`DocCustomeranalysis:INDEX.md`、`DocCustomeranalysis:README.md`、`DocCustomeranalysis:articles/2026-06-12-codex-goal-mode-usage-review.md`、`DocCustomeranalysis:concepts/codex-goals.md`
- **事项自动拆解**：`DocCustomeranalysis:skills/work-item-auto-decomposition/SKILL.md`
- **客群 DB 读回**：`DocCustomeranalysis:governance/harness-feedback-ledger.md`、`DocCustomeranalysis:governance/template-feedback-rules.md`、`DocCustomeranalysis:projects/development/execution/engineering-feedback-loop.md`、`DocCustomeranalysis:scripts/check_harness_feedback_ledger.py`、`DocCustomeranalysis:skills/customer-group-db-readback/SKILL.md`

## DocFilmCommunity

- **工程路径**：`/Users/hai/Documents/Code/DocFilmCommunity`
- **成熟概览**：领先 1；成熟 2；接入 1；局部 3；未见 7；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 未见 0/16 | 16 | Software/wiki | 无 | TRANSFER、body、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 未见 0/15 | 15 | Software/wiki | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 未见 0/11 | 11 | Software/wiki | 无 | TRANSFER、body、skill | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 局部 2/16 | 14 | fetch-adapter | body | TRANSFER、governance、large-body、sensor、skill | 追齐领先信号：优先补 TRANSFER, governance, large-body, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 局部 3/14 | 11 | AcknowledgeBase、Software/wiki | governance、small-body | TRANSFER、body、large-body、skill、template | 追齐领先信号：优先补 TRANSFER, body, large-body, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 7/16 | 9 | DocCustomeranalysis | body、governance、sensor | large-body、skill | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 接入 9/20 | 11 | Software/wiki | governance、large-body、sensor、template | TRANSFER、skill | 追齐领先信号：优先补 TRANSFER, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 成熟 17/21 | 4 | DocCustomeranalysis | body、sensor、skill、template、views | TRANSFER、governance、large-body | 追齐领先信号：优先补 TRANSFER, governance, large-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 成熟 10/13 | 3 | Software/wiki | skill、small-body、template | TRANSFER、body、governance | 追齐领先信号：优先补 TRANSFER, body, governance；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 领先 10/10 | 0 | AcknowledgeBase、Software/wiki、DocCustomeranalysis、DocFilmCommunity、LifeOS | goal-contract、governance、large-body、template | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **文档与 Agent 规则维护**：`DocFilmCommunity:AGENTS.md`
- **调研 / 研究能力**：`DocFilmCommunity:governance/BRAIN.md`
- **客群 DB 读回**：`DocFilmCommunity:governance/harness-feedback-ledger.md`、`DocFilmCommunity:governance/template-feedback-rules.md`、`DocFilmCommunity:projects/development/execution/engineering-feedback-loop.md`、`DocFilmCommunity:scripts/check_harness_feedback_ledger.py`
- **跨工程治理审计**：`DocFilmCommunity:governance/BRAIN.md`、`DocFilmCommunity:governance/POLICY.md`、`DocFilmCommunity:governance/README.md`、`DocFilmCommunity:governance/WORKFLOW.md`、`DocFilmCommunity:governance/execution-contract-semantics.md`
- **问题聚焦式图文呈现**：`DocFilmCommunity:scripts/check_problem_focused_visual_presentation.py`、`DocFilmCommunity:skills/problem-focused-visual-presentation/SKILL.md`、`DocFilmCommunity:templates/problem-focused-lens-template.md`、`DocFilmCommunity:views/lens-registry.md`
- **Issue / 事故分析**：`DocFilmCommunity:skills/issue-analysis/SKILL.md`、`DocFilmCommunity:templates/development-issue-template.md`
- **Goal Contract / 长时任务完成契约**：`DocFilmCommunity:AGENTS.md`、`DocFilmCommunity:INDEX.md`、`DocFilmCommunity:README.md`、`DocFilmCommunity:concepts/codex-goals.md`、`DocFilmCommunity:governance/BRAIN.md`

## fetch-adapter

- **工程路径**：`/Users/hai/Documents/Code/Customer/fetch-adapter`
- **成熟概览**：领先 1；成熟 5；接入 0；局部 2；未见 6；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 未见 0/16 | 16 | Software/wiki | 无 | TRANSFER、body、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 未见 0/15 | 15 | Software/wiki | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 未见 0/14 | 14 | AcknowledgeBase、Software/wiki | 无 | TRANSFER、body、governance、large-body、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 未见 0/11 | 11 | Software/wiki | 无 | TRANSFER、body、skill | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 2/16 | 14 | DocCustomeranalysis | governance | body、large-body、sensor、skill、small-body | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 局部 7/20 | 13 | Software/wiki | body、governance、sensor | TRANSFER、large-body、skill、template | 追齐领先信号：优先补 TRANSFER, large-body, skill, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 成熟 16/21 | 5 | DocCustomeranalysis | body、sensor、skill、views | TRANSFER、governance、large-body、template | 追齐领先信号：优先补 TRANSFER, governance, large-body, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 成熟 10/13 | 3 | Software/wiki | body、skill | TRANSFER、governance、template | 追齐领先信号：优先补 TRANSFER, governance, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 成熟 9/12 | 3 | customeranalysis、17lang | skill、small-body | body、governance | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 成熟 9/10 | 1 | AcknowledgeBase、Software/wiki、DocCustomeranalysis、DocFilmCommunity、LifeOS | goal-contract、governance、large-body | template | 追齐领先信号：优先补 template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 成熟 16/16 | 0 | fetch-adapter | governance、large-body、sensor、skill | TRANSFER | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 TRANSFER；覆盖证据信号并集后，才可重新评为领先。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 领先 9/9 | 0 | fetch-adapter、prefect | skill、small-body | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **客群 DB 读回**：`fetch-adapter:.codex/context/harness-feedback-ledger.md`
- **跨工程治理审计**：`fetch-adapter:.codex/context/agent-harness-goal-governance.md`、`fetch-adapter:.codex/context/harness-feedback-ledger.md`、`fetch-adapter:tools/check_agent_harness.py`
- **问题聚焦式图文呈现**：`fetch-adapter:.codex/skills/problem-focused-visual-presentation/SKILL.md`、`fetch-adapter:tools/check_problem_focused_visual_presentation.py`、`fetch-adapter:views/lens-registry.md`
- **Issue / 事故分析**：`fetch-adapter:.agents/skills/issue-incident-analysis/SKILL.md`、`fetch-adapter:.claude/skills/issue-incident-analysis/SKILL.md`
- **项目上下文入口**：`fetch-adapter:.codex/skills/customer-pipeline-docs/SKILL.md`
- **Goal Contract / 长时任务完成契约**：`fetch-adapter:.codex/context/agent-harness-goal-governance.md`、`fetch-adapter:.codex/context/harness-feedback-ledger.md`、`fetch-adapter:.codex/skills/problem-focused-visual-presentation/SKILL.md`、`fetch-adapter:AGENTS.md`、`fetch-adapter:tools/check_agent_harness.py`
- **文档与 Agent 规则维护**：`fetch-adapter:.agents/skills/agents-md-sync/SKILL.md`、`fetch-adapter:.agents/skills/backlog-management/SKILL.md`、`fetch-adapter:.agents/skills/document-changes/SKILL.md`、`fetch-adapter:.agents/skills/issue-incident-analysis/SKILL.md`、`fetch-adapter:.agents/skills/write-docs/SKILL.md`
- **Backlog 批处理**：`fetch-adapter:.agents/skills/backlog-management/SKILL.md`、`fetch-adapter:.claude/skills/backlog-management/SKILL.md`

## train_platform

- **工程路径**：`/Users/hai/Documents/Code/train_platform`
- **成熟概览**：领先 0；成熟 0；接入 1；局部 4；未见 9；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 未见 0/16 | 16 | Software/wiki | 无 | TRANSFER、body、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 未见 0/15 | 15 | Software/wiki | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 未见 0/13 | 13 | Software/wiki | 无 | TRANSFER、body、governance、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 未见 0/11 | 11 | Software/wiki | 无 | TRANSFER、body、skill | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 未见 0/10 | 10 | AcknowledgeBase、Software/wiki、DocCustomeranalysis、DocFilmCommunity、LifeOS | 无 | body、goal-contract、governance、large-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 局部 1/16 | 15 | fetch-adapter | small-body | TRANSFER、body、governance、large-body、sensor、skill | 追齐领先信号：优先补 TRANSFER, body, governance, large-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 局部 6/20 | 14 | Software/wiki | governance、sensor、small-body | TRANSFER、body、large-body、skill、template | 追齐领先信号：优先补 TRANSFER, body, large-body, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 3/16 | 13 | DocCustomeranalysis | governance、small-body | body、large-body、sensor、skill | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 局部 2/14 | 12 | AcknowledgeBase、Software/wiki | governance | TRANSFER、body、large-body、skill、small-body、template | 追齐领先信号：优先补 TRANSFER, body, large-body, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 接入 13/21 | 8 | DocCustomeranalysis | body、sensor、skill | TRANSFER、governance、large-body、template、views | 追齐领先信号：优先补 TRANSFER, governance, large-body, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |

### 证据路径

- **文档与 Agent 规则维护**：`train_platform:AGENTS.md`
- **跨工程治理审计**：`train_platform:.codex/context/harness-evolution.md`、`train_platform:.codex/context/harness-feedback-ledger.md`、`train_platform:scripts/check_harness_governance.py`
- **客群 DB 读回**：`train_platform:.codex/context/harness-feedback-ledger.md`
- **调研 / 研究能力**：`train_platform:.codex/context/main-control-coordination.md`
- **问题聚焦式图文呈现**：`train_platform:.codex/skills/problem-focused-visual-presentation/SKILL.md`、`train_platform:scripts/check_problem_focused_visual_presentation.py`

## prefect

- **工程路径**：`/Users/hai/Documents/Code/prefect`
- **成熟概览**：领先 1；成熟 2；接入 3；局部 3；未见 5；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 未见 0/16 | 16 | Software/wiki | 无 | TRANSFER、body、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 未见 0/15 | 15 | Software/wiki | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 未见 0/11 | 11 | Software/wiki | 无 | TRANSFER、body、skill | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 局部 2/20 | 18 | Software/wiki | body | TRANSFER、governance、large-body、sensor、skill、template | 追齐领先信号：优先补 TRANSFER, governance, large-body, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 局部 2/14 | 12 | AcknowledgeBase、Software/wiki | body | TRANSFER、governance、large-body、skill、template | 追齐领先信号：优先补 TRANSFER, governance, large-body, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 局部 7/10 | 3 | AcknowledgeBase、Software/wiki、DocCustomeranalysis、DocFilmCommunity、LifeOS | goal-contract、large-body | governance、template | 追齐领先信号：优先补 governance, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 接入 8/16 | 8 | DocCustomeranalysis | skill | body、governance、large-body、sensor、small-body | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 接入 13/21 | 8 | DocCustomeranalysis | body、skill、views | TRANSFER、governance、large-body、sensor、template | 追齐领先信号：优先补 TRANSFER, governance, large-body, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 接入 11/16 | 5 | fetch-adapter | large-body、skill | TRANSFER、governance、sensor | 追齐领先信号：优先补 TRANSFER, governance, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 成熟 10/13 | 3 | Software/wiki | body、skill | TRANSFER、governance、template | 追齐领先信号：优先补 TRANSFER, governance, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 成熟 9/12 | 3 | customeranalysis、17lang | skill、small-body | body、governance | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 领先 9/9 | 0 | fetch-adapter、prefect | skill、small-body | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **跨工程治理审计**：`prefect:.agents/rules/harness-goal-governance.md`、`prefect:.codex/agents/records/harness-feedback-ledger/README.md`、`prefect:.codex/agents/records/harness-goal-governance/README.md`、`prefect:.codex/agents/rules/harness-goal-governance.md`、`prefect:.codex/agents/templates/harness-episode-package.md`
- **调研 / 研究能力**：`prefect:.agents/rules/main-control-coordination.md`、`prefect:.codex/agents/records/main-control-coordination/README.md`、`prefect:.codex/agents/rules/main-control-coordination.md`
- **Goal Contract / 长时任务完成契约**：`prefect:.agents/rules/harness-goal-governance.md`、`prefect:.agents/rules/main-control-coordination.md`、`prefect:.codex/agents/README.md`、`prefect:.codex/agents/records/harness-feedback-ledger/README.md`、`prefect:.codex/agents/records/harness-goal-governance/README.md`
- **客群 DB 读回**：`prefect:.codex/agents/records/harness-feedback-ledger/README.md`、`prefect:.codex/skills/customer-group-db-readback/SKILL.md`
- **问题聚焦式图文呈现**：`prefect:.agents/skills/problem-focused-visual-presentation/SKILL.md`、`prefect:.codex/agents/skills/problem-focused-visual-presentation/SKILL.md`、`prefect:.codex/agents/templates/problem-focused-lens-template.md`、`prefect:views/lens-registry.md`
- **文档与 Agent 规则维护**：`prefect:.agents/rules/harness-goal-governance.md`、`prefect:.agents/rules/main-control-coordination.md`、`prefect:.agents/rules/subproject-bug-communication.md`、`prefect:.agents/skills/agents-md-sync/SKILL.md`、`prefect:.agents/skills/backlog-management/SKILL.md`
- **Issue / 事故分析**：`prefect:.agents/skills/issue-incident-analysis/SKILL.md`、`prefect:.codex/agents/records/issue-incident-analysis/README.md`、`prefect:.codex/agents/skills/issue-incident-analysis/SKILL.md`
- **项目上下文入口**：`prefect:.codex/skills/customer-pipeline-docs/SKILL.md`
- **Backlog 批处理**：`prefect:.agents/skills/backlog-management/SKILL.md`、`prefect:.claude/skills/backlog-management/SKILL.md`、`prefect:.codex/agents/skills/backlog-management/SKILL.md`

## customeranalysis

- **工程路径**：`/Users/hai/Documents/Code/customeranalysis`
- **成熟概览**：领先 1；成熟 0；接入 2；局部 4；未见 7；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 未见 0/15 | 15 | Software/wiki | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 未见 0/14 | 14 | AcknowledgeBase、Software/wiki | 无 | TRANSFER、body、governance、large-body、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 未见 0/13 | 13 | Software/wiki | 无 | TRANSFER、body、governance、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 未见 0/11 | 11 | Software/wiki | 无 | TRANSFER、body、skill | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 3/16 | 13 | DocCustomeranalysis | governance、small-body | body、large-body、sensor、skill | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 局部 7/20 | 13 | Software/wiki | body、governance、sensor | TRANSFER、large-body、skill、template | 追齐领先信号：优先补 TRANSFER, large-body, skill, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 局部 7/16 | 9 | fetch-adapter | body、governance、sensor | TRANSFER、large-body、skill | 追齐领先信号：优先补 TRANSFER, large-body, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 局部 5/10 | 5 | AcknowledgeBase、Software/wiki、DocCustomeranalysis、DocFilmCommunity、LifeOS | governance、large-body | goal-contract、template | 追齐领先信号：优先补 goal-contract, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 接入 12/21 | 9 | DocCustomeranalysis | skill、small-body、views | TRANSFER、body、governance、large-body、sensor、template | 追齐领先信号：优先补 TRANSFER, body, governance, large-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 接入 9/16 | 7 | Software/wiki | skill、small-body | TRANSFER、body、sensor | 追齐领先信号：优先补 TRANSFER, body, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 领先 12/12 | 0 | customeranalysis、17lang | body、governance、skill | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **客群 DB 读回**：`customeranalysis:.codex/context/harness-feedback-ledger.md`
- **跨工程治理审计**：`customeranalysis:.codex/context/harness-evolution.md`、`customeranalysis:.codex/context/harness-feedback-ledger.md`、`customeranalysis:.codex/skills/historical-dialogue-retrospective/SKILL.md`、`customeranalysis:scripts/check_agent_harness.py`
- **文档与 Agent 规则维护**：`customeranalysis:.codex/context/agent-coordination.md`、`customeranalysis:AGENTS.md`、`customeranalysis:scripts/check_agent_harness.py`
- **Goal Contract / 长时任务完成契约**：`customeranalysis:.codex/context/customeranalysis-engineering-context.md`、`customeranalysis:.codex/context/harness-feedback-ledger.md`、`customeranalysis:.codex/context/rule-conflict-resolution.md`、`customeranalysis:.codex/skills/customeranalysis-docs/SKILL.md`、`customeranalysis:AGENTS.md`
- **问题聚焦式图文呈现**：`customeranalysis:.codex/skills/problem-focused-visual-presentation/SKILL.md`、`customeranalysis:views/lens-registry.md`
- **复盘 / 回顾改进**：`customeranalysis:.codex/skills/historical-dialogue-retrospective/SKILL.md`
- **项目上下文入口**：`customeranalysis:.codex/context/customeranalysis-engineering-context.md`、`customeranalysis:.codex/skills/customeranalysis-docs/SKILL.md`

## LifeOS

- **工程路径**：`/Users/hai/Documents/Life`
- **成熟概览**：领先 2；成熟 1；接入 1；局部 4；未见 6；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 未见 0/15 | 15 | Software/wiki | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 未见 0/14 | 14 | AcknowledgeBase、Software/wiki | 无 | TRANSFER、body、governance、large-body、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 未见 0/11 | 11 | Software/wiki | 无 | TRANSFER、body、skill | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 局部 1/16 | 15 | fetch-adapter | small-body | TRANSFER、body、governance、large-body、sensor、skill | 追齐领先信号：优先补 TRANSFER, body, governance, large-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 局部 6/20 | 14 | Software/wiki | governance、large-body、template | TRANSFER、sensor、skill | 追齐领先信号：优先补 TRANSFER, sensor, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 局部 2/13 | 11 | Software/wiki | governance | TRANSFER、body、skill、small-body、template | 追齐领先信号：优先补 TRANSFER, body, skill, small-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 5/16 | 11 | DocCustomeranalysis | body、sensor | governance、large-body、skill | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 接入 8/16 | 8 | Software/wiki | skill | TRANSFER、body、sensor、small-body | 追齐领先信号：优先补 TRANSFER, body, sensor, small-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 成熟 20/21 | 1 | DocCustomeranalysis | governance、large-body、sensor、skill、template、views | TRANSFER | 追齐领先信号：优先补 TRANSFER；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 领先 10/10 | 0 | AcknowledgeBase、Software/wiki、DocCustomeranalysis、DocFilmCommunity、LifeOS | goal-contract、governance、large-body、template | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 领先 11/11 | 0 | LifeOS | governance、skill、small-body | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **文档与 Agent 规则维护**：`LifeOS:AGENTS.md`
- **跨工程治理审计**：`LifeOS:.codex/context/governance-reference.md`、`LifeOS:.codex/skills/system-harness-review/SKILL.md`、`LifeOS:automation/scripts/check_harness_feedback_ledger.py`、`LifeOS:automation/scripts/check_life_governance_depth.py`、`LifeOS:logs/system/harness-feedback-ledger.md`
- **Issue / 事故分析**：`LifeOS:rules/incident-lifecycle.md`
- **客群 DB 读回**：`LifeOS:automation/scripts/check_harness_feedback_ledger.py`、`LifeOS:logs/system/harness-feedback-ledger.md`
- **复盘 / 回顾改进**：`LifeOS:.codex/skills/system-harness-review/SKILL.md`
- **问题聚焦式图文呈现**：`LifeOS:.codex/skills/problem-focused-lens/SKILL.md`、`LifeOS:automation/scripts/check_problem_focused_lens.py`、`LifeOS:rules/problem-focused-lens.md`、`LifeOS:templates/lens.md`、`LifeOS:views/current/a-b-moving-priority-lens.html`
- **Goal Contract / 长时任务完成契约**：`LifeOS:.codex/context/governance-reference.md`、`LifeOS:.codex/context/lifeos-map.md`、`LifeOS:.codex/context/workflow-reference.md`、`LifeOS:.codex/skills/system-harness-review/SKILL.md`、`LifeOS:AGENTS.md`
- **生活系统管理**：`LifeOS:.codex/skills/inbox-triage/SKILL.md`、`LifeOS:.codex/skills/life-decision-review/SKILL.md`、`LifeOS:.codex/skills/life-matter-routing/SKILL.md`、`LifeOS:.codex/skills/weekly-review/SKILL.md`、`LifeOS:rules/life-matter-routing.md`

## DocERP

- **工程路径**：`/Users/hai/Documents/Code/DocERP`
- **成熟概览**：领先 0；成熟 1；接入 0；局部 4；未见 9；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 未见 0/21 | 21 | DocCustomeranalysis | 无 | TRANSFER、body、governance、large-body、sensor、skill、small-body、template、views | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 未见 0/16 | 16 | Software/wiki | 无 | TRANSFER、body、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 未见 0/15 | 15 | Software/wiki | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 未见 0/11 | 11 | Software/wiki | 无 | TRANSFER、body、skill | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 未见 0/10 | 10 | AcknowledgeBase、Software/wiki、DocCustomeranalysis、DocFilmCommunity、LifeOS | 无 | body、goal-contract、governance、large-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 局部 5/20 | 15 | Software/wiki | governance、large-body | TRANSFER、sensor、skill、template | 追齐领先信号：优先补 TRANSFER, sensor, skill, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 局部 2/16 | 14 | fetch-adapter | body | TRANSFER、governance、large-body、sensor、skill | 追齐领先信号：优先补 TRANSFER, governance, large-body, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 3/16 | 13 | DocCustomeranalysis | governance、small-body | body、large-body、sensor、skill | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 局部 2/14 | 12 | AcknowledgeBase、Software/wiki | governance | TRANSFER、body、large-body、skill、small-body、template | 追齐领先信号：优先补 TRANSFER, body, large-body, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 成熟 9/13 | 4 | Software/wiki | skill、small-body | TRANSFER、body、governance、template | 追齐领先信号：优先补 TRANSFER, body, governance, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |

### 证据路径

- **跨工程治理审计**：`DocERP:governance/BRAIN.md`、`DocERP:governance/POLICY.md`、`DocERP:governance/README.md`、`DocERP:governance/WORKFLOW.md`、`DocERP:governance/log-writing-rules.md`
- **文档与 Agent 规则维护**：`DocERP:AGENTS.md`
- **客群 DB 读回**：`DocERP:governance/template-feedback-rules.md`、`DocERP:projects/development/execution/engineering-feedback-loop.md`
- **调研 / 研究能力**：`DocERP:governance/BRAIN.md`
- **Issue / 事故分析**：`DocERP:skills/issue-analysis/SKILL.md`

## H100

- **工程路径**：`/Users/hai/Documents/Software/H100`
- **成熟概览**：领先 0；成熟 0；接入 1；局部 4；未见 9；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 未见 0/16 | 16 | Software/wiki | 无 | TRANSFER、body、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 未见 0/15 | 15 | Software/wiki | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 未见 0/13 | 13 | Software/wiki | 无 | TRANSFER、body、governance、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 未见 0/11 | 11 | Software/wiki | 无 | TRANSFER、body、skill | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 未见 0/10 | 10 | AcknowledgeBase、Software/wiki、DocCustomeranalysis、DocFilmCommunity、LifeOS | 无 | body、goal-contract、governance、large-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 局部 3/20 | 17 | Software/wiki | governance、small-body | TRANSFER、body、large-body、sensor、skill、template | 追齐领先信号：优先补 TRANSFER, body, large-body, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 局部 1/16 | 15 | fetch-adapter | small-body | TRANSFER、body、governance、large-body、sensor、skill | 追齐领先信号：优先补 TRANSFER, body, governance, large-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 2/16 | 14 | DocCustomeranalysis | governance | body、large-body、sensor、skill、small-body | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 局部 3/14 | 11 | AcknowledgeBase、Software/wiki | governance、small-body | TRANSFER、body、large-body、skill、template | 追齐领先信号：优先补 TRANSFER, body, large-body, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 接入 9/21 | 12 | DocCustomeranalysis | skill、small-body | TRANSFER、body、governance、large-body、sensor、template、views | 追齐领先信号：优先补 TRANSFER, body, governance, large-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |

### 证据路径

- **跨工程治理审计**：`H100:.codex/context/harness-feedback-ledger.md`、`H100:.codex/context/main-control-harness.md`
- **文档与 Agent 规则维护**：`H100:AGENTS.md`
- **客群 DB 读回**：`H100:.codex/context/harness-feedback-ledger.md`
- **调研 / 研究能力**：`H100:.codex/context/main-control-harness.md`
- **问题聚焦式图文呈现**：`H100:.codex/skills/problem-focused-visual-presentation/SKILL.md`

## 17lang

- **工程路径**：`/Users/hai/Documents/Code/17lang`
- **成熟概览**：领先 1；成熟 0；接入 0；局部 1；未见 12；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 未见 0/21 | 21 | DocCustomeranalysis | 无 | TRANSFER、body、governance、large-body、sensor、skill、small-body、template、views | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 未见 0/20 | 20 | Software/wiki | 无 | TRANSFER、body、governance、large-body、sensor、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 未见 0/16 | 16 | Software/wiki | 无 | TRANSFER、body、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 未见 0/16 | 16 | DocCustomeranalysis | 无 | body、governance、large-body、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 未见 0/16 | 16 | fetch-adapter | 无 | TRANSFER、body、governance、large-body、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 未见 0/15 | 15 | Software/wiki | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 未见 0/14 | 14 | AcknowledgeBase、Software/wiki | 无 | TRANSFER、body、governance、large-body、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 未见 0/13 | 13 | Software/wiki | 无 | TRANSFER、body、governance、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 未见 0/11 | 11 | Software/wiki | 无 | TRANSFER、body、skill | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 局部 4/10 | 6 | AcknowledgeBase、Software/wiki、DocCustomeranalysis、DocFilmCommunity、LifeOS | body、governance | goal-contract、large-body、template | 追齐领先信号：优先补 goal-contract, large-body, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 领先 12/12 | 0 | customeranalysis、17lang | body、governance、skill | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **Goal Contract / 长时任务完成契约**：`17lang:.codex/context/film-community-17lang-context.md`、`17lang:.codex/skills/film-community-docs/SKILL.md`、`17lang:docs/handoffs/README.md`
- **项目上下文入口**：`17lang:.codex/context/film-community-17lang-context.md`、`17lang:.codex/skills/film-community-docs/SKILL.md`
