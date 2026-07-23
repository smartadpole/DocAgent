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

这页承接“借鉴所有工程的智能化能力”这类跨工程吸收任务。它把上游知识治理库、主控工程、子工程、运行服务、数据 / 模型工程、知识库工程和运维 agent 中已经出现的 agent、harness、memory、workflow、evaluation 和 migration 能力，抽象成当前 wiki 的 repo-native 对齐图。

本页不复制源工程目录、项目事实、运行 ID、服务名、端口、矩阵分数、历史 log 或一次性 handoff。它只吸收系统层信息：触发条件、事实源分层、执行合同、记忆路由、评估口径、回写守卫、sensor 和不上推边界。

2026-07-23 起，本页还承接上游 topic 到 wiki 本地系统层的吸收图：总览入口是 [[projects/design/topics/implementation-engineering-template-system]] 与 [[projects/design/topics/agent-workflow-memory-harness-skill-landing]]；逐 source topic 的 ability adoption 清单和系统落点以 [[acknowledgebase-topic-system-adoption.v1]] 为准。该 manifest 用来证明 source topic 已落实到 agent、workflow、memory、harness、skill、topic、evaluation、governance、template 和 migration 层，而不是只复制文档。

## Source Coverage

本页的“全工程”口径以内部 source registry 当前登记集合为准。能力扫描可以额外发现本机目录信号，但闭环判断不能把“本地扫到路径”混成“登记工程”；也不能只挑一个最强样本就回答“所有工程已吸收”。作为对外模板工程，wiki 正文只暴露工程角色、能力包和证据边界；具体 source project 名称留在上游 registry、内部审计证据或历史 log，不进入模板概念层。

| Source archetype | Read depth | Reusable signal | Boundary |
| --- | --- | --- | --- |
| upstream knowledge-governance base | design topic + matrix / migration concept | 七层 Agent System 对象、per-dialogue / run trace、三层迁移验收、`structure-only` 与 `insufficient-evidence` 边界 | 不复制当前分数、profile hash、项目事实、source layout 或内部项目名。 |
| upstream source topics | source topic manifest | 所有 source topic 按 ability adoption 落到 wiki agent / workflow / memory / harness / skill / evaluation / governance / template / topic / migration owner | 逐 topic 覆盖只证明结构接线，不证明行为智能评分。 |
| controller / main-control project | AGENTS + governance / skills / templates / checker inventory | 主控治理、Issue 案件链、work-item 拆解、service registry、delivery bundle、Goal / Loop 长任务编排、agent-finalizer、external-write-boundary、acceptance-governance、long-task-progress、production readback | 不复制业务链路、服务实例、数据库表、运行 ID、发布 URL、当前调度状态、业务 readback skill 或项目专属 owner gate。 |
| subproject / implementation repo | AGENTS + local checker signal | Subproject Git Preflight、allowed writes、handoff、module regression guard、runtime service readback、narrow repo-local sensor | 只吸收工程类型、证据合同和不上推边界；不把当前服务状态、数据根、脚本参数或部署事实写成本仓通用默认。 |
| runtime-service / ops-agent | AGENTS + governance / skills / checker inventory | `local-operations-diagnostics`、第三方工程 / 外部依赖 source metadata、browser / runtime profile live readback、visual delivery verification、remote-control 边界 | 不复制本机工具路径、远程控制会话、插件资产、机器、端口或一次性性能样例。 |
| data-model / evaluation project | owner docs + memory / harness + checker | Agent System Capability Package、source freshness、evaluation-scheme-design、formal evaluation vs release separation、experiment sweep governance、review app live-link smoke | 不复制 dataset、benchmark、checkpoint、模型、运行状态或工程内记录。 |
| knowledge-base / domain-governance project | AGENTS + domain / lens / harness profiles | owner-first memory、domain routing、domain-bound skill、problem-focused-lens、publication boundary、L5 closeout proof | 只吸收 owner-first 和领域路由方法；不把领域事实写成实现类工程默认。 |
| lightweight repo | minimal AGENTS + conformance / validation signal | minimum viable governance profile、project conformance、Persistence Decision、dirty / local-only boundary | 不强行引入厚治理结构；不覆盖预存业务配置或本地运行事实。 |

## 2026-07-23 Registered Source Archetype Capability Absorption

本轮按内部 source registry 覆盖登记工程，但在 wiki 对外模板层只落成 source archetype 和 capability pack。结论不是“所有项目事实都进入 wiki”，而是每类工程的可复用 agent 治理层能力都有 `recognize / complete / upgrade / adapt / defer / reject` 裁决，并写清本仓 owner / sensor / 不上推边界。

