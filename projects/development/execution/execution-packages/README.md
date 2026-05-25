---
type: execution_package_index
id: DEV-EP-INDEX-001
project: PROJ-WIKI-001
status: active
source_of_truth: true
updated: 2026-05-25
tags: [development, execution, ep]
---

# EP 执行包索引

> EP 是 Execution Package，承接 Gate / 模块级可关闭执行包。每个 EP 一事一页；本页只做索引、状态扫描和维护规则。

## EP 定位

- EP 必须挂上游需求 / Gate / FP。
- EP 必须说明主责模块、协同方、上下游、包内 TASK、risk、issue、test、验收和报告入口。
- EP 负责汇总 TASK 证据，但不能用单个 TASK 通过替代 EP 关闭。
- EP 状态变化必须判断是否影响 FP、Gate、risk、issue、报告和状态页。

## 状态口径

- `planned`：执行包已识别，但任务、证据或 owner 尚未完整。
- `active`：正在推进。
- `review`：已有输出或 handoff，等待吸收、验收或关闭证据补齐。
- `blocked`：被外部事实、owner、权限、环境、设计或风险阻塞。
- `done`：包内 TASK、测试证据、risk / issue 和回写均已闭合。
- `archived`：被替代或不再作为活跃执行入口。

## 维护规则

- 新 EP 默认复制 [[templates/development-execution-package-template]]。
- EP 不能承接已发生 bug 的完整案件档案；已发生问题进入 [[projects/development/issues/README]]，EP 只保留摘要、影响和关闭入口。
- EP 不能承接单个小功能或局部修复；能自然归入现有父 EP 的工作默认拆成 TASK。
- EP 关闭前必须回看 [[projects/development/plan/work-item-system-model]]、包内 TASK、测试报告、风险、issue 和状态页。
