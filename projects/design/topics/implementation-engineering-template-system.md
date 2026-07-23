---
type: design-topic
id: DES-TOPIC-IMPLEMENTATION-TEMPLATE-001
project: PROJ-WIKI-001
status: accepted-design
stage: implementation-template
updated: 2026-07-23
tags: [design, implementation, template, agent-system, harness]
---

# 实现类工程合集与模板系统

上游：[[projects/design/topics/README]]、[[agent-system-maturity]]

相关：[[agent-system-cross-project-alignment.v1]]、[[wiki-governance-system-contract.v1]]、[[projects/development/plan/work-item-system-model]]、[[agent-orchestration]]、[[templates/implementation-project-profile-template]]

## 定位

当前 wiki 不再只是一套普通知识库模板，也不把自己定义成某一种工程模板。它的目标角色是**所有实现类工程的合集与模板**：主控仓库、子工程、运行服务、数据 / 模型工程、知识库 / 文档治理工程、运维 agent、前端 / 后端 / CLI / worker / scheduler 都要能在这里找到最小可复制的 owner、合同、技能、模板、sensor 和验收边界。

这页是实现类工程模板系统的设计 owner。它不保存任何具体工程的运行 ID、端口、业务表、服务状态或一次性 handoff；具体项目事实仍留在各项目自己的 owner、service registry、TASK / issue / report 或 handoff 中。

## 模板母体分层

wiki 是统一模板工程，对外输出的是 **Template Kernel + Project Profile Overlay + Capability Pack** 的模板母体，不是内部 source project 清单，也不是 controller / subproject / knowledge-base / ops-agent 中任何单一角色的副本。任何从下游工程、上游知识治理库或本机仓库吸收来的经验，进入本页时必须先去项目名化：

- `Template Kernel`：所有工程共享的 agent、workflow、memory、harness、skill、evaluation、governance、template、migration 基线。
- `Project Profile Overlay`：按工程角色裁剪模板，回答“这个目标工程需要哪些 owner、能力包和证据合同”。
- `Capability Pack`：可组合能力单元，回答“这个工程需要 runtime 控制面、主控验收、知识库维护、运维诊断、研究能力还是子工程 handoff”。
- `Source Provenance`：具体来源工程名、路径、服务事实、运行 ID 和一次性证据只留在内部 source registry、上游 topic、审计报告或历史 log；不进入对外模板概念层。
- `source_deidentification_rule`：任何进入 wiki 对外模板面的内容，必须把 source project 名称改写成工程角色、source archetype、capability pack 或证据边界；只有 provenance 层保留具名来源。

因此 wiki 可以生成主控模板、子工程模板、知识库模板或运维 agent 模板，但不能把任何真实工程名变成 profile 名、能力名或默认事实。目标工程接入时先裁决 profile 和 pack，再选择本地 owner；不得复制 wiki 整库结构来证明采纳。

画像和能力包不是能力裁剪菜单。wiki 的 Template Kernel 默认保留完整 agent / workflow / memory / harness / skill / evaluation / governance / migration 能力；profile 先正向声明主体角色、负责事项、事实归口、默认 owner、证据解释和哪些重治理默认不自动展开。目标工程如果暂时不需要某项能力，后续可以在本地 owner 中显式关闭或降级，但不能在 clone 初期因为少选能力而破坏基础智能体系。

## 工程类型覆盖

| 工程类型 | wiki 必须提供的模板能力 | 本仓落位 |
| --- | --- | --- |
| 主控 / controller | Goal、Run Capsule、事项主链、验收裁决、子工程回传、不上推边界 | [[agent-orchestration]]、[[templates/run-capsule-template]]、[[projects/development/plan/work-item-system-model]] |
| 子工程 / implementation repo | Subproject Git Preflight、allowed writes、handoff、代码 / runtime 证据 | [[templates/harness-adoption-template]]、[[templates/code-handoff-template]]、[[templates/implementation-project-profile-template]] |
| runtime-service | service registry、health / smoke / config profile、blocked readback | [[projects/service-registry]]、[[state-constraint-reasoning]] |
| 数据 / 模型工程 | source freshness、non-default / boundary evidence、readback、evaluation correction | [[agent-system-maturity]]、[[projects/development/reports/README]] |
| 知识库 / 文档治理工程 | owner-first、trace、memory、log、topic placement、documentation maintenance、lens | [[projects/memory/README]]、[[projects/trace]]、[[documentation-maintenance-rules]]、[[skills/problem-focused-visual-presentation/SKILL]] |
| 运维 agent / ops | service registry、runtime config switch、health、production readback、rollback、ops diagnostics | [[projects/service-registry]]、[[skills/runtime-config-switch/SKILL]]、[[skills/performance-bandwidth-analysis/SKILL]] |
| 调研 / 选型工程 | Research Contract、Source Ledger、evidence matrix、adoption contract | [[skills/research-capability/SKILL]]、[[templates/research-intake-template]] |

