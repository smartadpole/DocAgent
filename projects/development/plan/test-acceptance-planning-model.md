---
type: development_plan
id: DEV-TEST-ACCEPTANCE-PLANNING-001
project: PROJ-WIKI-001
status: active
source_of_truth: true
truth_scope: test_planning_and_acceptance_contract
updated: 2026-05-26
tags: [development, testing, acceptance, planning]
---

# 测试计划与验收合同模型

主入口：[[projects/development/plan/README]]

上游：[[projects/development/plan/work-item-system-model]]、[[projects/development/plan/task-design-model]]  \
下游：[[projects/development/acceptance/README]]、[[projects/development/reports/README]]、[[projects/development/execution/execution-packages/README]]、[[projects/development/execution/tasks/README]]、[[projects/development/issues/README]]

领域背景：[[concepts/software-testing-acceptance-release]]

这页定义测试开始前的规则：当 FP、EP、TASK、issue 或 Gate 判断需要验收时，必须先在对应事项页或 [[projects/development/acceptance/README]] 下的 `AP-*` 方案中写清测试计划和环境路由。测试报告只记录执行后的证据、结果和裁决，不负责临场决定本次该在哪测、按什么维度测。

测试计划只治理测试和验收合同这个子领域；执行类页面的单值裁决、非目标和证据层级防漂移规则看 [[execution-contract-semantics|执行合同语义]]。

核心结论：

> 测试计划是事项合同的一部分；`AP-*` 是复杂验收的测试前承接文件；测试报告是该合同的一次执行记录。

## 测试治理分级

| 等级 | 典型对象 | 计划落点 | 是否需要 AP | 报告 / 记录要求 | 状态上限 |
| --- | --- | --- | --- | --- | --- |
| L0 快速诊断 | 原因、位置、差异、规则解释、只读排查 | 最小读取范围和 checkpoint | 不需要 | 最终回复写 `confirmed / likely / possible / blocked` 和证据边界 | 不关闭事项 |
| L1 轻量事项 | 小型本地 TASK、纯文档补充、局部 fixture / 单测 / 合同修正 | 事项页 `验证要求` 或执行单轻量检查点 | 不机械新建 AP | 轻量报告、worklog 或事项页证据记录；必须写测试点、结果、未验证边界 | 最多关闭本 TASK 局部合同 |
| L2 标准验收 | 普通 issue / Bug、跨组件 TASK、真实服务组、DB / artifact / UI readback、灰度 | 事项页测试计划并链接 `AP-*` | 需要，除非已有等价 AP | 单报告文件，写计划来源、原 bug / 代表路径、回归守卫和不上推边界 | `review / partial / done` 按证据裁决 |
| L3 发布 / Gate 验收 | Gate、FP 准出、EP 聚合、生产发布、业务发布 | Gate / FP / EP / release 事项页和 `AP-*` | 必须 | 完整报告链，分 local、gray、production、人工确认和回滚边界 | 只有完整证据链可准出 |

若执行中出现真实调度、写库、UI、DB readback、用户现场失败、目标服务组或状态推进信号，必须从 L1 升级到 L2 / L3，并写清升级原因。

## 成熟度升级：从规则到系统

测试治理必须同时看流程设计和执行可验证性。规则存在但没有 sensor / 模板字段 / 报告字段承接，只能算“设计完成”，不能算“体系成熟”。

后续升级优先补可检查面：

- **AP 覆盖审计**：L2 / L3 事项必须有 `AP-*` 或显式 `不适用` 原因；L1 事项必须在事项页有轻量测试计划。
- **环境路由一致性检查**：通用概念页不得出现具体服务器、端口或事项编号；项目页出现具体环境时必须写清证据面和不上推边界。
- **非功能测试矩阵**：性能、可靠性、安全、可观测性、兼容性、数据 / 模型质量和合规按 Gate / FP / EP / TASK 风险触发。
- **fixture / oracle 台账**：固定样本、预期结果、数据来源、脱敏状态、版本和失效条件必须可追踪；没有 oracle 的测试只能写观察。
- **人工确认覆盖表**：业务、运维、法务、客户或 owner 才能裁决的事项必须独立列出。
- **发布 runbook / rollback checklist**：上线确认必须追溯版本、配置 readback、health、UI/API origin、监控、回滚和发布后观察窗口。
- **测试质量指标**：定期看逃逸缺陷、复验失败、重开、AP 覆盖、环境上推违规、未验证风险滞留和回归守卫入驻情况。

## 测试计划必填字段

任何进入实现、复验、关闭、准出或发布确认的事项，必须在自身页面或链接的 `AP-*` / 执行单中落下这些字段：

- **测试需求 / 验收目标**：本轮要证明什么。
- **测试范围 / 非目标**：覆盖什么，不覆盖什么，哪些只作为输入证据。
- **测试维度**：code-level / unit、functional、business-flow、service-side、end-to-end、相关功能回归、非默认值 / 边界值、UI / 人工操作、DB / artifact / 日志 / API readback。
- **测试服务器 / 环境路由**：开发 / CI / 集成 / 灰度 / 生产 / 外部依赖分别是否适用；适用时写目标服务组、入口和 readback 来源。
- **测试方案**：先做什么、再做什么、哪些证据互相印证。
- **测试用例 / 检查点**：大功能、跨模块、Gate、真实调度、写库、权限和 UI 必须有用例矩阵；小修复至少有检查点清单。
- **历史能力回归**：哪些已验收能力必须复跑，哪些说明不相关，哪些暂时不可复验。
- **证据与报告要求**：期望报告路径、截图 / 日志 / DB / artifact / UI 读回要求、子工程回传格式。
- **通过 / 失败 / partial 裁决**：哪些证据足以关闭本事项，哪些只能推进到 `review / partial`。
- **上推边界**：本事项通过能给父 EP / FP / Gate 提供什么输入，不能自动关闭什么。

## 环境路由

环境选择先看事项对象，再看证据需求，不按“越靠近生产越高级”机械晋级。灰度和生产都是特定证据面，不是普通修复验收的默认必经阶梯；低风险环境已能满足关闭合同时，不能把更高环境写成额外关闭阻塞。

固定口径：

- **开发 / local**：编码、自测、fixture、局部服务；必须写清 repo、运行方式、端口或 fixture 和能证明的边界。
- **CI**：自动化检查和构建可重复性；不能代表真实业务运行裁决。
- **集成 / service-side**：多组件联调、接口合同、服务组合和目标依赖 readback。
- **预发 / 灰度**：贴近生产配置、小范围业务验证和上线前输入；普通 issue / TASK 只有在关闭合同需要目标服务组证据时才必须进入。
- **生产**：上线确认、生产现场反馈、发布节点复判和回滚确认；不作为普通研发测试的首轮试验场。
- **外部依赖 / 读回源**：数据库、模型服务、第三方 API、湖仓、消息系统等，必须写清依赖方向和不上推边界。

## 报告反向约束

测试报告创建时必须引用或等价复述本轮测试计划来源：

- **计划来源**：链接到 TASK / EP / issue / FP / Gate 的测试计划字段，或对应 `AP-*`。
- **执行偏差**：实际未按计划执行时，写清原因、影响和恢复动作。
- **结果回写**：报告结论改变状态、关闭标准、未验证边界或环境路由时，必须回写对应事项页和 AP。

没有测试计划来源或 AP / 事项页入口的报告，只能作为临时观察或排障记录，不能作为关闭、准出或发布确认依据。
