---
type: development_acceptance
id: DEV-ACCEPTANCE-001
project: PROJ-WIKI-001
status: active
source_of_truth: true
updated: 2026-05-26
tags: [development, acceptance, testing]
---

# 验收计划

主入口：[[projects/development/plan/README]]

上游：[[projects/development/plan/test-acceptance-planning-model]]、[[projects/development/plan/work-item-system-model]]  \
下游：[[projects/development/reports/README]]、[[projects/status]]

这层承接复杂验收的 `AP-*` 计划、长用例索引和防漂移索引。它不承接测试报告正文；报告只记录计划执行后的证据、结果和裁决。

## 覆盖审计入口

- **AP 覆盖**：L2 / L3 验收必须有 `AP-*` 或显式 `不适用` 原因。
- **用例覆盖**：AP 至少写明测试需求、核心路径、失败路径、非默认值 / 边界值和回归范围。
- **非功能覆盖**：性能、可靠性、安全、可观测性、兼容性、数据 / 模型质量和合规按风险触发。
- **fixture / oracle 覆盖**：固定样本、预期结果、数据来源、脱敏状态、版本和失效条件必须可追踪；没有 oracle 的结果只能写观察。
- **人工确认覆盖**：业务、运维、法务、客户或 owner 才能裁决的事项独立列出。
- **发布覆盖**：上线确认必须能追溯版本、配置 readback、health、UI/API origin、监控、回滚和发布后观察窗口。

当前 sensor：`scripts/check_testing_system_maturity.py`。

## 子目录

- [[projects/development/acceptance/plans/README]]：`AP-*` 验收计划索引和覆盖审计规则。

## 最小规则

- 先有事项页测试计划或 `AP-*`，再有测试报告。
- 报告必须引用计划来源；实际偏离计划时，写清原因、影响和恢复动作。
- AP 和报告都要写上推边界；下层通过不能自动关闭上层。
- 环境是证据面，不是荣誉阶梯；环境路由必须给出本轮单值裁决。
