---
type: governance
id: GOV-AGENT-SYSTEM-MATURITY-001
scope: shared
status: active
source_of_truth: true
updated: 2026-07-14
tags: [governance, agent-system, maturity, intelligence, evaluation]
---

# Agent System Maturity

主入口：[[governance/README]]

相关：[[agent-system-cross-project-alignment.v1]]、[[acknowledgebase-topic-system-adoption.v1]]、[[projects/design/topics/implementation-engineering-template-system]]、[[projects/design/topics/agent-workflow-memory-harness-skill-landing]]、[[templates/implementation-project-profile-template]]、[[templates/agent-intelligence-evaluation-template]]、[[skills/README]]、[[skills/transferable-skill-governance/SKILL]]、[[skills/cross-project-skill-adoption-prompt/SKILL]]、[[projects/development/plan/work-item-system-model]]、[[harness-evolution]]、[[harness-feedback-ledger]]

## 定位

这页是本仓 Agent System Capability Package 的 owner。它回答“wiki 作为目标工程，是否具备可运行、可评估、可迁移、可被外部矩阵识别的 agent system”，而不是回答某个单项 skill 是否写得完整。

当前 wiki 的目标定位是**所有实现类工程的合集与模板**。主控、子工程、runtime service、数据 / 模型工程和文档治理工程接入时，必须优先使用 [[projects/design/topics/implementation-engineering-template-system]] 与 [[templates/implementation-project-profile-template]] 或等价 profile，证明本地 owner、agent system 七层、control plane、implementation boundaries 和 evidence contract 已经落地。

本页只承接体系对象、证据边界、评估 capsule、缺口分类和本仓落位；不承接 AcknowledgeBase 的当前分数、profile hash、历史 snapshot、项目事实或一次性矩阵输出。

跨工程智能化能力吸收的 source pack 和 adoption decision 由 [[agent-system-cross-project-alignment.v1]] 承接。它用于处理“借鉴所有工程的 agent / harness / memory / workflow 能力”这类任务，并把源工程信号分类为 `recognize / complete / upgrade / adapt / defer / reject`，不复制源工程事实或目录形态。

AcknowledgeBase `projects/design/topics/` 的逐 topic 能力吸收由 [[acknowledgebase-topic-system-adoption.v1]] 承接。它是 wiki 对上游 design topics 的 ability adoption source of truth：每个 source topic 必须抽象落实到 agent、workflow、memory、harness、skill、evaluation、governance、template、topic 或 migration 的本地 owner，不能只复制文档或只写 family 摘要。

## 七层对象

| 层 | 本仓 owner | 最小证据 | 不上推边界 |
| --- | --- | --- | --- |
| skill | [[skills/README]] 和各 `skills/*/SKILL.md` | skill frontmatter、README entry、TRANSFER 或不可迁移说明、专项 sensor | skill 完整不能证明 agent system 完整。 |
| runtime | `AGENTS.md`、`.codex/AGENTS.md`、tool / browser profile 规则、[[projects/service-registry]] | shell / git / browser profile / service registry readback 或 blocked 原因 | 工具列表不能证明工具被正确使用。 |
| harness | [[response-mode-routing]]、[[skills/goal-contract/SKILL]]、[[skills/loop-engineering/SKILL]]、[[agent-orchestration]] | Goal、Loop、Run Capsule、Subproject Git Preflight、closeout proof | harness 结构不能自动关闭 TASK / EP / Gate。 |
| memory | [[BRAIN]]、[[projects/memory/README]]、[[projects/trace]]、[[log]] | owner-first 读取、source-of-truth routing、log / trace / memory 分层 | 记忆存在不能替代当前 live readback。 |
| evaluation | `scripts/check_all.py`、`scripts/check_agent_system_maturity.py`、测试报告、受控 snapshot | 专项 sensor、完整检查、runtime / outcome / blocked 证据、报告 | 本地 green 不能冒充外部 evaluator 通过。 |
| governance | [[harness-evolution]]、[[harness-feedback-ledger]]、[[instruction-adherence]] | 用户纠偏、检查失败、模板 / sensor / skill 晋升或降级路由 | ledger 通道存在不等于 agent 已经学会。 |
| migration | [[skills/transferable-skill-governance/SKILL]]、[[skills/cross-project-skill-adoption-prompt/SKILL]]、skill transfer templates | true-gap / recognition-gap / signal-only-gap、target self-check、Goodhart guard | 不复制源工程目录形态或项目事实。 |

