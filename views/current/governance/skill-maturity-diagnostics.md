---
type: skill-maturity-diagnostics
lens_id: lens-skill-maturity-diagnostics-current
focus_object: per-project action diagnostics for cross-project skill maturity gaps
lens_type: knowledge
source_pages: skills/README.md; projects/governance/registry.md; scripts/update_skill_maturity_matrix.py
source_scope: same scan context as skill-maturity-matrix.html and skill-maturity-matrix.data.json
source_of_truth: false
generated_at: 2026-06-15 13:11
source_revision: 29eeb08
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
- **成熟概览**：领先 0；成熟 6；接入 3；局部 1；未见 5；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| transferable skill governance (`transferable-skill-governance`) | 通用 / 可迁移 | 未见 0/14 | 14 | DocCustomeranalysis、DocFilmCommunity、fetch-adapter | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 4/16 | 12 | DocCustomeranalysis | body、governance | large-body、sensor、skill | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 接入 10/21 | 11 | DocCustomeranalysis、DocFilmCommunity | goal-contract、governance、large-body、template | TRANSFER、skill | 追齐领先信号：优先补 TRANSFER, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 接入 8/19 | 11 | Software/wiki、DocCustomeranalysis、customeranalysis | governance、large-body、views | TRANSFER、sensor、skill | 追齐领先信号：优先补 TRANSFER, sensor, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 接入 10/16 | 6 | Software/wiki、DocCustomeranalysis | skill、small-body、template | TRANSFER、body、governance | 追齐领先信号：优先补 TRANSFER, body, governance；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 成熟 14/19 | 5 | Software/wiki、DocCustomeranalysis | governance、large-body、skill、template | TRANSFER、sensor | 追齐领先信号：优先补 TRANSFER, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 成熟 10/14 | 4 | Software/wiki | body、skill | TRANSFER、template | 追齐领先信号：优先补 TRANSFER, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 成熟 14/17 | 3 | Software/wiki、DocCustomeranalysis | governance、sensor、skill、small-body | TRANSFER | 追齐领先信号：优先补 TRANSFER；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 成熟 17/20 | 3 | Software/wiki、DocCustomeranalysis、DocFilmCommunity | governance、large-body、sensor、skill、template | TRANSFER | 追齐领先信号：优先补 TRANSFER；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 成熟 20/23 | 3 | DocCustomeranalysis | TRANSFER、body、sensor、skill、template、views | governance、large-body | 追齐领先信号：优先补 governance, large-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 成熟 16/16 | 0 | AcknowledgeBase、Software/wiki、DocCustomeranalysis | TRANSFER、body、skill、views | sensor | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 sensor；覆盖证据信号并集后，才可重新评为领先。 |

### 证据路径

- **客群 DB 读回**：`AcknowledgeBase:governance/harness-feedback-ledger.md`、`AcknowledgeBase:governance/template-feedback-rules.md`、`AcknowledgeBase:projects/development/execution/engineering-feedback-loop.md`
- **Goal Contract / 长时任务完成契约**：`AcknowledgeBase:AGENTS.md`、`AcknowledgeBase:INDEX.md`、`AcknowledgeBase:README.md`、`AcknowledgeBase:articles/2026-05-25-codex-goals-research.md`、`AcknowledgeBase:articles/2026-06-12-codex-goal-mode-public-guide.md`
- **文档与 Agent 规则维护**：`AcknowledgeBase:AGENTS.md`、`AcknowledgeBase:governance/agent-governance-strategy.md`、`AcknowledgeBase:views/current/governance/codex-goal-guide-agent-collaboration-retrospective.html`
- **Issue / 事故分析**：`AcknowledgeBase:skills/issue-analysis/SKILL.md`、`AcknowledgeBase:templates/development-issue-template.md`
- **调研 / 研究能力**：`AcknowledgeBase:governance/BRAIN.md`、`AcknowledgeBase:governance/state-constraint-reasoning.md`、`AcknowledgeBase:skills/industry-ai-research/SKILL.md`、`AcknowledgeBase:skills/open-source-project-research/SKILL.md`、`AcknowledgeBase:skills/technical-topic-research/SKILL.md`
- **跨工程技能迁移提示词**：`AcknowledgeBase:skills/cross-project-skill-adoption-prompt/SKILL.md`
- **知识关联**：`AcknowledgeBase:governance/knowledge-linking-rules.md`、`AcknowledgeBase:scripts/check_knowledge_linking.py`、`AcknowledgeBase:skills/knowledge-linking/SKILL.md`
- **跨工程治理审计**：`AcknowledgeBase:governance/BRAIN.md`、`AcknowledgeBase:governance/POLICY.md`、`AcknowledgeBase:governance/README.md`、`AcknowledgeBase:governance/WORKFLOW.md`、`AcknowledgeBase:governance/agent-governance-strategy.md`
- **问题聚焦式图文呈现**：`AcknowledgeBase:scripts/check_problem_focused_visual_presentation.py`、`AcknowledgeBase:skills/problem-focused-visual-presentation/SKILL.md`、`AcknowledgeBase:templates/problem-focused-lens-template.md`、`AcknowledgeBase:views/lens-registry.md`
- **复盘 / 回顾改进**：`AcknowledgeBase:skills/historical-dialogue-retrospective/SKILL.md`、`AcknowledgeBase:views/current/governance/codex-goal-guide-agent-collaboration-retrospective.html`

## Software/wiki

