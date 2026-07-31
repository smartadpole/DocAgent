---
type: governance
id: GOV-ACK-TOPIC-SYSTEM-ADOPTION-001
scope: shared
status: active
source_of_truth: true
updated: 2026-07-31
tags: [governance, acknowledgebase, topic-adoption, agent, workflow, memory, harness, skill]
---

# AcknowledgeBase Topic System Adoption Manifest

主入口：[[agent-system-maturity]]

相关：[[agent-system-cross-project-alignment.v1]]、[[projects/design/topics/agent-workflow-memory-harness-skill-landing]]、[[projects/design/topics/implementation-engineering-template-system]]、[[skills/README]]、[[harness-evolution]]、[[harness-feedback-ledger]]

## 定位

本页是 AcknowledgeBase `projects/design/topics/` 到 wiki 工程治理体系的逐 topic 吸收清单。它做的是 **ability adoption**，不是文档复制。

每个 source topic 必须被抽象成 wiki 本地可执行的 agent system 能力，并至少落到 agent、workflow、memory、harness、skill、evaluation、governance、template、topic 或 migration 中的一层。若不能落地，必须写明 `defer / reject` 和边界；不能只留下“已参考 source topic”。

## 覆盖不变量

- `source_topic` 必须逐一列出 AcknowledgeBase 的 topic 文件或 topic cluster 入口。
- `capability extraction` 只写系统层能力，不复制源工程项目事实、路径、运行 ID、状态、分数或一次性 handoff。
- `wiki system layers` 必须指向 agent / workflow / memory / harness / skill / evaluation / governance / template / topic / migration 的具体层。
- `wiki owner landing` 必须指向本仓现有 owner、模板、技能、sensor 或治理页；没有 owner 时只能 `defer`。
- `agent-system action` 必须能改变 agent 执行、判断、回写、验证、迁移或收尾行为。
- `validation` 必须能被专项 sensor 或明确人工 evaluator 检查。

## 逐 Topic 吸收矩阵

