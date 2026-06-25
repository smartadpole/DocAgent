---
type: skill-transfer-manifest
skill: delivery-retrospective
status: active
updated: 2026-06-25
tags: [skill, transfer, retrospective, delivery]
---

# Delivery Retrospective Transfer Manifest

## 能力目标

把项目、阶段、里程碑、发布、事故后专题、Issue 后专题或软件交付链复盘变成可执行流程，覆盖需求、设计、拆解、实现、测试验收、发布运行、协作治理、行动兑现回检和沉淀路由。

## 可以吸收

- 交付链回看：需求 -> 设计 -> 拆解 -> 实现 -> 测试验收 -> 发布运行 -> 协作治理。
- 证据读取顺序：项目目标、需求 trace、设计决策、执行拆解、验收报告、Issue / 事故、发布运行和历史过程。
- 偏差分类：需求、设计、拆解、实现、验证、发布运行和协作治理。
- 行动兑现回检：已兑现、部分兑现、未兑现、stale 或不适用。
- 行动分流：Issue、事故、task / milestone、acceptance、report、meetings、decisions、memory、trace、template、skill、ledger、sensor 或规则入口。

## 只能抽象吸收

- Gate / FP / EP / TASK / AP / report 术语；目标工程应映射到自己的事项体系。
- 本库项目层目录名、报告目录和服务台账形态。
- 当前 wiki 的复盘索引、历史记录和项目状态。

## 禁止复制

- 不复制项目事实、历史 log、具体复盘正文、服务路径、运行 ID、一次性 handoff 或当前状态。
- 不把测试报告、Issue 关闭或事故修复闭环当作复盘完成。
- 不把一次事故或单个 bug 直接泛化为全项目结论。
- 不把改进行动留在复盘正文里形成平行看板。

## 目标工程结构自检

- 先找目标工程已有 `projects/`、`docs/`、`issues/`、`incidents/`、`decisions`、`memory`、`trace`、`tasks`、`reports` 或等价入口。
- 已有 postmortem / lessons-learned / incident review 时优先复用，补交付链和行动分流字段。
- 没有 Gate / FP / EP / TASK 时，映射到 issue、task、milestone、acceptance、report 或项目自己的事项系统。
- 复盘模板如果不能放在根 `templates/`，使用目标工程明确的文档模板目录。

## 验证要求

- 用一个交付链样本验证能分清事实主档案、测试报告和复盘档案。
- 用一个行动项验证能路由到 owner 页面，而不是停在复盘正文。
- 用一个偏差样本验证能给出 `confirmed / likely / possible / blocked` 和不上推边界。
- 跑目标工程已有检查；如有 `check_all`，接入 `retrospective-system` 或等价检查。