- **工程路径**：`/Users/hai/Documents/Software/wiki`
- **成熟概览**：领先 4；成熟 4；接入 1；局部 1；未见 5；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| transferable skill governance (`transferable-skill-governance`) | 通用 / 可迁移 | 未见 0/14 | 14 | DocCustomeranalysis、DocFilmCommunity、fetch-adapter | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 7/16 | 9 | DocCustomeranalysis | body、governance、sensor | large-body、skill | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 接入 10/21 | 11 | DocCustomeranalysis、DocFilmCommunity | goal-contract、governance、large-body、template | TRANSFER、skill | 追齐领先信号：优先补 TRANSFER, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 成熟 22/23 | 1 | DocCustomeranalysis | TRANSFER、body、governance、sensor、skill、template、views | large-body | 追齐领先信号：优先补 large-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 成熟 16/16 | 0 | AcknowledgeBase、Software/wiki、DocCustomeranalysis | TRANSFER、body、sensor、skill | views | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 views；覆盖证据信号并集后，才可重新评为领先。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 成熟 19/19 | 0 | Software/wiki、DocCustomeranalysis、customeranalysis | TRANSFER、governance、large-body、sensor、skill | views | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 views；覆盖证据信号并集后，才可重新评为领先。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 成熟 19/19 | 0 | Software/wiki、DocCustomeranalysis | TRANSFER、body、governance、sensor、skill、template | large-body | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 large-body；覆盖证据信号并集后，才可重新评为领先。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 领先 16/16 | 0 | Software/wiki、DocCustomeranalysis | TRANSFER、body、governance、skill、template | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 领先 17/17 | 0 | Software/wiki、DocCustomeranalysis | TRANSFER、governance、sensor、skill、small-body | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 领先 14/14 | 0 | Software/wiki | TRANSFER、body、skill、template | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 领先 20/20 | 0 | Software/wiki、DocCustomeranalysis、DocFilmCommunity | TRANSFER、governance、large-body、sensor、skill、template | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **客群 DB 读回**：`Software/wiki:governance/harness-feedback-ledger.md`、`Software/wiki:governance/template-feedback-rules.md`、`Software/wiki:projects/development/execution/engineering-feedback-loop.md`、`Software/wiki:scripts/check_harness_feedback_ledger.py`
- **Goal Contract / 长时任务完成契约**：`Software/wiki:AGENTS.md`、`Software/wiki:INDEX.md`、`Software/wiki:README.md`、`Software/wiki:articles/2026-05-25-codex-goals-research.md`、`Software/wiki:concepts/codex-goals.md`
- **问题聚焦式图文呈现**：`Software/wiki:governance/problem-focused-visual-presentation-rules.md`、`Software/wiki:scripts/check_problem_focused_visual_presentation.py`、`Software/wiki:skills/problem-focused-visual-presentation/SKILL.md`、`Software/wiki:templates/problem-focused-lens-review-contract.md`、`Software/wiki:templates/problem-focused-lens-source-pack-contract.md`
- **复盘 / 回顾改进**：`Software/wiki:scripts/check_retrospective_system.py`、`Software/wiki:skills/historical-dialogue-retrospective/SKILL.md`
- **文档与 Agent 规则维护**：`Software/wiki:AGENTS.md`、`Software/wiki:governance/documentation-maintenance-rules.md`、`Software/wiki:scripts/check_documentation_maintenance.py`、`Software/wiki:skills/documentation-maintenance/SKILL.md`
- **调研 / 研究能力**：`Software/wiki:governance/BRAIN.md`、`Software/wiki:governance/documentation-maintenance-rules.md`、`Software/wiki:governance/research-capability-rules.md`、`Software/wiki:scripts/check_documentation_maintenance.py`、`Software/wiki:skills/documentation-maintenance/SKILL.md`
- **Issue / 事故分析**：`Software/wiki:governance/issue-analysis-rules.md`、`Software/wiki:skills/issue-analysis/SKILL.md`、`Software/wiki:templates/development-issue-template.md`
- **知识关联**：`Software/wiki:governance/knowledge-linking-rules.md`、`Software/wiki:scripts/check_knowledge_linking.py`、`Software/wiki:skills/knowledge-linking/SKILL.md`
- **跨工程技能迁移提示词**：`Software/wiki:skills/cross-project-skill-adoption-prompt/SKILL.md`、`Software/wiki:templates/skill-transfer-contract-template.md`、`Software/wiki:templates/skill-transfer-evidence-contract.md`、`Software/wiki:templates/skill-transfer-review-contract.md`
- **跨工程治理审计**：`Software/wiki:governance/BRAIN.md`、`Software/wiki:governance/POLICY.md`、`Software/wiki:governance/README.md`、`Software/wiki:governance/WORKFLOW.md`、`Software/wiki:governance/documentation-maintenance-rules.md`

## DocCustomeranalysis

- **工程路径**：`/Users/hai/Documents/Code/DocCustomeranalysis`
- **成熟概览**：领先 7；成熟 5；接入 0；局部 0；未见 3；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 成熟 12/14 | 2 | Software/wiki | TRANSFER、skill、template | body、small-body | 追齐领先信号：优先补 body, small-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| transferable skill governance (`transferable-skill-governance`) | 通用 / 可迁移 | 成熟 14/14 | 0 | DocCustomeranalysis、DocFilmCommunity、fetch-adapter | TRANSFER、governance、skill、small-body | sensor | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 sensor；覆盖证据信号并集后，才可重新评为领先。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 成熟 16/16 | 0 | AcknowledgeBase、Software/wiki、DocCustomeranalysis | TRANSFER、body、sensor、skill | views | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 views；覆盖证据信号并集后，才可重新评为领先。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 成熟 19/19 | 0 | Software/wiki、DocCustomeranalysis、customeranalysis | TRANSFER、governance、large-body、sensor、skill | views | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 views；覆盖证据信号并集后，才可重新评为领先。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 成熟 19/19 | 0 | Software/wiki、DocCustomeranalysis | TRANSFER、body、governance、sensor、skill、template | large-body | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 large-body；覆盖证据信号并集后，才可重新评为领先。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 领先 21/21 | 0 | DocCustomeranalysis、DocFilmCommunity | TRANSFER、goal-contract、governance、large-body、skill、template | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 领先 16/16 | 0 | Software/wiki、DocCustomeranalysis | TRANSFER、body、governance、skill、template | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 领先 9/9 | 0 | DocCustomeranalysis | skill、small-body | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 领先 16/16 | 0 | DocCustomeranalysis | governance、large-body、sensor、skill | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 领先 17/17 | 0 | Software/wiki、DocCustomeranalysis | TRANSFER、governance、sensor、skill、small-body | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 领先 20/20 | 0 | Software/wiki、DocCustomeranalysis、DocFilmCommunity | TRANSFER、governance、large-body、sensor、skill、template | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 领先 23/23 | 0 | DocCustomeranalysis | TRANSFER、governance、large-body、sensor、skill、template、views | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **跨工程技能迁移提示词**：`DocCustomeranalysis:skills/cross-project-skill-adoption-prompt/SKILL.md`、`DocCustomeranalysis:templates/skill-transfer-contract-template.md`
- **transferable skill governance**：`DocCustomeranalysis:governance/transferable-skill-governance-rules.md`、`DocCustomeranalysis:skills/transferable-skill-governance/SKILL.md`
- **复盘 / 回顾改进**：`DocCustomeranalysis:scripts/check_retrospective_system.py`、`DocCustomeranalysis:skills/historical-dialogue-retrospective/SKILL.md`、`DocCustomeranalysis:skills/retrospective/SKILL.md`
- **文档与 Agent 规则维护**：`DocCustomeranalysis:AGENTS.md`、`DocCustomeranalysis:governance/documentation-maintenance-rules.md`、`DocCustomeranalysis:scripts/check_documentation_maintenance.py`、`DocCustomeranalysis:skills/documentation-maintenance/SKILL.md`
- **调研 / 研究能力**：`DocCustomeranalysis:governance/BRAIN.md`、`DocCustomeranalysis:governance/documentation-maintenance-rules.md`、`DocCustomeranalysis:governance/research-capability-rules.md`、`DocCustomeranalysis:scripts/check_documentation_maintenance.py`、`DocCustomeranalysis:skills/documentation-maintenance/SKILL.md`
- **Goal Contract / 长时任务完成契约**：`DocCustomeranalysis:AGENTS.md`、`DocCustomeranalysis:INDEX.md`、`DocCustomeranalysis:README.md`、`DocCustomeranalysis:articles/2026-06-12-codex-goal-mode-usage-review.md`、`DocCustomeranalysis:concepts/codex-goals.md`
- **Issue / 事故分析**：`DocCustomeranalysis:governance/issue-analysis-rules.md`、`DocCustomeranalysis:skills/issue-analysis/SKILL.md`、`DocCustomeranalysis:templates/development-issue-template.md`
- **事项自动拆解**：`DocCustomeranalysis:skills/work-item-auto-decomposition/SKILL.md`
- **客群 DB 读回**：`DocCustomeranalysis:governance/harness-feedback-ledger.md`、`DocCustomeranalysis:governance/template-feedback-rules.md`、`DocCustomeranalysis:projects/development/execution/engineering-feedback-loop.md`、`DocCustomeranalysis:scripts/check_harness_feedback_ledger.py`、`DocCustomeranalysis:skills/customer-group-db-readback/SKILL.md`
- **知识关联**：`DocCustomeranalysis:governance/knowledge-linking-rules.md`、`DocCustomeranalysis:scripts/check_knowledge_linking.py`、`DocCustomeranalysis:skills/knowledge-linking/SKILL.md`
- **跨工程治理审计**：`DocCustomeranalysis:governance/BRAIN.md`、`DocCustomeranalysis:governance/POLICY.md`、`DocCustomeranalysis:governance/README.md`、`DocCustomeranalysis:governance/WORKFLOW.md`、`DocCustomeranalysis:governance/documentation-maintenance-rules.md`
- **问题聚焦式图文呈现**：`DocCustomeranalysis:governance/problem-focused-visual-presentation-rules.md`、`DocCustomeranalysis:scripts/check_problem_focused_visual_presentation.py`、`DocCustomeranalysis:skills/problem-focused-visual-presentation/SKILL.md`、`DocCustomeranalysis:templates/problem-focused-lens-template.md`、`DocCustomeranalysis:views/current/task-080-status-acceptance-lens.html`

