---
type: task_index
id: DEV-TASK-INDEX-001
project: PROJ-WIKI-001
status: active
source_of_truth: true
updated: 2026-05-25
tags: [development, execution, task]
---

# TASK 任务索引

> TASK 是父级 EP 下的状态化交付合同，负责把一个功能切片从 `planned` 推到 `done`。每个 TASK 必须一事一页；本页只做导航、摘要和维护规则。完整设计看 [[projects/development/plan/task-design-model]]。

## 状态口径

- `planned`：任务已识别，尚未开始；必须写清 done 差距和待确认项。
- `in_progress`：正在实现或联调。
- `implemented`：已有实现，等待服务侧、端到端或回归证据。
- `review`：已有输出或 handoff，等待主控吸收、验收或关闭证据补齐。
- `blocked`：被 owner、权限、环境、业务事实、设计或风险阻塞。
- `done`：Done Contract、验证证据、回归守卫和上推边界均已闭合。
- `archived`：被替代或不再作为活跃执行入口。

## 维护规则

- 新 TASK 默认复制 [[templates/development-task-template]]。
- TASK 必须挂父 EP；没有父 EP 时只能作为待关系校准候选，不能派发为可编码任务。
- TASK 关闭只能作为父 EP 输入证据，不能自动关闭父 EP、FP 或 Gate。
- TASK 涉及已发生 ISSUE / Bug 时，必须把原问题路径写进验证要求和回归守卫。
- TASK 尚未出现已发生 ISSUE 时，也必须写清 `issue-trigger`：什么失败、复验或用户可见现象会触发创建 / 复用 Issue。
- 修改 TASK 时同步检查关系矩阵、父 EP、测试报告、risk / issue 和状态页。
