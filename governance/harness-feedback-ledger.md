---
type: governance-ledger
id: GOV-HARNESS-FEEDBACK-LEDGER-001
scope: shared
status: active
source_of_truth: true
updated: 2026-05-25
tags: [agent, harness, feedback, episode]
---

# Harness Feedback Ledger

这页记录当前 wiki 模板级 Harness 的 episode 数据、sensor backlog 和规则晋升队列。判断规则见 [[harness-evolution]]，执行路由见 [[response-mode-routing]]。

## 记录规则

- 只记录能反哺 Harness 的结构性信号，不记录普通项目流水。
- 用户纠偏优先记录原始纠偏点，再记录 agent 侧改动。
- 一条 episode 可以先是 `observed`，等有 sensor、模板或规则承接后再改为 `promoted`。
- 不能因为写入 ledger 就自动升级 [[AGENTS]]、[[POLICY]] 或关闭任何项目事项。

## Episode Ledger

| 日期 | Episode | 触发信号 | 响应模式 | 成本类型 | 已采取改动 | Sensor / Artifact | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-25 | 响应效率治理入口 | 简单诊断容易直接进入完整治理闭环 | 规则升级 | 可优化成本 | 新增 [[response-mode-routing]]，拆分快速诊断、沉淀、验收、规则升级和子工程回传 | [[templates/harness-adoption-template]] | promoted |
| 2026-05-25 | DocCustomeranalysis Harness 反哺 | 用户指出同定位工程的 harness 设计和系统流程更健全 | 规则升级 | 可优化成本 | 新增 [[harness-evolution]]、本 ledger、episode / evolution 模板、`.codex/AGENTS.md` 和统一检查脚本 | `python3 scripts/check_all.py --only harness-governance` | promoted |

## Sensor Backlog

| 候选项 | 触发来源 | 拟补 sensor / 模板 | 当前状态 |
| --- | --- | --- | --- |
| Markdown / wikilink / frontmatter 检查 | 多入口文档库容易出现链接和元数据漂移 | 后续可补 `scripts/check_project_docs.py` 或扩展 `check_harness_governance.py` | observed |
| 技能质量检查 | 技能页可能复制项目事实或缺少触发 / 输出边界 | 后续可补技能结构检查 | observed |
| 模板完整性检查 | 新增模板后可能忘记挂入口或字段漂移 | 当前由 `check_harness_governance.py` 覆盖 Harness 模板入口 | active |
| 规则降级 / 删除提醒 | 自然语言规则可能继续膨胀 | 周期复盘时用 [[templates/harness-evolution-review-template]] 标记 stale / noisy 规则 | observed |

## Rule Promotion Queue

| 候选规则 | 来自 episode | 晋升目标 | 状态 |
| --- | --- | --- | --- |
| 工作阶段跑专项 sensor，收尾和提交前跑完整门禁 | DocCustomeranalysis Harness 反哺 | [[harness-evolution]] / `scripts/check_all.py` | promoted |
| H5 episode 不直接晋升硬规则，先进入 ledger 和复盘 | DocCustomeranalysis Harness 反哺 | [[harness-evolution]] | promoted |
| 规则不能只停在自然语言，重复失守要升级为模板字段、sensor、技能或最终证明 | DocCustomeranalysis Harness 反哺 | [[response-mode-routing]] / [[WORKFLOW]] / `scripts/check_harness_governance.py` | active |

## Rule Prune Queue

| 候选清理 | 原因 | 当前状态 |
| --- | --- | --- |
| 多处手写检查脚本清单 | 已由 `scripts/check_all.py --list` 和 `--only` 承接 | observed |
| 已被 sensor 覆盖的重复自然语言规则 | 避免入口页继续膨胀 | observed |
