---
type: template
id: TEMPLATE-LOOP-CONTRACT-001
status: active
updated: 2026-06-22
tags: [template, loop, harness, orchestration, evaluator]
---

# Loop Contract 模板

Loop Contract 是持续 agent 循环的控制面。它不替代 [[templates/goal-contract-template]]、[[templates/run-capsule-template]]、项目状态页、Issue、TASK、测试报告、服务台账或 memory；它只定义一个 loop 如何发现输入、分派执行、验证结果、持久化状态并决定下一轮。

## 适用性判断

- **是否启用 Loop Contract**：是 / 否
- **Loop 模式**：discovery-only / assisted-patch / structured-auto-fix / not-ready
- **当前响应模式**：
- **为什么不是一次性 Goal / Run Capsule**：
- **不启用理由**：
- **人工确认边界**：

## Objective

- **用户最新目标**：
- **Expected final state**：
- **Loop 成功判定**：
- **明确不做项**：
- **Stop / blocked conditions**：

## Discovery Source

- **发现源**：CI / issue / commit / inbox / raw / 监控 / 服务台账 / 测试报告 / 用户反馈 / 定时任务 / 其他
- **读取方式**：
- **去重规则**：
- **优先级规则**：
- **噪音 / 误报处理**：
- **已消费输入记录**：

## Trigger / Schedule

- **触发方式**：人工 / 定时 / 事件 / 外部平台 / 其他
- **调度位置**：本地机器 / CI / 云端 / 手动 thread / 其他
- **频率 / 时间窗**：
- **并发上限**：
- **重试 / 退避**：
- **本地调度失效边界**：关机、会话、profile、凭据、网络、端口、权限

## Run Queue And State

| Field | Value |
| --- | --- |
| state store |  |
| state schema | queued / running / passed / partial / blocked / failed / skipped |
| current iteration |  |
| queued items |  |
| running items |  |
| blocked items |  |
| consumed inputs |  |
| next-run marker |  |

## Agent Topology

- **Orchestrator / 主线程**：
- **Execution posture**：orchestrator-only / worker-assisted / evaluator-required / blocked
- **Worker agents / 子线程**：
- **Evaluator**：
- **是否使用独立 worktree / 独立线程 / 只读研究**：
- **子 agent 继承规则**：必须读取 Goal / Loop Contract / Run Capsule / AGENTS / owning page

## Subproject Git Preflight

Loop 涉及子工程代码或外部仓库时，每轮 Run Capsule 必须继承并刷新；不涉及则写不适用。

| Field | Value |
| --- | --- |
| directory |  |
| branch / upstream |  |
| remotes |  |
| fetch state | not-run / fetched / blocked |
| ahead / behind / diverged |  |
| dirty / untracked |  |
| local-only risk |  |
| update policy | 默认不 pull / merge / rebase / reset；只有授权且 fast-forward safe 才更新 |

## Worker Ownership

| Worker | Scope | Allowed writes | Required evidence | Limits required | Stop condition |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

Worker 缺少 `limits`、没有回到同一个 Loop Contract，或把局部证据写成整体闭环时，默认不能被 evaluator 采纳为完成。

## Evaluator Oracle

- **oracle 类型**：脚本 / 独立 agent / 人工 reviewer / 真实运行工具 / 组合
- **baseline fail + candidate pass**：
- **before-after evidence**：
- **误报 / 漏报处理**：
- **冲突处理**：
- **passed 条件**：
- **partial 条件**：
- **blocked 条件**：
- **failed 条件**：
- **skipped 条件**：

## Persistence Routing

| Signal | Decision | Landing |
| --- | --- | --- |
| 普通完成，无结构性新信息 | no-op / reply only |  |
| 影响未来理解 | log | [[log]] |
| 用户纠偏 / 检查失败 / 模式切换 / 重复失守 | harness ledger | [[harness-feedback-ledger]] |
| 长 Goal / 多 agent / Loop 收尾复盘信号 | retrospective | [[skills/historical-dialogue-retrospective/SKILL]] |
| 稳定背景 | memory | [[BRAIN]] / [[projects/memory/README]] |
| 可复用流程 | skill | `skills/` |
| 可复制字段 | template | `templates/` |
| 可机器检查 | sensor | `scripts/check_all.py --only loop-engineering` |
| P0 必须 / 禁止行为 | rule | [[AGENTS]] / [[POLICY]] |
| 软件研发候选 | software-development | risk / Issue / TASK / AP / report / service-registry / engineering feedback |

## Software Development Landing

- **候选进入哪里**：Gate / FP / EP / TASK / risk / Issue / AP / report / service-registry / engineering feedback
- **禁止新建平行看板**：
- **状态关闭条件**：
- **人工确认项**：
- **不上推边界**：

## Budget And Safety

- **token / 时间 / 成本预算**：
- **轮次上限**：
- **并发上限**：
- **重试次数**：
- **rollback**：
- **必须停止并汇报的条件**：
- **禁止自动执行的动作**：合并、发布、生产写入、关闭 Gate / FP / EP / TASK / Issue、改高优先级规则

## Next-run Decision

- **本轮状态**：passed / partial / blocked / failed / skipped
- **下一轮动作**：stop / rerun / retry-after / split / escalate / wait-human / schedule-next
- **下一轮触发条件**：
- **Process Record**：本轮消费输入、关键动作、失败项和状态变更落点。
- **Reuse entry proof**：进入 skill / template / sensor / rule 的复用证据；没有则写 no-op。
- **Retrospective trigger decision**：no-op / 轻量复盘 checkpoint / 标准复盘 / 深度复盘
- **需人工确认**：
- **需补 sensor / 模板 / skill / rule**：

## Closeout Proof

- **Loop Contract 状态**：
- **Run Capsule / Worker 回传是否齐全**：
- **Evaluator 结论**：
- **状态持久化位置**：
- **检查 / sensor**：
- **仍需人工确认**：
