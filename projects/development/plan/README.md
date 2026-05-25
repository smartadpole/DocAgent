---
type: development_plan
id: DEV-PLAN-001
project: PROJ-WIKI-001
status: active
source_of_truth: true
updated: 2026-05-25
tags: [development, plan, progress]
---

# 研发执行总控

主入口：[[projects/development/README]]

上游：[[projects/README]]、[[projects/status]]、[[projects/trace]]、[[projects/design/README]]、[[projects/decisions]]  \
下游：[[projects/development/execution/execution-packages/README]]、[[projects/development/execution/tasks/README]]、[[projects/development/execution/todo]]、[[projects/development/execution/developer-execution-workflow]]、[[projects/development/execution/engineering-feedback-loop]]、[[projects/development/issues/README]]、[[projects/development/reports/README]]、[[projects/development/execution/worklog]]

## 这页负责什么

这页是开发层置顶总控页，回答：

- 当前研发阶段或 Gate 是什么
- 当前下一步看哪里
- 开发层各子目录分别负责什么
- 哪些规则决定 Gate、FP、EP、TASK、证据、风险、Issue 和验收的流转

它不是第二份设计、第二份执行包、第二份任务清单或第二份功能点清单。设计正文看 [[projects/design/README]]，执行包看 [[projects/development/execution/execution-packages/README]]，TASK 看 [[projects/development/execution/tasks/README]]，轻量待办看 [[projects/development/execution/todo]]，单功能点看 [[projects/development/feature-points/README]]。

## 目录职责

- [[projects/development/plan/README]]：研发总控、路线图和阶段推进摘要。
- [[projects/development/plan/work-item-system-model]]：`Gate -> FP -> EP -> TASK` 事项关系模型，以及 risk / issue / test / 验收关系节点。
- [[projects/development/plan/task-design-model]]：TASK 作为父级 EP 下状态化交付合同的设计规则。
- [[projects/development/execution/README]]：执行包、TASK、待办、编码交接、反馈纠偏和过程记录。
- [[projects/development/execution/execution-packages/README]]：EP 执行包索引。
- [[projects/development/execution/tasks/README]]：TASK 任务索引。
- [[projects/development/gates/README]]：阶段门、准入准出和 Gate 报告入口。
- [[projects/development/implementation/README]]：服务 / 模块实现指导和候选功能点池。
- [[projects/development/issues/README]]：已发生问题、bug 和偏差的案件档案入口。
- [[projects/development/reports/README]]：测试方案、测试用例、测试结论和准出报告。
- [[projects/development/risks/README]]：风险、卡点、待确认项和会议归口。
- [[projects/development/feature-points/README]]：单功能点实体页。

## 当前摘要

按项目实际补充：

- 当前阶段 / Gate：
- 当前 P0：
- 当前阻塞：
- 下一步：
- 需要会议或决策的问题：

## 维护规则

- 本页只维护摘要和入口，不复制支撑页正文。
- 正式执行主链按 `Gate -> FP -> EP -> TASK` 维护；TODO 只做轻量待办和过渡视图，不替代 EP / TASK。
- 关闭任何 Gate / FP / EP / TASK 前，必须回看关系节点覆盖：`risk:`、`test:`、`验收:`、`issue-trigger:`。
- 阶段准入准出看 [[projects/development/gates/README]] 和 [[projects/development/reports/README]]。
- 如果实现反馈改变需求、范围、设计口径或决策，必须同步 [[projects/trace]]、[[projects/design/README]] 或 [[projects/decisions]]。
