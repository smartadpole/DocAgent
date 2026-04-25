---
type: entry
id: ENTRY-GOV-001
scope: shared
status: active
source_of_truth: true
updated: 2026-04-25
tags: [entry, governance]
---

# 治理层入口

这层回答的不是“项目在做什么”，而是“这套文档系统按什么方式运行、判断、约束和沉淀”。

如果只记一件事，就记住这组边界：

- [[POLICY]]：规则裁定。回答“什么能晋升、什么必须人工确认、冲突时按什么优先级处理”
- [[AGENTS]]：执行约束。回答“agent 必须怎么做、不能怎么做”
- [[WORKFLOW]]：流程编排。回答“事情通常按什么顺序推进”
- [[BRAIN]]：共享背景。回答“哪些已确认前提要自动带入后续工作”
- [[log-writing-rules]]：`[[log]]` 的治理规则
- [[trace-writing-rules]]：`[[projects/trace]]` 的治理规则
- [[template-feedback-rules]]：下游项目结构、流程、规则和模板反哺规则
- 会议材料和正式纪要的治理，优先看 [[WORKFLOW]] 里的会议管理段，再看 [[projects/meetings/README]]

## 逻辑结构

当前整套系统按六层理解：

1. 入口层：[[README]]、[[INDEX]]
2. 治理层：[[governance/README]]、[[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[BRAIN]]
3. 运行层：[[projects/README]] 和 `projects/`
4. 沉淀层：`articles/`、`concepts/`、`indexes/`
5. 历史层：[[log]]、`archive/`
6. 证据层：`raw/`、`inbox/`、`assets/`

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
4. 如果要实际执行修改，再看 [[WORKFLOW]]
5. 如果要知道 agent 的行为边界，再看 [[AGENTS]]
6. 如果要治理 `[[log]]`、[[projects/trace]] 或模板反哺，再看对应规则页

## `POLICY` 和 `AGENTS` 的权衡

这两个最容易混。

- [[POLICY]] 定义的是系统裁定规则
- [[AGENTS]] 定义的是执行这些规则时的操作约束

判断口诀：

- 如果问题是“什么情况下可以 / 不可以”，优先写 [[POLICY]]
- 如果问题是“agent 修改时必须怎么做”，优先写 [[AGENTS]]
- 如果问题是“通常按什么顺序推进”，优先写 [[WORKFLOW]]
- 如果问题是“哪些背景以后默认成立”，优先写 [[BRAIN]]
- 如果问题是“下游项目的进化能不能带回模板”，优先写 [[template-feedback-rules]]

优先级上，先看 [[POLICY]] 的裁定，再由 [[AGENTS]] 把它落实成执行纪律。
