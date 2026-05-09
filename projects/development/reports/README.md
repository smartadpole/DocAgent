---
type: development_reports
id: DEV-REPORTS-001
project: PROJ-WIKI-001
status: active
updated: 2026-05-09
tags: [development, reports, testing]
---

# 测试和准出报告

主入口：[[projects/development/plan/README]]

上游：[[projects/development/execution/todo]]、[[projects/development/gates/README]]  \
下游：[[projects/status]]、[[projects/releases]]、[[projects/incidents/README]]

## 这页负责什么

这页收口测试方案、测试用例 / 检查点、测试结论、相关功能回归范围和 Gate 准出报告。

它不是命令流水，也不是只写“通过 / 失败”。测试报告要能说明：

- 验证对象是什么
- 用什么方案验证
- 覆盖了哪些核心用例和相关回归
- 哪些失败项、未验证项和人工确认项仍然存在
- 当前结论能关闭哪一层对象

## 报告规则

- 先声明本次验证对象类型：`handoff / artifact 包`、`代码实现`、`联调闭环` 或 `Gate 准出`。
- 大功能、跨模块功能、Gate 准出和真实数据 / 调度 / 写入 / 权限相关功能必须有完整测试方案。
- 小功能可以轻量化，但不能省略测试结论和未验证边界。
- 跨服务或多组件验收必须区分 `local validation`、`service-side validation` 和 `end-to-end validation`，缺哪一层就写清缺口，不能用局部通过替代用户行为闭环。
- 多工程联调接口验收必须写清请求接收、状态查询、后台副作用和最终 artifact / DB / UI 投影之间的关系。
- 如果本轮涉及参数、配置、profile、feature flag、限流、采样或筛选条件，至少验证一个非默认值或边界值，并证明它真实改变了执行结果。
- 报告必须回链对应 TODO / FP / Gate；对应 TODO / FP / Gate 也要回链最新有效报告。
- 新 bug、漏测、复验失败或合同变化要升级成后续测试项、回归用例或准出守卫。
- 新报告可以覆盖旧结论，但不删除旧报告的证据价值。

## 最小报告骨架

默认复制 [[templates/development-test-report-template]]，不要在本页维护第二份模板正文。
