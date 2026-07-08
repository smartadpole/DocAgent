---
type: governance
id: GOV-INSTRUCTION-ADHERENCE-001
scope: shared
status: active
source_of_truth: true
truth_scope: instruction_adherence_execution_coverage
updated: 2026-05-28
tags: [agent, harness, instruction-following]
---

# 指令遵循治理

这页回答一个单独问题：规则已经存在时，如何让它稳定进入执行路径。它不是新的规则总表，而是 [[AGENTS]]、[[WORKFLOW]]、[[POLICY]] 和模板 / sensor 的执行覆盖层。

核心判断：

> 重大规则不能长期停在自然语言。重复失守、影响证据 / 验收 / 提交 / 权限 / 用户原始事实的规则，必须升级为触发信号、模板字段、sensor、统一门禁或最终回复证明。

## 边界

- 本页只管“已有规则怎样被触发、检查和证明”，不单独改变 TASK、issue、EP、FP、Gate、测试、验收或发布语义。
- 如果执行覆盖升级暴露出原规则本身需要改变，回到对应 source of truth 页面正式修改。
- [[governance/execution-contract-semantics|执行合同语义]] 负责裁决“当前执行合同是否被参考规则、非目标或证据说明污染”；本页只负责把这种失守接入触发矩阵、模板字段和 sensor。
- 快速诊断只减少读取面和默认写入面，不削弱命中的 always-on guard。

## Rule Coverage Ladder

| 层级 | 形态 | 可靠性 |
| --- | --- | --- |
| L0 | 自然语言规则 | 最低，靠注意力 |
| L1 | 触发矩阵 | 明确什么信号触发什么动作 |
| L2 | 模板字段 / checklist | 写作时有固定坑位 |
| L3 | 本地 sensor / check 脚本 | 可机器识别的失守直接红灯 |
| L4 | 统一门禁 / CI 复跑 | 防止绕过本地检查入口 |
| L5 | 最终回复证明 | 用户能看到检查、提交、未验证边界和例外原因 |

重复出现两次以上，或单次影响 P0 事实、证据、验收、提交、权限边界的规则，至少升到 L1 + L2；能脚本化的必须升到 L3。

## 触发矩阵

| 触发信号 | 必须执行 | 当前可检查点 | 人工语义边界 |
| --- | --- | --- | --- |
| 本轮产生实际文件变更 | 更新 [[log]]、跑相关 sensor、收尾跑 `python3 scripts/check_all.py`、区分本轮改动和预存脏改、提交或说明例外 | [[WORKFLOW]] / `scripts/check_all.py` | 哪些脏改属于本轮 |
| 用户提供截图、日志、接口响应或运行输出 | 在 issue / incident / 报告里转成结构化证据；拿不到原始二进制时写明原因和待补路径 | 模板字段 / 项目文档检查 | 当前工具是否真实取得原图 |
| 用户要求验收、复验、关闭、准出或写 `done` | 先锁定验收对象、测试计划来源、证据层级、人工确认边界和不上推边界 | [[projects/development/plan/test-acceptance-planning-model]] / [[projects/development/reports/README]] | 证据是否足以关闭当前层级 |
| 执行页出现“默认不需要，但如果”、`可选 / 视情况 / 后续可能` 或非目标展开 | 按 [[governance/execution-contract-semantics]] 上移参考规则，当前事项只保留单值裁决 | `scripts/check_execution_contract_semantics.py` | 该句是否承担当前执行裁决 |
| 用户指出规则没有被遵循 | 写入或更新 [[harness-feedback-ledger]]，判断是否晋升模板 / sensor / 流程 | [[harness-evolution]] | 一次性失误还是可复用缺口 |
| 规则改动或规则迁移 | 做原始规则保全，判断补充、澄清、弱化、替换或冲突 | [[POLICY]] / [[template-feedback-rules]] | 改动是否降低旧规则强度 |

## 当前 sensor 覆盖

- `scripts/check_instruction_adherence.py` 检查本页触发矩阵、边界、收尾证明、ledger 回链和 `scripts/check_all.py` 接线，避免规则执行覆盖只停在自然语言。
- `scripts/check_harness_feedback_ledger.py` 检查 [[harness-feedback-ledger]] 的四张表、状态词表、active episode、sensor backlog 和晋升来源回链。
- `scripts/check_project_docs.py` 检查 wiki 入口页、治理元数据和本地 wikilink，避免入口漂移或链接断裂。
- `scripts/check_harness_governance.py` 仍检查整体 Harness wiring、主动对话、Goal Contract、模板和治理入口；新拆出的专项 sensor 负责细颗粒度红灯。
- 这些 sensor 只能覆盖结构和可见文本；证据是否足以关闭、规则是否该晋升、一次性偏好是否值得沉淀，仍由本页、[[harness-evolution]] 和人工语义判断共同裁定。

## 提交闭环防漏

只要本轮产生实际文件变更，最终回复前按固定顺序：

1. 运行相关专项 sensor；收尾或提交前运行 `python3 scripts/check_all.py`。
2. 运行 `git status --short`，区分本轮同主题改动和预存无关改动。
3. 用户没有明确禁止提交时，提交本轮同一主题改动；无法提交时写出具体例外原因。
4. 提交后再次检查状态和 `git log -1 --oneline`；最终回复给出 commit hash 和剩余脏改归属。

## 规则瘦身判定

规则瘦身不是删掉防线，而是把同一条防线放到更合适的执行层：

- P0 事实、证据、验收、提交、权限防线保留。
- 已经有 owning page 的规则，入口页只保留短触发和回链。
- 已经被模板字段或 sensor 覆盖的重复正文，进入 [[harness-feedback-ledger]] 的 Rule Prune Queue。
- 没有 episode、失守样本或用户可见风险的重检查，先标 `observed`，等待周期复盘。

## 收尾证明

重大规则遵循不以“我记住了”收尾。最终回复至少说明：

- 本轮响应模式和是否切换到规则升级 / 验收 / 收尾。
- 改了哪些治理页、模板或 sensor。
- 跑了哪些检查，结果是什么。
- 是否提交；未提交时说明例外。
- 哪些已被 sensor 覆盖，哪些仍是人工语义边界。