## Intelligence Evidence Lens

智能化不直接给总分。首版只要求八维证据位全部出现；缺行为证据时必须保持 `insufficient-evidence`，`agent_intelligence_score` 为 `null`。从结构接线推进到行为评估时，使用 [[templates/agent-intelligence-evaluation-template]] 收集 positive / negative behavior corpus、evaluator provenance、Goodhart guard 和 external readback 边界。

| 维度 | 本仓可读证据 | 当前状态 |
| --- | --- | --- |
| `intent_modeling` | Goal Contract、trace、最终范围 / 不做项 | `insufficient-evidence`，缺跨轮正负样本审查。 |
| `mode_selection` | [[response-mode-routing]]、log、报告中的阶段判断 | `insufficient-evidence`，缺 rubric-backed 行为评估。 |
| `tool_and_runtime_use` | git / shell / browser profile readback、非默认值验证记录 | `insufficient-evidence`，缺系统化负证据审查。 |
| `context_and_memory_use` | BRAIN / project memory / trace / log 路由 | `insufficient-evidence`，缺行为样本和 stale memory 反查。 |
| `decomposition_and_orchestration` | [[agent-orchestration]]、Run Capsule、work-item decomposition | `insufficient-evidence`，缺 worker / evaluator 合流行为证据。 |
| `evidence_judgment` | 测试报告、service registry、external readback / blocked 口径 | `insufficient-evidence`，缺结构 / runtime / outcome / manual 边界样本审查。 |
| `recovery_and_learning` | [[harness-feedback-ledger]]、复盘、sensor 晋升 | `insufficient-evidence`，缺偏差后实际学习效果评估。 |
| `user_alignment` | scope control、dirty worktree guard、commit 范围、最终回复证据 | `insufficient-evidence`，缺用户纠偏序列审查。 |

## Matrix Recognition Capsule

| Field | Current value |
| --- | --- |
| evaluator | AcknowledgeBase skill maturity matrix + agent-system maturity diagnostics；外部 evaluator 循环由主控持有。 |
| candidate files / scanned surfaces | `AGENTS.md`、`.codex/AGENTS.md`、`governance/`、`skills/`、`templates/`、`scripts/check_*.py`、`views/`、`projects/development/reports/`、[[projects/service-registry]]。 |
| current baseline | 2026-06-30 本地 baseline：`skill-maturity` 和 `work-item-matrix` 专项通过；外部旧诊断中 wiki 的 `work-item-auto-decomposition` 为缺口，agent-system/intelligence 需要目标工程本地 snapshot。 |
| true-gap | 缺本仓自己的 agent-system owner、runtime / evaluation snapshot、intelligence 八维证据位、事项自动拆解项目绑定入口。 |
| recognition-gap | cross-project skill adoption 和 transferable governance 已有，但缺 agent-system / matrix recognition capsule 字段在本仓本地 owner 中成套出现。 |
| signal-only-gap | 为矩阵识别补 entrypoint link、checker key 和 expected impact；不得扩写空能力或复制 AcknowledgeBase 当前分数。 |
| Goodhart guard | 不复制项目事实、不补空 skill、不把 skill 高分上推成 agent system / intelligence 高分、不把本地 green 当外部 readback。 |
| external readback | 本轮只提供主控可刷新的 capsule 和 expected impact；外部矩阵未在本仓内运行，状态为 `blocked-by-orchestrator-readback`。 |

## Gap Table

