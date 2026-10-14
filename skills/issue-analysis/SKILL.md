---
name: issue-analysis
description: 调查已发生故障、偏差、验收争议或证据冲突；保留原始现象并先做最小可区分验证，跨工程分工与正式案件按实际需要展开。
maturity: leading
evidence_signals: [skill, README entry, governance, sensor, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only skill-maturity
conditional_sources: [skills/issue-analysis/references/cross-project-investigation.md]
---

# Issue Analysis

把观察到的问题收敛到有证据的原因、责任边界与验证动作。单次问因先快速诊断，不自动建 Issue、任务树或改状态；需要持续跟踪、正式修复或影响验收时再进入对应 owner。

## 最小诊断

保留原始现象、触发入口、期望、影响范围与直接证据；期望未知时标明待确认，不替用户编造。列出最小根因候选，优先执行能区分候选的验证，避免先铺整个业务链路。

区分直接观察、上下文、反证和未知项。用 confirmed / likely / possible / blocked 表达把握；只有现象、机制和影响路径串起来才确认根因。定位不到内部机制时停在最窄可信边界，明确下一项证据。

## 状态与证据冲突

先归一对象、单位、ID、时间点和权威源：requirements 定义期望；orchestration 表示调度；service_contract / service_internal 表示服务合同与处理；domain_units 表示业务分母；persistence 表示持久化；presentation 表示展示；agent_process 表示 agent 实际操作。

请求成功或 accepted/running 不等于后台完成，receipt 不等于 DB readback，artifact 包通过不等于代码实现或端到端通过。UI、日志摘要、原始模型输出不能替代合同定义的业务结果。不同运行 ID、请求 ID、写入 ID、flow run ID 不混用。

跨工程联调、责任争议或多层状态冲突需要分工时，读取 [[skills/issue-analysis/references/cross-project-investigation]]。涉及 agent 行为时先读真正影响该行为的入口规则、技能、配置和 handoff，缺口决定扩读，不遍历全部上下文目录。

## 修复与留证

验证覆盖原始复现、实际影响层和相关回归。参数问题用非默认值/边界值证明参数真实生效；服务或持久化问题需要对应 readback。不能验证时报告具体缺口，不写 done。

正式案件使用 [[templates/development-issue-template]] 保存 Issue Intake：原始现象、入口、report-or-task、artifact-class、root-cause 状态及关联证据。报告承接单次测试，TASK 承接修复，设计/需求/服务 owner 承接变化，Issue 保留案件事实；不复制到平行状态表。根因解释不自动关闭 TASK / EP / FP / Gate。

主控默认只读子工程；已获授权才在 allowed write roots 内修复。规则 owner：[[governance/issue-analysis-rules]]；迁移见 [[skills/issue-analysis/TRANSFER]]。
