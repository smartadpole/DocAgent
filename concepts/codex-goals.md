---
type: concept
updated: 2026-06-12
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

在当前 wiki 里，Goal Contract 的切入位置固定在响应模式判断之后、正式长时执行之前。它先服务三条防线：期望最终状态防跑偏，验证面 / 证据边界防漂移，预算 / 阻塞停止条件防无限探索。

## Goal Contract 的分层归属

Goal Contract 不是单一层级的文件，而是一种跨层治理能力；但它的主入口和可复制正文以 [[templates/goal-contract-template]] 为准。

| 层级 | 归属 | 职责 |
| --- | --- | --- |
| 概念层 | 本页和 [[articles/2026-06-12-codex-goal-mode-usage-guide]] | 解释它是什么、解决什么问题、常见误区是什么 |
| 模板层 | [[templates/goal-contract-template]] | 承接可复制字段：记录位置、最终状态、完成判定、验收维度、证据边界、约束和停止条件 |
| 工作流层 | [[response-mode-routing]]、[[WORKFLOW]] | 规定什么时候启用：响应模式判断之后、正式长时执行之前 |
| 规则层 | [[POLICY]] | 规定不能替代什么：项目状态、验收报告、规则层、memory、`log.md`、检查、提交和 finalizer |
| Skill 层 | 不是普通 `SKILL.md` skill | 具体 skill 可以引用 Goal Contract，但 Goal Contract 本身不是一个执行技能 |

因此最准确的说法是：Goal Contract 是**模板为主体、规则和工作流共同约束的治理契约**，不是普通 skill。

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

## 使用方法

如果要实际启动 Goal，先把它写成 [[templates/goal-contract-template]]，再压缩成当前 Codex 界面可接受的目标表达。更详细的操作流程见 [[articles/2026-06-12-codex-goal-mode-usage-guide]]。

最小流程是：

1. 先按 [[response-mode-routing]] 判断这是不是长时任务。
2. 指定契约记录位置 / owning page，让 Goal 实例能从 TASK、Issue、AP、测试报告、handoff 或 episode package 回看。
3. 写清期望最终状态、完成判定、验收目标维度、验证面 / 证据边界、约束、允许边界和停止条件。
4. 每轮自动续跑或用户要求继续时，先回到完成契约检查是否继续、收尾或阻塞。
5. 收尾时只按证据写 done / partial / review / blocked，不把 health、日志、handoff、自述或 accepted / running 中间态上推成闭环；也不把全量 / 上线目标误写成本轮关闭条件。

## 常见误区

- 把 Goal 当成更长的 prompt
- 只写“让它更好”这种没有终点线的目标
- 把预算耗尽误当成完成
- 用 Goal 掩盖证据缺口或范围不清
- 把线程级契约误用成团队级真相源
- 把 Goal 自动续跑当成跳过 `log.md`、检查、finalizer 或提交闭环的例外
- 让 Goal 实例只漂在聊天里，没有 owning page
- 把本轮验收维度和上线 / 全量执行目标混成一个关闭条件

## 和当前 wiki 的关系

- [[response-mode-routing]] 负责判断本轮怎么推进。
- 这页负责定义长时任务的线程级完成契约。
- [[concepts/harness-engineering]] 负责更大一层的 Agent 工程化运行环境。

三者的关系可以简化成：

`Harness 定义环境，Routing 定义本轮模式，Goal 定义当前线程的终点线。`

## 相关页面

- [[articles/2026-05-25-codex-goals-research]]
- [[articles/2026-06-12-codex-goal-mode-usage-guide]]
- [[concepts/harness-engineering]]
- [[response-mode-routing]]
