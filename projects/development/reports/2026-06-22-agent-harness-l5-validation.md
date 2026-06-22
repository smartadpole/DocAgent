---
type: development_test_report
id: REPORT-2026-06-22-AGENT-HARNESS-L5
project: PROJ-WIKI-001
status: passed
updated: 2026-06-22
tags: [report, harness, l5, validation]
---

# Agent Harness L5 Validation

- 验证对象：整体 Agent Harness 体系升级后的可执行性和不上推边界。
- 验证对象类型：代码实现 / 文档 Harness / sensor gate。
- 上游 EP / TASK / FP / Gate / ISSUE：本轮用户纠偏“没有验证的边界必须验证好，达到 L5”。
- 关联回链：[[agent-governance-strategy]]、[[state-constraint-reasoning]]、[[agent-orchestration]]、[[templates/goal-contract-template]]、[[templates/run-capsule-template]]、[[templates/loop-contract-template]]、[[harness-feedback-ledger]]。
- 计划来源 / AP：[[projects/development/reports/README]] 的独立抽查包、关闭裁决包；[[instruction-adherence]] 的 L5 final proof。
- 触发信号：上一轮最终回复把真实运行质量、多 agent 运行质量和子工程 Git 状态写成未验证边界。
- 验收执行包类型：独立抽查包 / 关闭裁决包 / Harness sensor 包。
- 验收对象 / 关闭判据：代表性 Goal、Run Capsule、Harness Evolution 和 Git preflight 均可由本库脚本复跑；局部证据不能上推为真实项目完成。

## 测试方案

1. **Goal Contract dry-run**：构造一个只具备 `local validation / sensor / git readback` 的长时任务样例，要求脚本判定为 `partial`，不能上推到 `service-side validation / end-to-end validation`。
2. **Run Capsule dry-run**：构造 Worker 自称完成但没有 evaluator 的样例，要求脚本判定为 `blocked`；再构造 evaluator 明确 `passed` 的样例，要求脚本才允许关闭。
3. **Subproject Git Preflight live readback**：在当前仓库执行真实 Git preflight，读取 branch、upstream、remote、ahead / behind 和 dirty / untracked 状态，证明 preflight 字段可执行。
4. **Harness Evolution correction route**：检查本轮纠偏已经进入 [[harness-feedback-ledger]]，并有 sensor / promotion route 承接。
5. **L5 final proof**：最终回复必须给出检查命令、结果、commit hash、push readback 和不能上推边界。

## 核心用例 / 检查点

| 用例 | 输入 | 期望 | 结果 |
| --- | --- | --- | --- |
| Goal Contract dry-run | local-only evidence | `partial`，不能上推 | passed |
| Run Capsule dry-run | Worker self-claim without evaluator | `blocked` | passed |
| Run Capsule dry-run | Worker claim + evaluator passed | `passed` | passed |
| Subproject Git Preflight live readback | 当前 repo Git 状态 | branch / upstream / remote / ahead-behind 可读 | passed |
| Harness Evolution correction route | 用户 L5 纠偏 | ledger + sensor 承接 | passed |

## fixture / oracle

- fixture：`scripts/check_agent_harness_l5.py` 内置三个代表性样例；当前 Git 仓库作为 preflight live readback 对象。
- oracle：脚本断言 `local-only` 不能关闭 service / end-to-end，Worker 自评不能关闭整体，Git preflight 字段必须可解析，报告必须包含 L5 final proof。

## 相关功能回归范围

- `scripts/check_all.py --only agent-harness-l5`
- `scripts/check_all.py --only harness-governance,loop-engineering,instruction-adherence`
- 完整 `python3 scripts/check_all.py`
- `git diff --check`

## local validation

- `python3 scripts/check_agent_harness_l5.py`：passed。
- `python3 scripts/check_all.py --only agent-harness-l5`：passed。
- `python3 scripts/check_all.py --only harness-governance,loop-engineering,instruction-adherence`：passed。
- `python3 scripts/check_all.py`：passed。
- `git diff --check`：passed。

## service-side validation

本库是文档 / Harness 仓库，没有运行服务侧 API。对应的 service-side 替代面是 Git remote readback：

- `git rev-list --left-right --count HEAD...@{u}`：上一轮提交后为 `0	0`。
- `git ls-remote origin refs/heads/master`：读回上一轮 commit。
- `git ls-remote hai refs/heads/master`：读回上一轮 commit。

## end-to-end validation

端到端口径为：用户纠偏 -> 新增 L5 sensor -> 报告落地 -> 专项检查 -> 完整门禁 -> 提交 -> push -> remote readback -> 最终回复证明。

本报告和 `scripts/check_agent_harness_l5.py` 覆盖纠偏到检查；提交、push 和 remote readback 在本轮最终回复中给出。

## 本轮独立取证动作

- 读取 [[instruction-adherence]]，确认 L5 是最终回复证明，但本轮需要叠加实际样例验证。
- 新增 `scripts/check_agent_harness_l5.py`，让 Goal / Run / Git preflight / ledger route 可复跑。
- 新增本报告，作为验证证据层，不替代 [[harness-feedback-ledger]] 或 [[log]]。

## 非默认值 / 边界值生效证据

- Goal dry-run 故意缺少 `service-side validation` 和 `end-to-end validation`，脚本必须返回 `partial` 而非 `passed`。
- Run Capsule dry-run 故意让 Worker 自称完成但不提供 evaluator，脚本必须返回 `blocked`。
- Git preflight 不要求工作区干净，只要求读出真实 dirty / untracked 状态；这验证 preflight 能揭示而不是掩盖本地状态。

## 结果

passed。Agent Harness 的 L5 验证面已经从“结构 wiring + 静态 sensor”升级为“代表性样例 dry-run + live Git preflight + ledger route + final proof”。

## 失败项

无。

## 未验证项

无本轮应关闭项。仍不能上推为“未来任意真实长时任务、多 agent 任务或外部子工程都会成功”；这属于通用能力的适用边界，不是本轮升级缺口。

## 待人工确认项

无。

## 不上推边界 / 禁止上推边界

- 本报告证明 Harness 合同、样例和 preflight 可执行，不证明任何具体业务任务已经完成。
- 本报告证明当前 repo Git preflight 可读，不证明所有外部子工程远程状态可靠。
- 本报告证明 Worker 自评被拦截，不证明未来所有 Worker 输出质量都高。
- sensor 证明结构 wiring 和代表性 oracle，不替代人工语义判断、真实服务端验证或业务验收。

## 当前关闭判断

本轮用户指出的“未验证边界必须验证到 L5”已关闭到本库 Harness 能力层：L3 sensor、L4 `check_all` 接入和 L5 final proof 均具备。