## Project Profile Overlay

| Profile overlay | 默认必选能力包 | 可选能力包 | 默认不引入 |
| --- | --- | --- | --- |
| `controller-profile` | Goal / Run Capsule、work-item control、acceptance-governance、agent-finalizer、subproject dispatch | public / lens、research、runtime readback | 业务 DB readback、具体服务配置、下游项目事实。 |
| `subproject-profile` | Subproject Git Preflight、allowed writes、handoff、local validation、regression guard | runtime config switch、service-side smoke | 主控裁决权、跨仓关闭权、上游 topic 直写权。 |
| `runtime-service-profile` | service registry、health / smoke、runtime config switch、production readback、rollback | performance-bandwidth-analysis、public URL live readback | 业务验收上推、数据库事实复制、机器事实模板化。 |
| `knowledge-base-profile` | owner-first、topic placement、memory / trace / log、documentation maintenance、research routing | problem-focused lens、public HTML publish、retrospective | 代码级写入默认、部署事实默认、重型 TASK 链。 |
| `ops-agent-profile` | local-operations-diagnostics、third-party source boundary、browser / runtime profile readback、external-write-boundary | visual delivery verification、remote-control runbook | 用户级配置写入、外部工程整包复制、本机路径进入 tracked 文件。 |
| `data-model-profile` | source freshness、evaluation-scheme-design、non-default / boundary evidence、review / readback | experiment sweep governance、performance analysis | 模型 / 数据集 / benchmark 数字模板化。 |
| `lightweight-repo-profile` | minimal AGENTS、project conformance、Persistence Decision、validation command | thin adapter、small local sensor | 厚 governance 树、完整主控事项链、长期 service registry。 |
| `hybrid-profile` | 先列主角色，再组合 2 到 3 个 overlay，并写明冲突裁决 | 按目标工程需要补 capability pack | 无限制叠加所有能力包。 |

Hybrid 必须声明 `primary_profile` 和 `secondary_profiles`。冲突时按 owner precedence 裁决：运行事实以 service registry 为主，项目状态以项目主页 / status 为主，验收关闭以主控 evaluator 为主，知识沉淀以 owner topic / memory / trace 为主。

## Owner Topology Compatibility

个人能力 owner 拓扑和软件 / 代码工程治理集合是两层系统。wiki 作为模板母体要能被 clone 成 Personal Strategy、Career、Wealth、Public Output、知识库、运维 agent 或实现工程，但它不替这些 owner 保存真实人生事实、职业事实、财务事实、服务运行事实或代码项目事实。

因此所有从 wiki clone 的目标工程，除工程画像外还要声明一条 owner 拓扑身份轴：

| 字段 | 含义 |
| --- | --- |
| `owner_topology_role` | method-center / life-owner / strategy-owner / career-owner / wealth-risk-owner / public-output-owner / software-governance-object / implementation-object / hybrid-owner |
| `owner_independence_gate` | independent-owner / subordinate-view / registry-object / temporary-incubator；用于判断它是不是长期单一信息源。 |
| `responsibility_scope` | 这个工程的主体职责、核心事项、事实归口、方法、证据和行动闭环。 |
| `privacy_currentness_boundary` | 是否涉及私密、高敏、外部当前事实、生产状态或需人工确认的内容。 |
| `research_depth_default` | strong / medium / light；表示默认调研证据等级，不表示是否具备调研能力。 |
| `clone_instantiation_mode` | new-owner / implementation-object / knowledge-owner / ops-agent / hybrid；用于第一次从模板落地时选择初始化检查。 |
| `mother_seed_policy` | keep-as-template-reference / archive / remove-from-current-state；用于避免模板母体内容污染目标工程当前事实。 |

