---
type: policy
id: POLICY-001
memory_layer: policy
scope: shared
status: confirmed
priority: highest
source_of_truth: true
updated: 2026-04-25
tags: [policy]
---

# 规则层

这页属于治理层，统一由 [[governance/README]] 收口。

这页放共享规则、优先级和记忆路由约束。

## 这页负责什么

- 定义哪些内容可以自动晋升为共享背景或项目记忆
- 定义冲突时的优先级和升级路径
- 定义共享背景、项目记忆、决策和会话的边界
- 定义哪些规则必须人工确认后才生效

## 这页不负责什么

- 不放项目阶段的具体取舍，那进 [[projects/decisions]]
- 不放项目内需求到实现的完整演进链，那进 [[projects/trace]]
- 不放时间顺序上的主题化过程记录，那进 [[log]]
- 不放逐条对话转录，那留在会话历史
- 不放单轮会话草稿，那留在会话 / 临时收口区
- 不放共享背景正文，那是 [[BRAIN]]
- 不放下游项目事实或业务决策；模板反哺只吸收抽象后的系统层信息，具体执行看 [[template-feedback-rules]]

## 读取优先级

- [[POLICY]]
- [[projects/decisions]]
- [[projects/memory/README]]
- [[projects/memory/shared]]
- [[BRAIN]]
- `workspace-memory`
- session / chat history

## 自动沉淀规则

### 规则 1：默认都先不进长期记忆

- 新信息默认先留在会话、`inbox/` 或临时草稿
- 没有满足晋升条件前，不直接写入 [[BRAIN]]、[[projects/memory/shared]] 或 [[POLICY]]

### 规则 2：满足条件才升到共享背景或项目记忆

满足下面任一条件时，才考虑从 session 晋升：

- 同一件事多轮重复出现
- 明确会影响后续多个任务
- 明确属于项目共识
- 如果不沉淀，下次会重复沟通

晋升方式：

- 跨任务但仍属于共享前提的，进入 [[BRAIN]]
- 只对当前项目长期有效的，进入 [[projects/memory/shared]]

### 规则 3：只有拍板后的内容才进规则层

以下内容只有在已经确认后，才进入这页：

- 冲突升级规则
- 自动沉淀边界
- 优先级顺序
- 例外处理规则

### 规则 4：发生冲突不直接覆盖

固定流程：

1. 标记冲突
2. 写到 [[projects/decisions]]
3. 等拍板
4. 再回写 [[BRAIN]]、[[POLICY]] 或项目页

## 自动写入边界

- agent 可以自动写入：`inbox/`、临时草稿、已确认结构下的普通项目页、已确认模板的 frontmatter
- agent 可以自动写入 [[log]]，但只记录按对话整理后的主题、用户意图、关键动作、结构变化和结论，不机械转录每个提问
- agent 可以自动写入 [[projects/trace]]，前提是这轮已经形成明确的项目推进内容，而且该变化会影响当前需求主题的实现口径；写入时要和相关 [[projects/requirements]]、[[projects/design/README]]、[[projects/decisions]] 同轮联动，不把它写成第二份 [[log]]，也不记录原始来源材料清单、出处或格式转换过程
- agent 可以自动执行格式归一化：把本库内错误的 Markdown 页面引用收敛成 `[[wikilink]]`，把明显失效的空链接、占位链接和本机绝对路径引用修正掉
- agent 可以在用户要求反哺模板时，按 [[template-feedback-rules]] 把下游项目中已经验证的结构、流程、规则、记忆路由、模板、写法和自动化契约抽象回模板库；抽象时不得复制项目事实、业务状态或具体技术拍板
- agent 需要先形成明确结论再写入：[[BRAIN]]、[[projects/memory/shared]]
- agent 不应直接拍板写入：高优先级规则、冲突结论、覆盖旧规则的变更
- 任何会改变后续执行方式的内容，优先先进入 [[projects/decisions]] 再回写

## 路由规则

- 临时会话信息先留在会话或 `inbox/`
- 时间顺序上的历史记录进入 [[log]]；记录单位是“每次对话”，不是“每个问题”或“每天一个主题”；如果要写用户提问，只记录能代表该次对话主题的提炼意图，相关问题可合并，不抄问题清单
- 需求从原始意图到当前实现的演进链进入 [[projects/trace]]；它按需求主题维护，不按日期分组，也不替代 [[log]]。原始来源整理、文件改名、PDF 到 Markdown / PDF->md、链接清理和出处索引不进入 [[projects/trace]]
- 重复出现、且只对当前项目长期有用的信息，先进入 [[projects/memory/README]]
- 跨任务、跨会话、但仍属于共享背景的信息，进入 [[BRAIN]]
- 会改变后续执行方式的内容，进入 [[POLICY]]
- 项目冲突和最终拍板，进入 [[projects/decisions]]
- 文档库本体的框架级说明和层级边界，默认写根 [[README]]；如果需要补背景，写 [[BRAIN]]；如果需要写规则，写 [[POLICY]]
- 下游项目反哺模板时，先进入 [[template-feedback-rules]] 的判断流程；可复用的结构写入口和结构页，可复用的执行顺序写 [[WORKFLOW]]，硬约束写 [[AGENTS]]，规则边界和记忆路由写 [[POLICY]]，共享背景写 [[BRAIN]]，可复制写法和模板骨架写 `templates/`
- 除非明确是当前项目的结论，否则不要把这类内容写进 `projects/`、`projects/memory/` 或 `projects/design/memory/`

## 优先级顺序

- [[POLICY]] 高于 [[projects/memory/shared]]
- [[projects/memory/shared]] 高于 [[BRAIN]]
- [[BRAIN]] 高于 `workspace-memory`
- `workspace-memory` 高于 session / chat history

## 冲突处理

- 如果新信息与现有规则冲突，先不要直接覆盖
- 先在 [[projects/decisions]] 或相关页面写清楚冲突和背景
- 如果冲突影响后续路由、优先级或自动沉淀边界，再回写这里
- 只有确认后，旧规则才可以被新规则替换
