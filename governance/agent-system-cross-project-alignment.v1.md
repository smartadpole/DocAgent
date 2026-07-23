---
type: governance
id: GOV-AGENT-SYSTEM-CROSS-PROJECT-ALIGNMENT-001
scope: shared
status: active
source_of_truth: true
updated: 2026-07-23
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
| DocCustomeranalysis | AGENTS + governance / skills / templates / checker inventory, 2026-07-23 refresh | 主控治理、Issue 案件链、work-item 拆解、service registry、delivery bundle、public profile live readback、Goal / Loop 长任务编排、agent-finalizer、external-write-boundary、acceptance-governance、long-task-progress、performance-bandwidth-analysis、runtime-config-switch、production readback | 不复制客户分析业务链路、149 / 141 服务实例、数据库表、运行 ID、发布 URL、Prefect 当前状态、DB readback 业务 skill 或项目专属 owner gate。 |
| DocFilmCommunity | AGENTS + frontier intake skill | Frontier Technology Intake、Intelligence Contract、parser / evaluator / A3 compensation、knowledge landing | 不复制影像社区业务事实或候选技术结论。 |
| LifeOS | AGENTS + presentation / publication profiles, partial read | owner-first personal memory、domain routing、public / lens 边界 | 只作为记忆路由信号；未作为直接 adoption 证据。 |
| OpsMind | AGENTS + governance / skills / checker inventory | workstation / remote-control、第三方工程摄入边界、repo-native skill package、browser / runtime profile readback、visual delivery verification | 不复制本机皮肤路径、远程控制会话、插件资产或一次性性能样例。 |
| fetch-adapter / prefect / customeranalysis / H100 / haimind / store_stream_download / data_analysis | registered project inventory + AGENTS / local checker signal | 子工程 Git preflight、runtime service readback、conformance profile、implementation evidence、narrow repo-local sensor 的实现类工程信号 | 只吸收工程类型、证据合同和不上推边界；不把这些仓库的当前服务状态、数据根、脚本参数或部署事实写成本仓通用默认。 |

## 2026-07-23 Registered Project Refresh

本轮按 AcknowledgeBase registry 覆盖的 14 个工程做能力盘点。结论不是“所有能力已完全吸收”，而是：

| Project group | Current judgment | Wiki action |
| --- | --- | --- |
| AcknowledgeBase | 上游 topic / skill / template / harness / research owner 最完整，是系统层方案来源。 | 继续通过 [[acknowledgebase-topic-system-adoption.v1]] 和本页证明 topic 到 wiki owner 的结构吸收；本机存在 AcknowledgeBase 时，相关 topic 必须 `updated` 才算闭环。 |
| Software/wiki | 已有实现类工程模板、跨工程对齐图、agent-system maturity、harness / instruction / execution-contract / research / lens / public / testing sensors。 | 本轮补齐 source freshness 和 DocCustomeranalysis 后发升级的显式裁决。 |
| DocCustomeranalysis | 近期升级明显超过本页旧摘要：控制面已经覆盖 Goal / Loop 长任务编排、Run Capsule / dispatch、agent-finalizer、external-write-boundary、acceptance-governance、long-task-progress、issue070-owner-gate、module-regression-guards、prefect-concurrency-drift，以及 performance / runtime-config / DB readback 专项技能。 | `upgrade + adapt`：吸收“证据分层、长任务控制面、finalizer 范围证明、外部写边界、验收治理、runtime 配置切换、性能流水账、生产 readback”的系统层合同；DB readback 只保留证据分层，不新增通用业务 skill。 |
| DocFilmCommunity / OpsMind | 已有 repo-native skill、frontier / visual / runtime / third-party boundary 等强信号。 | `recognize`：继续作为研究、视觉交付、第三方摄入和 runtime readback 的源信号；若 wiki 出现同类高频任务再 `upgrade` 为本地 skill / sensor。 |
| LifeOS | owner-first memory、domain routing、lens / publication 表达强，主要是个人知识工程。 | `adapt`：吸收 owner-first 路由和呈现边界；不把生活域任务事实写入实现类工程模板。 |
| fetch-adapter / train_platform / prefect / customeranalysis / H100 / haimind / store_stream_download / data_analysis | 主要提供子工程、runtime、数据 / 模型、服务台账、生产 readback、窄 sensor 的 implementation evidence。 | `recognize`：作为实现类工程 profile 的工程类型和证据合同样例；具体脚本、参数、服务状态和数据事实留在各自仓库。 |

## DocCustomeranalysis Delta Decision

| Capability from DocCustomeranalysis | Gap type | Decision | Wiki landing / guard |
| --- | --- | --- | --- |
| Goal / Loop 长任务编排、Run Capsule、subproject dispatch、Evaluator | recognition-gap | complete through existing owner | 由 [[agent-orchestration]]、[[skills/goal-contract/SKILL]] 和 [[skills/loop-engineering/SKILL]] 承接；本页补 source freshness，不复制 ISSUE-070 / TASK-152 状态。 |
| `agent-finalizer` 的 scoped commit / dirty residual / post-write proof | true-gap | upgrade | 进入 [[agent-orchestration#Production-Grade Control Plane Hardening]] 和 `agent-control-plane-hardening` sensor；本仓只规定范围证明、预存 dirty 分类、post-write check 和最终状态读回，不复制脚本路径。 |
| `external-write-boundary` | recognition-gap + true-gap-lite | upgrade | 进入 [[agent-orchestration#Production-Grade Control Plane Hardening]]；与 AcknowledgeBase topic updated 规则、Subproject Git Preflight 和上游写入授权门共同承接。 |
| `acceptance-governance` / `long-task-progress` | true-gap | upgrade | 进入 [[agent-orchestration#Production-Grade Control Plane Hardening]]；补长 Goal / Loop 的 current_slice、blocked_for_done、not_blocked_for_implementation、monitoring policy 和验收上推边界。 |
| `performance-bandwidth-analysis` | mixed general | complete | 新增 [[skills/performance-bandwidth-analysis/SKILL]] 和 [[skills/performance-bandwidth-analysis/TRANSFER]]；吸收 timing ledger、coverage matrix、分层证据、非单点指标和生产容量不上推边界。 |
| `runtime-config-switch` | mixed general | complete | 新增 [[skills/runtime-config-switch/SKILL]] 和 [[skills/runtime-config-switch/TRANSFER]]；吸收 live service config readback、service-registry 回写、smoke / cleanup / rollback 合同。 |
| `customer-group-db-readback` | project-bound | reject / adapt | 不迁移业务表、账号、DSN 或批次前缀；只保留“receipt、ingress、DB / service-side readback 不能互相替代”的通用证据分层。 |
| `issue070-owner-gate`、`module-regression-guards`、`prefect-concurrency-drift` | project-specific | defer / signal-only | 作为 narrow sensor 设计范例保留；不变成 wiki 默认门禁，除非本仓出现同名 owner 或同类执行合同。 |

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
| DocCustomeranalysis long-task control plane | true-gap | upgrade | 通用合同落到 [[agent-orchestration#Production-Grade Control Plane Hardening]]、[[skills/performance-bandwidth-analysis/SKILL]]、[[skills/runtime-config-switch/SKILL]] 和 `agent-control-plane-hardening` sensor。 |
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
