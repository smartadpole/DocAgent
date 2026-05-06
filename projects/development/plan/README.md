---
type: development_plan
id: DEV-PLAN-001
project: PROJ-WIKI-001
status: active
source_of_truth: true
updated: 2026-05-06
tags: [development, plan, progress]
---

# 研发执行总控

主入口：[[projects/development/README]]

上游：[[projects/README]]、[[projects/status]]、[[projects/trace]]、[[projects/design/README]]、[[projects/decisions]]  \
下游：[[projects/development/execution/todo]]、[[projects/development/execution/developer-execution-workflow]]、[[projects/development/execution/engineering-feedback-loop]]、[[projects/development/reports/README]]、[[projects/development/execution/worklog]]

## 这页负责什么

这页是开发层置顶总控页，回答：

- 当前研发阶段或 Gate 是什么
- 当前下一步看哪里
- 开发层各子目录分别负责什么
- 哪些规则决定待办、功能点、证据和风险的流转

它不是第二份设计、第二份待办或第二份功能点清单。设计正文看 [[projects/design/README]]，当前行动看 [[projects/development/execution/todo]]，单功能点看 [[projects/development/feature-points/README]]。

## 目录职责

- [[projects/development/plan/README]]：研发总控、路线图和阶段推进摘要。
- [[projects/development/plan/work-item-system-model]]：需求、目标、功能点、TODO、反馈和证据之间的事项关系模型。
- [[projects/development/execution/README]]：待办、编码交接、反馈纠偏和过程记录。
- [[projects/development/gates/README]]：阶段门、准入准出和 Gate 报告入口。
- [[projects/development/implementation/README]]：服务 / 模块实现指导和候选功能点池。
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
- 当前执行项只维护在 [[projects/development/execution/todo]]。
- 阶段准入准出看 [[projects/development/gates/README]] 和 [[projects/development/reports/README]]。
- 如果实现反馈改变需求、范围、设计口径或决策，必须同步 [[projects/trace]]、[[projects/design/README]] 或 [[projects/decisions]]。
