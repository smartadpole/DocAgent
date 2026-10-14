---
type: template
id: TEMPLATE-RUN-CAPSULE-001
status: active
updated: 2026-10-14
tags: [template, harness, goal, orchestration, evaluator]
conditional_sources: [templates/run-capsule-extensions.md]
---

# Run Capsule 模板

仅承接独立运行身份、恢复游标或跨角色合流。先复用已有 owner；普通持续执行、跨仓修改或一次性协作不自动创建。启动条件见 [[agent-orchestration]]，Goal 工具授权见 [[skills/goal-contract/SKILL]]。没有启动条件时直接推进原事项，不生成未启用说明。

## 最小生效核心

- **Run id 与 owner**：运行标识、记录落点、原事项 / 合同链接及本次需要独立身份或恢复记录的原因。
- **本轮目标与输入**：引用用户最新目标、完成判定和消费输入，仅补本轮范围差异；属于持续 Loop 时链接实际 Parent Loop Contract。
- **授权与停止**：允许写入范围、必须保持的约束、不做项、预算和停止 / blocked 条件。
- **证据与 limits**：本次直接完成证据、必要层级、缺测及不能上推的范围。health、自述或 accepted / running 不能替代必要功能和验收证据。
- **结果与恢复游标**：实际状态 passed / partial / blocked / failed、关键动作与失败项链接、下一步动作和负责 owner；跨 run 恢复前重新读回现场状态。

这些信息可在原 owner 通过短链接承接；Capsule 不复制目标正文、另建任务状态或替 evaluator 宣布整体闭环。

## 条件扩展

仅命中时读取 [[templates/run-capsule-extensions]] 对应章节：跨角色合流用“多角色合流”；外部仓库动作前用“外部仓库现场检查”；多个验收面 / 参数用“分层证据”；Loop run 用“循环回传”；稳定方法或复盘信号用“沉淀与复盘”。Worker 回传的 limits 与不上推边界始终保留；未触发项无需写空表、不适用或 no-op。