## DocFilmCommunity

- **工程路径**：`/Users/hai/Documents/Code/DocFilmCommunity`
- **成熟概览**：领先 2；成熟 6；接入 2；局部 1；未见 4；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 7/16 | 9 | DocCustomeranalysis | body、governance、sensor | large-body、skill | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 接入 11/17 | 6 | Software/wiki、DocCustomeranalysis | TRANSFER、skill | governance、sensor、small-body | 追齐领先信号：优先补 governance, sensor, small-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 接入 11/16 | 5 | AcknowledgeBase、Software/wiki、DocCustomeranalysis | TRANSFER、skill | body、sensor、small-body、views | 追齐领先信号：优先补 body, sensor, small-body, views；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 成熟 14/19 | 5 | Software/wiki、DocCustomeranalysis、customeranalysis | TRANSFER、large-body、skill | governance、sensor、views | 追齐领先信号：优先补 governance, sensor, views；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 成熟 15/19 | 4 | Software/wiki、DocCustomeranalysis | TRANSFER、governance、skill、small-body、template | body、large-body、sensor | 追齐领先信号：优先补 body, large-body, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 成熟 13/16 | 3 | Software/wiki、DocCustomeranalysis | TRANSFER、skill、small-body、template | body、governance | 追齐领先信号：优先补 body, governance；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 成熟 11/14 | 3 | Software/wiki | TRANSFER、skill | body、small-body、template | 追齐领先信号：优先补 body, small-body, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 成熟 20/23 | 3 | DocCustomeranalysis | TRANSFER、body、sensor、skill、template、views | governance、large-body | 追齐领先信号：优先补 governance, large-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| transferable skill governance (`transferable-skill-governance`) | 通用 / 可迁移 | 成熟 14/14 | 0 | DocCustomeranalysis、DocFilmCommunity、fetch-adapter | TRANSFER、governance、skill、small-body | sensor | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 sensor；覆盖证据信号并集后，才可重新评为领先。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 领先 21/21 | 0 | DocCustomeranalysis、DocFilmCommunity | TRANSFER、goal-contract、governance、large-body、skill、template | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 领先 20/20 | 0 | Software/wiki、DocCustomeranalysis、DocFilmCommunity | TRANSFER、governance、large-body、sensor、skill、template | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **客群 DB 读回**：`DocFilmCommunity:governance/harness-feedback-ledger.md`、`DocFilmCommunity:governance/template-feedback-rules.md`、`DocFilmCommunity:projects/development/execution/engineering-feedback-loop.md`、`DocFilmCommunity:scripts/check_harness_feedback_ledger.py`
- **知识关联**：`DocFilmCommunity:skills/knowledge-linking/SKILL.md`
- **复盘 / 回顾改进**：`DocFilmCommunity:skills/historical-dialogue-retrospective/SKILL.md`
- **文档与 Agent 规则维护**：`DocFilmCommunity:AGENTS.md`、`DocFilmCommunity:skills/documentation-maintenance/SKILL.md`
- **调研 / 研究能力**：`DocFilmCommunity:governance/BRAIN.md`、`DocFilmCommunity:skills/documentation-maintenance/SKILL.md`、`DocFilmCommunity:skills/technology-research/SKILL.md`、`DocFilmCommunity:templates/technology-research-contract-template.md`
- **Issue / 事故分析**：`DocFilmCommunity:skills/issue-analysis/SKILL.md`、`DocFilmCommunity:templates/development-issue-template.md`
- **跨工程技能迁移提示词**：`DocFilmCommunity:skills/cross-project-skill-adoption-prompt/SKILL.md`
- **问题聚焦式图文呈现**：`DocFilmCommunity:scripts/check_problem_focused_visual_presentation.py`、`DocFilmCommunity:skills/problem-focused-visual-presentation/SKILL.md`、`DocFilmCommunity:templates/problem-focused-lens-template.md`、`DocFilmCommunity:views/lens-registry.md`
- **transferable skill governance**：`DocFilmCommunity:governance/transferable-skill-governance-rules.md`、`DocFilmCommunity:skills/transferable-skill-governance/SKILL.md`
- **Goal Contract / 长时任务完成契约**：`DocFilmCommunity:AGENTS.md`、`DocFilmCommunity:INDEX.md`、`DocFilmCommunity:README.md`、`DocFilmCommunity:concepts/codex-goals.md`、`DocFilmCommunity:governance/BRAIN.md`
- **跨工程治理审计**：`DocFilmCommunity:governance/BRAIN.md`、`DocFilmCommunity:governance/POLICY.md`、`DocFilmCommunity:governance/README.md`、`DocFilmCommunity:governance/WORKFLOW.md`、`DocFilmCommunity:governance/execution-contract-semantics.md`

