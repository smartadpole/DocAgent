---
type: policy
memory_layer: policy
scope: shared
status: active
source_of_truth: true
updated: 2026-04-09
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

- `POLICY.md`
- `[[projects/decisions]]`
- `[[projects/memory/README]]`
- `[[projects/memory/shared]]`
- `[[BRAIN]]`
- `workspace-memory`
- session / chat history

## 路由规则

- 临时会话信息先留在 session 或 `inbox/`
- 重复出现、且只对当前项目长期有用的信息，先进入 `[[projects/memory/README]]`
- 跨任务、跨会话、但仍属于共享背景的信息，进入 `BRAIN.md`
- 会改变后续执行方式的内容，进入 `POLICY.md`
- 项目冲突和最终拍板，进入 `[[projects/decisions]]`

## 冲突处理

- 如果新信息与现有 policy 冲突，先不要直接覆盖
- 先在 `[[projects/decisions]]` 或相关页面写清楚冲突和背景
- 如果冲突影响后续路由、优先级或自动沉淀边界，再回写这里
- 只有确认后，旧规则才可以被新规则替换
