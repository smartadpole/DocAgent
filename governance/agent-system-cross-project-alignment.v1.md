---
type: governance
id: GOV-AGENT-SYSTEM-CROSS-PROJECT-ALIGNMENT-001
scope: shared
status: active
source_of_truth: true
updated: 2026-07-06
tags: [governance, agent-system, cross-project, intelligence, harness, memory, workflow]
---

# Cross-Project Agent Intelligence Alignment Map

主入口：[[agent-system-maturity]]

相关：[[acknowledgebase-topic-system-adoption.v1]]、[[skills/transferable-skill-governance/SKILL]]、[[skills/cross-project-governance-audit/SKILL]]、[[agent-orchestration]]、[[harness-evolution]]、[[harness-feedback-ledger]]

## 定位

这页承接“借鉴所有工程的智能化能力”这类跨工程吸收任务。它把 AcknowledgeBase、train_platform、H100、DocCustomeranalysis、DocFilmCommunity、LifeOS 等工程里已经出现的 agent、harness、memory、workflow、evaluation 和 migration 能力，抽象成当前 wiki 的 repo-native 对齐图。

本页不复制源工程目录、项目事实、运行 ID、服务名、端口、矩阵分数、历史 log 或一次性 handoff。它只吸收系统层信息：触发条件、事实源分层、执行合同、记忆路由、评估口径、回写守卫、sensor 和不上推边界。

2026-07-23 起，本页还承接 AcknowledgeBase topic 到 wiki 本地系统层的吸收图：总览入口是 [[projects/design/topics/implementation-engineering-template-system]] 与 [[projects/design/topics/agent-workflow-memory-harness-skill-landing]]；逐 source topic 的 ability adoption 清单和系统落点以 [[acknowledgebase-topic-system-adoption.v1]] 为准。该 manifest 用来证明 source topic 已落实到 agent、workflow、memory、harness、skill、topic、evaluation、governance、template 和 migration 层，而不是只复制文档。

## Source Coverage

| Source | Read depth | Reusable signal | Boundary |
| --- | --- | --- | --- |
| AcknowledgeBase | design topic + matrix / migration concept | 七层 Agent System 对象、per-dialogue / run trace、三层迁移验收、`structure-only` 与 `insufficient-evidence` 边界 | 不复制当前分数、profile hash、项目事实或 source layout。 |
| AcknowledgeBase design topics | source topic manifest | 所有 source topic 按 ability adoption 落到 wiki agent / workflow / memory / harness / skill / evaluation / governance / template / topic / migration owner | 逐 topic 覆盖只证明结构接线，不证明行为智能评分。 |
| train_platform | owner docs + memory / harness + checker | Agent System Capability Package、source freshness、alignment map、evaluation correction closeout、Agent Memory Contract | 不复制 dataset、benchmark、运行状态或工程内记录。 |
| H100 | `.codex/governance` + AGENTS | L5 blocked-boundary proof、Run Capsule、Loop Contract、Subproject Git Preflight、final reply contract | 不复制远程机器事实、任务状态或 handoff 路径。 |
| DocCustomeranalysis | AGENTS + issue / work-item / lens / publication skills | 主控治理、Issue 案件链、work-item 拆解、service registry、delivery bundle、public profile live readback | 不复制客户分析业务链路、服务实例、数据库或发布 URL。 |
| DocFilmCommunity | AGENTS + frontier intake skill | Frontier Technology Intake、Intelligence Contract、parser / evaluator / A3 compensation、knowledge landing | 不复制影像社区业务事实或候选技术结论。 |
| LifeOS | AGENTS + presentation / publication profiles, partial read | owner-first personal memory、domain routing、public / lens 边界 | 只作为记忆路由信号；未作为直接 adoption 证据。 |
| OpsMind / fetch-adapter / prefect / haimind / customeranalysis | AGENTS or memory-index signal, partial source pack | workstation / remote-control / cross-project audit / runtime ledger 候选信号 | 本轮未深读到可直接落地的独立 owner，先保持 candidate。 |

## Seven-Layer Absorption Matrix