## fetch-adapter

- **工程路径**：`/Users/hai/Documents/Code/Customer/fetch-adapter`
- **成熟概览**：领先 1；成熟 4；接入 2；局部 2；未见 6；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 未见 0/19 | 19 | Software/wiki、DocCustomeranalysis | 无 | TRANSFER、body、governance、large-body、sensor、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 未见 0/17 | 17 | Software/wiki、DocCustomeranalysis | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 未见 0/16 | 16 | AcknowledgeBase、Software/wiki、DocCustomeranalysis | 无 | TRANSFER、body、sensor、skill、small-body、views | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 未见 0/14 | 14 | Software/wiki | 无 | TRANSFER、body、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 2/16 | 14 | DocCustomeranalysis | governance | body、large-body、sensor、skill、small-body | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 局部 7/20 | 13 | Software/wiki、DocCustomeranalysis、DocFilmCommunity | body、governance、sensor | TRANSFER、large-body、skill、template | 追齐领先信号：优先补 TRANSFER, large-body, skill, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 接入 9/21 | 12 | DocCustomeranalysis、DocFilmCommunity | goal-contract、governance、large-body | TRANSFER、skill、template | 追齐领先信号：优先补 TRANSFER, skill, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 接入 10/16 | 6 | Software/wiki、DocCustomeranalysis | body、skill | TRANSFER、governance、template | 追齐领先信号：优先补 TRANSFER, governance, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 成熟 19/23 | 4 | DocCustomeranalysis | TRANSFER、body、sensor、skill、views | governance、large-body、template | 追齐领先信号：优先补 governance, large-body, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 成熟 16/19 | 3 | Software/wiki、DocCustomeranalysis、customeranalysis | governance、large-body、sensor、skill | TRANSFER、views | 追齐领先信号：优先补 TRANSFER, views；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 成熟 9/12 | 3 | customeranalysis、17lang | skill、small-body | body、governance | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| transferable skill governance (`transferable-skill-governance`) | 通用 / 可迁移 | 成熟 14/14 | 0 | DocCustomeranalysis、DocFilmCommunity、fetch-adapter | governance、sensor、skill、small-body | TRANSFER | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 TRANSFER；覆盖证据信号并集后，才可重新评为领先。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 领先 9/9 | 0 | fetch-adapter、prefect | skill、small-body | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **客群 DB 读回**：`fetch-adapter:.codex/context/harness-feedback-ledger.md`
- **跨工程治理审计**：`fetch-adapter:.codex/context/agent-harness-goal-governance.md`、`fetch-adapter:.codex/context/harness-feedback-ledger.md`、`fetch-adapter:.codex/context/transferable-skill-governance.md`、`fetch-adapter:.codex/skills/transferable-skill-governance/SKILL.md`、`fetch-adapter:tools/check_agent_harness.py`
- **Goal Contract / 长时任务完成契约**：`fetch-adapter:.codex/context/agent-harness-goal-governance.md`、`fetch-adapter:.codex/context/harness-feedback-ledger.md`、`fetch-adapter:.codex/skills/problem-focused-visual-presentation/SKILL.md`、`fetch-adapter:AGENTS.md`、`fetch-adapter:tools/check_agent_harness.py`
- **Issue / 事故分析**：`fetch-adapter:.agents/skills/issue-incident-analysis/SKILL.md`、`fetch-adapter:.claude/skills/issue-incident-analysis/SKILL.md`
- **问题聚焦式图文呈现**：`fetch-adapter:.codex/skills/problem-focused-visual-presentation/SKILL.md`、`fetch-adapter:tools/check_problem_focused_visual_presentation.py`、`fetch-adapter:views/lens-registry.md`
- **文档与 Agent 规则维护**：`fetch-adapter:.agents/skills/agents-md-sync/SKILL.md`、`fetch-adapter:.agents/skills/backlog-management/SKILL.md`、`fetch-adapter:.agents/skills/document-changes/SKILL.md`、`fetch-adapter:.agents/skills/issue-incident-analysis/SKILL.md`、`fetch-adapter:.agents/skills/write-docs/SKILL.md`
- **项目上下文入口**：`fetch-adapter:.codex/skills/customer-pipeline-docs/SKILL.md`
- **transferable skill governance**：`fetch-adapter:.codex/context/transferable-skill-governance.md`、`fetch-adapter:.codex/skills/transferable-skill-governance/SKILL.md`、`fetch-adapter:tools/check_transferable_skill_governance.py`
- **Backlog 批处理**：`fetch-adapter:.agents/skills/backlog-management/SKILL.md`、`fetch-adapter:.claude/skills/backlog-management/SKILL.md`

## train_platform

- **工程路径**：`/Users/hai/Documents/Code/train_platform`
- **成熟概览**：领先 0；成熟 4；接入 5；局部 1；未见 5；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| transferable skill governance (`transferable-skill-governance`) | 通用 / 可迁移 | 未见 0/14 | 14 | DocCustomeranalysis、DocFilmCommunity、fetch-adapter | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 3/16 | 13 | DocCustomeranalysis | governance、small-body | body、large-body、sensor、skill | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 接入 12/19 | 7 | Software/wiki、DocCustomeranalysis、customeranalysis | TRANSFER、skill、small-body | body、governance、large-body、sensor、views | 追齐领先信号：优先补 body, governance, large-body, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 接入 16/23 | 7 | DocCustomeranalysis | TRANSFER、body、sensor、skill | governance、large-body、template、views | 追齐领先信号：优先补 governance, large-body, template, views；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 接入 11/17 | 6 | Software/wiki、DocCustomeranalysis | TRANSFER、skill | governance、sensor、small-body | 追齐领先信号：优先补 governance, sensor, small-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 接入 11/16 | 5 | Software/wiki、DocCustomeranalysis | TRANSFER、skill | body、governance、small-body、template | 追齐领先信号：优先补 body, governance, small-body, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 接入 11/16 | 5 | AcknowledgeBase、Software/wiki、DocCustomeranalysis | TRANSFER、skill | body、sensor、small-body、views | 追齐领先信号：优先补 body, sensor, small-body, views；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 成熟 15/21 | 6 | DocCustomeranalysis、DocFilmCommunity | TRANSFER、goal-contract、skill | body、governance、large-body、template | 追齐领先信号：优先补 body, governance, large-body, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 成熟 14/19 | 5 | Software/wiki、DocCustomeranalysis | TRANSFER、governance、skill、small-body | body、large-body、sensor、template | 追齐领先信号：优先补 body, large-body, sensor, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 成熟 11/14 | 3 | Software/wiki | TRANSFER、skill | body、small-body、template | 追齐领先信号：优先补 body, small-body, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 成熟 18/20 | 2 | Software/wiki、DocCustomeranalysis、DocFilmCommunity | TRANSFER、body、governance、sensor、skill | large-body、template | 追齐领先信号：优先补 large-body, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |

