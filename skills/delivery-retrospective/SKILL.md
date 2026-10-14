---
name: delivery-retrospective
description: 复盘项目或软件交付链的结果偏差、机制原因和改进行动；适用于明确复盘请求或有证据的跨阶段机制问题，单点排障不自动扩成项目复盘。
maturity: mature
evidence_signals: [skill, README entry, template, governance, sensor, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only retrospective-system,skill-maturity
---

# Delivery Retrospective

这是 [[skills/retrospective-capability/SKILL]] 的交付分析分支。总入口负责深度与归档；本技能补充交付链证据，不重复建立合同或状态体系。

## 交付链视角

从原始目标与实际结果的差距出发，只读取受影响环节的 owner：

| 环节 | 判断重点 | 证据入口 |
| --- | --- | --- |
| 需求 | 用户、范围和验收是否明确，变化是否传播 | requirements / trace |
| 设计 | 架构、接口、数据与权限是否支持目标 | design / decisions |
| 拆解 | 父级归属、依赖与关闭证据是否成立 | Gate / FP / EP / TASK |
| 实现 | 实际代码、配置、迁移与合同是否相符 | diff / commit / handoff |
| 测试验收 | oracle、样本、边界值与回归能否支撑结论 | AP / report / Issue |
| 发布运行 | 服务事实、监控、事故和回滚是否闭环 | releases / service registry / incidents |
| 协作治理 | 信息是否到达消费方与正确 owner | worklog / trace / owner 页 |

这些是证据地图，不要求每次按序读全库。按证据还原需求 -> 设计 -> 拆解 -> 实现 -> 测试验收 -> 发布运行中实际涉及的链路，避免事后用当前版本解释历史状态。

## 机制判断与行动

区分已确认原因、强候选和待验证假设；记录反证与替代解释。相关上一篇复盘存在 open 行动时回检已兑现、部分兑现、未兑现、stale 或不适用，不把旧行动直接抄成新待办。

输出结果偏差、机制原因、值得保留的做法及可验证改进。Issue、事故和报告保存原始事实，复盘保存学习；行动进入既有 owner，不在复盘中另建看板。单次事故不能自动外推全项目或升级硬规则。

需要档案时使用 [[templates/project-retrospective-template]] 的适用模块；归档与索引按总技能。复盘不替代测试报告、Issue 关闭或发布准出。相关验证：`python3 scripts/check_all.py --only retrospective-system`；迁移见 [[skills/delivery-retrospective/TRANSFER]]。
