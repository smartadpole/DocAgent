---
type: skill-transfer-manifest
id: MANIFEST-TRANSFERABLE-SKILL-2026-06-26-AGENT-EVIDENCE-V12
skill: transferable-skill-governance
status: active
source_of_truth: false
source_snapshot_generated_at: 2026-06-26 11:39
source_revision: 308bc64
scoring_schema_version: agent-evidence-v12
updated: 2026-07-20
tags: [skill-transfer, agent-system, conformance, matrix-adoption]
---

# AcknowledgeBase 通用 Agent 技能吸收清单

本清单记录本仓基于 AcknowledgeBase 2026-06-26 11:39 技能成熟度矩阵快照的 repo-native 吸收结果。它是 [[skills/transferable-skill-governance/SKILL]] 的证据清单，不替代 [[skills/README]]、各技能 `SKILL.md` / `TRANSFER.md`、治理页、模板、sensor、项目状态或验证报告。

## 源资料

- `$HOME/Documents/Docs/AcknowledgeBase/skills/README.md`
- `$HOME/Documents/Docs/AcknowledgeBase/skills/transferable-skill-governance/SKILL.md`
- `$HOME/Documents/Docs/AcknowledgeBase/skills/transferable-skill-governance/TRANSFER.md`
- `$HOME/Documents/Docs/AcknowledgeBase/skills/cross-project-skill-adoption-prompt/SKILL.md`
- `$HOME/Documents/Docs/AcknowledgeBase/skills/cross-project-skill-adoption-prompt/TRANSFER.md`
- `$HOME/Documents/Docs/AcknowledgeBase/templates/skill-transfer-manifest-template.md`
- `$HOME/Documents/Docs/AcknowledgeBase/views/current/governance/skill-maturity-matrix.data.json`
- `$HOME/Documents/Docs/AcknowledgeBase/views/current/governance/skill-maturity-diagnostics.md`

重点源能力：Goal Contract、Loop Engineering、复盘能力、documentation-maintenance、issue-analysis、topic-visual-presentation、public-html-publish、knowledge-linking、research-capability、cross-project-governance-audit、frontier-technology-intake。存在源 `TRANSFER.md` 的能力，以 `TRANSFER.md` 的迁移边界优先。

## 本仓吸收原则

- 可以吸收：触发条件、读取顺序、事实源分层、执行流程、输出格式、禁止项、验证口径、回写守卫和 sensor wiring。
- 只能抽象吸收：AcknowledgeBase 或下游工程的目录形态、脚本实现方式、历史样例、矩阵 marker、具体 host / prefix / profile 和一次性验收方式。
- 禁止复制：项目事实、业务名、服务名、数据库表、运行 ID、handoff、历史 log、密钥、环境配置、source revision 作为当前事实、以及为追分创建空 skill / 空模板 / 空 sensor。
- 处理动作：逐能力只使用 `recognize / complete / upgrade / merge / adapt / defer / reject`；`merge` 仅用于合并本仓已有等价能力或多个源工程的可复用切片，不用于混合项目事实。
- 验证边界：本清单和 sensor 只证明结构 wiring、入口可发现和分类裁决存在，不证明真实运行质量、审美质量、外部 evaluator readback 或业务验收通过。

## Project Conformance

| 字段 | 本仓声明 |
| --- | --- |
| `local_source_of_truth` | [[skills/README]] 是技能入口；各技能 `SKILL.md` 是执行源；同目录 `TRANSFER.md` 是迁移边界源；本清单记录矩阵吸收裁决；[[governance/README]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]] 是规则入口；`views/` 只承接持久呈现。 |
| `allowed_write_scope` | 本仓授权范围内可更新 `skills/`、`templates/`、`governance/`、`scripts/`、`views/`、`projects/` 和 [[log]]；外部项目事实、运行 ID、服务实例、handoff 和历史 log 不进入本仓通用事实。 |
| `required_profile` | 跨工程吸收先走 [[skills/transferable-skill-governance/SKILL]]；任务书生成走 [[skills/cross-project-skill-adoption-prompt/SKILL]]；长时任务走 [[skills/goal-contract/SKILL]]；持续循环走 [[skills/loop-engineering/SKILL]]；主题呈现和公开发布分别走 [[skills/topic-visual-presentation/SKILL]] 与 [[skills/public-html-publish/SKILL]]。 |
| `validation_command` | 本清单专项检查：`python3 scripts/check_all.py --only transferable-skill-baseline`；技能体系改动至少跑 `python3 scripts/check_all.py --only skill-maturity,research-capability,loop-engineering,public-html-publish,topic-visual-presentation,documentation-maintenance,cross-project-governance-audit,transferable-skill-baseline`；收尾跑完整 `python3 scripts/check_all.py` 和 `git diff --check`。 |
| `blocked_when_missing` | 缺目标结构自检、`TRANSFER.md`、owner 页面、专项 sensor、非默认 / 边界验证、人工确认边界、live readback 或外部 evaluator readback 时，只能写 `partial / blocked / review`，不能写完成、发布、验收或迁移闭环。 |
| `exceptions` | 简单问答、一次性小修、只读解释、无持久沉淀价值的临时判断不强套完整技能包；项目 / 领域绑定能力只抽象方法，不硬升通用 skill；sensor 只证明结构，不证明执行质量。 |

