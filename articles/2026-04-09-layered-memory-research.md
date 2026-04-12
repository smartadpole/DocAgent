---
type: article
date: 2026-04-09
updated: 2026-04-09
updated: 2026-04-12
---

# 分层 Memory 研究

- 来源：多轮内部讨论沉淀
- 日期：2026-04-09
- 类型：研究

## 一句话总结

分层 memory 的核心不是“记忆仓库”，而是把临时信息、稳定偏好、项目共识和决策规则分层沉淀，并按优先级自动注入后续任务的编排系统。

## 关键要点

### 1. 不是所有内容都该进 memory

建议先把信息分成四类：

- 即时上下文：只对当前任务有用，任务结束就该淡化
- 稳定偏好：会长期影响协作方式
- 项目事实：围绕某个项目、模块持续有效的共识
- 决策与制度：不是普通信息，而是裁决结果

### 2. 推荐做成 5 层

- `L0 Session Working Memory`
  当前会话内的临时上下文
- `L1 User Memory`
  用户稳定偏好
- `L2 Project / Workspace Memory`
  项目共享脑
- `L3 Decision / Policy Memory`
  高优先级规则和裁决
- `L4 Knowledge Artifact`
  可检索、可审计、可回溯的知识资产

### 3. 层间流动比分层本身更重要

建议默认链路：

`对话内容 -> 候选事实 -> 分类 -> 置信度判断 -> 写入对应层 -> 周期性压缩或升级`

基本规则：

1. 默认先落 `L0`
2. 满足条件再晋升到 `L1` 或 `L2`
3. 只有被裁决的内容才进入 `L3`
4. 高价值的 `L2/L3` 再固化到 `L4`

### 4. 路由要清楚

- 进 `Agent Prompt / System Context`
  只放当前必须知道的最小集
- 进 `Memory Store`
  放可复用、非瞬时、未来有价值的内容
- 进 `Decision / Policy`
  放会改变后续执行规则的内容

### 5. 自动沉淀要有判定器

每轮结束或任务结束时，至少判断：

- 是否稳定
- 是否可复用
- 是否影响未来输出
- 是否已确认
- 是否属于用户、项目还是制度

建议映射：

- 临时任务信息 -> `L0`
- 用户长期偏好 -> `L1`
- 项目背景与共识 -> `L2`
- 拍板后的规则 -> `L3`
- 需要可审计归档 -> `L4`

### 6. 冲突处理必须单独设计

memory 不该是覆盖式，而应带状态。

建议每条记忆至少有：

- `scope`
- `status`
- `confidence`
- `source`
- `last_verified_at`
- `owner`
- `supersedes`

冲突处理流程：

1. 标记 `conflicted`
2. 生成冲突摘要
3. 等待决策
4. 决策后将旧记录标记为 `deprecated`，新记录改为 `confirmed`

### 7. 优先级顺序要固定

建议读取顺序：

`Policy > Project Memory > User Memory > Session Memory > Raw Chat History`

这样可以避免：

- 临时一句话覆盖长期规则
- 个人偏好压过项目规范
- 旧聊天片段干扰新决策

### 8. 落地模块可以这样拆

- `Capture`
- `Classifier`
- `Consolidator`
- `Conflict Resolver`
- `Retriever`
- `Publisher`

### 9. 最小可执行版本

V1 可以先只做四层：

- `session_memory`
- `user_memory`
- `workspace_memory`
- `decision_memory`

V1 规则：

1. 默认都先入 `session_memory`
2. 重复出现或明确声明的，晋升到 `user` 或 `workspace`
3. 影响多人协作或流程的，进入 `decision`

V1 冲突机制：

- 新旧不一致时不覆盖
- 先标记冲突
- 等待决策
- 决策后更新

V1 注入顺序：

- `decision > workspace > user > session`

## 当前落点

这套分层现在已经有明确文件分工：

- [[BRAIN]]：共享背景
- `projects/memory/`：项目级稳定记忆
- [[POLICY]]：规则、优先级和自动沉淀边界
- [[projects/decisions]]：项目拍板
- `articles/` / `concepts/`：已经稳定的长期知识

## 开源工具

现成开源工具是有的，但大多更擅长“记忆存储”，不直接覆盖“记忆治理”。

### Mem0

更适合：

- 对话压缩
- 记忆抽取
- 记忆检索
- 作为通用长期记忆底座

### Zep

更适合：

- 项目级上下文
- 实体关系
- 多源上下文汇总
- 关系型共享脑

### Letta

更适合：

- 长期有状态 agent
- 跨会话状态保持
- 持续协作型 agent 运行时

### 当前判断

如果目标是尽快做出可用版：

- 用 `Mem0` 或 `Zep` 作为底层记忆组件
- 自己补分层 schema、晋升规则、冲突状态机、policy 层

如果目标是做完整 agent 操作系统：

- 更接近 `Letta + 自己的 policy / memory orchestration`

## 相关概念

- [[concepts/layered-memory]]

## 后续动作

- 如果后续把这套方案真正引入当前系统，再按项目层、规则层和共享背景层继续细化
- 如果继续调研具体实现，再补字段设计、流程图和触发规则
