---
name: goal-contract
description: 为明确要求独立完成契约，或现有 owner 无法承接的持久恢复、依赖和累计预算建立 Goal Contract；普通持续执行不触发。
maturity: mature
evidence_signals: [skill, README entry, template, governance, TRANSFER, verification-loop, quality-gate]
transfer_ready: true
sensor: python3 scripts/check_all.py --only skill-maturity
---

# Goal Contract

先复用当前 owner 的目标、授权、验收与停止条件。只有用户明确要求独立合同，或必要的持久恢复、依赖控制、累计预算无法由原 owner 承接时，才建立独立记录。任务复杂、多轮或“继续做到完成”本身不构成触发。

Goal 工具仅在用户明确要求 Goal 时调用；文档合同不等于工具授权。Run Capsule 仅用于真实运行身份、恢复游标或跨角色合流需要；Loop 另须持续发现源与持久队列。

## 完成契约

使用 [[templates/goal-contract-template]] 补充缺项，已有字段引用 owner：最终状态、范围、验收条件、验证面、适用证据层、预算、停止/阻塞条件与记录落点。依任务区分实现、研究判断、只读 trace 或方法候选，不把结构识别当成实现完成。

选取能证明目标的 code-level / functional / service-side / end-to-end / non-default / manual-confirmation 证据层；并非所有任务都需要每层。缺失适用证据时明确 partial / blocked，不能用 health、accepted/running、自述或历史报告代替本轮结果。

继续执行时按实际目标变化校准，关闭前逐项对照验收。合同不能替代 TASK / Issue / EP / FP / Gate 的正式关闭标准，不将未来扩展、全量上线或额外优化反写成本轮阻塞。

## 记录与验证

合同和证据落在现有 TASK、Issue、AP、handoff 或等价 owner；不要形成第二状态源。只有发生可复用方法或结构性问题时才进入 [[harness-evolution]]。协作确有需要时读取 [[agent-orchestration]]，不预建角色和回执。

结构验证：`python3 scripts/check_all.py --only skill-maturity,harness-governance`；真实完成由任务验收证据证明。迁移见 [[skills/goal-contract/TRANSFER]]。
