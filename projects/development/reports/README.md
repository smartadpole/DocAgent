---
type: development_reports
id: DEV-REPORTS-001
project: PROJ-WIKI-001
status: active
updated: 2026-05-06
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

- 大功能、跨模块功能、Gate 准出和真实数据 / 调度 / 写入 / 权限相关功能必须有完整测试方案。
- 小功能可以轻量化，但不能省略测试结论和未验证边界。
- 新 bug、漏测、复验失败或合同变化要升级成后续测试项、回归用例或准出守卫。
- 新报告可以覆盖旧结论，但不删除旧报告的证据价值。

## 最小报告骨架

```md
## 测试报告标题

- 验证对象：
- 上游 TODO / FP / Gate：
- 测试方案：
- 核心用例 / 检查点：
- 相关功能回归范围：
- 执行命令或人工步骤：
- 结果：
- 失败项：
- 未验证项：
- 待人工确认项：
- 当前关闭判断：
- 后续测试计划演进：
```
