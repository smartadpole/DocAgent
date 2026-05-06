---
type: development_execution_index
id: DEV-EXECUTION-INDEX-001
project: PROJ-WIKI-001
status: active
updated: 2026-05-06
tags: [development, execution]
---

# 执行控制

主入口：[[projects/development/plan/README]]

上游：[[projects/development/README]]、[[projects/status]]  \
下游：[[projects/development/feature-points/README]]、[[projects/development/reports/README]]、[[projects/trace]]

## 这页负责什么

这页收口开发层里的执行控制文件：待办、编码交接、反馈纠偏和过程记录。事项类型、关系类型和防跑偏策略看 [[projects/development/plan/work-item-system-model]]。

它回答“今天怎么推进、怎么交接、怎么回传、过程写哪里、完成后落到哪里”。

## 文件

- [[projects/development/execution/todo]]：待办看板，当前下一步的单一执行源。
- [[projects/development/execution/developer-execution-workflow]]：代码工程协作、单功能开发闭环、编码任务执行单和回传包。
- [[projects/development/execution/engineering-feedback-loop]]：工程反馈、偏差、错误、疑惑和验收失败的处理闭环。
- [[projects/development/execution/worklog]]：开发、联调、验证和排障过程记录。

## 使用顺序

1. 先从 [[projects/development/plan/README]] 确认当前阶段。
2. 再从 [[projects/development/execution/todo]] 选待办。
3. 进入编码前，按 [[projects/development/execution/developer-execution-workflow#单功能开发闭环]] 判断当前阶段。
4. 完成一个可回看的开发节点后，按 [[projects/development/execution/developer-execution-workflow#代码工程回传包]] 回传。
5. 偏差和测试结果分别进入 [[projects/development/execution/engineering-feedback-loop]] 和 [[projects/development/reports/README]]。

## 完成后的落脚点

开发类待办完成后，不只把 TODO 改成 `done`。默认按这个顺序落点：

1. [[projects/development/execution/todo]]：更新 TODO 状态。
2. [[projects/development/feature-points/README]] 或对应 FP 页：更新功能点状态、验收结果和下一步。
3. [[projects/development/reports/README]]：记录测试方案、用例、结论和失败项。
4. [[projects/development/execution/worklog]]：记录实际开发、联调、验证和排障过程。
5. [[projects/status]]：只有当结果改变当前阶段、下一步或阻塞项时才同步。
6. [[projects/trace]]、[[projects/decisions]]、设计页、风险页或会议页：只有当实现结果改变需求口径、设计口径、决策、风险或待拍板事项时才同步。
