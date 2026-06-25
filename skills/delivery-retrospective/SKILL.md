---
name: delivery-retrospective
description: 项目交付与软件研发链复盘子技能。用于项目、阶段、里程碑、发布、事故后专题、Issue 后专题或软件交付链复盘，按需求、设计、拆解、实现、测试验收、发布运行和协作治理读取证据，输出项目结果偏差、机制原因、行动兑现回检和沉淀路由；属于 retrospective-capability 的内部子项。
maturity: mature
evidence_signals: [skill, README entry, template, governance, sensor, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only retrospective-system,skill-maturity
---

# Delivery Retrospective

## 定位

本技能是 [[skills/retrospective-capability/SKILL]] 的内部子项，专门承接项目交付复盘和软件研发链复盘。

它把 [[concepts/project-retrospective]] 与 [[concepts/software-development-project-retrospective]] 的方法变成可执行流程。历史对话、Agent 工作流和 Harness episode 复盘继续使用 [[skills/historical-dialogue-retrospective/SKILL]]。

## 成熟度与证据信号

- `maturity`：`mature`。本技能有执行流程、README 入口、复盘模板、治理接线、专项 sensor 和迁移说明。
- `template`：输出使用 [[templates/project-retrospective-template]]，并保留软件研发交付链回看、上轮行动兑现回检和治理自演进判断。
- `governance`：显式复盘请求、自动触发分级、行动分流和不上推边界由 [[skills/retrospective-capability/SKILL]]、[[WORKFLOW]]、[[POLICY]] 和 [[AGENTS]] 共同约束。
- `sensor`：`python3 scripts/check_all.py --only retrospective-system,skill-maturity`。
- `TRANSFER`：跨工程吸收边界见 [[skills/delivery-retrospective/TRANSFER]]。
- `evidence boundary`：本技能形成复盘学习资产，不替代 Issue、事故、测试报告、验收关闭或发布准出。

## 触发场景

- 项目、阶段、里程碑、发布准备或重要交付链结束。
- 软件研发过程出现需求偏差、设计偏差、事项拆解偏差、实现偏差、测试验收偏差、发布运行偏差或协作治理偏差。
- 事故、Issue、验收失败或返工暴露出跨页面、跨 owner、跨阶段的机制问题。
- 用户要求复盘项目交付、软件研发链、阶段结果、发布过程或“为什么这条交付链没闭环”。

单个 bug、单个事故或单次测试报告先回到 Issue / 事故 / report 主档案保真；只有暴露机制缺口或可复用经验时才启动本技能。

## 响应模式

- 显式交付复盘请求：默认标准复盘并落档到 `projects/retrospectives/<year>/`，并同步 [[projects/retrospectives/indexes/by-year]]。
- 重大事故、重复验收失败、跨阶段交付偏差或会改变模板 / sensor / 规则的经验：深度复盘。
- 只是问单点原因：先快速诊断或 Issue 分析，不直接扩成全项目复盘。
- 涉及关闭事项、发布准出或验收裁决：切到验收关闭，本技能只提供学习和改进路由。

## 证据读取顺序

默认先读和复盘对象直接相关的单一信息源：

1. 项目目标和阶段：[[projects/README]]、[[projects/status]]
2. 需求和范围：[[projects/requirements]]、[[projects/trace]]
3. 设计和决策：[[projects/design/README]]、[[projects/decisions]]
4. 拆解和执行：[[projects/development/plan/README]]、[[projects/development/execution/README]]
5. 测试和验收：[[projects/development/acceptance/README]]、[[projects/development/reports/README]]
6. Issue 和事故：[[projects/development/issues/README]]、[[projects/incidents/README]]
7. 发布和运行：[[projects/releases]]、[[projects/service-registry]]
8. 历史过程：[[log]]、[[projects/development/execution/worklog]]

如果对象更窄，只读相关 owner 页；不要为了“项目复盘”机械扩大到整项目。

## 工作流

1. 框定对象：项目、阶段、里程碑、发布、事故后专题、Issue 后专题或某条交付链。
2. 回检相关上一篇复盘的改进行动：已兑现、部分兑现、未兑现、stale 或不适用。
3. 还原交付链：需求 -> 设计 -> 拆解 -> 实现 -> 测试验收 -> 发布运行 -> 协作治理。
4. 分类偏差：需求偏差、设计偏差、拆解偏差、实现偏差、验证偏差、发布运行偏差、协作治理偏差；每项标注 `confirmed / likely / possible / blocked`。
5. 区分事实主档案和学习档案：Issue、事故和 report 保留事实；复盘解释机制和下轮改进。
6. 写保留做法、改进行动、沉淀路由和未验证边界。
7. 把行动分流到已有 owner 页面，并按 [[harness-evolution]] 判断是否进入 ledger、模板、skill、sensor 或规则。
8. 如果形成标准 / 深度复盘正文，同步 [[projects/retrospectives/indexes/by-year]]，必要时同步 [[projects/retrospectives/indexes/by-theme]] 或 [[projects/retrospectives/indexes/by-type]]。

## 交付链回看

- **需求**：问题、用户、范围、非目标、验收标准是否清楚，需求变化是否进入 [[projects/trace]]。
- **设计**：架构、接口、数据、权限、写操作、部署和运行质量是否支撑实现和验收。
- **拆解**：Gate / FP / EP / TASK / risk / issue / AP / report 是否各有 owner，证据是否没有上推过度。
- **实现**：代码、配置、迁移、服务和 handoff 是否按 TASK / EP / 设计合同落地。
- **测试验收**：测试计划、AP、fixture / oracle、报告、人工确认和回归范围是否足够支撑结论。
- **发布运行**：发布范围、服务台账、监控、事故、回滚和运行质量是否闭环。
- **协作治理**：信息是否进入正确单一信息源，而不是停在对话、handoff、测试报告或最终回复里。

## 输出格式

使用 [[templates/project-retrospective-template]]，至少保留：

- 复盘对象、原始目标、实际结果、关键事实。
- 上轮行动兑现回检。
- 交付链回看。
- 偏差与原因。
- 保留做法、改进行动和沉淀路由。
- 治理自演进判断和未验证边界。

## 禁止项

- 不把测试报告当复盘。
- 不把 Issue 关闭当复盘完成。
- 不把一次事故直接泛化成全项目结论。
- 不把项目事实原样搬进通用模板、skill 或治理规则。
- 不让行动项停留在复盘正文里，也不新建平行看板。
- 不把交付复盘正文平铺到 `projects/retrospectives/` 根目录；正文进入年份目录，索引页承接阅读路径。
