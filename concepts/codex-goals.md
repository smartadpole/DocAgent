---
type: concept
updated: 2026-05-25
tags: [codex, ai-agent, workflow]
---

# Codex Goals

## 定义

Codex Goals 是 Codex 中面向长时任务的持久目标机制。它把“持续工作直到某个结果成立”定义成当前线程里的完成契约，而不是一次性 prompt。

它最关键的特征不是“自动继续”，而是：

- 目标持续存在
- 完成必须由证据审计
- 生命周期可控
- 作用域限于当前线程

## 边界

Codex Goals 不是：

- 全局 memory
- 仓库级规则
- 项目级 workflow
- 没有边界的后台自治

它更像线程级状态，负责把目标、预算、进度和完成判定留在当前工作链里。

## 一个强 Goal 应该包含什么

- 结果：完成时什么必须成立
- 证据：用什么证明结果
- 约束：哪些性质不能回退
- 边界：允许动哪些文件、工具、数据和资源
- 迭代策略：每轮之后下一步怎么选
- 阻塞停止条件：什么时候该停并报告

## 生命周期

这份专题材料中出现的控制面包括：

- `/goal`：设置或查看 Goal
- `/goal pause`：暂停
- `/goal resume`：恢复
- `/goal clear`：清除

对应的核心状态是：活跃、暂停、完成，以及预算受限停止。

## 适用场景

- benchmark 驱动的性能优化
- flaky test 调查
- 多步骤迁移和重构
- 需要复现的复杂 bug 排查
- 需要最终报告和证据分层的研究任务

## 常见误区

- 把 Goal 当成更长的 prompt
- 只写“让它更好”这种没有终点线的目标
- 把预算耗尽误当成完成
- 用 Goal 掩盖证据缺口或范围不清
- 把线程级契约误用成团队级真相源

## 和当前 wiki 的关系

- [[response-mode-routing]] 负责判断本轮怎么推进。
- 这页负责定义长时任务的线程级完成契约。
- [[concepts/harness-engineering]] 负责更大一层的 Agent 工程化运行环境。

三者的关系可以简化成：

`Harness 定义环境，Routing 定义本轮模式，Goal 定义当前线程的终点线。`

## 相关页面

- [[articles/2026-05-25-codex-goals-research]]
- [[concepts/harness-engineering]]
- [[response-mode-routing]]
