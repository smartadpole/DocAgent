---
type: governance
id: GOV-AGENT-GOVERNANCE-STRATEGY-001
scope: shared
status: active
source_of_truth: true
updated: 2026-06-22
tags: [governance, harness, agent, strategy]
---

# Agent Governance Strategy

这页回答“规则要管到什么强度”。它不是新规则总集，而是防止 Harness 把所有问题都推成重治理、全量检查、强制 log 或新模板的分级器。

## 分级模型

| Level | 含义 | 典型动作 |
| --- | --- | --- |
| P0 hard constraint | 不遵守会造成错误写入、越权、数据污染或用户明确禁止 | 写入 [[AGENTS]] / [[POLICY]]，必要时补 sensor |
| P1 semantic gate | 不判断会让执行合同、证据层级或状态关闭漂移 | 写入 [[WORKFLOW]]、模板字段或专项检查 |
| P2 workflow default | 多数情况下有益，但可按响应模式和成本预算裁剪 | 写入 [[response-mode-routing]]、技能流程或模板提示 |
| P3 backlog / idea | 只有观察到重复 episode 或可脚本化价值后才晋升 | 写入 [[harness-feedback-ledger]] 或复盘 |

## 常见降级判断

- `log eligibility`：实质内容或结构变化才必须写 [[log]]；纯本地状态、临时缓存或无长期价值的试探不强制记录。
- `check budget`：工作阶段优先跑专项 sensor；入口、规则或提交前再跑完整 `python3 scripts/check_all.py`。
- `Goal Contract`：只用于长时、跨轮、证据敏感或主控 / 子工程回传任务；普通一次性任务不套合同。
- `template feedback`：下游经验默认进入候选判断，不表示原样写入模板。
- `retrospective`：复盘是学习资产，不是每次测试通过或 Issue 关闭后的固定动作。

## Cross-Project Governance Audit Guard

跨工程治理审计属于 P1 semantic gate：它可以生成 Project Governance Audit 和 handoff-ready 任务书，但不能用矩阵、文件存在或 Worker 自述替代目标工程 runtime validation。

最小字段如下：

| Field | Contract |
| --- | --- |
| `audit_id` | `CPGA-YYYY-MM-DD-<project>` |
| `audit_month` | `YYYY-MM` |
| `skill` | `cross-project-governance-audit` / `Cross-Project Governance Audit` |
| `git preflight` | 读取 `git remote -v`、`git fetch --all --prune` 和 ahead / behind / diverged；不可读时写 blocked |
| `source-depth` | 说明读到入口、治理页、技能、TRANSFER、template、sensor、report、matrix 还是只读表层文件 |
| `handoff-ready` | 只表示建议可交给目标工程 agent 执行，不代表目标工程已修复、已提交或已验收 |
| `skill-transfer` | 只吸收触发条件、事实源分层、输出格式、验证和禁止项 |
| `Transfer Manifest` | 写明 can absorb / abstract only / must not copy |
| `non-reference` | 业务事实、运行 ID、服务实例、生活项目、backlog 状态、一次性 source revision 和排名不得写成本库通用事实 |
| `Drift Report` | true-gap / recognition-gap / signal-only-gap |
| `verification-loop` | 记录本轮可复跑检查；缺 runtime validation 时写 no runtime validation |

深度审计还要写证据计划、深度等级、触发优先级、完整产物、行动 owner、检查方式、完成口径、上层抽象和举一反三；这些字段只在审计对象需要时启用，不把一次轻量检查升级成重治理。

## 使用流程

1. 先按 [[response-mode-routing]] 判断当前响应模式。
2. 对新增或升级规则标注 P0 / P1 / P2 / P3。
3. 判断是否已有等价规则、模板或 sensor，优先增强旧入口。
4. 如果是单次偏差，优先写 [[harness-feedback-ledger]]，不要直接升硬规则。
5. 如果重复、影响面大或能被机器检查，才晋升为 template / sensor / skill / rule。

## 输出口径

```markdown
- Signal:
- Proposed rule / field / sensor:
- Level: P0 / P1 / P2 / P3
- Landing:
- Why not heavier:
- Why not lighter:
- Review / prune condition:
```

## 禁止项

- 不把所有建议都升级成 [[AGENTS]] 或 [[POLICY]] 硬规则。
- 不因为一次用户纠偏就扩大成全库重治理。
- 不用完整检查替代专项检查预算。
- 不让模板字段、sensor 或复盘要求成为普通问答的隐形负担。
