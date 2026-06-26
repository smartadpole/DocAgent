---
type: template
id: TEMPLATE-RUN-CAPSULE-001
status: active
updated: 2026-06-22
tags: [template, harness, goal, orchestration, evaluator]
---

# Run Capsule 模板

Run Capsule 是 Goal、多 agent、多线程或跨工程长任务的最小运行控制面。它不是项目状态页、验收报告、全局 memory 或每轮必填表；只有当任务需要持续推进、并行 agent、跨工程回传或严格证据合流时才使用。

## 适用性判断

- **是否启用 Run Capsule**：是 / 否
- **触发信号**：Goal / 多 agent / 多线程 / 主控 + 子工程 / 长时验证 / 证据漂移风险 / 其他
- **不启用理由**：
- **当前响应模式**：
- **记录落点**：chat-level / TASK / Issue / AP / handoff / episode package / 其他
- **Parent Loop Contract**：如属于持续循环，链接 [[templates/loop-contract-template]] 或实际 Loop Contract 记录；不属于则写不适用。
- **Run id**：
- **Input discovery item**：本次运行消费的发现项、队列项、issue、CI、监控或用户输入。

## Objective

- **用户最新目标**：
- **Expected final state**：
- **Acceptance criteria**：
- **Out of scope**：
- **Stop / blocked conditions**：

## Agent Topology

- **Orchestrator / 主线程**：
- **Execution posture**：direct-execution / orchestrator-only / worker-assisted / evaluator-required / blocked
- **Worker agents / 子线程**：
- **Acceptance / evaluator thread**：
- **是否使用独立 worktree / 独立仓库 / 只读研究**：
- **并行理由**：
- **不适合并行的部分**：

## Subproject Git Preflight

涉及子工程代码、handoff 或外部仓库时填写；不涉及则写不适用。

| Field | Value |
| --- | --- |
| directory |  |
| branch / upstream |  |
| remotes |  |
| fetch state | not-run / fetched / blocked |
| ahead / behind / diverged |  |
| dirty / untracked |  |
| local-only risk |  |
| update policy | ff-only update；默认不 pull / merge / rebase / reset；只有授权且 fast-forward safe 才更新 |

## Worker Ownership

| Worker | Scope | Allowed writes | Required evidence | Output format | Stop condition |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

Worker 必须继承本次 Goal / Parent Loop Contract / Run Capsule / AGENTS / owning page 的边界；缺少 `limits`、未声明不能上推的证据或把局部通过写成整体闭环时，默认不能用于关闭整体任务。

## Evidence Layers

- **code-level / unit**：
- **functional / business-flow**：
- **service-side**：
- **end-to-end**：
- **non-default / boundary**：
- **related regression**：
- **manual-confirmation**：
- **不能上推的辅助证据**：

## Evaluator

- **Evaluator owner**：主线程 / 验收线程 / 人工 reviewer / sensor / 组合
- **合流规则**：
- **冲突处理**：
- **passed 条件**：
- **partial 条件**：
- **blocked 条件**：
- **failed 条件**：

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
| 可机器检查 | sensor | `scripts/check_all.py --only <check-key>` |
| P0 必须 / 禁止行为 | rule | [[AGENTS]] / [[POLICY]] |

标准路由枚举：`no-op / log / harness ledger / retrospective / memory / skill / template / sensor / rule`。

## Closeout Proof

- **Run Capsule 状态**：passed / partial / blocked / failed
- **Worker 回传是否齐全**：
- **Evaluator 结论**：
- **Process Record**：本轮关键命令、文件变更、决策和失败项落点；不把流水写成事实源。
- **State transition**：queued / running / passed / partial / blocked / failed / skipped
- **Consumed inputs**：
- **Next-run recommendation**：stop / rerun / retry-after / split / escalate / wait-human / schedule-next
- **Retrospective trigger decision**：no-op / 轻量复盘 checkpoint / 标准复盘 / 深度复盘；如由 Worker 提供信号，写明 evaluator 裁决理由
- **Reuse entry proof**：如形成可复用流程，说明进入 skill / template / sensor / rule 的证据；否则写 no-op。
- **沉淀路由及理由**：
- **检查 / sensor**：
- **仍需人工确认**：