### 证据路径

- **客群 DB 读回**：`train_platform:.codex/context/harness-feedback-ledger.md`
- **文档与 Agent 规则维护**：`train_platform:.codex/skills/documentation-maintenance/SKILL.md`、`train_platform:AGENTS.md`
- **问题聚焦式图文呈现**：`train_platform:.codex/skills/problem-focused-visual-presentation/SKILL.md`、`train_platform:scripts/check_problem_focused_visual_presentation.py`
- **知识关联**：`train_platform:.codex/skills/knowledge-linking/SKILL.md`
- **Issue / 事故分析**：`train_platform:.codex/skills/issue-analysis/SKILL.md`
- **复盘 / 回顾改进**：`train_platform:.codex/skills/historical-dialogue-retrospective/SKILL.md`
- **Goal Contract / 长时任务完成契约**：`train_platform:.codex/skills/goal-contract/SKILL.md`
- **调研 / 研究能力**：`train_platform:.codex/context/main-control-coordination.md`、`train_platform:.codex/skills/documentation-maintenance/SKILL.md`、`train_platform:.codex/skills/research-capability/SKILL.md`
- **跨工程技能迁移提示词**：`train_platform:.codex/skills/cross-project-skill-adoption-prompt/SKILL.md`
- **跨工程治理审计**：`train_platform:.codex/context/harness-evolution.md`、`train_platform:.codex/context/harness-feedback-ledger.md`、`train_platform:.codex/skills/cross-project-governance-audit/SKILL.md`、`train_platform:.codex/skills/historical-dialogue-retrospective/SKILL.md`、`train_platform:scripts/check_harness_governance.py`

## prefect

- **工程路径**：`/Users/hai/Documents/Code/prefect`
- **成熟概览**：领先 1；成熟 6；接入 4；局部 1；未见 3；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| transferable skill governance (`transferable-skill-governance`) | 通用 / 可迁移 | 未见 0/14 | 14 | DocCustomeranalysis、DocFilmCommunity、fetch-adapter | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 局部 7/21 | 14 | DocCustomeranalysis、DocFilmCommunity | goal-contract、large-body | TRANSFER、governance、skill、template | 追齐领先信号：优先补 TRANSFER, governance, skill, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 接入 8/16 | 8 | DocCustomeranalysis | skill | body、governance、large-body、sensor、small-body | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 接入 13/20 | 7 | Software/wiki、DocCustomeranalysis、DocFilmCommunity | TRANSFER、body、skill | governance、large-body、sensor、template | 追齐领先信号：优先补 governance, large-body, sensor, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 接入 16/23 | 7 | DocCustomeranalysis | TRANSFER、body、skill、views | governance、large-body、sensor、template | 追齐领先信号：优先补 governance, large-body, sensor, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 接入 13/19 | 6 | Software/wiki、DocCustomeranalysis | TRANSFER、body、skill | governance、large-body、sensor、template | 追齐领先信号：优先补 governance, large-body, sensor, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 成熟 14/19 | 5 | Software/wiki、DocCustomeranalysis、customeranalysis | TRANSFER、large-body、skill | governance、sensor、views | 追齐领先信号：优先补 governance, sensor, views；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 成熟 12/17 | 5 | Software/wiki、DocCustomeranalysis | TRANSFER、skill、small-body | governance、sensor | 追齐领先信号：优先补 governance, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 成熟 12/16 | 4 | AcknowledgeBase、Software/wiki、DocCustomeranalysis | TRANSFER、skill、small-body | body、sensor、views | 追齐领先信号：优先补 body, sensor, views；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 成熟 13/16 | 3 | Software/wiki、DocCustomeranalysis | TRANSFER、body、skill | governance、template | 追齐领先信号：优先补 governance, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 成熟 9/12 | 3 | customeranalysis、17lang | skill、small-body | body、governance | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 成熟 12/14 | 2 | Software/wiki | TRANSFER、skill、small-body | body、template | 追齐领先信号：优先补 body, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 领先 9/9 | 0 | fetch-adapter、prefect | skill、small-body | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **Goal Contract / 长时任务完成契约**：`prefect:.agents/rules/harness-goal-governance.md`、`prefect:.agents/rules/main-control-coordination.md`、`prefect:.codex/agents/README.md`、`prefect:.codex/agents/records/harness-feedback-ledger/README.md`、`prefect:.codex/agents/records/harness-goal-governance/README.md`
- **客群 DB 读回**：`prefect:.codex/agents/records/harness-feedback-ledger/README.md`、`prefect:.codex/skills/customer-group-db-readback/SKILL.md`
- **跨工程治理审计**：`prefect:.agents/rules/harness-goal-governance.md`、`prefect:.agents/skills/cross-project-governance-audit/SKILL.md`、`prefect:.agents/skills/historical-dialogue-retrospective/SKILL.md`、`prefect:.codex/agents/records/harness-feedback-ledger/README.md`、`prefect:.codex/agents/records/harness-goal-governance/README.md`
- **问题聚焦式图文呈现**：`prefect:.agents/skills/problem-focused-visual-presentation/SKILL.md`、`prefect:.codex/agents/skills/problem-focused-visual-presentation/SKILL.md`、`prefect:.codex/agents/skills/problem-focused-visual-presentation/TRANSFER.md`、`prefect:.codex/agents/templates/problem-focused-lens-template.md`、`prefect:views/lens-registry.md`
- **调研 / 研究能力**：`prefect:.agents/rules/main-control-coordination.md`、`prefect:.agents/skills/documentation-maintenance/SKILL.md`、`prefect:.agents/skills/technology-research/SKILL.md`、`prefect:.codex/agents/records/main-control-coordination/README.md`、`prefect:.codex/agents/rules/main-control-coordination.md`
- **文档与 Agent 规则维护**：`prefect:.agents/rules/harness-goal-governance.md`、`prefect:.agents/rules/main-control-coordination.md`、`prefect:.agents/rules/subproject-bug-communication.md`、`prefect:.agents/skills/agents-md-sync/SKILL.md`、`prefect:.agents/skills/backlog-management/SKILL.md`
- **知识关联**：`prefect:.agents/skills/knowledge-linking/SKILL.md`、`prefect:.codex/agents/skills/knowledge-linking/SKILL.md`、`prefect:.codex/agents/skills/knowledge-linking/TRANSFER.md`
- **复盘 / 回顾改进**：`prefect:.agents/skills/historical-dialogue-retrospective/SKILL.md`、`prefect:.codex/agents/skills/historical-dialogue-retrospective/SKILL.md`、`prefect:.codex/agents/skills/historical-dialogue-retrospective/TRANSFER.md`、`prefect:.codex/agents/templates/retrospective-report-template.md`
- **Issue / 事故分析**：`prefect:.agents/skills/issue-incident-analysis/SKILL.md`、`prefect:.codex/agents/records/issue-incident-analysis/README.md`、`prefect:.codex/agents/skills/issue-incident-analysis/SKILL.md`、`prefect:.codex/agents/skills/issue-incident-analysis/TRANSFER.md`、`prefect:.codex/agents/templates/issue-analysis-report-template.md`
- **项目上下文入口**：`prefect:.codex/skills/customer-pipeline-docs/SKILL.md`
- **跨工程技能迁移提示词**：`prefect:.agents/skills/cross-project-skill-adoption-prompt/SKILL.md`、`prefect:.codex/agents/skills/cross-project-skill-adoption-prompt/SKILL.md`、`prefect:.codex/agents/skills/cross-project-skill-adoption-prompt/TRANSFER.md`、`prefect:.codex/agents/templates/skill-transfer-contract-template.md`
- **Backlog 批处理**：`prefect:.agents/skills/backlog-management/SKILL.md`、`prefect:.claude/skills/backlog-management/SKILL.md`、`prefect:.codex/agents/skills/backlog-management/SKILL.md`

