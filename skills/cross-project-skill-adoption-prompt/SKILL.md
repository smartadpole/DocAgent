---
name: cross-project-skill-adoption-prompt
description: 跨工程采纳或迁移技能：目标与写入授权明确时完成原生适配、验证和回执；用户只要提示词、目标不可写或由另一 agent 执行时生成可执行任务书。
maturity: mature
evidence_signals: [skill, README entry, governance, template, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only skill-maturity
conditional_sources: [skills/cross-project-skill-adoption-prompt/references/taskbook.md]
---

# Cross-Project Skill Adoption

把源能力适配到目标工程已有结构。先辨明本轮交付是直接迁移、维护源能力还是生成任务书；已有授权持续有效，不反复要求确认。

## 授权内完成迁移

读取源技能及其迁移边界、目标工程规则和直接依赖。确认 allowed write roots、当前分支、dirty 和已有等价能力；保护未提交工作。根据用户要求选择完整采纳或局部能力，不能擅自缩小已授权的全范围迁移。

逐能力决定复用、补全、升级、合并、原生适配或不适用。只有受影响合同确需时扩读模板、sensor 和 governance，不把迁移单一技能扩大成整套 agent system 改造。修改源 owner、发现入口及实际消费者，使目标工程可以执行；在目标工程规则下验证、提交并读回结果。若无法完成具体步骤，报告阻塞而非把已授权执行退回任务书。

可迁移的是触发、判断方法、关键边界、真实验证和必要资源；项目事实、业务链路、运行 ID、私有路径、凭据、排行与一次性 handoff 不复制。下游经验可抽象适配到已授权目标；写回上游源能力另受写入权限约束，未吸收内容不冒充上游标准。

## 条件工作方式

用户明确只要提示词、目标不可写或由目标 agent 执行时，读取 [[skills/cross-project-skill-adoption-prompt/references/taskbook]]，生成具体可执行任务书。

涉及外部矩阵或系统级成熟度时才使用 [[skills/transferable-skill-governance/SKILL]] 和相应系统 owner，分开 skill、runtime、harness、memory、evaluation、governance、migration 及 intelligence evidence。Golden baseline 比较语义覆盖、风险边界和执行结果，不比较字数或固定章节顺序。

## 验证与交付

检查入口、条件参考、实际消费者和运行行为；结构 sensor 不能替代真实 outcome 或 external readback。按需要验证正反例与原生结构，不用 Worker 自述、expected impact 或本地 green 宣称外部 evaluator 已通过。

回执说明实际修改与提交、验证、未吸收内容和未验证边界。任务书输出明确尚未执行；直接执行输出真实落地状态。迁移约束见 [[skills/cross-project-skill-adoption-prompt/TRANSFER]]。