这条身份轴只回答“这个 clone 出来的库在个人能力体系或工程治理体系里是什么 owner”。它不替代 `project_role`，也不改变 wiki 全能力内核。举例：`knowledge-base-profile` 可以是方法中控、人生策略库、职业资本库或公共输出库；真正差别不在于它有没有 memory / research / lens 能力，而在于 owner 拓扑、主体职责、隐私边界、当前事实边界和研究深度默认值。

## Capability Packs

| Capability pack | 解决的问题 | 主要 owner |
| --- | --- | --- |
| `work-item-control-pack` | 主控如何拆 Gate / FP / EP / TASK、Issue、risk、test 和验收 | [[projects/development/plan/work-item-system-model]]、[[skills/work-item-auto-decomposition/SKILL]] |
| `subproject-handoff-pack` | 子工程如何接收任务、保护 Git 状态、回传证据 | [[agent-orchestration]]、[[templates/code-handoff-template]] |
| `runtime-control-plane-pack` | 服务配置切换、health / smoke、production readback、rollback | [[projects/service-registry]]、[[skills/runtime-config-switch/SKILL]] |
| `acceptance-governance-pack` | 验收对象、证据层级、manual boundary 和 finalizer | [[agent-orchestration]]、[[projects/development/acceptance/README]] |
| `ops-diagnostics-pack` | timing ledger、coverage matrix、容量、外部依赖、浏览器 / runtime profile 和不上推边界 | [[skills/performance-bandwidth-analysis/SKILL]]、[[state-constraint-reasoning]] |
| `research-intelligence-pack` | 调研合同、source plan、证据等级和落地裁决 | [[skills/research-capability/SKILL]]、[[skills/technology-research/SKILL]] |
| `memory-trace-log-pack` | owner-first、topic、memory、trace、log 和文档维护 | [[projects/memory/README]]、[[projects/trace]]、[[skills/documentation-maintenance/SKILL]] |
| `visual-publication-pack` | lens、HTML、public URL、同源导出和 live readback | [[skills/problem-focused-visual-presentation/SKILL]]、[[skills/public-html-publish/SKILL]] |

下游工程贡献的是可抽象能力包，不是整套项目事实。业务名、服务名、运行 ID、端口、表、账号、dataset、模型、机器、路径和一次性 handoff 只能作为 source evidence，不进入 pack 正文。

## Adoption Matrix

任何新实现类工程接入 wiki 模板时，先建立或填写 [[templates/implementation-project-profile-template]]，至少裁决：

| 字段 | 含义 |
| --- | --- |
| `project_role` | controller / subproject / runtime-service / knowledge-base / documentation-governance / data-model / ops-agent / hybrid |
| `primary_profile` | hybrid 或多角色工程的主画像 |
| `secondary_profiles` | 需要叠加的补充画像 |
| `required_packs` | 完成当前工程角色必须接入的能力包 |
| `optional_packs` | 可按阶段、规模或权限延后接入的能力包 |
| `forbidden_packs` | 不应引入的重治理、runtime、发布或主控能力 |
| `owner_topology_role` | 目标工程在个人能力 owner 拓扑或软件治理集合中的身份 |
| `owner_independence_gate` | 是否已经是独立 owner，还是 view、registry object 或 incubator |
| `responsibility_scope` | 目标工程的主体职责、核心事项、事实归口、方法、证据和行动闭环 |
| `clone_instantiation_mode` | clone 初始落地方式和初始化检查口径 |
| `mother_seed_policy` | 模板母体内容在目标工程中保留、归档或移除的策略 |
| `privacy_currentness_boundary` | 隐私、当前性、生产事实和人工确认边界 |
| `research_depth_default` | 默认调研证据等级和升级触发 |
| `project_bound_facts` | 不能上推到 wiki 模板的业务事实、运行事实和一次性证据 |
| `closeout_proof` | 该角色怎么算完成，以及缺哪层证据时只能报 partial / blocked |

