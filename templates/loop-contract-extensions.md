---
type: template
id: TEMPLATE-LOOP-CONTRACT-EXTENSIONS-001
status: active
updated: 2026-10-14
tags: [template, loop, conditional]
---

# Loop Contract 条件扩展

入口见 [[templates/loop-contract-template]]。扩展只补核心合同尚未承接的条件信息，队列和原事项仍是各自状态 owner。

## 调度恢复

**触发**：定时、事件或外部平台自动触发，或运行中断后需要恢复。

- **运行依赖**：调度位置、时间窗、并发占用与重复触发处理；本地调度需检查关机、会话、profile、凭据、网络、端口和权限失效边界。
- **恢复合同**：running 项的重入 / 超时裁决、重试次数与退避、已消费输入读回、next-run marker 持久化与恢复验证；停止后不得遗留仍在自动写入的调度。

## 协作与现场检查

**触发**：已授权多角色执行、外部仓库写入或跨角色合流。

- **Agent Topology**：Orchestrator、Worker、独立 Evaluator、execution posture，以及 worktree / 线程隔离方式。单执行者与独立脚本 oracle 无需为形式创建多 agent。
- **Worker Ownership**：任务范围、Allowed writes、Required evidence、limits、停止条件与回传入口；Worker 必须继承实际存在的 Goal / Loop / Run Capsule、AGENTS 和 owning page 边界，不能要求读取不存在的合同。
- **Subproject Git Preflight**：每轮外部仓库动作前刷新 [[templates/run-capsule-extensions#外部仓库现场检查]]，不能复用旧 run 的现场安全证据。
- 需要独立运行身份、恢复游标或跨角色合流时使用 [[templates/run-capsule-template]]。没有回到同一 Loop、缺少 limits 或夸大证据的回传不能被 evaluator 采纳为完成。

## Evaluator 细化

**触发**：Loop 修复问题、改实现、改 agent 行为或据结果推进状态。

- **oracle 类型与独立性**：脚本 / 独立 agent / 人工 reviewer / 真实运行工具 / 组合；记录它实际能证明什么。
- **baseline fail + candidate pass**：用于回归或行为修复的同口径前后证据；before-after evidence 需能辨认输入、环境和候选版本。
- **状态语义**：passed 为必要证据全部满足；partial 为部分满足且缺口明确；blocked 为权限、环境或证据阻断；failed 为已执行而不符合；skipped 为有据可查的不消费 / 不执行裁决。
- **误报 / 漏报与冲突**：记录可辨别 oracle 错判的复验方法，冲突未裁定不能报 passed。
- **Closeout Proof**：实际采用的 Run / Worker 证据、Evaluator 结论、state store 读回、专项检查和仍需人工确认的事项。仅有静态接线检查不算业务或模型效果验证。

## 研发落位

**触发**：发现的软件研发候选需要进入正式 owner。

- **Software Development Landing**：按性质进入既有 Gate / FP / EP / TASK / risk / Issue / AP / report / service-registry / engineering feedback，记录实际落点。
- **状态边界**：保留原始问题、父级关系、状态关闭条件、人工确认项和不上推边界。Loop 仅提出或回传，不另建平行看板，也不把 oracle 通过当作事项自动关闭。

## 沉淀

**触发**：纠偏、稳定背景、可复用方法或复盘请求。

使用 [[templates/run-capsule-extensions#沉淀与复盘]]；Process Record 留下实际消费输入、关键动作、失败和状态变更链接，Reuse entry proof 只在确有复用入口时记录。普通轮次不复制完整沉淀路由表。