## customeranalysis

- **工程路径**：`/Users/hai/Documents/Code/customeranalysis`
- **成熟概览**：领先 1；成熟 6；接入 4；局部 1；未见 3；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 3/16 | 13 | DocCustomeranalysis | governance、small-body | body、large-body、sensor、skill | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 接入 15/23 | 8 | DocCustomeranalysis | TRANSFER、skill、small-body、views | body、governance、large-body、sensor、template | 追齐领先信号：优先补 body, governance, large-body, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 接入 12/19 | 7 | Software/wiki、DocCustomeranalysis | TRANSFER、skill、small-body | body、governance、large-body、sensor、template | 追齐领先信号：优先补 body, governance, large-body, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 接入 11/17 | 6 | Software/wiki、DocCustomeranalysis | TRANSFER、skill | governance、sensor、small-body | 追齐领先信号：优先补 governance, sensor, small-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 接入 11/16 | 5 | Software/wiki、DocCustomeranalysis | TRANSFER、skill | body、governance、small-body、template | 追齐领先信号：优先补 body, governance, small-body, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 成熟 12/16 | 4 | AcknowledgeBase、Software/wiki、DocCustomeranalysis | TRANSFER、skill、small-body | body、sensor、views | 追齐领先信号：优先补 body, sensor, views；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| transferable skill governance (`transferable-skill-governance`) | 通用 / 可迁移 | 成熟 11/14 | 3 | DocCustomeranalysis、DocFilmCommunity、fetch-adapter | TRANSFER、skill | governance、sensor、small-body | 追齐领先信号：优先补 governance, sensor, small-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 成熟 11/14 | 3 | Software/wiki | TRANSFER、skill | body、small-body、template | 追齐领先信号：优先补 body, small-body, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 成熟 20/21 | 1 | DocCustomeranalysis、DocFilmCommunity | TRANSFER、goal-contract、governance、large-body、skill | template | 追齐领先信号：优先补 template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 成熟 19/20 | 1 | Software/wiki、DocCustomeranalysis、DocFilmCommunity | TRANSFER、governance、large-body、sensor、skill | template | 追齐领先信号：优先补 template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 成熟 19/19 | 0 | Software/wiki、DocCustomeranalysis、customeranalysis | TRANSFER、governance、large-body、sensor、skill | views | 互补优秀但不能标为领先：先补齐同技能全体工程的独特信号 views；覆盖证据信号并集后，才可重新评为领先。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 领先 12/12 | 0 | customeranalysis、17lang | body、governance、skill | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **客群 DB 读回**：`customeranalysis:.codex/context/harness-feedback-ledger.md`
- **问题聚焦式图文呈现**：`customeranalysis:.codex/skills/problem-focused-visual-presentation/SKILL.md`、`customeranalysis:views/lens-registry.md`
- **调研 / 研究能力**：`customeranalysis:.codex/skills/documentation-maintenance/SKILL.md`、`customeranalysis:.codex/skills/research-capability/SKILL.md`
- **知识关联**：`customeranalysis:.codex/skills/knowledge-linking/SKILL.md`
- **Issue / 事故分析**：`customeranalysis:.codex/skills/issue-analysis/SKILL.md`
- **复盘 / 回顾改进**：`customeranalysis:.codex/skills/historical-dialogue-retrospective/SKILL.md`
- **transferable skill governance**：`customeranalysis:.codex/skills/transferable-skill-governance/SKILL.md`
- **跨工程技能迁移提示词**：`customeranalysis:.codex/skills/cross-project-skill-adoption-prompt/SKILL.md`
- **Goal Contract / 长时任务完成契约**：`customeranalysis:.codex/context/agent-coordination.md`、`customeranalysis:.codex/context/customeranalysis-engineering-context.md`、`customeranalysis:.codex/context/general-skill-governance.md`、`customeranalysis:.codex/context/harness-evolution.md`、`customeranalysis:.codex/context/harness-feedback-ledger.md`
- **跨工程治理审计**：`customeranalysis:.codex/context/general-skill-governance.md`、`customeranalysis:.codex/context/harness-evolution.md`、`customeranalysis:.codex/context/harness-feedback-ledger.md`、`customeranalysis:.codex/skills/cross-project-governance-audit/SKILL.md`、`customeranalysis:.codex/skills/historical-dialogue-retrospective/SKILL.md`
- **文档与 Agent 规则维护**：`customeranalysis:.codex/context/agent-coordination.md`、`customeranalysis:.codex/skills/documentation-maintenance/SKILL.md`、`customeranalysis:AGENTS.md`、`customeranalysis:scripts/check_agent_harness.py`
- **项目上下文入口**：`customeranalysis:.codex/context/customeranalysis-engineering-context.md`、`customeranalysis:.codex/skills/customeranalysis-docs/SKILL.md`

## LifeOS

