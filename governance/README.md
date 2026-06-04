---
type: entry
id: ENTRY-GOV-001
scope: shared
status: active
source_of_truth: true
updated: 2026-06-04
tags: [entry, governance]
---

# 治理层入口

这层回答的不是“项目在做什么”，而是“这套文档系统按什么方式运行、判断、约束和沉淀”。

如果只记一件事，就记住这组边界：

- [[POLICY]]：规则裁定。回答“什么能晋升、什么必须人工确认、冲突时按什么优先级处理”
- [[agent-governance-strategy]]：Agent 治理策略。回答“哪些是 P0 硬约束，哪些只是语义门、流程或 backlog”
- [[AGENTS]]：执行约束。回答“agent 必须怎么做、不能怎么做”
- [[WORKFLOW]]：流程编排。回答“事情通常按什么顺序推进”
- [[response-mode-routing]]：响应模式路由。回答“本轮该先快速诊断、沉淀、验收、实现还是升级规则”
- [[proactive-dialogue-system]]：主动对话与引导式设计。回答“目标还没完整表达时，agent 该如何自动判定场景、少量提问、假设推进并产物化”
- [[state-constraint-reasoning]]：状态与约束推演。回答“新信息进入系统后，哪些状态、依赖、阻塞和可执行性会被改变”
- [[instruction-adherence]]：指令遵循治理。回答“已有规则怎样变成触发器、模板字段、sensor、门禁和最终证明”
- [[execution-contract-semantics]]：执行合同语义。回答“当前执行裁决是否被参考规则、非目标或上层证据污染”
- [[harness-evolution]]：Harness H5 自演进。回答“用户纠偏、检查失败和重复失守如何形成 episode，并何时晋升为 sensor、模板、技能或规则”
- [[harness-feedback-ledger]]：Harness episode ledger。回答“哪些 episode 已观察、已晋升、待补 sensor 或待降级”
- [[BRAIN]]：共享背景。回答“哪些已确认前提要自动带入后续工作”
- [[log-writing-rules]]：`[[log]]` 的治理规则
- [[trace-writing-rules]]：`[[projects/trace]]` 的治理规则
- [[knowledge-linking-rules]]：知识关联规则。回答“新增知识怎样形成入口、上位概念、邻接页面和反向承接，而不是成为孤岛页”
- [[template-feedback-rules]]：下游项目系统层信息反哺规则
- 会议材料和正式纪要的治理，优先看 [[WORKFLOW]] 里的会议管理段，再看 [[projects/meetings/README]]

## 逻辑结构

当前整套系统按七层理解：

1. 入口层：[[README]]、[[INDEX]]
2. 治理层：[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[agent-governance-strategy]]、[[response-mode-routing]]、[[proactive-dialogue-system]]、[[state-constraint-reasoning]]、[[instruction-adherence]]、[[execution-contract-semantics]]、[[harness-evolution]]、[[harness-feedback-ledger]]、[[POLICY]]、[[BRAIN]]
3. 技能层：[[skills/README]] 和 `skills/`
4. 运行层：[[projects/README]] 和 `projects/`
5. 沉淀层：`articles/`、`concepts/`、`indexes/`
6. 历史层：[[log]]、`archive/`
7. 证据层：`raw/`、`inbox/`、`assets/`

## 物理结构

治理层现在统一收在 `governance/`，只有 [[AGENTS]] 保留在根目录作为共享 agent 规则正文。`CLAUDE.md` 可以作为 Claude Code 适配壳导入 [[AGENTS]]，但不承接第二份规则正文；`.codex/AGENTS.md` 如果存在，只能作为 thin Codex adapter 指回根 [[AGENTS]]。

这样做有两个目的：

- 把散落在根目录的规则、流程、背景和写法指南收成一层，避免继续平铺
- 保留 [[AGENTS]] 作为根级特殊入口，保证 agent 打开仓库时能先读到硬约束；Claude Code 通过 `CLAUDE.md` 导入它，Codex 直接读取根 `AGENTS.md`，可选 `.codex/AGENTS.md` 只做薄适配