## 能力分类与处理

| 能力 | 类型 | 缺口类型 | 处理方式 | 本仓落位 | 剩余边界 |
| --- | --- | --- | --- | --- | --- |
| Goal Contract | baseline 候选 | recognition-gap + 局部 true-gap | complete | [[skills/goal-contract/SKILL]]、[[skills/goal-contract/TRANSFER]]、[[templates/goal-contract-template]]、[[agent-orchestration]] | 真实完成仍需任务自己的 code-level / business-flow / service-side / end-to-end / manual-confirmation 证据。 |
| Loop Engineering | baseline 候选 | recognition-gap | upgrade | [[skills/loop-engineering/SKILL]]、[[skills/loop-engineering/TRANSFER]]、[[templates/loop-contract-template]]、[[templates/run-capsule-template]]、[[loop-engineering]] | 本仓只声明控制面；写入型 loop、调度、合并、发布仍需授权和 evaluator。 |
| 复盘能力 | baseline 候选 | signal-only-gap | recognize | [[skills/retrospective-capability/SKILL]]、[[skills/delivery-retrospective/SKILL]]、[[skills/historical-dialogue-retrospective/SKILL]]、[[projects/retrospectives/README]] | 自动触发的 `no-op / 轻量 checkpoint` 不降级显式复盘请求；复盘不替代 Issue / 报告。 |
| Public HTML Publish | baseline 候选 | recognition-gap | complete | [[skills/public-html-publish/SKILL]]、[[skills/public-html-publish/TRANSFER]]、[[views/publication]]、`scripts/check_public_html_publish.py` | live 公开需 `--live` readback；静态检查通过不等于公网可访问。 |
| documentation-maintenance | transferable skill | recognition-gap | upgrade | [[skills/documentation-maintenance/SKILL]]、[[skills/documentation-maintenance/TRANSFER]]、[[documentation-maintenance-rules]]、`scripts/check_documentation_maintenance.py` | 文档同步检查不替代设计 owner 或项目验收。 |
| issue-analysis | transferable skill | signal-only-gap | recognize | [[skills/issue-analysis/SKILL]]、[[skills/issue-analysis/TRANSFER]]、[[issue-analysis-rules]]、[[templates/development-issue-template]] | Issue 分析只定位和分流；关闭仍由 Issue 档案、报告和验收证据裁决。 |
| topic-visual-presentation | transferable skill | recognition-gap + 局部 true-gap | complete | [[skills/topic-visual-presentation/SKILL]]、[[skills/topic-visual-presentation/TRANSFER]]、[[views/README]]、[[views/lens-registry]] | topic presentation 不替代事实源、验收关闭、Issue 关闭、决策拍板或报告；PDF / PNG 是派生导出。 |
| knowledge-linking | transferable skill | recognition-gap | recognize | [[skills/knowledge-linking/SKILL]]、[[skills/knowledge-linking/TRANSFER]]、[[knowledge-linking-rules]]、`scripts/check_knowledge_linking.py` | 链接质量仍需语义判断；sensor 只防孤岛和入口漏项。 |
| research-capability | transferable skill | true-gap | upgrade | [[skills/research-capability/SKILL]]、[[skills/research-capability/TRANSFER]]、[[templates/research-intake-template]]、[[research-capability-rules]] | 子项覆盖是成熟度信号；不把外部 13 个研究子项平铺成并列 skill。 |
| frontier-technology-intake | transferable 子项 | true-gap | adapt | 作为 research-capability 的 Frontier Tech Intake / Research Intake 子项和模板字段吸收 | 不新增并列通用 skill；不绕过平台访问、版权、隐私和人工确认边界。 |
| cross-project-governance-audit | transferable skill | recognition-gap | upgrade | [[skills/cross-project-governance-audit/SKILL]]、[[skills/cross-project-governance-audit/TRANSFER]]、[[templates/cross-project-governance-audit-contract-template]] | `handoff-ready` 不代表目标工程已修复、已提交或已验证；审计报告无 runtime validation。 |
| cross-project-skill-adoption-prompt | transferable skill | recognition-gap | upgrade | [[skills/cross-project-skill-adoption-prompt/SKILL]]、[[skills/cross-project-skill-adoption-prompt/TRANSFER]]、[[templates/skill-transfer-manifest-template]] | 任务书生成不等于目标工程已执行；外部 evaluator 需要 readback 或 blocked reason。 |
| transferable-skill-governance | transferable skill | recognition-gap | complete | [[skills/transferable-skill-governance/SKILL]]、[[skills/transferable-skill-governance/TRANSFER]]、本清单、`scripts/check_transferable_skill_baseline.py` | 本清单不替代后续每次迁移的 source-depth 和目标工程自检。 |
| Agent System Capability Package | system capability | true-gap + recognition-gap | complete | [[agent-system-maturity]]、`governance/agent-system-maturity-snapshot.v1.json`、`scripts/check_agent_system_maturity.py` | 当前 intelligence evidence 仍为 `insufficient-evidence`；skill maturity 不能上推为整体智能化分。 |
| work-item-auto-decomposition | project-bound | true-gap | adapt | [[skills/work-item-auto-decomposition/SKILL]]，绑定本仓 `Gate -> FP -> EP -> TASK` 模型 | `transfer_ready: false`；不作为所有工程通用 skill。 |
| project-context-entry | project-bound | 不适用 | reject / adapt | 只抽象上下文入口、读序和 handoff 边界到相关治理规则 | 不复制目标工程上下文入口或本地 handoff 结构。 |
| customer-group-db-readback | project-bound | 不适用 | reject / adapt | 只抽象“真实写入需 DB / service-side readback”方法 | 不复制业务表、运行 ID、服务名或云 DB 事实。 |
| backlog-management | project-bound | 不适用 | reject / adapt | 只抽象批处理、去重、状态分流和人工 review 方法 | 不把开源仓 backlog 队列变成本仓通用事实。 |
| lifeos-management | project-bound | 不适用 | reject / adapt | 只抽象生活系统 inbox / review / memory routing 方法 | 不复制个人生活事实、周报状态或 LifeOS 目录。 |
| performance-bandwidth-analysis / runtime-config-switch / procurement 类能力 | mixed | 待目标触发 | defer / adapt | 暂不新增通用 skill；后续若本仓出现稳定高频触发，再按 true-gap 自检 | 当前只保留为矩阵线索，不创建空能力。 |

