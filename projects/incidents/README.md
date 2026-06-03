---
type: incident-index
project: wiki
status: active
updated: 2026-04-09
---

# 事故

这页是事故目录总览。

上游：[[projects/releases]]、[[projects/development/execution/worklog]]、[[projects/decisions]]、[[projects/memory/README]]
下游：每一条独立事故记录、[[projects/retrospectives/README]]

## 这页负责什么

- 汇总当前项目的事故记录
- 说明事故相关的整体状态
- 链接到每一条独立事故记录
- 保留事故事实、影响、修复、恢复和回滚的索引

## 这页不负责什么

- 不承接跨阶段学习资产；事故经验上升为复盘主题时，进入 [[projects/retrospectives/README]]。
- 不替代测试报告；验证证据仍进入 [[projects/development/reports/README]]。
- 不替代 Issue；已发生 bug、偏差和验收失败仍按 [[projects/development/issues/README]] 保真。

## 使用方式

- 每一个事故单独建一个文件
- 文件名尽量稳定，建议带日期和主题
- 这页只做总览、状态和入口，不把所有事故细节堆在这里

示例命名：

- `2026-04-09-login-timeout.md`
- `2026-04-12-payment-retry-loop.md`

## 当前内容

按需要维护：

- 当前事故状态总览
- 事故索引
- 修复和恢复状态
- 需要进入 [[projects/retrospectives/README]] 的学习主题

## 维护说明

- 如果事故结论会长期影响项目推进，回写到 [[projects/memory/README]]、[[POLICY]] 或 [[projects/decisions]]
- 如果事故暴露跨事故、跨阶段或会影响研发实践 / 方案设计 / 工程治理的机制问题，回链到 [[projects/retrospectives/README]]
- 事故目录只做索引和事实入口，不重复堆正文