- **工程路径**：`/Users/hai/Documents/Life`
- **成熟概览**：领先 1；成熟 1；接入 2；局部 4；未见 7；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 未见 0/19 | 19 | Software/wiki、DocCustomeranalysis | 无 | TRANSFER、body、governance、large-body、sensor、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 未见 0/17 | 17 | Software/wiki、DocCustomeranalysis | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| transferable skill governance (`transferable-skill-governance`) | 通用 / 可迁移 | 未见 0/14 | 14 | DocCustomeranalysis、DocFilmCommunity、fetch-adapter | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 未见 0/14 | 14 | Software/wiki | 无 | TRANSFER、body、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 局部 1/19 | 18 | Software/wiki、DocCustomeranalysis、customeranalysis | small-body | TRANSFER、body、governance、large-body、sensor、skill、views | 追齐领先信号：优先补 TRANSFER, body, governance, large-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 局部 2/16 | 14 | Software/wiki、DocCustomeranalysis | governance | TRANSFER、body、skill、small-body、template | 追齐领先信号：优先补 TRANSFER, body, skill, small-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 局部 6/20 | 14 | Software/wiki、DocCustomeranalysis、DocFilmCommunity | governance、large-body、template | TRANSFER、sensor、skill | 追齐领先信号：优先补 TRANSFER, sensor, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 5/16 | 11 | DocCustomeranalysis | body、sensor | governance、large-body、skill | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 接入 10/21 | 11 | DocCustomeranalysis、DocFilmCommunity | goal-contract、governance、large-body、template | TRANSFER、skill | 追齐领先信号：优先补 TRANSFER, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 接入 8/16 | 8 | AcknowledgeBase、Software/wiki、DocCustomeranalysis | skill | TRANSFER、body、sensor、small-body、views | 追齐领先信号：优先补 TRANSFER, body, sensor, small-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 成熟 20/23 | 3 | DocCustomeranalysis | governance、large-body、sensor、skill、template、views | TRANSFER | 追齐领先信号：优先补 TRANSFER；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 领先 11/11 | 0 | LifeOS | governance、skill、small-body | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **文档与 Agent 规则维护**：`LifeOS:AGENTS.md`
- **Issue / 事故分析**：`LifeOS:rules/incident-lifecycle.md`
- **跨工程治理审计**：`LifeOS:.codex/context/governance-reference.md`、`LifeOS:.codex/skills/system-harness-review/SKILL.md`、`LifeOS:automation/scripts/check_harness_feedback_ledger.py`、`LifeOS:automation/scripts/check_life_governance_depth.py`、`LifeOS:logs/system/harness-feedback-ledger.md`
- **客群 DB 读回**：`LifeOS:automation/scripts/check_harness_feedback_ledger.py`、`LifeOS:logs/system/harness-feedback-ledger.md`
- **Goal Contract / 长时任务完成契约**：`LifeOS:.codex/context/governance-reference.md`、`LifeOS:.codex/context/lifeos-map.md`、`LifeOS:.codex/context/workflow-reference.md`、`LifeOS:.codex/skills/system-harness-review/SKILL.md`、`LifeOS:AGENTS.md`
- **复盘 / 回顾改进**：`LifeOS:.codex/skills/system-harness-review/SKILL.md`
- **问题聚焦式图文呈现**：`LifeOS:.codex/skills/problem-focused-lens/SKILL.md`、`LifeOS:automation/scripts/check_problem_focused_lens.py`、`LifeOS:rules/problem-focused-lens.md`、`LifeOS:templates/lens.md`、`LifeOS:views/current/a-b-moving-priority-lens.html`
- **生活系统管理**：`LifeOS:.codex/skills/inbox-triage/SKILL.md`、`LifeOS:.codex/skills/life-decision-review/SKILL.md`、`LifeOS:.codex/skills/life-matter-routing/SKILL.md`、`LifeOS:.codex/skills/weekly-review/SKILL.md`、`LifeOS:rules/life-matter-routing.md`

## DocERP

- **工程路径**：`/Users/hai/Documents/Code/DocERP`
- **成熟概览**：领先 0；成熟 0；接入 1；局部 4；未见 10；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 未见 0/23 | 23 | DocCustomeranalysis | 无 | TRANSFER、body、governance、large-body、sensor、skill、small-body、template、views | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 未见 0/21 | 21 | DocCustomeranalysis、DocFilmCommunity | 无 | TRANSFER、body、goal-contract、governance、large-body、skill、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 未见 0/17 | 17 | Software/wiki、DocCustomeranalysis | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 未见 0/16 | 16 | AcknowledgeBase、Software/wiki、DocCustomeranalysis | 无 | TRANSFER、body、sensor、skill、small-body、views | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| transferable skill governance (`transferable-skill-governance`) | 通用 / 可迁移 | 未见 0/14 | 14 | DocCustomeranalysis、DocFilmCommunity、fetch-adapter | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 未见 0/14 | 14 | Software/wiki | 无 | TRANSFER、body、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 局部 2/19 | 17 | Software/wiki、DocCustomeranalysis、customeranalysis | body | TRANSFER、governance、large-body、sensor、skill、views | 追齐领先信号：优先补 TRANSFER, governance, large-body, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 局部 2/19 | 17 | Software/wiki、DocCustomeranalysis | governance | TRANSFER、body、large-body、sensor、skill、small-body、template | 追齐领先信号：优先补 TRANSFER, body, large-body, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 局部 5/20 | 15 | Software/wiki、DocCustomeranalysis、DocFilmCommunity | governance、large-body | TRANSFER、sensor、skill、template | 追齐领先信号：优先补 TRANSFER, sensor, skill, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 3/16 | 13 | DocCustomeranalysis | governance、small-body | body、large-body、sensor、skill | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 接入 9/16 | 7 | Software/wiki、DocCustomeranalysis | skill、small-body | TRANSFER、body、governance、template | 追齐领先信号：优先补 TRANSFER, body, governance, template；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |

### 证据路径

- **文档与 Agent 规则维护**：`DocERP:AGENTS.md`
- **调研 / 研究能力**：`DocERP:governance/BRAIN.md`
- **跨工程治理审计**：`DocERP:governance/BRAIN.md`、`DocERP:governance/POLICY.md`、`DocERP:governance/README.md`、`DocERP:governance/WORKFLOW.md`、`DocERP:governance/log-writing-rules.md`
- **客群 DB 读回**：`DocERP:governance/template-feedback-rules.md`、`DocERP:projects/development/execution/engineering-feedback-loop.md`
- **Issue / 事故分析**：`DocERP:skills/issue-analysis/SKILL.md`

## H100

