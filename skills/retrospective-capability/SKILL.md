---
name: retrospective-capability
description: 复盘能力总技能。用于把项目交付、软件研发链、历史对话、Agent 工作流、Harness episode 和治理自演进复盘收敛到同一套复盘合同、深度分级、证据计划、子项路由、行动兑现回检、行动分流和升级边界；子项可以有执行技能，但对外统一按 retrospective-capability 入口调用和迁移。
maturity: leading
evidence_signals: [skill, README entry, template, governance, sensor, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only retrospective-system,skill-maturity
---

# Retrospective Capability

## 定位

本技能是当前 wiki 的复盘总入口。它把“复盘”固定为一套可持续运行的能力系统，而不是散落的目录、模板、概念页或历史对话技巧。

项目交付复盘、软件研发链复盘、历史对话复盘、Agent 工作流复盘、Harness episode 复盘和治理自演进回看都属于本技能的内部子项。子项可以有独立执行技能来提高覆盖面，但对外调用、跨工程迁移和成熟度评估时，统一按 `retrospective-capability` 这一项看。

## 成熟度与证据信号

- `maturity`：`leading`。当前体系具备总技能、交付复盘子技能、历史对话子技能、复盘档案入口、通用模板、治理接线、专项 sensor 和迁移边界。
- `template`：复盘正文骨架在 [[templates/project-retrospective-template]]，本技能只维护复盘合同和子项路由，不复制模板正文。
- `governance`：复盘触发、深度分级、行动分流和治理自演进分别回到 [[response-mode-routing]]、[[WORKFLOW]]、[[POLICY]]、[[harness-evolution]] 和 [[harness-feedback-ledger]]。
- `sensor`：`python3 scripts/check_all.py --only retrospective-system,skill-maturity` 检查总 skill、子 skill、模板字段、入口接线和单一信息源边界。
- `TRANSFER`：跨工程吸收边界见 [[skills/retrospective-capability/TRANSFER]]。
- `evidence boundary`：本技能只证明复盘体系可运行，不替代项目验收、Issue / 事故主档案、测试报告、状态关闭或发布准出。

## 触发场景

- 用户要求“复盘”“写复盘”“沉淀复盘”“总结教训”“举一反三”。
- 项目、阶段、里程碑、发布、事故、Issue 后专题、长 Goal、多 agent、Run Capsule、Loop iteration 或复杂规则升级结束。
- 实际结果和原始目标出现偏差、返工、验收失败、协作失灵、漏验证、漏提交、漏沉淀或重复失守。
- 结论会影响后续需求判断、设计、研发实践、测试验收、运行治理、模板、skill、sensor 或规则。

普通一次性问答、小修小改、无结构性新信息且用户没有显式复盘请求时，可以 `no-op`；不要把复盘仪式化成每轮必做。

## 响应模式

先按 [[response-mode-routing]] 判断本轮模式：

- 显式“复盘 / 写复盘 / 沉淀复盘”：默认标准复盘并落档到 [[projects/retrospectives/README]]，除非用户明确说只口头、不写文件或先分析。
- 显式“深度 / 完整 / 全面复盘 / 为什么没有自动做好 / 举一反三”：进入深度复盘；首轮目标、用户纠偏序列、原始 session / rollout 证据计划、git / diff / 检查输出和上层抽象都必须纳入。
- 自动触发：长 Goal、多 agent、Run Capsule、Loop 或复杂规则升级收尾时，由 evaluator 在 `no-op / 轻量复盘 checkpoint / 标准复盘 / 深度复盘` 中裁决，并说明为什么没有升降级。
- 影响验收、关闭、发布或 Gate 准出时，先切到验收关闭；复盘不能替代关闭裁决。

## 统一复盘合同

启动前先固定：

- **复盘对象**：项目、阶段、发布、事故、Issue、交付链、历史对话、Agent 工作流、Harness episode 或治理主题。
- **复盘目标**：找目标偏差、解释交付结果、还原工作链、校准行动分流、评估 agent 质量，还是判断规则 / 模板 / sensor 是否失效。
- **深度等级**：`no-op / 轻量复盘 checkpoint / 标准复盘 / 深度复盘`；显式复盘请求默认不低于标准复盘。
- **证据计划**：哪些来源能直接证明事实，哪些只是整理记录或推论，哪些必须补原始 session、git、测试或 owner 页。
- **上轮行动兑现回检**：标准 / 深度复盘开始前，回看相关上一篇复盘的 open 行动，记录已兑现、部分兑现、未兑现、stale 或不适用。
- **输出形态**：短 checkpoint、复盘档案、Harness episode、模板 / skill / sensor 候选、规则变更或 owner 页回写。
- **不做项**：不重写历史，不把测试报告当复盘，不把 Issue 关闭当复盘完成，不把单次偏差直接升级硬规则，不让行动停在复盘正文。

## 子项路由

| 复盘对象 | 子项 | 执行 |
| --- | --- | --- |
| 项目 / 阶段 / 里程碑 / 发布交付 | 项目交付复盘 | [[skills/delivery-retrospective/SKILL]] + [[concepts/project-retrospective]] |
| 软件研发链：需求 -> 设计 -> 拆解 -> 实现 -> 测试验收 -> 发布运行 | 软件研发链复盘 | [[skills/delivery-retrospective/SKILL]] + [[concepts/software-development-project-retrospective]] |
| 历史对话 / Agent 工作流 / Harness episode | 历史对话与 Agent 工作流复盘 | [[skills/historical-dialogue-retrospective/SKILL]] + [[concepts/agent-work-retrospective]] |
| 规则、模板、sensor、evaluator 或自演进机制失效 | Harness 自演进复盘 | [[harness-evolution]] + [[harness-feedback-ledger]] |

## 工作流

1. 固定复盘对象、深度等级、证据计划和不做范围。
2. 按子项路由读取 owner 页；只读和对象相关的最小证据集，深度复盘再扩大到原始 session / rollout、git、检查输出和 memory 线索。
3. 用 [[templates/project-retrospective-template]] 建立复盘档案；轻量 checkpoint 可以只写到 [[log]]、Closeout Proof 或 owner 页。
4. 还原目标、实际结果、关键事实和偏差原因；每个判断标注 `confirmed / likely / possible / blocked`。
5. 先做上轮行动兑现回检，再写本轮改进行动。
6. 把行动分流到已有 owner 页面；不要在复盘目录形成平行看板。
7. 按治理自演进判断决定是否更新模板、skill、sensor、[[WORKFLOW]]、[[AGENTS]]、[[POLICY]] 或 [[harness-feedback-ledger]]。
8. 跑 `python3 scripts/check_all.py --only retrospective-system`，收尾前跑完整门禁。

## 输出格式

完整复盘默认输出为 [[templates/project-retrospective-template]] 形态。最终回复只摘要：

```markdown
**复盘对象**
- 对象：
- 深度：
- 子项路由：

**证据计划**
- 直接证据：
- 整理记录：
- 缺口：

**主要结论**
- confirmed：
- likely：
- possible / blocked：

**行动分流**
- owner 页：
- 模板 / skill / sensor：
- ledger / 规则：

**未验证边界**
-
```

## 禁止项

- 不把 `retrospective-capability` 平铺成多个互相竞争的入口。
- 不把历史对话复盘当成全部复盘体系。
- 不只凭 [[log]] 或当前上下文判断完整历史。
- 不把复盘行动项留在复盘正文里形成平行看板。
- 不把测试报告当复盘，不把 Issue 关闭当复盘完成，不把一次事故直接泛化成全项目结论。
- 不为了“完整复盘”无限扩读；先定义时间窗、证据计划和抽样边界。