| 能力 | 缺口类型 | 本仓处理 | 剩余边界 |
| --- | --- | --- | --- |
| Agent System Capability Package | true-gap | 本页 + `governance/agent-system-maturity-snapshot.v1.json` + `scripts/check_agent_system_maturity.py` | 仍需主控外部矩阵读回。 |
| Intelligence Evidence Refresh | true-gap | 八维证据位入 snapshot，全部缺行为证据时保持 `insufficient-evidence` | 不输出正式智能化总分。 |
| Cross-project skill adoption frontier maintenance | recognition-gap | 在 [[skills/cross-project-skill-adoption-prompt/SKILL]] 和 TRANSFER 补 matrix capsule / source-depth / golden boundary | 不代表目标工程已迁移。 |
| Transferable Skill Governance review contract | recognition-gap | 在 [[skills/transferable-skill-governance/SKILL]] 和 TRANSFER 补 review contract | sensor 只证明 wiring。 |
| work-item-auto-decomposition | true-gap + project-bound | 新增本仓项目 / 领域绑定 skill，并接入 work-item matrix checker | 不硬升为通用可迁移 skill。 |
| Cross-project agent intelligence alignment | true-gap | 新增 [[agent-system-cross-project-alignment.v1]]，把上游知识治理库、主控、子工程、运行服务、数据 / 模型工程、知识库工程和运维 agent 的系统层能力抽象到本仓七层对象 | 结构对齐不能上推为行为智能得分；source project 名称只保留在 provenance，不进入对外模板概念。 |
| Implementation Project Template System | true-gap | 新增 [[projects/design/topics/implementation-engineering-template-system]]、[[projects/design/topics/agent-workflow-memory-harness-skill-landing]]、[[templates/implementation-project-profile-template]] 和 `scripts/check_implementation_template_system.py` | 模板接线不能上推为任何具体工程已上线、已验收或已具备行为智能。 |
| Agent Intelligence Evaluation Path | true-gap | 新增 [[templates/agent-intelligence-evaluation-template]]，把正负行为样本、八维 intelligence lens、evaluator provenance 和 Goodhart guard 固定成可复用评估合同 | 缺 negative evidence review、external readback 或人工 reviewer 时继续保持 `agent_intelligence_score: null`。 |
| AcknowledgeBase Topic System Adoption | true-gap | 新增 [[acknowledgebase-topic-system-adoption.v1]] 和 `scripts/check_acknowledgebase_topic_adoption.py`，逐 source topic 检查能力是否落到 wiki 的 agent / workflow / memory / harness / skill / evaluation / governance / template / topic / migration 层 | 逐 topic 结构落地不能上推为未来每轮 agent 行为已通过外部 evaluator。 |

## Persistence Decision

每次升级 agent 规则、workflow、harness、skill、evaluator、sensor、template 或默认入口行为时，本仓必须在收尾写明 `artifact-needed / no-op / blocked`：

- `artifact-needed`：已形成可复用系统层知识，落到 owner、skill、template、sensor、ledger 或 AcknowledgeBase 回传包，并能从入口发现。
- `no-op`：只产生 wiki 局部事实、一次性验证或无长期价值结论，说明不沉淀原因。
- `blocked`：识别出应沉淀内容但缺 owner、权限、证据或上游裁决，记录恢复条件。

Worker findings、治理 delta 和 future-task knowledge 没有完成 Persistence Decision 时，不能上推成 AcknowledgeBase 系统层方案；项目事实、服务实例、运行 ID 和本地 handoff 不得原样上推。

## 验证口径

- 专项：`python3 scripts/check_all.py --only agent-system-maturity,implementation-template-system,acknowledge-topic-adoption,skill-maturity,work-item-matrix`
- 完整：`python3 scripts/check_all.py`
- whitespace：`git diff --check`
- 外部 evaluator：由主控刷新 AcknowledgeBase matrix；本仓只回传 capsule、expected impact、blocked reason 和未验证边界。
