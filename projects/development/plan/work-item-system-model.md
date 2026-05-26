---
type: development_plan
id: DEV-WORK-ITEM-SYSTEM-001
project: PROJ-WIKI-001
status: active
source_of_truth: true
updated: 2026-05-25
tags: [development, planning, work-items, traceability]
---

# 需求到事项的系统模型

主入口：[[projects/development/plan/README]]

上游：[[projects/requirements]]、[[projects/trace]]、[[projects/design/README]]  \
横向：[[projects/development/feature-points/README]]、[[projects/development/execution/execution-packages/README]]、[[projects/development/execution/tasks/README]]、[[projects/development/execution/engineering-feedback-loop]]、[[projects/development/risks/README]]、[[projects/development/issues/README]]、[[projects/development/plan/test-acceptance-planning-model]]  \
下游：[[projects/development/acceptance/README]]、[[projects/development/reports/README]]、[[projects/status]]

## 这页解决什么

这页回答“需求、目标、Gate、FP、EP、TASK、risk、issue、test、验收和证据之间是什么关系”。

核心目标不是把列表做复杂，而是把研发推进变成一张可追踪工作项图：每个执行项都能说明它服务哪个需求、处在哪个 Gate、覆盖哪个 FP、归属哪个 EP、拆成哪些 TASK、被哪些 risk / issue / test / 验收关系节点影响，以及哪些证据可以关闭它。

## 总体链路

默认主链是 `Gate -> FP -> EP -> TASK`，再通过 risk、issue、test、验收、报告、handoff 和服务台账等关系节点连接证据与状态。

```text
需求 / 目标
  -> Gate
  -> FP / 候选能力
  -> EP / Execution Package
  -> TASK
  -> risk / issue / test / 验收 / 报告 / handoff 关系节点
  -> status / trace / decisions / meetings 同步
```

这条链路有三条红线：

- `EP` 是模块级、Gate 级或跨组件执行包；`TASK` 是父 EP 下的状态化交付合同。小功能、局部修复、短周期跟进默认进 TASK，不轻易升成 EP。
- `risk`、`test`、`验收` 是链路上的关系节点，不是硬切的平行层级。它们的层级由关联对象推导：可以发现于 TASK，影响 EP / FP / Gate，也可以由 Gate 目标反向约束多个 EP / TASK。
- `issue` 是后验问题事实。只有 bug、实施偏差、事故、复验失败或验收失败已经发生后，才创建或复用 issue；功能尚未实现或只是识别到风险时，不预建 issue，只记录 `issue-trigger:` 触发边界。

## 事项类型

| 类型 | 负责回答 | 不负责什么 | 主入口 / 模板 |
| --- | --- | --- | --- |
| 需求 / 目标 | 为什么做、做到什么算有价值 | 不直接写代码任务 | [[projects/requirements]]、[[projects/trace]] |
| Gate | 阶段准入、准出、冻结对象和准出证据 | 不替代单功能验收 | [[projects/development/gates/README]]、[[templates/development-gate-template]] |
| FP | 稳定系统能力、能力边界和验收口径 | 不承担当前执行排期 | [[projects/development/feature-points/README]]、[[templates/development-feature-point-template]] |
| EP | 模块级 / Gate 级执行包，承接主责、协同、输出、联调、验收和关闭状态 | 不作为第二份需求或第二份设计；不承接太小的零散动作 | [[projects/development/execution/execution-packages/README]]、[[templates/development-execution-package-template]] |
| TASK | 父 EP 下的状态化交付合同，推动一个功能切片从 `planned` 到 `done` | 不单独代表 Gate 准出；不替代父 EP / FP / Gate 的关闭证据 | [[projects/development/execution/tasks/README]]、[[templates/development-task-template]] |
| risk | 风险评估、影响对象、缓解方案、剩余风险和准出影响 | 不等同 bug，不承担具体复现和修复包 | [[projects/development/risks/README]]、[[templates/development-risk-template]] |
| issue | 已发生问题、复现、根因边界、关闭标准、最新有效报告和报告链 | 不替代 risk，也不绕过 EP / TASK 修复 | [[projects/development/issues/README]]、[[templates/development-issue-template]] |
| test / 验收 / AP / 报告 | 测试计划、环境路由、样本、证据、结论和上推边界 | 不自动关闭上游目标；报告不临场发明测试计划 | [[projects/development/plan/test-acceptance-planning-model]]、[[projects/development/acceptance/README]]、[[projects/development/reports/README]]、[[templates/development-acceptance-plan-template]]、[[templates/development-test-report-template]] |
| 决策 / 会议 | 冲突拍板、人工确认和跨 owner 协调 | 不承担实现本身 | [[projects/decisions]]、[[projects/meetings/README]] |

## 核心不变量

所有研发事项都必须能回答这些问题：

