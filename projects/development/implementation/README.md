---
type: development_implementation
id: DEV-IMPLEMENTATION-001
project: PROJ-WIKI-001
status: active
updated: 2026-05-06
tags: [development, implementation]
---

# 实现指导

主入口：[[projects/development/plan/README]]

上游：[[projects/design/README]]、[[projects/development/gates/README]]  \
下游：[[projects/development/feature-points/README]]、[[projects/development/execution/todo]]

## 这页负责什么

这页收口服务 / 模块级实现指导和候选功能点池。

它适合放：

- 服务或模块边界
- 候选功能点池
- 从设计对象到工程任务的拆分规则
- 接口、数据合同和测试要求的实现提示

它不适合放：

- 当前下一步，那属于 [[projects/development/execution/todo]]
- 过程流水，那属于 [[projects/development/execution/worklog]]
- Gate 准出判断，那属于 [[projects/development/gates/README]] 和 [[projects/development/reports/README]]

## 候选项提升规则

- 候选项需要 owner、排期、独立验收或阻塞下一 Gate 时，提升成 [[projects/development/feature-points/README]] 下的实体页。
- 候选项只是父功能点的内部步骤时，可以先留在候选池。
- 提升实体页前，至少补齐目标、范围、不做项、接口 / 数据合同、测试方案和关闭证据。
