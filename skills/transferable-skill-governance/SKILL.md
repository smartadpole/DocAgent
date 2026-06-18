---
name: transferable-skill-governance
description: 可迁移技能治理技能。用于根据外部成熟度矩阵、源技能或下游经验吸收通用能力时，先判断 true-gap / recognition-gap / signal-only-gap，再决定 recognize / complete / upgrade / merge / adapt / defer / reject，避免为追分创建空技能或复制项目事实。
maturity: active
evidence_signals: [skill, README entry, TRANSFER, governance, template, sensor, quality-gate, verification-loop]
transfer_ready: true
sensor: python3 scripts/check_all.py --only skill-maturity
---

# Transferable Skill Governance

## 定位

本技能负责“怎么吸收外部通用技能”，不是某个具体业务技能。它把成熟度矩阵、源工程 skill、TRANSFER、模板、governance、sensor 和目标工程结构放到同一个决策面里，避免两种常见偏差：

- 看到缺口就照单全收，复制项目事实或目录形态。
- 看到 leader / 领先就误以为真实执行质量已经通过验证。

本仓库是 wiki / 模板源工程，吸收对象必须先经过本库身份筛选，只落到既有 `skills/`、`templates/`、`governance/`、`scripts/`、`views/` 等层级。

## 触发场景

- 用户要求根据 AcknowledgeBase、矩阵、诊断、下游工程或附件升级通用技能。
- 某个技能有成熟度缺口、source project、leader 标记或跨工程迁移任务。
- 需要判断外部经验是系统层信息、项目材料、一次性状态还是不可吸收内容。
- 新增或重写 `SKILL.md`、`TRANSFER.md`、模板、governance、sensor 或 views 接线。

## 成熟度与证据信号

- `skill`：本页定义吸收流程和决策枚举。
- `TRANSFER`：迁移边界见 [[skills/transferable-skill-governance/TRANSFER]]。
- `governance`：与 [[template-feedback-rules]]、[[documentation-maintenance-rules]]、[[WORKFLOW]] 和 [[AGENTS]] 共用反哺边界。
- `template`：跨工程任务书、证据和 review 使用 [[templates/skill-transfer-contract-template]]、[[templates/skill-transfer-evidence-contract]]、[[templates/skill-transfer-review-contract]]。
- `sensor`：`skill-maturity` 检查技能 frontmatter、README entry、TRANSFER 和必要结构；它只证明 wiring，不证明真实执行质量。
- `evidence boundary`：矩阵是缺口雷达，不是执行命令。

## 工作流

1. 读取目标工程入口规则和既有结构，确认是否已有等价体系。
2. 从矩阵或诊断中过滤目标工程、`scope=general` 和能力清单，按 `score_gap` 排序。
3. 对每个能力先判缺口类型：
   - `true-gap`：本地确实缺触发、流程、模板、sensor、验证或入口。
   - `recognition-gap`：本地已有能力，但命名、入口、TRANSFER 或 sensor 不可识别。
   - `signal-only-gap`：缺的是 body、large-body、benchmark 等弱信号，不值得为分数补噪声。
4. 再判处理方式：
   - `recognize`：承认已有体系，不改或只补入口说明。
   - `complete`：补缺失的耐久落点。
   - `upgrade`：吸收更成熟方法，增强本地 skill / template / sensor。
   - `merge`：合并多个本地能力，防止平行系统。
   - `adapt`：只抽象方法，不复制目录或事实。
   - `defer`：适用但当前没有运行条件或证据。
   - `reject`：不适用、冲突、隐私风险或第二真相源风险。
5. 对要升级的能力选择最小耐久落点：`SKILL.md`、`TRANSFER.md`、模板、governance、sensor、views，按真实需要组合。
6. 更新入口页和检查脚本，运行专项检查和完整检查。
7. 最终回复列明未复制内容、未验证边界和结构 wiring 与真实运行质量的区别。

## 输出格式

```markdown
| 能力 | 矩阵原状态 | 缺口类型 | 处理方式 | 落位 | 剩余边界 |
| --- | --- | --- | --- | --- | --- |
|  |  | true-gap / recognition-gap / signal-only-gap | recognize / complete / upgrade / merge / adapt / defer / reject |  |  |
```

## 禁止项

- 不复制项目事实、业务链路、服务名、表名、运行 ID、真实路径、历史 log、一次性 handoff、密钥或环境配置。
- 不为了追分创建没有触发面、没有使用方式、没有检查意义的空 skill、空模板或空 view。
- 不把 `leader / 领先` 当作真实执行质量、审美质量、验收闭环或项目状态。
- 不让外部目录形态压过本工程已有结构。
- 不把下游工程“不吸收清单”变成本库维护下游同步状态的台账。