| 问题 | 目的 | 主落点 |
| --- | --- | --- |
| 它服务哪个需求或目标 | 防止无源任务膨胀 | [[projects/requirements]]、[[projects/trace]]、本页 |
| 它处在哪个 Gate | 防止准入、准出和发布边界混用 | [[projects/development/gates/README]] |
| 它覆盖哪个 FP / 候选能力 | 防止只做局部任务却忘记能力边界 | [[projects/development/feature-points/README]] |
| 它归属哪个 EP | 防止小功能误升为独立执行包 | [[projects/development/execution/execution-packages/README]] |
| 它是否需要 TASK | 把小功能、局部修复、吸收和补测落到可交付合同 | [[projects/development/execution/tasks/README]] |
| 它和上游是什么关系 | 判断分解、实现、派生、阻塞、约束、修复或验证 | 关系矩阵、EP、TASK |
| 它产出什么可验收结果 | 避免只写主题或过程动作 | EP、TASK、测试报告 |
| 它是否影响运行实例事实 | 避免验收和部署绕过服务台账 | [[projects/service-registry]] |
| 什么证据能关闭它 | 避免代码完成、handoff 通过和 Gate 准出混用 | [[projects/development/reports/README]]、[[projects/development/execution/worklog]] |
| 它的反馈要回写到哪 | 避免局部修复改变总目标却没有 trace | [[projects/trace]]、设计页、风险、会议或决策 |

没有上游目标、Gate / FP / EP 归属、关系类型和关闭证据的 EP / TASK，不应作为 Gate 准出依据。

## 关系类型

| 关系 | 含义 | 使用时机 |
| --- | --- | --- |
| `decomposes` | 上游目标被拆成能力或子能力 | 需求到 FP、FP 到 EP / 候选项 |
| `realizes` | 执行项实现某项能力 | EP / TASK 对应 FP 或局部能力 |
| `enables` | 一个事项让后续事项可执行 | 基础设施、合同、fixture、配置 |
| `derives_from` | 从反馈、失败或缺口派生补修 | bug、漏测、合同缺口、复验失败 |
| `constrains` | 一项约束限制另一项实现方式 | 权限、容量、运行模式、外部规则 |
| `validates` | 证据验证事项是否成立 | 测试报告、复验、Gate 报告 |
| `blocks` | 未确认项阻塞关闭或准出 | owner、凭据、业务事实、权限 |
| `mitigates` | 一个 EP / TASK 缓解某个风险 | 风险处理、准出前置、长期治理 |
| `fixes` | 一个 TASK 或 EP 修复某个 issue / Bug | 已发生问题、复验失败、子工程修复 |
| `feeds_back_to` | 实现反馈反向修正上游 | 合同变化、设计不成立、验收边界变化 |
| `supersedes / absorbs` | 一个事项覆盖或吸收另一个事项的范围 | 重复任务、下游 handoff 被主控吸收 |

关系可以多条，但必须标主关系。

## 关系节点覆盖

关系矩阵必须显式写 `risk:`、`test:`、`验收:`、`issue-trigger:` 这四类节点。

| 节点 | 必须写清 | 不能做什么 |
| --- | --- | --- |
| `risk:` | 发现来源、影响对象、缓解动作、关闭证据、剩余风险 | 不把未发生风险改名成 issue |
| `test:` | 计划来源、验证对象、核心用例、环境、样本、回归范围、AP 或不适用原因 | 不用默认 happy path 替代边界值 / 非默认值；不让报告替代测试计划 |
| `验收:` | local / service-side / end-to-end 证据层级、能否上推、不能上推边界 | 不把 TASK 通过直接写成 EP / FP / Gate 通过 |
| `issue-trigger:` | 当前是否已有已发生 issue；没有时写触发条件和创建 / 复用规则 | 不把候选风险、漏测或未实现事项预建成 issue |

如果 risk 被真实复现、测试失败、日志 / DB / UI / artifact 证据、现场事故或验收失败触发，必须创建或复用 issue，并保留原 risk 的剩余风险和准出影响。

## EP 和 TASK 分工

EP 是执行包，回答“这一组工作如何形成模块级或 Gate 级闭环”。EP 必须写清：

- 上游需求 / Gate / FP。
- 主责模块、协同方、上下游。
- 包内 TASK、risk、issue、test、验收和报告入口。
- 输出物、关闭证据、不能上推关闭的边界。

TASK 是父 EP 下的状态化交付合同，回答“这个功能切片如何从 planned 到 done”。TASK 必须写清：

- 出发点和目标。
- 当前状态和 done 差距。
- 归属与责任。
- Done Contract。
- 功能边界和正确性约束。
- 上下游和联调路径。
- 验证要求。
- 体系关系和证据记录。

TASK 关闭只能作为父 EP 的输入证据，不自动关闭父 EP、FP 或 Gate。多个 TASK 形成模块级闭环时，应回到父 EP 汇总，不把 TASK 当作隐形 EP。

## Issue 与报告分工

Issue 是案件档案，报告是每次庭审记录。

