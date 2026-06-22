---
name: goal-contract
description: 长时任务完成契约技能。用于终点清楚但路径需要探索、可能跨多轮推进、跨工程回传或证据边界敏感时，先固定目标、范围、验收面、证据层级、预算、停止条件和记录落点。
maturity: active
evidence_signals: [skill, README entry, template, governance, TRANSFER, verification-loop, quality-gate]
transfer_ready: true
sensor: python3 scripts/check_all.py --only skill-maturity
---

# Goal Contract

## 定位

Goal Contract 是本仓库的长时任务完成契约能力，位置固定在 [[response-mode-routing]] 完成响应模式判断之后、正式长时执行之前。

它只回答“这一轮到底怎样才算完成、用哪些证据证明、何时停止或阻塞汇报”。它不替代项目状态、验收报告、TASK / Issue 关闭标准、[[templates/run-capsule-template]]、[[BRAIN]]、[[POLICY]] 或人工确认。

## 触发场景

- 用户要求持续推进、长时间执行、反复验证、跨多轮跟进或“未解决不允许停”。
- 任务终点清楚，但实现、排障、迁移、调研、复验或跨工程回传路径需要探索。
- 本轮需要区分 implementation scope、evidence scope 和 closure scope。
- 多 agent、主控 / 子工程、实现 / 验收分工容易把局部证据上推成完整闭环。
- health、日志、accepted / running、自述、handoff 或历史报告可能被误当作完成证据。

普通一次性问答、短命令、简单改文档、范围尚未裁定的探索，不默认启动 Goal Contract。

## 成熟度与证据信号

- `skill`：本页定义触发、流程、输出格式和禁止项。
- `template`：合同字段骨架在 [[templates/goal-contract-template]]，多 agent / 多线程运行细节进入 [[templates/run-capsule-template]]。
- `governance`：响应模式和证据边界由 [[WORKFLOW]]、[[execution-contract-semantics]]、[[harness-evolution]] 和 [[harness-feedback-ledger]] 共同约束。
- `TRANSFER`：迁移边界见 [[skills/goal-contract/TRANSFER]]。
- `sensor`：当前由 `skill-maturity`、`harness-governance` 和完整 `check_all` 覆盖结构接线；它只能证明 wiring，不证明某次任务真实完成。
- `evidence boundary`：Goal Contract 是完成契约，不是完成结论。

## 工作流

1. 判适用性：说明为什么这不是普通一次性任务；不适用时直接说明原因，不创建空合同。
2. 建立合同：使用 [[templates/goal-contract-template]] 写清 objective、expected final state、scope、acceptance criteria、verification surface、evidence layers、budget、stop conditions 和 closure boundary。
3. 绑定记录落点：chat-level、TASK、Issue、AP、handoff、episode package 或其他 owning page；不能只靠最终回复成为长期事实源。
4. 记录 Pipeline trace：写清用户目标、source pack、执行位置、Run Capsule / handoff、验证面和沉淀落点之间的链路。
5. 多 agent 或子工程任务进入 [[agent-orchestration]]：使用 [[templates/run-capsule-template]] 固定 Orchestrator、Worker、Evaluator、Subproject Git Preflight 和 Worker 不能上推的证据边界。
6. 执行中校准：每轮继续前回看合同，不让中间日志、health、子工程自述或矩阵分数改写目标。
7. 合流验证：关闭前逐条检查 acceptance criteria，区分完成证据、辅助证据、不能上推的证据和仍需人工确认项。
8. 收口沉淀：按 [[agent-governance-strategy]] 和 [[harness-evolution]] 判断 Method capture decision、Persistence landing、Reuse decision、Retrospective trigger decision 是否进入 log、ledger、memory、skill、template、sensor、rule 或 retrospective。

## 输出格式

```markdown
## Goal Contract

- Objective:
- Expected final state:
- In scope:
- Out of scope:
- Source pack:
- Acceptance criteria:
- Evidence layers:
- Verification surface:
- Record landing:
- Pipeline trace:
- Method capture decision:
- Persistence landing:
- Reuse decision:
- Iteration budget:
- Stop / blocked conditions:
- Closure boundary:
```

## 禁止项

- 不把 Goal Contract 当项目状态、验收报告、规则页、memory 或普通业务 skill。
- 不把 health、日志、任务 accepted / running、子工程 handoff、自述、历史报告或矩阵分数上推成完成证据。
- 不用 Goal Contract 替代 EP / TASK / FP / Gate、Issue 或 AP 的关闭标准。
- 不在目标不清、范围未裁定或普通一次性任务上强行套模板。
- 不把未来扩展目标、上线目标、全量跑批或额外优化反写成本轮阻塞。
