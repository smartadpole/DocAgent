---
name: retrospective-capability
description: 复盘交付、历史对话或治理机制中的结果偏差和可复用经验；明确复盘请求按所需深度归档，普通任务收尾不自动启动复盘。
maturity: leading
evidence_signals: [skill, README entry, template, governance, sensor, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only retrospective-system,skill-maturity
---

# Retrospective Capability

从目标、实际结果和证据解释偏差，形成能够兑现的改进。复盘不替代项目验收、Issue/事故事实档案、测试报告或状态关闭。

## 触发与深度

显式“复盘/写复盘/沉淀复盘/总结教训”默认标准复盘并落档；用户只要口头、先分析或不写文件时尊重该范围。明确深度/完整/全面请求要覆盖约定时间窗、首轮目标、纠偏和直接证据，不以篇幅代替完整性。

单点问因先快速诊断。重复机制失守或跨阶段偏差可以触发有针对性的复盘；任务长、多 agent、普通收尾本身不触发。无需向用户逐次汇报 no-op 或升降级理由。缺少长期学习价值的轻量信号补原 owner 或聚合专题，避免一信号一档案。

## 对象与行动

先固定本轮对象、目标、时间窗和关键证据缺口，复用已有信息而非新建完整合同。项目/软件交付链走 [[skills/delivery-retrospective/SKILL]]；历史对话/Agent 工作过程走 [[skills/historical-dialogue-retrospective/SKILL]]；规则机制问题按需要读取 [[harness-evolution]] 与 [[harness-feedback-ledger]]。

区分事实、原因候选和推测，保留反证与未验证边界。相关上一篇复盘存在 open 行动时做上轮行动兑现回检：已兑现、部分兑现、未兑现、stale 或不适用。新行动绑定已有 owner 与验证方式，复盘保留引用，不建立平行看板。

一次失误不自动升级硬规则；先判断是执行未遵守、机制缺口还是偶发事件。仅在证据支持时更新相应模板、skill、sensor 或规则。

## 档案与验证

标准/深度档案使用 [[templates/project-retrospective-template]] 的适用模块，正文在 `projects/retrospectives/<year>/`，同步 [[projects/retrospectives/indexes/by-year]]；稳定主题或类型需要时同步 by-theme / by-type。根入口只放导航，Issue、事故、log 和报告继续保留各自事实。

最终回复摘要主要结论、已落实动作和边界，不复制整套空字段。运行 `python3 scripts/check_all.py --only retrospective-system` 验证归档与接线；结构检查不能证明因果判断正确。迁移见 [[skills/retrospective-capability/TRANSFER]]。
