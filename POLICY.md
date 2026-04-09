---
type: policy
id: POLICY-001
memory_layer: policy
scope: shared
status: confirmed
priority: highest
source_of_truth: true
updated: 2026-04-10
tags: [policy]
---

# POLICY

这页放共享规则、优先级和 memory 路由约束。

## 这页负责什么

- 定义哪些内容可以自动晋升为共享背景或项目记忆
- 定义冲突时的优先级和升级路径
- 定义 shared background、project memory、decision、session 的边界
- 定义哪些规则必须人工确认后才生效

## 这页不负责什么

- 不放项目阶段的具体取舍，那进 `[[projects/decisions]]`
- 不放时间顺序上的过程记录，那进 `log.md`
- 不放单轮会话草稿，那留在 session / inbox
- 不放共享背景正文，那是 `[[BRAIN]]`

## 读取优先级

- POLICY.md
- `[[projects/decisions]]`
- `[[projects/memory/README]]`
- `[[projects/memory/shared]]`
- `[[BRAIN]]`
- `workspace-memory`
- session / chat history

## 自动沉淀规则

### 规则 1：默认都先不进长期 memory

- 新信息默认先留在 session、`inbox/` 或临时草稿
- 没有满足晋升条件前，不直接写入 `[[BRAIN]]`、`[[projects/memory/shared]]` 或 `[[POLICY]]`

### 规则 2：满足条件才升到共享背景或项目记忆

满足下面任一条件时，才考虑从 session 晋升：

- 同一件事多轮重复出现
- 明确会影响后续多个任务
- 明确属于项目共识
- 如果不沉淀，下次会重复沟通

晋升方式：

- 跨任务但仍属于共享前提的，进入 `[[BRAIN]]`
- 只对当前项目长期有效的，进入 `[[projects/memory/shared]]`

### 规则 3：只有拍板后的内容才进 policy

以下内容只有在已经确认后，才进入这页：

- 冲突升级规则
- 自动沉淀边界
- 优先级顺序
- 例外处理规则

### 规则 4：发生冲突不直接覆盖

固定流程：

1. 标记冲突
2. 写到 `[[projects/decisions]]`
3. 等拍板
4. 再回写 `[[BRAIN]]`、`[[POLICY]]` 或项目页

## 自动写入边界

- agent 可以自动写入：`inbox/`、临时草稿、已确认结构下的普通项目页、已确认模板的 frontmatter
- agent 需要先形成明确结论再写入：`[[BRAIN]]`、`[[projects/memory/shared]]`
- agent 不应直接拍板写入：高优先级 policy、冲突结论、覆盖旧规则的变更
- 任何会改变后续执行方式的内容，优先先进入 `[[projects/decisions]]` 再回写

## 路由规则

- 临时会话信息先留在 session 或 `inbox/`
- 重复出现、且只对当前项目长期有用的信息，先进入 `[[projects/memory/README]]`
- 跨任务、跨会话、但仍属于共享背景的信息，进入 `BRAIN.md`
- 会改变后续执行方式的内容，进入 `POLICY.md`
- 项目冲突和最终拍板，进入 `[[projects/decisions]]`

## 优先级顺序

- `[[POLICY]]` 高于 `[[projects/memory/shared]]`
- `[[projects/memory/shared]]` 高于 `[[BRAIN]]`
- `[[BRAIN]]` 高于 `workspace-memory`
- `workspace-memory` 高于 session / chat history

## 冲突处理

- 如果新信息与现有 policy 冲突，先不要直接覆盖
- 先在 `[[projects/decisions]]` 或相关页面写清楚冲突和背景
- 如果冲突影响后续路由、优先级或自动沉淀边界，再回写这里
- 只有确认后，旧规则才可以被新规则替换
