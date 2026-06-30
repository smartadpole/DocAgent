---
type: entry
id: ENTRY-GOV-001
scope: shared
status: active
source_of_truth: true
updated: 2026-05-28
tags: [entry, governance]
---

# 治理层入口

这层回答的不是“项目在做什么”，而是“这套文档系统按什么方式运行、判断、约束和沉淀”。

如果只记一件事，就记住这组边界：

- [[POLICY]]：规则裁定。回答“什么能晋升、什么必须人工确认、冲突时按什么优先级处理”
- [[AGENTS]]：执行约束。回答“agent 必须怎么做、不能怎么做”
- [[WORKFLOW]]：流程编排。回答“事情通常按什么顺序推进”
- [[response-mode-routing]]：响应模式路由。回答“本轮该先快速诊断、沉淀、验收、实现还是升级规则”
- [[proactive-dialogue-system]]：主动对话与引导式设计。回答“目标还没完整表达时，agent 该如何自动判定场景、少量提问、假设推进并产物化”
- [[agent-governance-strategy]]：Agent 治理分级。回答“哪些约束是 P0 硬规则，哪些只是 P1/P2/P3 的语义门、流程默认或 backlog”
- [[state-constraint-reasoning]]：状态约束推理。回答“当前权限、远程、预算、证据和用户确认状态允许 agent 做什么”
- [[agent-orchestration]]：Agent 编排。回答“Goal、Run Capsule、Orchestrator、Worker、Evaluator、子工程 Git preflight 和沉淀路由怎么分工”
- [[agent-system-maturity]]：Agent System Maturity。回答“目标工程 agent system 七层对象、智能化证据、外部矩阵识别和 Goodhart 边界怎么判断”
- [[instruction-adherence]]：指令遵循治理。回答“已有规则怎样变成触发器、模板字段、sensor、门禁和最终证明”
- [[execution-contract-semantics]]：执行合同语义。回答“当前执行裁决是否被参考规则、非目标或上层证据污染”
- [[harness-evolution]]：Harness H5 自演进。回答“用户纠偏、检查失败和重复失守如何形成 episode，并何时晋升为 sensor、模板、技能或规则”
- [[harness-feedback-ledger]]：Harness episode ledger。回答“哪些 episode 已观察、已晋升、待补 sensor 或待降级”
- [[BRAIN]]：共享背景。回答“哪些已确认前提要自动带入后续工作”
- [[log-writing-rules]]：`[[log]]` 的治理规则
- [[trace-writing-rules]]：`[[projects/trace]]` 的治理规则
- [[template-feedback-rules]]：下游项目系统层信息反哺规则
- [[documentation-maintenance-rules]]：documentation-maintenance 的触发、证据顺序、保守同步和 sensor 接线
- [[knowledge-linking-rules]]：knowledge-linking 的有效链接、单一信息源和关系画像规则
- [[issue-analysis-rules]]：issue-analysis 的快速根因链、完整案件和验收 / 规则升级分流
- [[problem-focused-visual-presentation-rules]]：problem-focused lens 的 source pack、导出、views 和不上推规则
- [[public-html-publish-rules]]：public-html-publish 的 HTML-only、public_url、host / prefix、live readback 和 blocked 裁定规则
- [[research-capability-rules]]：research-capability 的证据等级、行动等级、查证和沉淀落位规则
- 复盘总入口看 [[skills/retrospective-capability/SKILL]]，复盘方法看 [[concepts/project-retrospective]]，archive root 看 [[projects/retrospectives/README]]，具体复盘正文进入 `projects/retrospectives/<year>/` 并同步索引；项目交付 / 软件研发链复盘用 [[skills/delivery-retrospective/SKILL]]，历史对话 / Agent 工作流复盘用 [[skills/historical-dialogue-retrospective/SKILL]]，复盘暴露的重复失守或机制缺口再回到 [[harness-evolution]] 和 [[harness-feedback-ledger]]
- 会议材料和正式纪要的治理，优先看 [[WORKFLOW]] 里的会议管理段，再看 [[projects/meetings/README]]

## 逻辑结构

当前整套系统按七层理解：

1. 入口层：[[README]]、[[INDEX]]
2. 治理层：[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[response-mode-routing]]、[[proactive-dialogue-system]]、[[agent-governance-strategy]]、[[state-constraint-reasoning]]、[[agent-orchestration]]、[[instruction-adherence]]、[[execution-contract-semantics]]、[[harness-evolution]]、[[harness-feedback-ledger]]、[[POLICY]]、[[BRAIN]]
3. 技能层：[[skills/README]] 和 `skills/`
4. 运行层：[[projects/README]] 和 `projects/`
5. 沉淀层：`articles/`、`concepts/`、`indexes/`
6. 历史层：[[log]]、`archive/`
7. 证据层：`raw/`、`inbox/`、`assets/`

## 物理结构

治理层现在统一收在 `governance/`，只有 [[AGENTS]] 保留在根目录。

这样做有两个目的：

