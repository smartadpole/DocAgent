---
name: loop-engineering
description: 构建跨 run 持续发现、去重、调度与恢复的循环控制；需要稳定来源、持久状态、评价依据及预算停止条件，普通长任务不触发。
maturity: mature
evidence_signals: [skill, README entry, template, governance, verification-loop, sensor, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only loop-engineering
conditional_sources: [skills/loop-engineering/references/delegated-runs.md]
---

# Loop Engineering

仅在需要持续发现新输入、维护去重 Run queue、持久化状态并由 Scheduler / trigger 调度时使用。普通“继续直到完成”、一次多 agent 合作或长任务不需要 Loop。

## 启动与控制面

先复用现有 owner，按 [[templates/loop-contract-template]] 补齐真正需要的控制字段：

- Discovery source：来源与可重复读取边界。
- Run queue：去重标识、排序和 queued/running/passed/partial/blocked/failed/skipped 转换。
- Persistent state：消费游标、结果证据和恢复位置。
- Evaluator oracle：可复核脚本、真实运行读回、独立 reviewer 或人工裁决。
- Scheduler / trigger：实际触发环境与失效方式。
- Budget / stop：时间、轮次、重试退避、并发和停止条件。
- 写入范围、人工确认边界、回滚以及结果 owner。

缺关键来源、状态或 oracle 时只能 not-ready / discovery-only，不能启动写入型循环。调度配置不等于可靠运行，本地机器/会话/profile 失效要进入边界。

## 执行与恢复

每轮读取新输入、去重、在授权范围执行、按 oracle 判结果，持久化消费项、状态转换、证据和 next-run decision：stop / rerun / retry-after / split / escalate / wait-human / schedule-next。失败原因和恢复游标应足以避免重复副作用；停机/预算耗尽时不伪报完成。

单 agent 可承担循环，角色和代理数量不是能力要求。确需委派且已有授权时才读取 [[skills/loop-engineering/references/delegated-runs]]。Run Capsule 仅用于独立运行身份、恢复或合流需要，不强制另建 Goal；Goal 工具仍需用户明确要求。

评价与生成相分离：自评、Worker 自述、health、PR 已开、accepted/running 或测试全绿不能替代合同要求的结果证据。确定性 oracle 适用时不额外强制模型评审。

## 状态与权限

Loop 是控制面，不是第二套项目看板。业务状态回写既有 TASK、Issue、risk、报告或服务 owner。只有发现真实可复用增量或结构性失守才做复用/复盘判断，不要求每轮空 no-op 回执。

Loop 本身不授权无人值守外部写入、合并、发布、生产变更或关闭父级事项；按已有授权与各 owner 的证据条件执行。跨仓更新保护 dirty 和分叉历史，不默认 pull/merge/rebase/reset。

相关验证：`python3 scripts/check_all.py --only loop-engineering`；它验证控制面接线，实际循环须以恢复、停止与结果证据证明。迁移见 [[skills/loop-engineering/TRANSFER]]。