## 读取顺序

默认读取顺序：

1. 先看 [[README]] 和 [[INDEX]]
2. 再看 [[BRAIN]]
3. 如果涉及规则、优先级或记忆路由，再看 [[POLICY]]
4. 如果要判断治理是否过硬、该保留硬约束还是降成语义门，再看 [[agent-governance-strategy]]
5. 如果要判断先轻量诊断还是进入重治理闭环，再看 [[response-mode-routing]]
6. 如果要设计新系统、新工具或把粗糙目标想完整，再看 [[proactive-dialogue-system]]
7. 如果要判断一条新信息进入系统后会怎样改写状态、依赖和可执行性，再看 [[state-constraint-reasoning]]
8. 如果要判断规则已有但没执行的问题，再看 [[instruction-adherence]]
9. 如果要判断执行页是否出现口径漂移，再看 [[execution-contract-semantics]]
10. 如果要判断本轮偏差是否应沉淀成 episode，再看 [[harness-evolution]] 和 [[harness-feedback-ledger]]
11. 如果要实际执行修改，再看 [[WORKFLOW]]
12. 如果要知道 agent 的行为边界，再看 [[AGENTS]]
13. 如果要治理 `[[log]]`、[[projects/trace]] 或模板反哺，再看对应规则页
14. 如果要新增长期知识页、概念页或摘要卡片，再看 [[knowledge-linking-rules]]

## `POLICY` 和 `AGENTS` 的权衡

这两个最容易混。

- [[POLICY]] 定义的是系统裁定规则
- [[AGENTS]] 定义的是执行这些规则时的操作约束

判断口诀：

- 如果问题是“什么情况下可以 / 不可以”，优先写 [[POLICY]]
- 如果问题是“治理规则是不是过硬、是否应该降级、是否应该做资格判断”，优先写 [[agent-governance-strategy]]
- 如果问题是“agent 修改时必须怎么做”，优先写 [[AGENTS]]
- 如果问题是“通常按什么顺序推进”，优先写 [[WORKFLOW]]
- 如果问题是“先快后重怎么路由”，优先写 [[response-mode-routing]]
- 如果问题是“该不该主动问、问什么、怎么把想法想完整”，优先写 [[proactive-dialogue-system]]
- 如果问题是“这条新信息进入系统后会影响哪些状态和可执行性”，优先写 [[state-constraint-reasoning]]
- 如果问题是“规则已有但执行失守”，优先写 [[instruction-adherence]]
- 如果问题是“执行裁决被参考规则、非目标或上层证据污染”，优先写 [[execution-contract-semantics]]
- 如果问题是“Harness 怎样从真实 episode 里自我修正”，优先写 [[harness-evolution]] 和 [[harness-feedback-ledger]]
- 如果问题是“新增知识怎样避免孤岛页”，优先写 [[knowledge-linking-rules]]
- 如果问题是“哪些背景以后默认成立”，优先写 [[BRAIN]]
- 如果问题是“下游项目的进化能不能带回模板”，优先写 [[template-feedback-rules]]

优先级上，先看 [[POLICY]] 的裁定，再由 [[AGENTS]] 把它落实成执行纪律。

## 相关专题

- [[concepts/agent-governance]]：Agent 治理专题总览。它不替代本层任何单一信息源，只用于统筹响应路由、指令遵循、执行合同、H5 自演进、技能、模板、sensor 和 Agent 工作复盘之间的知识库关系。
- [[knowledge-linking-rules]]：长期知识、概念页和摘要卡片的网状关联规则，定义入口、上位概念、邻接页面、反向承接和 sensor 检查。
- [[agent-governance-strategy]]：Agent 治理瘦身和分级策略。它把硬约束、语义门、流程和 backlog 区分开，避免 `[[log]]`、完整检查、产物化或二阶反思变成无条件仪式。
- [[governance/platform-standards]]：平台级治理标准。定义主控工程 L3、子工程 L2 的各维度成熟度指标，供跨工程治理审计技能使用。