| Source archetype | System-layer capability to absorb | Decision | Wiki landing / guard |
| --- | --- | --- | --- |
| upstream knowledge-governance base | topic owner、过程方案沉淀、研究技能族、skill maturity / dynamic benchmark、cross-repository governance acceptance、`acknowledge_topic_update_required` | complete | [[acknowledgebase-topic-system-adoption.v1]]、[[wiki-governance-system-contract.v1]]、[[agent-system-maturity]] 和本页承接；闭环必须有上游 topic `updated`。 |
| template source project | 实现类工程合集与模板、agent system maturity、implementation project profile、topic-to-owner adoption、本仓治理 system contract | complete | [[projects/design/topics/implementation-engineering-template-system]]、[[templates/implementation-project-profile-template]]、[[wiki-governance-system-contract.v1]]；本仓是模板源，不把自身当前状态伪装成目标工程采纳。 |
| ops-agent / workstation engineering project | `local-operations-diagnostics`、第三方工程 / 外部依赖 source metadata、browser / runtime profile live readback、visual delivery verification、remote-control 边界 | recognize / adapt | 第三方摄入边界已进上游 topic；wiki 侧以 [[skills/research-capability/SKILL]]、[[state-constraint-reasoning]]、[[skills/problem-focused-visual-presentation/SKILL]] 承接，不复制本机工具路径和外部资产。 |
| controller / production control-plane project | Goal / Loop 长任务控制面、Run Capsule dispatch、agent-finalizer、external-write-boundary、acceptance-governance、long-task-progress、production readback、performance-bandwidth-analysis、runtime-config-switch、DB / receipt / ingress readback 分层 | upgrade / complete / adapt | [[agent-orchestration#Production-Grade Control Plane Hardening]]、[[skills/performance-bandwidth-analysis/SKILL]]、[[skills/runtime-config-switch/SKILL]] 和 `agent-control-plane-hardening` sensor；DB readback 不新增通用业务 skill。 |
| frontier / product intelligence controller | problem-focused visual presentation、frontier technology intake、Goal / Run / Loop / evaluator、A3 compensation、knowledge landing | recognize / adapt | 继续由 [[skills/problem-focused-visual-presentation/SKILL]]、[[skills/research-capability/SKILL]]、[[agent-orchestration]] 承接；不复制领域业务事实、候选技术结论或专项内容库。 |
| knowledge-base / domain-governance project | owner-first memory、domain routing、domain-bound decision review、problem-focused-lens、weekly / system harness review、L5 closeout proof | adapt | 吸收 owner-first 路由、领域绑定能力不上推、lens / publication 证据边界；不把领域事实、建议或计划变成软件模板事实。 |
| data ingestion / adapter repo | consumer-path smoke、service-side backend switch、source mapping preflight、runtime switch evidence | recognize / adapt | 作为 [[skills/runtime-config-switch/SKILL]] 和实现类工程 `evidence_contract` 的样例；不复制数据源、服务 URL、脚本参数或 pipeline 事实。 |
| data-model / evaluation platform | evaluation-scheme-design、source freshness、formal evaluation vs release separation、review app live link smoke、experiment sweep governance | recognize / adapt | 进入 [[agent-system-maturity]] 的 evaluation / source freshness 边界和 implementation profile 的 evidence contract；不复制数据集、checkpoint、模型、benchmark 或训练运行事实。 |
| scheduler / orchestration runtime | read-only preflight、真实操作优先于 mock、polling 而非同步断言、admission / lease / heartbeat、staged validation rollback、runtime config 切换 | recognize / adapt | 作为 [[agent-orchestration]] 的 scheduler / service orchestration invariant 和 [[state-constraint-reasoning]] 的可执行性门；不复制调度框架内部实现、部署状态或并发参数。 |
| service repo with generated agent adapters | 根 AGENTS 与 tool-specific thin adapter 边界、modular source rules、generated agent entry、service-side / end-to-end evidence boundary、read / write path fix preference | recognize / adapt | 吸收“agent 规则单一正文 + thin adapter / generated guard”模式到入口治理判断；不复制服务业务、环境、规则源码路径或生产数据。 |
| model-serving / hardware-runtime project | L5 blocked-boundary proof、hardware / runtime / router preflight、implementation vs acceptance ownership split、live readback appendix、Persistence Decision | recognize / adapt | 进入 [[agent-orchestration]]、[[state-constraint-reasoning]] 和 [[agent-system-maturity]] 的 runtime-proof ladder；不复制机器、硬件、模型、端口或远程会话事实。 |
| AI application / managed service repo | local governance conformance、agent-harness-conformance、runtime service facts local、public URL claims require live public readback、latency / service ledger 边界 | recognize / adapt | 吸收 conformance profile 与 service-registry / public readback 分层；不复制具体服务、地址、运行 ledger 或模型配置事实。 |
| lightweight code repo | 轻量代码仓最小 AGENTS、project conformance、Persistence Decision、运行验证本地化 | recognize | 作为 minimum viable governance profile：轻量仓也要有入口、conformance、validation 和 persistence 决策；不新增厚治理结构。 |
| lightweight data-analysis repo | 轻量代码仓最小 AGENTS、预存业务配置改动避让、project conformance、Persistence Decision | recognize | 同 lightweight code repo；额外吸收 dirty / local-only 边界，不能为治理整改覆盖业务配置。 |

工程能力覆盖集可以小于内部 source registry 全集，例如某个 publication、research profile、skill maturity 或治理优先级只覆盖部分工程；但当用户问“所有工程是否吸收”时，必须回到 registry 全集逐行审计，再在 wiki 中输出为匿名 archetype / capability pack。

## Production Control-Plane Delta Decision

| Capability from production control-plane source | Gap type | Decision | Wiki landing / guard |
| --- | --- | --- | --- |
| Goal / Loop 长任务编排、Run Capsule、subproject dispatch、Evaluator | recognition-gap | complete through existing owner | 由 [[agent-orchestration]]、[[skills/goal-contract/SKILL]] 和 [[skills/loop-engineering/SKILL]] 承接；本页补 source freshness，不复制 ISSUE-070 / TASK-152 状态。 |
| `agent-finalizer` 的 scoped commit / dirty residual / post-write proof | true-gap | upgrade | 进入 [[agent-orchestration#Production-Grade Control Plane Hardening]] 和 `agent-control-plane-hardening` sensor；本仓只规定范围证明、预存 dirty 分类、post-write check 和最终状态读回，不复制脚本路径。 |
| `external-write-boundary` | recognition-gap + true-gap-lite | upgrade | 进入 [[agent-orchestration#Production-Grade Control Plane Hardening]]；与 AcknowledgeBase topic updated 规则、Subproject Git Preflight 和上游写入授权门共同承接。 |
| `acceptance-governance` / `long-task-progress` | true-gap | upgrade | 进入 [[agent-orchestration#Production-Grade Control Plane Hardening]]；补长 Goal / Loop 的 current_slice、blocked_for_done、not_blocked_for_implementation、monitoring policy 和验收上推边界。 |
| `performance-bandwidth-analysis` | mixed general | complete | 新增 [[skills/performance-bandwidth-analysis/SKILL]] 和 [[skills/performance-bandwidth-analysis/TRANSFER]]；吸收 timing ledger、coverage matrix、分层证据、非单点指标和生产容量不上推边界。 |
| `runtime-config-switch` | mixed general | complete | 新增 [[skills/runtime-config-switch/SKILL]] 和 [[skills/runtime-config-switch/TRANSFER]]；吸收 live service config readback、service-registry 回写、smoke / cleanup / rollback 合同。 |
| `customer-group-db-readback` | project-bound | reject / adapt | 不迁移业务表、账号、DSN 或批次前缀；只保留“receipt、ingress、DB / service-side readback 不能互相替代”的通用证据分层。 |
| project owner gate、module-regression-guards、scheduler-concurrency-drift | project-specific | defer / signal-only | 作为 narrow sensor 设计范例保留；不变成 wiki 默认门禁，除非本仓出现同名 owner 或同类执行合同。 |

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
| topic-landing | 上游 topic 中已覆盖方案按 wiki 系统层吸收，不复制原目录 | [[projects/design/topics/agent-workflow-memory-harness-skill-landing]]、[[acknowledgebase-topic-system-adoption.v1]] | complete source topic adoption manifest |

## Adoption Decisions

| Candidate | Gap type | Decision | Landing / guard |
| --- | --- | --- | --- |
| Cross-project agent intelligence alignment map | true-gap | complete | 本页作为 [[agent-system-maturity]] 的 source pack 和 decision record。 |
| upstream topic landing into wiki systems | true-gap | complete | 使用 [[acknowledgebase-topic-system-adoption.v1]] 逐 source topic 映射到 agent / workflow / memory / harness / skill / evaluation / governance / template / topic / migration 层；[[projects/design/topics/agent-workflow-memory-harness-skill-landing]] 只保留摘要矩阵。 |
| Implementation engineering template system | true-gap | complete | 使用 [[projects/design/topics/implementation-engineering-template-system]] 和 [[templates/implementation-project-profile-template]] 承接所有实现类工程合集与模板目标。 |
| source freshness policy | recognition-gap | adapt | 在本页、snapshot 和 checker 中记录 source coverage；不伪造外部 freshness hash。 |
| per-dialogue / run trace | true-gap | defer runtime implementation | 先承认为 intelligence evidence 缺口；没有行为语料时保持 `insufficient-evidence`。 |
| evaluation correction closeout | true-gap-lite | adapt | 作为报告和 future sensor 候选；不把来源工程的具体 evaluation records 搬入本仓。 |
| L5 blocked-boundary proof | recognition-gap | recognize + adapt | 继续由 [[agent-orchestration]]、[[state-constraint-reasoning]] 和报告口径承接；checker 只验证关键术语可发现。 |
| public / lens delivery bundle | recognition-gap | recognize | 本仓已有 [[skills/problem-focused-visual-presentation/SKILL]] 和 [[views/README]]；来源工程只作为 provenance 信号。 |
| production control-plane long-task control | true-gap | upgrade | 通用合同落到 [[agent-orchestration#Production-Grade Control Plane Hardening]]、[[skills/performance-bandwidth-analysis/SKILL]]、[[skills/runtime-config-switch/SKILL]] 和 `agent-control-plane-hardening` sensor。 |
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
