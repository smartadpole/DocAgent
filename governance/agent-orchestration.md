---
type: governance
id: GOV-AGENT-ORCHESTRATION-001
scope: shared
status: active
source_of_truth: true
updated: 2026-06-22
tags: [governance, harness, orchestration, run-capsule]
---

# Agent Orchestration

这页定义本库的多 agent / 多线程 / 子工程任务编排口径。核心模型是 `Goal Contract -> Run Capsule -> Orchestrator -> Worker -> Evaluator -> Persistence Routing`。

## 启动条件

满足任一条件时使用 [[templates/run-capsule-template]]：

- 同一目标需要多个 Worker 并行读取、实现、验证或审计。
- 主控库和子工程之间需要明确写入边界、证据层级和回传口径。
- 长时任务已经有 Goal Contract，但单轮运行需要记录 Worker ownership 和 evaluator 合流。
- 结果可能被 health、日志、handoff、自述或局部测试错误上推为整体闭环。

## 角色分工

| Role | 责任 | 禁止项 |
| --- | --- | --- |
| Orchestrator | 固定目标、范围、写入边界、证据层级和关闭条件；合并 Worker 结果 | 不把 Worker 自评直接写成整体完成 |
| Worker | 在授权 scope 内读取、修改或验证，回传证据和未验证边界 | 不宣布整体闭环，不关闭主控事项 |
| Evaluator | 独立判断证据能关闭哪一层、是否需要重试 / 拆分 / 人工确认 | 不用生成者自评替代合流裁决 |

Worker 只交证据，不能宣布整体闭环。

## Subproject Git Preflight

涉及子工程代码前，Orchestrator 或 Worker 必须先记录：

| Field | Required |
| --- | --- |
| directory | 当前工作目录和目标仓库是否一致 |
| branch | 当前分支、upstream 和任务分支关系 |
| remotes | remote 名称和 URL |
| fetch state | fetch 后 ahead / behind / diverged |
| dirty state | 本轮相关改动、预存脏改动和未跟踪文件 |
| local-only risk | 本地领先、未推送或无 upstream 的风险 |
| update policy | 默认不 pull / merge / rebase / reset；只有授权且 fast-forward safe 才更新 |

## Persistence Routing

标准落点枚举：`no-op / log / harness ledger / retrospective / memory / skill / template / sensor / rule`。

| Signal | Landing |
| --- | --- |
| 普通完成且无结构性新信息 | no-op / final reply |
| 影响后续理解的主题化过程 | [[log]] |
| 用户纠偏、检查失败、模式切换、重复失守 | [[harness-feedback-ledger]] |
| 长 Goal / 多 agent / Loop 收尾学习信号 | [[skills/historical-dialogue-retrospective/SKILL]] |
| 稳定背景 | [[BRAIN]] / `projects/memory/README.md` |
| 可复用流程 | `skills/` |
| 可复制字段 | `templates/` |
| 可机器检查 | `scripts/check_all.py --only <check-key>` |
| P0 硬约束 | [[AGENTS]] / [[POLICY]] |

## Closeout Proof

收尾时必须说明：

- Run Capsule 状态：passed / partial / blocked / failed。
- Worker 回传是否齐全，缺口在哪里。
- Evaluator 结论和不能上推的证据边界。
- State transition 与 Next-run recommendation。
- Persistence Routing 的实际落点。
- 运行了哪些 sensor；sensor 只证明结构 wiring，不证明真实运行质量。

## 禁止项

- 不用多 agent 数量替代目标、边界和 evaluator。
- 不让 Worker 修改未授权仓库、事项状态或规则入口。
- 不把子工程 local pass、handoff、自述、accepted / running 或 health 上推成主控闭环。
- 不在没有持久状态、evaluator oracle 和停止条件时伪装成 Loop。
