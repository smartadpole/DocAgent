---
type: development_gates
id: DEV-GATES-001
project: PROJ-WIKI-001
status: active
updated: 2026-05-06
tags: [development, gates]
---

# 阶段门

主入口：[[projects/development/plan/README]]

上游：[[projects/development/plan/README]]、[[projects/development/implementation/README]]  \
下游：[[projects/development/execution/README]]、[[projects/development/reports/README]]

## 这页负责什么

这页收口项目开发中的阶段门方案，回答每个 Gate 要冻结什么、怎样验收、哪些内容不能提前混入。

## 使用规则

- Gate 只记录阶段准入、准出、冻结对象和验收证据，不重复写完整设计正文。
- 每个 Gate 必须说明：目标、准入条件、准出条件、测试要求、风险和未确认项。
- 未达到准出条件时，不用局部实现成功替代 Gate 准出。
- Gate 准出必须回看 [[projects/development/reports/README]]。

## Gate 模板

默认复制 [[templates/development-gate-template]]，不要在本页维护第二份模板正文。
