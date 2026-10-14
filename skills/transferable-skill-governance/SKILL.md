---
name: transferable-skill-governance
description: 吸收外部技能或成熟度反馈时判断真实能力、识别缺口与项目绑定边界，选择原生适配；普通技能小改不自动启动矩阵治理。
maturity: active
evidence_signals: [skill, README entry, TRANSFER, governance, template, sensor, quality-gate, verification-loop]
transfer_ready: true
sensor: python3 scripts/check_all.py --only skill-maturity
---

# Transferable Skill Governance

外部矩阵是缺口雷达，不是执行命令。依据用户目标、影响与证据判断需要改变什么，不为分数、篇幅或术语制造结构。

## 缺口与处理

先检查目标已有等价能力和实际使用方式，区分：true-gap（缺真实能力）、recognition-gap（已有但不可发现）、signal-only-gap（只缺弱信号）、project-bound-gap（依赖领域或事项 owner）。按价值与风险排序，不能只按 score_gap。

逐项选择 recognize / complete / upgrade / merge / adapt / defer / reject。落点使用现有 skill、reference、template、governance 或 sensor；只建立真实需要的组合，不为单一技能强铺系统层。公开模板不携带来源工程身份、私有路径、业务状态或一次性 evidence。

## 条件证据

外部 evaluator 或矩阵级吸收需要可核对的能力清单、source-depth、candidate files、baseline、逐项裁决与剩余边界；使用 [[templates/skill-transfer-evidence-contract]] 和 [[templates/skill-transfer-review-contract]] 的适用字段。矩阵识别与真实行为分离，缺 external readback 就写未验证，expected impact 不是已通过。

系统级能力升级才读取 [[agent-system-maturity]]，分别判断 skill、runtime、harness、memory、evaluation、governance、migration 及 intelligence evidence；单项 skill 高分不能外推其他层。普通能力升级不强制 Matrix Recognition Capsule 或全维评分。

矩阵级或多能力吸收保留 repo-native adoption manifest 或等价裁决清单，记录 source snapshot、实际落点、授权、验证与例外；它只索引证据，不替代 owner，也不固定某次历史快照为永久标准。

## 验证与交付

检查原生入口、条件参考、实际消费者和行为边界；新 sensor 应验证有意义的不变量而不是固定措辞。对有价值的 golden baseline 比较语义覆盖，不以变短判失败。拒绝为空白分数补空 skill、空 view、重复正文。

输出逐能力决定、实际变更、验证和未证明的范围。单项迁移执行用 [[skills/cross-project-skill-adoption-prompt/SKILL]]；反哺规则归 [[template-feedback-rules]]。专项检查可用 `python3 scripts/check_all.py --only transferable-skill-baseline,skill-maturity`；结构 green 不是运行质量。迁移见 [[skills/transferable-skill-governance/TRANSFER]]。
