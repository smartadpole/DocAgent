---
type: skill-transfer-manifest
skill: retrospective-capability
status: active
updated: 2026-06-25
tags: [skill, transfer, retrospective]
---

# Retrospective Capability Transfer Manifest

## 能力目标

把项目交付、软件研发链、历史对话、Agent 工作流、Harness episode、行动分流和治理自演进收敛为目标工程可持续运行的复盘系统。

## 可以吸收

- 复盘总技能 + 子项路由，而不是把项目、软件研发和历史对话复盘平铺成互相竞争的入口。
- 复盘合同：对象、目标、深度等级、证据计划、上轮行动兑现回检、输出形态和不做项。
- 项目交付 / 软件研发链的读取顺序、交付链回看、偏差分类和行动分流。
- 历史对话 / Agent 工作流的证据源分层、自动触发矩阵和显式深度复盘要求。
- 行动分流到已有 owner 页面，不在复盘目录形成平行看板。
- `retrospective-system` 或等价 sensor 作为机器可发现入口。

## 只能抽象吸收

- 本库的 `projects/`、`governance/`、`skills/`、`templates/` 目录名。
- Gate / FP / EP / TASK / AP / report 事项体系；目标工程应映射到自己的 issue、task、milestone、acceptance 或 report 系统。
- Harness ledger 形态和 sensor 接入方式；目标工程已有治理 backlog 时优先复用。
- 当前 wiki 的 wikilink、log、提交和检查脚本习惯。

## 禁止复制

- 不复制项目事实、历史 log、复盘正文、ledger 条目、运行 ID、服务路径、用户偏好、一次性 handoff 或当前状态。
- 不把 `historical-dialogue-retrospective` 当成完整复盘体系。
- 不把行动项留在复盘目录里形成第二看板。
- 不为了迁移制造空壳 skill；目标工程没有技能体系时，先把流程落到 AGENTS、WORKFLOW 或 docs 方法页。

## 目标工程结构自检

- 已有 retrospective / postmortem / incident review / lessons-learned 结构时优先复用。
- 有 `projects/` 时，复盘档案优先落到 `projects/retrospectives/`；没有时按目标工程文档治理区选择 `docs/retrospectives/` 或等价目录。
- `templates/` 如果是前端或运行资产目录，不把复盘模板塞进去，改用文档模板目录。
- 没有 `skills/` 体系时，不制造空壳 skill；先写入 agent workflow 或规则入口。

## 验证要求

- 检查入口可发现性：README、INDEX、AGENTS / WORKFLOW、skills、templates、复盘档案入口都有短链接。
- 检查模板字段：对象、目标、实际结果、关键事实、上轮行动回检、证据地图、偏差原因、行动分流、治理自演进、未验证边界。
- 检查单一信息源：Issue、事故、测试报告、决策、memory、trace 和复盘职责没有互相替代。
- 跑目标工程已有检查；如有 `check_all`，接入 `retrospective-system` 或等价检查。
- 最终回复说明落位、检查结果、commit hash、未验证边界和没有复制的项目事实。