## 验证与回看

- 本清单结构：`python3 scripts/check_all.py --only transferable-skill-baseline`
- 相关技能束：`python3 scripts/check_all.py --only skill-maturity,research-capability,loop-engineering,public-html-publish,topic-visual-presentation,documentation-maintenance,cross-project-governance-audit,agent-system-maturity`
- 收尾总门禁：`python3 scripts/check_all.py`
- 空白 / whitespace：`git diff --check`

## 未验证边界

- 本轮不刷新 AcknowledgeBase 上游矩阵，不声称外部 evaluator 已读回本仓最新工作树。
- 本轮不证明未来每次 Goal、Loop、复盘、调研、图文 lens 或公开发布都达到真实 L5；只证明本仓 repo-native 入口、迁移边界、模板和 sensor wiring。
- 本轮不把 public HTML 静态检查上推为公网 live 发布；live 仍需 `python3 scripts/check_public_html_publish.py --live`。
- 本轮不关闭任何 Gate / FP / EP / TASK / Issue，不改变项目阶段。

## 人工确认事项

- 是否把 Goal Contract、Loop Engineering、复盘和 Public HTML Publish 进一步提升为跨工作区 Universal Harness Baseline，需要系统级 owner 裁决；本仓只保留 conformance。
- 是否为 performance-bandwidth-analysis、runtime-config-switch 这类 mixed general 能力建立本仓通用 skill，需要等本仓出现稳定高频触发或用户明确要求。
- 外部矩阵的最新分数、hit window、动态 markers 和 source revision 只能由 AcknowledgeBase Orchestrator 刷新后确认。
