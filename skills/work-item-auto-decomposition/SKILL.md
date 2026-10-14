---
name: work-item-auto-decomposition
description: 按本工程 Gate→FP→EP→TASK 模型拆解已授权事项或修补实际关系缺口；这是项目绑定能力，不为矩阵识别自动创建任务树。
maturity: adopted
evidence_signals: [skill, README entry, governance, template, sensor, report]
transfer_ready: false
sensor: python3 scripts/check_all.py --only work-item-matrix,agent-system-maturity
---

# Work Item Auto Decomposition

本技能服务本仓 `Gate -> FP -> EP -> TASK` 及 risk / Issue / test / 验收 / report / service registry 关系，是项目 / 领域绑定能力，`transfer_ready: false`。跨工程只能借鉴方法，不复制编号、目录或当前事实。

## 按目标拆解

明确拆解对象与授权后，只读取直接相关的需求/trace/design 和当前事项 owner。事项语义以 [[projects/development/plan/work-item-system-model]]、[[projects/development/plan/task-design-model]]、[[projects/development/plan/test-acceptance-planning-model]] 为准。

先复用既有项，按真实交付边界确定父级、主责、依赖、输出和关闭证据。普通小改不因可拆解而新建 EP；未授权创建正式事项时输出候选，已有授权时完成范围内创建与回写，不默认停在建议。

没有父 EP 的 TASK 可作关系校准候选，不能直接派发正式编码。随着执行需要补 risk:、test:、验收:、issue-trigger: 及回归、反馈关系，不在最初阶段预填整个执行表。完整矩阵需要时使用 [[templates/development-work-item-matrix-template]] 的适用列。

## 问题与关闭

未发生风险记录 risk 与触发条件，不预建 Issue。单点问因可先诊断；已发生问题进入正式跟踪/修复时，用 Issue 保留原始现象，报告记录测试，TASK 承接修复，避免以一个 owner 替代另一个。

TASK done 只作为父 EP 的输入证据，不能自动关闭父 EP、FP 或 Gate。测试计划、实际测试报告、参数非默认/边界值验证各有用途，handoff、结构检查或 Worker 自述不等于业务验收或外部 evaluator readback。

## 关系校验

关系缺失是 true-gap；已有关系不可发现是 recognition-gap；只影响矩阵词语是 signal-only-gap，不创建空事项补分。结果回写现有需求、设计、事项、报告或服务 owner，不另建看板。

运行 `python3 scripts/check_all.py --only work-item-matrix` 验证关系接线；仅涉及系统级外部识别时再用 agent-system-maturity。说明实际创建/修正的关系、未确认项与验收边界。