- 把散落在根目录的规则、流程、背景和写法指南收成一层，避免继续平铺
- 保留 [[AGENTS]] 作为根级特殊入口，保证 agent 打开仓库时能先读到硬约束

## 读取顺序

默认读取顺序：

1. 先看 [[README]] 和 [[INDEX]]
2. 再看 [[BRAIN]]
3. 如果涉及规则、优先级或记忆路由，再看 [[POLICY]]
4. 如果要判断先轻量诊断还是进入重治理闭环，再看 [[response-mode-routing]]
5. 如果要设计新系统、新工具或把粗糙目标想完整，再看 [[proactive-dialogue-system]]
6. 如果要判断治理动作是否过重、是否该升级成硬规则，再看 [[agent-governance-strategy]]
7. 如果要判断当前状态是否允许执行、提交、推送、发布或关闭，再看 [[state-constraint-reasoning]]
8. 如果要拆分多 agent、子工程或 Worker / Evaluator，再看 [[agent-orchestration]]
9. 如果要判断 agent-system / intelligence maturity、外部矩阵识别或七层能力包，再看 [[agent-system-maturity]]
10. 如果要判断规则已有但没执行的问题，再看 [[instruction-adherence]]
11. 如果要判断执行页是否出现口径漂移，再看 [[execution-contract-semantics]]
12. 如果要判断本轮偏差是否应沉淀成 episode，再看 [[harness-evolution]] 和 [[harness-feedback-ledger]]
13. 如果要实际执行修改，再看 [[WORKFLOW]]
14. 如果要知道 agent 的行为边界，再看 [[AGENTS]]
15. 如果要治理 `[[log]]`、[[projects/trace]] 或模板反哺，再看对应规则页

## `POLICY` 和 `AGENTS` 的权衡

这两个最容易混。

- [[POLICY]] 定义的是系统裁定规则
- [[AGENTS]] 定义的是执行这些规则时的操作约束

判断口诀：

- 如果问题是“什么情况下可以 / 不可以”，优先写 [[POLICY]]
- 如果问题是“agent 修改时必须怎么做”，优先写 [[AGENTS]]
- 如果问题是“通常按什么顺序推进”，优先写 [[WORKFLOW]]
- 如果问题是“先快后重怎么路由”，优先写 [[response-mode-routing]]
- 如果问题是“该不该主动问、问什么、怎么把想法想完整”，优先写 [[proactive-dialogue-system]]
- 如果问题是“治理动作是不是过重、规则是否该升级或降级”，优先写 [[agent-governance-strategy]]
- 如果问题是“当前状态是否允许执行某动作”，优先写 [[state-constraint-reasoning]]
- 如果问题是“多 agent、子工程、Worker 和 Evaluator 怎么分工”，优先写 [[agent-orchestration]]
- 如果问题是“agent 体系成熟度、智能化证据或外部 evaluator 识别怎么判”，优先写 [[agent-system-maturity]]
- 如果问题是“规则已有但执行失守”，优先写 [[instruction-adherence]]
- 如果问题是“执行裁决被参考规则、非目标或上层证据污染”，优先写 [[execution-contract-semantics]]
- 如果问题是“Harness 怎样从真实 episode 里自我修正”，优先写 [[harness-evolution]] 和 [[harness-feedback-ledger]]
- 如果问题是“哪些背景以后默认成立”，优先写 [[BRAIN]]
- 如果问题是“下游项目的进化能不能带回模板”，优先写 [[template-feedback-rules]]
- 如果问题是“文档是否随代码、规则或结构变化同步”，优先写 [[documentation-maintenance-rules]]
- 如果问题是“新增知识怎样落位、入口和回链”，优先写 [[knowledge-linking-rules]]
- 如果问题是“问题要快诊断、完整 Issue、验收还是规则升级”，优先写 [[issue-analysis-rules]]
- 如果问题是“复杂信息是否要做成图文 lens 或持久 views”，优先写 [[problem-focused-visual-presentation-rules]]
- 如果问题是“canonical HTML 是否已经公网可访问、能否给 public URL”，优先写 [[public-html-publish-rules]] 和 [[views/publication]]
- 如果问题是“调研能否形成可行动判断”，优先写 [[research-capability-rules]]

优先级上，先看 [[POLICY]] 的裁定，再由 [[AGENTS]] 把它落实成执行纪律。

## Loop Engineering 接入

- [[skills/loop-engineering/SKILL]]：持续 agent 循环控制技能，用于判断何时从一次性 Goal / Run Capsule 升级为可验证、可停、可持久化的 loop。
- [[governance/loop-engineering]]：Loop Engineering 的成熟度合同、quality gate、benchmark、反模式和持久化边界。
- [[templates/loop-contract-template]]：Loop Contract 控制面，记录 discovery source、run queue、evaluator、persistent state、budget / stop 和 next-run decision。
- [[templates/run-capsule-template]]：单轮运行胶囊，承接 Parent Loop Contract、Input discovery item、Worker limits、State transition 和 Next-run recommendation。
- 专项检查：`python3 scripts/check_all.py --only loop-engineering`。
