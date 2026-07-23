---
type: governance
id: GOV-AGENT-ORCHESTRATION-001
scope: shared
status: active
source_of_truth: true
updated: 2026-07-23
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

## Governance System Run Capsule

当任务目标是“全面整改 wiki 治理体系”或同时触及 agent、workflow、memory、harness、skill、evaluation、governance、template、topic、migration 多层时，Run Capsule 必须引用 [[wiki-governance-system-contract.v1]]。

最小字段：

| Field | Required |
| --- | --- |
| source coverage | 上游 topic / 下游经验 / 用户纠偏 / 矩阵信号和不可复制边界 |
| ability extraction | 触发条件、事实源、agent behavior、writeback guard、evidence boundary |
| owner landing | 每一层实际写入的 owner、skill、template、memory、ledger 或 sensor |
| evaluator | `governance-system-rectification` 专项、相关专项 sensor、完整 `check_all` 和人工 / external readback 边界 |
| persistence routing | log、harness ledger、project memory、skill、template、sensor、rule 的 needed / no-op / blocked |
| closeout proof | commit、structure-only、insufficient-evidence、runtime / external evaluator 未验证边界 |

如果只完成 topic manifest、摘要矩阵、入口链接或单个 sensor，Evaluator 只能裁决 `partial / review`，不能裁决治理体系全面完成。

## Closeout Proof

收尾时必须说明：

- Run Capsule 状态：passed / partial / blocked / failed。
- Worker 回传是否齐全，缺口在哪里。
- Evaluator 结论和不能上推的证据边界。
- State transition 与 Next-run recommendation。
- Persistence Routing 的实际落点。
- 运行了哪些 sensor；sensor 只证明结构 wiring，不证明真实运行质量。

## Production-Grade Control Plane Hardening

从 DocCustomeranalysis 等实战工程吸收的控制面能力，一旦已经上升到 agent 治理层，就不再只是下游经验，而是本仓实现类工程模板的默认合同。它们包括：

| Capability | Wiki contract | Non-goal |
| --- | --- | --- |
| `agent-finalizer` | 有文件改动、提交、跨仓回传或 scoped closeout 时，必须有范围证明、预存 dirty / residual 分类、post-write check 和最终状态读回；finalizer 可以是脚本、模板字段或人工 evaluator，但不能只靠最终回复自述。 | 不复制某个工程的脚本路径、protected repo 清单或提交数量。 |
| `external-write-boundary` | 主控 / 子工程 / 上游 owner 必须分清 `not authorized / orchestrator-only / explicitly authorized`；能访问文件系统不等于有写授权。 | 不把目标工程事实写进 AcknowledgeBase、wiki 或用户级配置。 |
| `acceptance-governance` | 验收前先冻结对象、测试方案、核心用例、环境路由、人工确认边界和上推边界；局部 smoke、health 或接口回显不能关闭父级 Goal / Gate / Issue。 | 不把下游具体 AP、TASK、Issue 状态复制成本仓状态。 |
| `long-task-progress` | 长 Goal / Loop / Run Capsule 必须可读当前切片、已收集材料、已执行动作、结果 / 阻塞、下一步、证据入口、`blocked_for_done`、`not_blocked_for_implementation` 和 monitoring policy。 | 不把运行中、accepted 或 Worker 自述当整体完成。 |
| production readback | 生产或 runtime 结论必须有 service-side / live readback；本地配置、代码 diff、health 绿灯和局部日志都只能作为辅助证据。 | 不复制具体机器、服务、端口、表名、账号或运行 ID。 |
| performance evidence ledger | 触发性能、吞吐、带宽或容量判断时，使用 [[skills/performance-bandwidth-analysis/SKILL]] 先建立 timing ledger、coverage matrix 和不可上推边界。 | 不把单点 probe、raw transfer 或小样本 smoke 上推成生产容量。 |
| runtime config switch | 触发配置切换时，使用 [[skills/runtime-config-switch/SKILL]] 证明 live service 使用新配置，并写回 service registry / TASK / report / log。 | 不把文件 diff、请求级 override 或 health 当默认配置已切换。 |

这些能力的共性不是“更厚的流程”，而是防止 agent 把容易获得的 proxy evidence 上推为真实闭环。DB / service-side readback 只作为证据分层原则吸收；涉及业务表、账号、DSN、批次前缀或项目持久化 schema 的 DB readback skill 仍保持项目绑定，不进入本仓通用技能层。

## 禁止项

- 不用多 agent 数量替代目标、边界和 evaluator。
- 不让 Worker 修改未授权仓库、事项状态或规则入口。
- 不把子工程 local pass、handoff、自述、accepted / running 或 health 上推成主控闭环。
- 不在没有持久状态、evaluator oracle 和停止条件时伪装成 Loop。
- 不把 DocCustomeranalysis 等下游工程的生产事实、机器、表、运行 ID、项目专属 gate 或脚本路径复制成本仓治理事实。