| source_topic | capability extraction | wiki system layers | wiki owner landing | agent-system action | validation |
| --- | --- | --- | --- | --- | --- |
| `projects/design/topics/README.md` | Topic 入口不是内容仓库，而是 design topic 生命周期、状态和 owner routing 的总目录。 | governance / topic / workflow / evaluation | [[projects/design/topics/README]]、[[response-mode-routing]]、本页 | 新方案先判是否已有 owner、是否进入 topic、是否需要设计先行或只做 no-op。 | `acknowledge-topic-adoption` 检查 source_topic 全覆盖和入口回链。 |
| `projects/design/topics/universal-agent-harness-baseline.md` | 全工程 agent baseline 需要本地化为七层能力包，而不是复制 harness 文档。 | agent / harness / governance / template / evaluation | [[agent-system-maturity]]、[[templates/harness-adoption-template]]、[[skills/goal-contract/SKILL]] | 新工程接入必须说明 agent、runtime、harness、memory、evaluation、governance、migration 的本地证据。 | `agent-system-maturity`、`harness-governance`、`acknowledge-topic-adoption`。 |
| `projects/design/topics/agent-harness-memory-evaluation-and-migration.md` | skill maturity 扩展为完整 agent system maturity，并加入 intelligence evidence lens。 | agent / memory / workflow / evaluation / migration / governance | [[agent-system-maturity]]、[[agent-system-cross-project-alignment.v1]]、[[templates/agent-intelligence-evaluation-template]] | 不能用 skill 完整度上推 agent 智能；必须保留 `insufficient-evidence`、Goodhart guard 和 external readback 边界。 | `agent-system-maturity` 检查八维 intelligence 和不上推边界。 |
| `projects/design/topics/agent-harness-memory-evaluation-and-migration/README.md` | 将大型 agent-system topic 拆成 cluster hub，避免 Goal、过程沉淀和跨仓验收互相污染。 | governance / topic / workflow / migration | [[agent-system-cross-project-alignment.v1]]、本页 | wiki 只吸收 cluster 中的系统能力，并把每个子 topic 分别落到 owner，不把 cluster 当单页结论。 | `acknowledge-topic-adoption` 检查子 topic 单独出现。 |
| `projects/design/topics/agent-harness-memory-evaluation-and-migration/goal-orchestration-governance.md` | Goal、Run Capsule、Worker、Evaluator、Subproject Git Preflight 和 persistence routing 是一个编排合同。 | agent / workflow / harness / template / evaluation | [[agent-orchestration]]、[[skills/goal-contract/SKILL]]、[[templates/run-capsule-template]]、[[templates/loop-contract-template]] | 启动长 Goal 或子工程 Worker 前必须先定义 topology、证据层、blocked_for_done 和 not_blocked_for_implementation。 | `harness-governance`、`loop-engineering`、`acknowledge-topic-adoption`。 |
| `projects/design/topics/agent-harness-memory-evaluation-and-migration/cross-repository-governance-acceptance.md` | 跨仓治理验收要分清结构接线、本地 conformance、runtime readback 和外部 evaluator。 | workflow / harness / evaluation / governance / migration | [[agent-system-cross-project-alignment.v1]]、[[templates/skill-transfer-evidence-contract]]、[[projects/development/reports/README]] | 子工程完成不能自动上推为主控通过；必须回传证据层级和 blocked-by-orchestrator-readback。 | `agent-system-maturity` 和 transfer / governance 相关 sensor。 |
| `projects/design/topics/agent-harness-memory-evaluation-and-migration/process-knowledge-persistence.md` | 过程知识沉淀要区分 run trace、method capture、memory owner、log 和 future-task knowledge。 | memory / workflow / harness / template / evaluation | [[projects/memory/README]]、[[log-writing-rules]]、[[harness-feedback-ledger]]、[[templates/agent-intelligence-evaluation-template]] | 收尾必须做 Persistence Decision：artifact-needed、no-op 或 blocked；不得把对话结论只留在最终回复。 | `agent-system-maturity`、`harness-feedback-ledger`、`acknowledge-topic-adoption`。 |
| `projects/design/topics/collaborative-code-and-work-item-id-governance.md` | 多电脑代码协作与事项编号要由 canonical remote、Git preflight 和 Gate -> FP -> EP -> TASK 合同承接。 | workflow / governance / evaluation / template | [[projects/development/plan/work-item-system-model]]、[[skills/work-item-auto-decomposition/SKILL]]、[[templates/development-work-item-matrix-template]] | 编码任务必须有父级合同、风险、测试、验收和 issue-trigger 边界；git 同步不能覆盖 dirty worktree。 | `work-item-matrix`、`execution-contract-semantics`。 |
| `projects/design/topics/cross-project-log-architecture.md` | log 是原子活动记录加生成视图，不能作为唯一事实源，也不能替代 memory、issue 或 report。 | memory / workflow / governance / template | [[log-writing-rules]]、[[projects/memory/README]]、[[template-feedback-rules]] | 有结构、规则、状态、决策或验收变化时写 log；纯局部格式或临时状态可 no-op。 | `documentation-maintenance`、`acknowledge-topic-adoption`。 |
| `projects/design/topics/design-topic-file-governance.md` | topic 内部组织要有 README / workflow / memory 粒度判断和插入协议。 | governance / topic / workflow / evaluation | [[projects/design/topics/README]]、[[documentation-maintenance-rules]]、本页 | 修改 topic 时优先更新已有 owner；只有需要 cluster / 子页时才新建页面。 | `project-docs`、`acknowledge-topic-adoption`。 |
| `projects/design/topics/dialogue-knowledge-persistence-system.md` | 对话知识持久化需要 Persistence Decision、artifact landing matrix、Worker finding adoption 和 negative-space evaluator。 | memory / harness / evaluation / workflow / template | [[projects/memory/README]]、[[harness-evolution]]、[[harness-feedback-ledger]]、[[templates/agent-intelligence-evaluation-template]] | 用户纠偏、Worker finding、future-task knowledge 必须判是否进入 owner、ledger、skill、template 或 no-op。 | `harness-feedback-ledger`、`agent-system-maturity`。 |
| `projects/design/topics/dialogue-work-state-capture-and-retrieval.md` | 对话状态识别要区分探索、设计、待拍板、执行、review、blocked、done 和 current view。 | memory / workflow / evaluation / governance / topic | [[response-mode-routing]]、[[projects/status]]、[[projects/trace]]、[[views/README]] | 不能把当前对话状态直接写成项目事实；必须读 owner、判 eligibility、保留 stale / missing / blocked 边界。 | `project-docs`、`documentation-maintenance`、`acknowledge-topic-adoption`。 |
| `projects/design/topics/dialogue-work-state-capture-loop-contract.md` | work-state capture 的循环只能做发现、刷新、评估和 next-run decision，不能自动关闭正式状态。 | workflow / harness / evaluation / template | [[skills/loop-engineering/SKILL]]、[[templates/loop-contract-template]]、[[templates/run-capsule-template]] | Loop 输出必须写 next-run decision 和 persistence routing，不自动合并发布、关闭 Gate 或改生产事实。 | `loop-engineering`。 |
| `projects/design/topics/dialogue-work-state-capture-phase-one-pilot.md` | 试点报告提供样本、snapshot、HTML current view、manual refresh 和最小 sensor 的能力证据边界。 | evaluation / memory / workflow / topic | [[projects/development/reports/README]]、[[views/README]]、[[projects/status]] | 试点结果只能作为 evidence seed；没有持续样本和 evaluator 时保持 partial / insufficient-evidence。 | `public-html-publish`、`agent-system-maturity`。 |
| `projects/design/topics/execution-process-record-system.md` | Goal、Loop、Run Capsule、process record 和 method capture 要形成一次运行的可追溯档案。 | harness / memory / workflow / template / evaluation | [[agent-orchestration]]、[[templates/run-capsule-template]]、[[templates/loop-contract-template]]、[[log-writing-rules]] | 长运行收尾必须说明过程记录去向、方法沉淀和未归档原因；不默认新建平行 runs 目录。 | `loop-engineering`、`harness-governance`。 |
| `projects/design/topics/personal-capability-system-architecture.md` | 个人能力工程架构只抽象 owner topology 和 project admission，不复制个人规划正文。 | governance / memory / topic / workflow | [[projects/memory/README]]、[[projects/README]]、[[projects/design/topics/README]] | wiki 只保留可迁移的 owner-first routing、project_role 和 admission 条件；个人事实留在目标工程。 | `implementation-template-system`、`acknowledge-topic-adoption`。 |
| `skills/topic-visual-presentation/SKILL.md` | 主题呈现先做 eligibility；admit 默认 HTML，problem-focus 是 scope。 | skill / workflow / evaluation / template / concept | [[skills/topic-visual-presentation/SKILL]]、[[topic-visual-presentation-rules]]、[[templates/topic-presentation-template]] | 即时 subject/source 不要求预建 Topic；public publish 独立。 | `topic-visual-presentation`、`public-html-publish`。 |
| `projects/design/topics/research-operating-system-design.md` | 调研从搜索升级为 Research Contract、Source Plan、Source Ledger、Evidence Delta、Judgment、Assets、Revision Loop 和 Evaluator。 | skill / workflow / memory / evaluation / template | [[skills/research-capability/SKILL]]、[[skills/technology-research/SKILL]]、[[templates/research-intake-template]]、[[templates/technology-research-evidence-matrix-template]] | `strong-template-kernel` 完整吸收可迁移合同；深度调研先定 source plan、coverage、验证阶梯和行动等级，上游领域知识不复制。 | `research-capability` 的结构化正负 fixture。 |
| `projects/design/topics/retrospective-archive-storage-structure.md` | 复盘档案应按年度、主题、类型索引，并把行动项分流到 owner，而不是复盘内平行看板。 | memory / skill / template / evaluation / governance | [[skills/retrospective-capability/SKILL]]、[[projects/retrospectives/README]]、[[templates/project-retrospective-template]] | 显式复盘默认落档；复杂纠偏进入标准 / 深度复盘，行动项必须回写对应 owner。 | `retrospective-system`。 |
| `projects/design/topics/skill-maturity-integrated-scoring-loop-contract.md` | 技能成熟度评分要用 Loop Contract 连接 evidence corpus、评分、校准和 next-run decision。 | skill / harness / evaluation / workflow | [[skills/README]]、[[skills/loop-engineering/SKILL]]、[[agent-system-maturity]] | 评分更新必须有 evidence、golden boundary、negative sample 和 next-run decision，不只改分数。 | `skill-maturity`、`loop-engineering`。 |
| `projects/design/topics/skill-maturity-scoring-evolution.md` | 成熟度评分从结构评分升级为结构底座、runtime evidence、skill-specific outcome rubric 和 cross-skill synthesis。 | skill / evaluation / governance / template | [[skills/README]]、[[templates/agent-intelligence-evaluation-template]]、[[agent-system-maturity]] | 结构齐全不能上推 outcome；需区分 common rubric、差异 rubric、正负样本和 reviewer provenance。 | `skill-maturity`、`agent-system-maturity`。 |
| `projects/design/topics/technical-research-capability-upgrade.md` | 技术研究需要 R2+ Source Plan、coverage matrix、Research Case Packet、Revision Brief 和 Delta Source Plan。 | skill / workflow / evaluation / template / memory | [[skills/technology-research/SKILL]]、[[templates/technology-research-contract-template]]、[[templates/technology-research-report-template]]、[[research-capability-rules]] | R2+ 必须先过 source plan checkpoint；Adopt 必须有 L1、claim-scope local validation 和 outcome review。 | `research-capability` validator + positive / negative fixtures。 |
| `projects/design/topics/topic-placement-and-state-routing.md` | 话题落位和状态路由要把 owner discovery、落位轴、生命周期和状态读取连成决策。 | governance / topic / workflow / memory | [[response-mode-routing]]、[[projects/design/topics/README]]、[[projects/trace]]、[[projects/memory/README]] | 新信息进入时先判 owner discovery、state routing、是否冲击 trace / memory / decision / task。 | `documentation-maintenance`、`acknowledge-topic-adoption`。 |

