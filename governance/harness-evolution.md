---
type: governance
id: GOV-HARNESS-EVOLUTION-001
scope: shared
status: active
source_of_truth: true
updated: 2026-05-28
tags: [agent, harness, feedback, evolution]
---

# Harness Evolution

这页定义当前 wiki 模板级 Agent Harness 的 H5 自演进闭环。[[response-mode-routing]] 负责本轮怎么做，[[harness-feedback-ledger]] 负责把执行中的偏差、纠偏和可复用改进沉淀成可回看的 episode 数据。

## H5 定义

H5 不是“规则更多”，而是让 Harness 可以从真实 episode 中学习。

- 每次用户纠偏、平台假设错误、重复手工检查、明显变慢、模式切换、检查失败或返工，都要判断是否形成 episode 数据。
- episode 数据先进入 [[harness-feedback-ledger]]，不直接晋升成硬规则。
- 长 Goal、Run Capsule、多 agent 或 Loop iteration 收尾时，先进入 [[skills/retrospective-capability/SKILL]]，再按 [[skills/historical-dialogue-retrospective/SKILL#自动触发矩阵]] 判断 no-op / 轻量复盘 checkpoint / 标准复盘 / 深度复盘；只有标准 / 深度复盘或结构性信号才进入 ledger。
- 重复出现、影响面大或已经被 sensor 验证的模式，才进入规则、模板、脚本或技能。
- 已经过期、制造噪音或无法被证据支持的规则，要进入降级 / 删除候选。

## Episode 数据

触发以下任一信号时，优先记录 episode：

- 用户指出 agent 的默认假设错误，例如平台、路径、环境、提交方式、目录归类或权限边界。
- 同一类检查、同步或回写动作在多个回合反复靠人工提醒完成。
- 快速诊断切到沉淀、验收、规则升级或收尾，且切换原因值得复用。
- 工作阶段检查或统一门禁失败，并暴露出规则、模板或 sensor 缺口。
- 复杂 episode 明显变慢，但慢点不是业务事实复杂，而是 Harness 路由、读取、检查或提交闭环不清。
- 复盘触发矩阵被跳过，导致长 Goal、多 agent、Run Capsule / Loop 或重复纠偏没有形成应有 checkpoint / 标准复盘 / 深度复盘。
- 用户指出“只做逐 topic 清单 / 文档复制 / sensor 接线，不等于治理体系全面整改”，说明目标完成口径被子目标偷换；此类 episode 必须回到 [[wiki-governance-system-contract.v1]]，补 agent、workflow、memory、harness、skill、evaluation、governance、template、topic 和 migration 的 owner landing。

最小字段为：触发信号、响应模式、成本类型、用户可见影响、已采取改动、对应 sensor / 模板 / 规则、当前状态。

## 规则晋升

episode 进入规则、模板、脚本或技能前，必须满足至少一项：

- 两次以上相似 episode 指向同一 Harness 缺口。
- 单次 episode 影响提交、远程、验收、用户可见事实保真、目录归类或权限边界。
- 已经能用脚本、模板字段、CI、工作阶段 sensor 或检查命令稳定表达。

晋升顺序默认是：

1. 先补模板字段或 ledger 记录口径。
2. 能脚本化时优先补 sensor。
3. 影响执行顺序时补 [[WORKFLOW]]。
4. 影响 agent 必须 / 禁止行为时补 [[AGENTS]]。
5. 影响自动写入、优先级或裁定边界时补 [[POLICY]]。

## 降级和删除

H5 同时要求清理噪音。以下内容要进入降级 / 删除候选：

- 只被单次场景触发，且没有复用价值的候选规则。
- 已经被脚本或模板覆盖，但仍在多个入口重复陈述的自然语言规则。
- 增加读取成本，却没有在 episode 中发现真实问题的检查项。
- 和当前平台、remote、目录结构或主控边界不再一致的旧适配层。

## 工作节奏

- 工作阶段：按 [[response-mode-routing]] 先判模式，再用 `python3 scripts/check_all.py --only <check-key>` 跑相关 sensor。
- 治理体系全面整改阶段：按 [[wiki-governance-system-contract.v1]] 和 [[templates/governance-system-upgrade-contract-template]] 固定 source coverage、ability extraction、system layer landing、sensor / evaluator、persistence routing 和 closeout proof；专项检查为 `python3 scripts/check_all.py --only governance-system-rectification`。
- Ledger 结构更新后运行 `python3 scripts/check_all.py --only harness-feedback-ledger`；指令遵循覆盖更新后运行 `python3 scripts/check_all.py --only instruction-adherence`；入口、frontmatter 或 wikilink 改动运行 `python3 scripts/check_all.py --only project-docs`。
- 阶段边界：如果发生模式切换、用户纠偏、检查失败或扩大编辑面，回看是否需要写入 [[harness-feedback-ledger]]，再跑相关专项 sensor。
- 收尾阶段：完整门禁、提交和最终回复之后，判断本轮是否产生新的 H5 episode。
- 周期复盘：用 [[templates/harness-evolution-review-template]] 汇总一段时间内的 episode，决定晋升、降级、删除或继续观察。

## 非目标

- 不用 episode 数据自动关闭项目事项、功能点、Gate 或发布节点。
- 不把用户一次性偏好直接写成全局硬规则。
- 不把 memory 当团队单一信息源；可持续规则必须回到本库文件。
- 不让 CI、`.codex/` 或某个平台配置替代 `scripts/check_all.py` 的门禁真相源。