- **工程路径**：`/Users/hai/Documents/Software/H100`
- **成熟概览**：领先 0；成熟 0；接入 1；局部 4；未见 10；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 未见 0/21 | 21 | DocCustomeranalysis、DocFilmCommunity | 无 | TRANSFER、body、goal-contract、governance、large-body、skill、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 未见 0/17 | 17 | Software/wiki、DocCustomeranalysis | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 未见 0/16 | 16 | Software/wiki、DocCustomeranalysis | 无 | TRANSFER、body、governance、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 未见 0/16 | 16 | AcknowledgeBase、Software/wiki、DocCustomeranalysis | 无 | TRANSFER、body、sensor、skill、small-body、views | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| transferable skill governance (`transferable-skill-governance`) | 通用 / 可迁移 | 未见 0/14 | 14 | DocCustomeranalysis、DocFilmCommunity、fetch-adapter | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 未见 0/14 | 14 | Software/wiki | 无 | TRANSFER、body、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 未见 0/12 | 12 | customeranalysis、17lang | 无 | body、governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 局部 1/19 | 18 | Software/wiki、DocCustomeranalysis、customeranalysis | small-body | TRANSFER、body、governance、large-body、sensor、skill、views | 追齐领先信号：优先补 TRANSFER, body, governance, large-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 局部 3/20 | 17 | Software/wiki、DocCustomeranalysis、DocFilmCommunity | governance、small-body | TRANSFER、body、large-body、sensor、skill、template | 追齐领先信号：优先补 TRANSFER, body, large-body, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 局部 3/19 | 16 | Software/wiki、DocCustomeranalysis | governance、small-body | TRANSFER、body、large-body、sensor、skill、template | 追齐领先信号：优先补 TRANSFER, body, large-body, sensor；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 局部 2/16 | 14 | DocCustomeranalysis | governance | body、large-body、sensor、skill、small-body | 只抽象方法：补本工程自己的事实源、验收口径和检查脚本；不要复制源工程的业务表、路径、运行 ID 或 handoff。 |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 接入 9/23 | 14 | DocCustomeranalysis | skill、small-body | TRANSFER、body、governance、large-body、sensor、template、views | 追齐领先信号：优先补 TRANSFER, body, governance, large-body；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |

### 证据路径

- **文档与 Agent 规则维护**：`H100:AGENTS.md`
- **跨工程治理审计**：`H100:.codex/context/harness-feedback-ledger.md`、`H100:.codex/context/main-control-harness.md`
- **调研 / 研究能力**：`H100:.codex/context/main-control-harness.md`
- **客群 DB 读回**：`H100:.codex/context/harness-feedback-ledger.md`
- **问题聚焦式图文呈现**：`H100:.codex/skills/problem-focused-visual-presentation/SKILL.md`

## 17lang

- **工程路径**：`/Users/hai/Documents/Code/17lang`
- **成熟概览**：领先 1；成熟 0；接入 0；局部 1；未见 13；阻塞 0。

| 技能 / 能力 | 范围 | 当前 | 分差 | 对标 / 领先工程 | 已有信号 | 待补领先信号 | 建议修改方向 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| 问题聚焦式图文呈现 (`problem-focused-visual-presentation`) | 通用 / 可迁移 | 未见 0/23 | 23 | DocCustomeranalysis | 无 | TRANSFER、body、governance、large-body、sensor、skill、small-body、template、views | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程治理审计 (`cross-project-governance-audit`) | 通用 / 可迁移 | 未见 0/20 | 20 | Software/wiki、DocCustomeranalysis、DocFilmCommunity | 无 | TRANSFER、body、governance、large-body、sensor、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 文档与 Agent 规则维护 (`documentation-maintenance`) | 通用 / 可迁移 | 未见 0/19 | 19 | Software/wiki、DocCustomeranalysis、customeranalysis | 无 | TRANSFER、body、governance、large-body、sensor、skill、small-body、views | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 调研 / 研究能力 (`research-capability`) | 通用 / 可迁移 | 未见 0/19 | 19 | Software/wiki、DocCustomeranalysis | 无 | TRANSFER、body、governance、large-body、sensor、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 知识关联 (`knowledge-linking`) | 通用 / 可迁移 | 未见 0/17 | 17 | Software/wiki、DocCustomeranalysis | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Issue / 事故分析 (`issue-analysis`) | 通用 / 可迁移 | 未见 0/16 | 16 | Software/wiki、DocCustomeranalysis | 无 | TRANSFER、body、governance、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 复盘 / 回顾改进 (`retrospective-capability`) | 通用 / 可迁移 | 未见 0/16 | 16 | AcknowledgeBase、Software/wiki、DocCustomeranalysis | 无 | TRANSFER、body、sensor、skill、small-body、views | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 客群 DB 读回 (`customer-group-db-readback`) | 项目 / 领域绑定 | 未见 0/16 | 16 | DocCustomeranalysis | 无 | body、governance、large-body、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| transferable skill governance (`transferable-skill-governance`) | 通用 / 可迁移 | 未见 0/14 | 14 | DocCustomeranalysis、DocFilmCommunity、fetch-adapter | 无 | TRANSFER、governance、sensor、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 跨工程技能迁移提示词 (`cross-project-skill-adoption-prompt`) | 通用 / 可迁移 | 未见 0/14 | 14 | Software/wiki | 无 | TRANSFER、body、skill、small-body、template | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 生活系统管理 (`lifeos-management`) | 项目 / 领域绑定 | 未见 0/11 | 11 | LifeOS | 无 | governance、skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Backlog 批处理 (`backlog-management`) | 项目 / 领域绑定 | 未见 0/9 | 9 | fetch-adapter、prefect | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| 事项自动拆解 (`work-item-auto-decomposition`) | 项目 / 领域绑定 | 未见 0/9 | 9 | DocCustomeranalysis | 无 | skill、small-body | 先补入口：新增或对齐 SKILL.md / 治理页中的触发条件、事实源、输出格式和禁止项，再补可检测的 sensor 或示例产物。 |
| Goal Contract / 长时任务完成契约 (`goal-contract`) | 通用 / 可迁移 | 局部 4/21 | 17 | DocCustomeranalysis、DocFilmCommunity | body、governance | TRANSFER、goal-contract、large-body、skill、template | 追齐领先信号：优先补 TRANSFER, goal-contract, large-body, skill；若已具备能力但未被识别，把入口文件、TRANSFER、sensor 或 views 路径命名对齐。 |
| 项目上下文入口 (`project-context-entry`) | 项目 / 领域绑定 | 领先 12/12 | 0 | customeranalysis、17lang | body、governance、skill | 无 | 保持领先：继续把可复用增量沉淀到 TRANSFER / sensor / 示例产物，避免让一次性项目事实进入通用能力。 |

### 证据路径

- **Goal Contract / 长时任务完成契约**：`17lang:.codex/context/film-community-17lang-context.md`、`17lang:.codex/skills/film-community-docs/SKILL.md`、`17lang:docs/handoffs/README.md`
- **项目上下文入口**：`17lang:.codex/context/film-community-17lang-context.md`、`17lang:.codex/skills/film-community-docs/SKILL.md`