| Layer | Cross-project capability | Wiki owner / landing | Adoption decision |
| --- | --- | --- | --- |
| skill | 技能不是孤立 `SKILL.md`，必须有 trigger、fact source、output、writeback guard、TRANSFER 或不可迁移边界 | [[skills/README]]、[[skills/transferable-skill-governance/SKILL]] | recognize + continue existing owner |
| runtime | 工具 / 浏览器 / 服务 / 远程状态必须有 profile、readback、blocked reason 和权限判断 | `AGENTS.md`、[[state-constraint-reasoning]]、[[projects/service-registry]] | adapt where runtime is actually used |
| harness | response mode、Goal、Run Capsule、Loop、Subproject Git Preflight、Orchestrator / Worker / Evaluator、closeout proof | [[response-mode-routing]]、[[agent-orchestration]]、[[skills/goal-contract/SKILL]]、[[skills/loop-engineering/SKILL]] | complete through owner links |
| memory | entry memory、current project state、conversation trace、stable governance context、reusable method memory、evidence memory、learning memory | [[BRAIN]]、[[projects/memory/README]]、[[projects/trace]]、[[log]]、[[harness-feedback-ledger]] | upgrade routing language only |
| evaluation | checker、source freshness、negative evidence、L5 blocked-boundary proof、runtime / outcome / synthesis snapshot | `scripts/check_all.py`、`scripts/check_agent_system_maturity.py`、[[projects/development/reports/README]] | upgrade local structural sensor |
| governance | 用户纠偏、检查失败、重复失守和模式切换先形成 episode，再晋升模板 / sensor / skill / rule | [[harness-evolution]]、[[harness-feedback-ledger]]、[[instruction-adherence]] | recognize existing path |
| migration | Agent System Capability Package、target self-check、project conformance、security boundary、rollback / defer | [[agent-system-maturity]]、[[skills/cross-project-skill-adoption-prompt/SKILL]]、skill transfer templates | complete cross-project alignment map |
| implementation-template | 主控 / 子工程 / runtime service / data-model / documentation-governance 的工程画像、控制面和证据合同 | [[projects/design/topics/implementation-engineering-template-system]]、[[templates/implementation-project-profile-template]] | complete local implementation template owner |
| topic-landing | AcknowledgeBase topic 中已覆盖方案按 wiki 系统层吸收，不复制原目录 | [[projects/design/topics/agent-workflow-memory-harness-skill-landing]]、[[acknowledgebase-topic-system-adoption.v1]] | complete source topic adoption manifest |

## Adoption Decisions

| Candidate | Gap type | Decision | Landing / guard |
| --- | --- | --- | --- |
| Cross-project agent intelligence alignment map | true-gap | complete | 本页作为 [[agent-system-maturity]] 的 source pack 和 decision record。 |
| AcknowledgeBase topic landing into wiki systems | true-gap | complete | 使用 [[acknowledgebase-topic-system-adoption.v1]] 逐 source topic 映射到 agent / workflow / memory / harness / skill / evaluation / governance / template / topic / migration 层；[[projects/design/topics/agent-workflow-memory-harness-skill-landing]] 只保留摘要矩阵。 |
| Implementation engineering template system | true-gap | complete | 使用 [[projects/design/topics/implementation-engineering-template-system]] 和 [[templates/implementation-project-profile-template]] 承接所有实现类工程合集与模板目标。 |
| source freshness policy | recognition-gap | adapt | 在本页、snapshot 和 checker 中记录 source coverage；不伪造外部 freshness hash。 |
| per-dialogue / run trace | true-gap | defer runtime implementation | 先承认为 intelligence evidence 缺口；没有行为语料时保持 `insufficient-evidence`。 |
| evaluation correction closeout | true-gap-lite | adapt | 作为报告和 future sensor 候选；不把 train_platform 的具体 evaluation records 搬入本仓。 |
| L5 blocked-boundary proof | recognition-gap | recognize + adapt | 继续由 [[agent-orchestration]]、[[state-constraint-reasoning]] 和报告口径承接；checker 只验证关键术语可发现。 |
| public / lens delivery bundle | recognition-gap | recognize | 本仓已有 [[skills/problem-focused-visual-presentation/SKILL]] 和 [[views/README]]；DocCustomeranalysis 只作为信号。 |
| Frontier Technology Intake Intelligence Contract | signal-only-gap | recognize | 已由 research intake / research-capability 承接；不新增并列研究技能。 |
| source project facts, run IDs, secrets, ports, current scores | not reusable | reject | 任何目标工程事实不得写成本仓通用规则或 maturity 证据。 |

## Current Wiki Upgrade

本轮只做结构吸收和可检查接线：

- [[agent-system-maturity]] 增加本页作为 cross-project source pack。
- `governance/agent-system-maturity-snapshot.v1.json` 更新 proof、evidence corpus 和 blind spot，仍保持 `agent_intelligence_score: null`。
- `scripts/check_agent_system_maturity.py` 检查本页、entrypoint、source coverage 和 Goodhart boundary。
- [[projects/development/reports/2026-07-06-cross-project-agent-intelligence-absorption]] 记录验证对象、测试命令和不上推边界。

## Evidence Boundary

- `structure-only`：本轮证明当前 wiki 已有跨工程智能化能力吸收的 owner、source pack、checker 和报告，不证明未来每轮 agent 行为已经更聪明。
- `insufficient-evidence`：没有采集 rubric-backed 正负行为语料、per-dialogue / run trace 或外部 evaluator readback 时，智能化维度继续保持未评分。
- `not copied`：源工程的项目事实、服务状态、业务对象、路径、运行记录和矩阵分数不进入本仓。
- `blocked-by-orchestrator-readback`：外部矩阵刷新仍由主控执行；本仓只提供可读 capsule、expected impact 和本地验证证据。

## Future Evaluation Hooks

后续若要把这页从结构对齐推进到行为智能验证，必须另起 evidence collection：

1. 抽样历史对话和工具调用，形成 positive / negative behavior corpus。
2. 按八维 intelligence lens 打分，并记录 evaluator provenance。
3. 对 source freshness、L5 blocked-boundary proof、per-dialogue / run trace 和 correction closeout 做正反样本。
4. 只有外部 readback 或本地 evaluator 评分真实完成后，才允许调整 `agent_intelligence_score`。
