---
type: development_todo
id: DEV-TODO-001
project: PROJ-WIKI-001
status: active
updated: 2026-05-06
tags: [development, todo]
---

# 待办看板

主入口：[[projects/development/execution/README]]

上游：[[projects/development/plan/README]]、[[projects/development/plan/work-item-system-model]]  \
下游：[[projects/development/feature-points/README]]、[[projects/development/reports/README]]、[[projects/development/execution/worklog]]

## 这页负责什么

这页是“下一步做什么”的单一执行源。

它不替代需求、设计、功能点正文、测试报告或过程记录。每个待办都必须能回到上游目标、功能点或候选项，并写清关闭证据。

## 状态

- `todo`：已确认要做，还未开始。
- `doing`：正在处理。
- `review`：已有输出或 handoff，等待吸收、验收或关闭证据补齐。
- `blocked`：被外部事实、owner、权限、环境或设计缺口阻塞。
- `done`：输出、测试、失败分流和回写均已完成。
- `canceled`：确认不再执行。

## 最小字段

```md
| ID | 优先级 | 状态 | 上游需求 / 目标 | 功能点 / 候选项 | 关系类型 | 主责模块 | 输出物 | 关闭证据 | 反馈回写 | 未确认项 | 下一步 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

## 关闭规则

- 代码完成但待验证，状态只能是 `review`。
- 只产出 handoff、草稿、执行包或测试报告初稿时，默认是 `review`，不能直接 `done`。
- 失败项、未验证项和待人工确认项必须归口后，才能关闭。
- 影响 Gate 准出的待办必须进入 [[projects/development/reports/README]]。
- 如果待办反馈改变需求、设计、决策或风险，必须同步 [[projects/trace]]、设计页、[[projects/decisions]] 或 [[projects/development/risks/README]]。

## 当前待办

按项目实际补充。