## Implementation Project Profile

[[templates/implementation-project-profile-template]] 是总 profile 模板，负责把 Kernel、Project Profile Overlay 和 Capability Pack 裁决写成一张可提交的接入合同。它至少裁决：

- `project_role`：controller / subproject / runtime-service / knowledge-base / documentation-governance / data-model / ops-agent / hybrid。
- `owner_topology_role`：method-center / life-owner / strategy-owner / career-owner / wealth-risk-owner / public-output-owner / software-governance-object / implementation-object / hybrid-owner。
- `owner_independence_gate`：independent-owner / subordinate-view / registry-object / temporary-incubator。
- `profile_overlay`：primary profile、secondary profiles、启用 / 禁用的 overlay 默认值。
- `capability_packs`：required / optional / forbidden packs。
- `clone_instantiation`：clone_instantiation_mode、mother_seed_policy、identity rewrite 和 current-state reset。
- `privacy_currentness_boundary`：隐私、敏感事实、外部当前事实、生产状态和人工确认边界。
- `research_depth_default`：strong / medium / light 以及升级触发；不表示工程没有调研能力。
- `owner_surfaces`：项目主页、AGENTS、service registry、work-item chain、memory、trace、report、handoff。
- `agent_system_layers`：skill、runtime、harness、memory、evaluation、governance、migration 七层是否有本地 owner。
- `control_plane`：Goal / Loop / Run Capsule / Worker / Evaluator / Issue policy / persistence policy 的落点。
- `implementation_boundaries`：allowed writes、forbidden writes、Git preflight、dirty / diverged / local-only 处理。
- `evidence_contract`：code-level、functional、service-side、end-to-end、non-default / boundary、manual confirmation。
- `template_adoption`：直接使用、局部适配、项目绑定、拒绝或延后。
- `project_bound_facts`：哪些下游事实只能留在目标工程。
- `closeout_proof`：本 profile 的完成证明和不能上推边界。

## Topic 到系统层落地

上游 design topics 进入 wiki 时，不按原目录复制；按系统层吸收：

| Upstream 方案族 | wiki 系统层 | 本仓落地 |
| --- | --- | --- |
| Universal Agent Harness Baseline | harness + governance + template | [[agent-system-maturity]]、[[templates/harness-adoption-template]] |
| Agent Harness / Memory / Evaluation / Migration | agent-system 七层对象 | [[agent-system-cross-project-alignment.v1]]、[[projects/design/topics/agent-workflow-memory-harness-skill-landing]] |
| Goal Orchestration / Run Capsule | workflow + harness | [[agent-orchestration]]、[[templates/run-capsule-template]] |
| Process Knowledge Persistence / Dialogue Persistence | memory + persistence | [[projects/memory/README]]、[[log]]、[[harness-feedback-ledger]] |
| Research Operating System / Technical Research | skill + template + sensor | [[skills/research-capability/SKILL]]、[[skills/technology-research/SKILL]] |
| topic placement / Design Topic Governance | topic owner + project docs sensor | [[projects/design/topics/README]]、本页 |
| Cross-project Log Architecture | memory + log + generated view boundary | [[log-writing-rules]]、[[projects/memory/README]] |
| Public / Lens / Visual Presentation | views + skill + publication boundary | [[skills/problem-focused-visual-presentation/SKILL]]、[[skills/public-html-publish/SKILL]] |

## 不能上推边界

## 完成边界

本页达成的是结构和模板能力，不自动证明任何具体工程已经上线、验收或达到智能化行为分数。完整实现类工程接入必须另有：

- 本地 profile 或等价 owner。
- 明确的 Project Profile Overlay 和 Capability Pack 裁决。
- 目标工程自己的 `python3 scripts/check_all.py` 或等价验证。
- 子工程 Git preflight 和 handoff。
- 主控侧 evaluator 关闭裁决。
- 缺 runtime / live readback / 人工确认时明确 `blocked / partial / review`。

## 验证

- `python3 scripts/check_all.py --only implementation-template-system`
- `python3 scripts/check_all.py --only agent-system-maturity`
- 收尾前 `python3 scripts/check_all.py`
