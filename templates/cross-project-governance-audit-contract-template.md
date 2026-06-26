---
type: template
id: TEMPLATE-CROSS-PROJECT-GOVERNANCE-AUDIT-001
status: active
updated: 2026-06-26
tags: [template, cross-project-governance-audit, governance, audit, handoff]
---

# Cross-Project Governance Audit Contract Template

用于生成跨工程治理审计报告或 handoff-ready 任务书。它只承接系统层治理证据，不复制目标工程业务事实、运行 ID、服务实例、队列、生活项目状态或一次性 handoff。

## Audit Header

- **audit_id**：`CPGA-YYYY-MM-DD-<project>`
- **audit_month**：`YYYY-MM`
- **target_project**：
- **mode**：single-project / multi-project / self-audit / handoff-ready
- **Cross-Project scope**：
- **Project Governance Audit objective**：
- **not in scope**：

## Source Depth

| Layer | Read? | Evidence | Gap |
| --- | --- | --- | --- |
| AGENTS / root rules |  |  |  |
| governance routing |  |  |  |
| Goal Contract / Run Capsule / Loop Engineering |  |  |  |
| skills / TRANSFER / skill-transfer |  |  |  |
| templates / Transfer Manifest |  |  |  |
| sensors / `python3 scripts/check_all.py --only harness-governance` |  |  |  |
| git preflight / `git remote -v` / `git fetch --all --prune` |  |  |  |
| reports / handoff / log |  |  |  |

## Drift Report

- **true-gap**：
- **recognition-gap**：
- **signal-only-gap**：
- **non-reference**：项目事实、业务状态、一次性分数、旧 source revision、服务路径和运行 ID 不进入通用规则。
- **no runtime validation**：文件检查、矩阵刷新、sensor 通过和 Worker 自述都不能替代目标工程真实运行验收。

## Handoff-Ready Taskbook

- **handoff-ready**：yes / no / partial
- **目标工程结构自检**：
- **allowed writes**：
- **操作步骤**：
- **verification-loop**：
- **expected evidence**：
- **action owner**：
- **行动 owner**：
- **检查方式**：
- **完成口径**：
- **blocked / wait-human 条件**：

## Transfer Manifest

- **source capability**：
- **can absorb**：
- **abstract only**：
- **must not copy**：
- **上层抽象 / 可复用模式**：
- **举一反三 / 同类风险**：
- **artifact completeness**：审计报告、任务书、验证命令、未验证边界和最终回传是否齐全。

## Closeout

- **verification commands**：
- **runtime validation boundary**：
- **next action**：no-op / log / harness ledger / skill / template / sensor / rule / wait-human
- **final reply requirements**：
