---
name: goal-contract
description: 为明确要求 Goal 或确需独立持久恢复、依赖与累计预算的任务建立完成契约；复用现有 owner，普通继续执行不自动创建 Goal 或 Loop。
maturity: mature
evidence_signals: [skill, README entry, template, governance, TRANSFER, verification-loop, quality-gate]
transfer_ready: true
sensor: python3 scripts/check_all.py --only skill-maturity
---

# Goal Contract

## 定位

Goal Contract 是本仓库的长时任务完成契约能力，在 [[response-mode-routing]] 完成模式判断且命中启动条件后使用。

它只回答“这一轮到底怎样才算完成、用哪些证据证明、何时停止或阻塞汇报”。它不替代项目状态、验收报告、TASK / Issue 关闭标准、[[templates/run-capsule-template]]、[[BRAIN]]、[[POLICY]] 或人工确认。

## 启动条件

先复用当前 owner 的目标、授权、验收和停止条件。只有用户明确要求独立完成契约，或持久恢复、依赖控制、累计预算确需独立记录且原 owner 无法承接时，才建立 Goal Contract。普通持续执行、复杂排障、跨多轮验证或区分证据层级，本身均不构成启动条件。

Goal 工具仅在用户明确要求 Goal 时调用；需要文档合同不等于获准创建 Goal 工具对象。仅“持续做到完成”时直接继续已有任务。

Run Capsule 仅在独立运行身份、恢复游标或跨角色合流确有需要时建立；Loop 须有跨 run 发现源与持久队列。

## 成熟度与证据信号

- `skill`：本页定义触发、流程、输出格式和禁止项。
- `template`：合同字段骨架在 [[templates/goal-contract-template]]，多 agent / 多线程运行细节进入 [[templates/run-capsule-template]]。
- `governance`：响应模式和证据边界由 [[WORKFLOW]]、[[execution-contract-semantics]]、[[harness-evolution]] 和 [[harness-feedback-ledger]] 共同约束。
- `TRANSFER`：迁移边界见 [[skills/goal-contract/TRANSFER]]。
- `sensor`：当前由 `skill-maturity`、`harness-governance` 和完整 `check_all` 覆盖结构接线；它只能证明 wiring，不证明某次任务真实完成。
- `evidence boundary`：Goal Contract 是完成契约，不是完成结论。
- `maturity`：`mature`。本技能已有完成契约、模板、Run Capsule 接线、主控 / 子工程分工、证据不上推边界和结构 sensor；真实闭环仍必须由本轮验收对象的 local / service-side / end-to-end / manual-confirmation 证据证明。

## 工作流

1. 判适用性：确认现有 owner 无法承接的具体需要；不适用时继续原任务，不创建空合同。
2. 建立合同：复用已有字段，仅使用 [[templates/goal-contract-template]] 补充缺项，写清 objective、expected final state、scope、acceptance criteria、verification surface、evidence layers、budget、stop conditions 和 closure boundary。
3. 选择证据层级：按任务性质声明 `code-level / unit`、`functional / business-flow`、`service-side`、`end-to-end`、`non-default / boundary` 和 `manual-confirmation` 是否适用；缺哪一层就写 partial / blocked，不能用结构检查替代真实证据。
4. 标注合同类型：`implementation-goal`、`trace-only`、`method-candidate`、`research-decision` 或 `orchestrator-acceptance`，避免把方法沉淀、矩阵识别或只读 trace 误当成实现完成。
5. 绑定记录落点：chat-level、TASK、Issue、AP、handoff、episode package 或其他 owning page；不能只靠最终回复成为长期事实源。
6. 记录 Pipeline trace：写清用户目标、source pack、执行位置、Run Capsule / handoff、验证面和沉淀落点之间的链路。
7. 需要独立运行身份、恢复或跨角色合流的任务进入 [[agent-orchestration]]：使用 [[templates/run-capsule-template]] 固定 Orchestrator、Worker、Evaluator、Subproject Git Preflight 和 Worker 不能上推的证据边界。
8. 执行中校准：每轮继续前回看合同，不让中间日志、health、子工程自述或矩阵分数改写目标。
9. 合流验证：关闭前逐条检查 acceptance criteria，区分完成证据、辅助证据、不能上推的证据和仍需人工确认项。
10. 收口沉淀：按 [[agent-governance-strategy]] 和 [[harness-evolution]] 判断 Method capture decision、Persistence landing、Reuse decision、Retrospective trigger decision 是否进入 log、ledger、memory、skill、template、sensor、rule 或 retrospective。

## 输出格式

仅使用 [[templates/goal-contract-template]] 的适用字段；目标、授权和验收引用已有 owner，不在本技能复制第二份模板。

## 禁止项

- 不把 Goal Contract 当项目状态、验收报告、规则页、memory 或普通业务 skill。
- 不把 health、日志、任务 accepted / running、子工程 handoff、自述、历史报告或矩阵分数上推成完成证据。
- 不用 Goal Contract 替代 EP / TASK / FP / Gate、Issue 或 AP 的关闭标准。
- 不在目标不清、范围未裁定或普通一次性任务上强行套模板。
- 不把未来扩展目标、上线目标、全量跑批或额外优化反写成本轮阻塞。