## 系统层汇总

| layer | 已吸收能力 | 验证口径 |
| --- | --- | --- |
| agent | Goal / Run / Worker / Evaluator / final proof / 不上推边界 | [[agent-system-maturity]]、`agent-system-maturity` |
| workflow | response mode、owner discovery、state routing、research contract、work-item contract、closeout | [[response-mode-routing]]、[[WORKFLOW]]、`project-docs` |
| memory | BRAIN、project memory、trace、log、ledger、report、run / method capture 分层 | [[projects/memory/README]]、[[log-writing-rules]] |
| harness | Goal Contract、Loop Contract、Run Capsule、Subproject Git Preflight、Persistence Decision | [[agent-orchestration]]、[[skills/loop-engineering/SKILL]]、`harness-governance` |
| skill | research、retrospective、visual lens、work item、transferable skill governance | [[skills/README]]、`skill-maturity` |
| evaluation | source coverage、negative evidence、Goodhart guard、external readback、current / snapshot boundary | [[agent-system-maturity]]、`scripts/check_all.py` |
| governance | topic owner、design-first、instruction adherence、harness evolution、template feedback | [[governance/README]]、[[harness-evolution]] |
| template | implementation profile、agent intelligence evaluation、run / loop / research / retrospective contracts | [[templates/README]] |
| topic | topic placement、topic file governance、source topic adoption manifest | [[projects/design/topics/README]]、本页 |
| migration | source-depth、recognize / complete / upgrade / adapt / defer / reject、project conformance | [[agent-system-cross-project-alignment.v1]]、[[skills/transferable-skill-governance/SKILL]] |

## 不复制边界

- `not copied`：本页不复制 AcknowledgeBase 的项目事实、topic 状态、复盘原文、运行记录、分数、路径、服务名或本机 handoff。
- `ability adoption`：只有抽象后的触发条件、事实源分层、判断合同、agent 行为、写回守卫、模板字段和 sensor 才能进入 wiki。
- `structure-only`：本页证明 wiki 有逐 topic owner landing 和检查入口，不证明每次 agent 行为已通过外部 evaluator。
- `insufficient-evidence`：缺行为样本、runtime readback、negative evidence review 或人工 reviewer 时，智能评分继续为空。

## 验证

- `python3 scripts/check_all.py --only acknowledge-topic-adoption`
- `python3 scripts/check_all.py --only agent-system-maturity,implementation-template-system,harness-governance,skill-maturity`
- `python3 scripts/check_all.py`