- 一个已发生问题只保留一个 ISSUE 主档案页，收口原始现象、当前状态、主责和协同方、根因边界、关闭标准、最新有效结论、未闭合缺口和报告链。
- 每次验收、复验、补测、部署验证、现场失败、关闭争议或证据边界变化，都进入独立测试报告。
- 同一个 ISSUE 可以有多份报告；新报告改变状态、owner、关闭标准、根因边界或未验证项时，必须回写 ISSUE 档案页和索引。
- 关闭读取顺序是：先读 issue 档案页的当前结论和最新有效报告，再沿报告链回看历轮证据。

## 信息回馈闭环

状态变动即触发回馈。`planned -> in_progress`、`review -> blocked`、`review -> done`、issue 打开 / 关闭、risk 触发 / 缓解、测试失败 / 通过，都必须判断是否需要回写源 TASK、父 EP、兄弟 TASK、FP / Gate、测试报告、风险和状态入口。

最小传播规则：

- **进入不等于吸收**：issue 页记录了新事实，只说明信息进入了 issue；源 TASK / EP 必须抽象总结到当前状态、done 差距、验证要求、关闭证据和不能上推边界，才算吸收。
- **吸收不等于上推**：TASK 吸收 issue 后，只证明 TASK 局部状态变化；父 EP 是否更新，取决于它是否影响父 EP 输出物、联调路径、关闭证据、共享接口 / 数据 / 配置或下游消费。
- **上推不等于能力完成**：父 EP 更新后，只有影响 FP 能力边界、用户可见行为、验收口径、Gate 准出输入且无替代证据时，才更新 FP / Gate。
- **报告不等于计划**：测试报告是计划执行记录；如果报告发现测试计划缺失、环境路由错误或验收对象变化，必须回写事项页或 `AP-*`，不能只在报告里形成新关闭标准。
- **父项变化要检查兄弟项**：共享接口、数据、配置、fixture、回归守卫或依赖输出的兄弟 TASK 必须重新判断状态。
- **派生生命周期持续联动**：新建子 TASK、issue、risk、测试报告或 handoff 时，父 EP / 源 TASK 立即记录派生原因、影响范围、期望回收方式和证据入口；派生项关闭时再总结修正结果、仍保留的缺口和是否上推。

## 关系矩阵

默认参考 [[templates/development-work-item-matrix-template]]，不要在本页维护第二份模板正文。

矩阵列必须包含：

```text
上游需求 / 目标 | Gate | 功能点 / 候选项 | EP | TASK | 子工程增量 | 关系类型 | 主责模块 | 当前状态 | 输出物 | 关闭证据 | 回归守卫 | 关系节点覆盖 | 反馈回写 | 未确认项 | 备注
```

其中 `关系节点覆盖` 必须包含 `risk:`、`test:`、`验收:`、`issue-trigger:`。缺失任一项时，这一行不能作为 Gate 准出证据。

## 防跑偏策略

| 新问题类型 | 能否改变需求 / 目标 | 默认处理 |
| --- | --- | --- |
| 实现 bug | 否 | 创建 / 复用 issue，修实现，补测试，更新源 TASK / EP、报告和回归守卫 |
| 合同缺口 | 可能 | 先补设计 / Gate 方案和 EP / TASK，若改变范围再回写 trace |
| 验收缺口 | 否，除非验收标准本身不成立 | 补测试报告、TASK、相关回归范围和验收上推边界 |
| 运行质量缺口 | 可能后置 | 判断是否属于当前 Gate 关闭前置；否则进 risk 或后续 EP / TASK |
| 业务事实缺失 | 可能阻塞准出 | 进入待人工确认、risk 或会议，不让 agent 代拍板 |
| 需求范围变化 | 是 | 先更新 [[projects/requirements]] 和 [[projects/trace]]，必要时进 [[projects/decisions]] |

局部修复不能直接改总目标。只有当新问题被判定为“需求范围变化”或“设计口径不成立”时，才允许从 TASK / EP 反向改需求、trace 或设计。

## 关闭守卫

| 事项类型 | 最小关闭证据 |
| --- | --- |
| FP | 相关 EP / TASK 证据可支撑能力边界，测试报告覆盖用户可见行为和回归范围 |
| EP | 包内 TASK 状态、输出物、联调证据、测试报告、risk / issue 处理和人工确认齐全 |
| TASK | 输出物存在，Done Contract 满足，local / service-side / end-to-end 边界写清，失败项和待人工确认项已归口 |
| issue | 原始现象保真，复现 / 根因边界 / 修复证据 / 回归守卫 / 最新有效报告齐全 |
| risk | 缓解动作、剩余风险、准出影响和 owner / 会议 / 后续任务归口齐全 |
| Gate 准出 | 覆盖矩阵、测试报告、risk / issue / 人工确认项和 owner 决议齐全 |

如果一个 EP / TASK 只是产出 handoff、执行包、字段合同、细化稿或报告草稿，且下游吸收还没完成，默认只能停在 `review`。
