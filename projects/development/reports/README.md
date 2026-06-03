---
type: development_reports
id: DEV-REPORTS-001
project: PROJ-WIKI-001
status: active
updated: 2026-05-09
tags: [development, reports, testing]
---

# 报告和验证

主入口：[[projects/development/plan/README]]

上游：[[projects/development/plan/test-acceptance-planning-model]]、[[projects/development/acceptance/README]]、[[projects/development/execution/todo]]、[[projects/development/gates/README]]  \
下游：[[projects/status]]、[[projects/releases]]、[[projects/incidents/README]]

## 这页负责什么

这页收口测试方案、测试用例 / 检查点、测试结论、相关功能回归范围、Issue 复验记录和 Gate 准出报告。

它不是命令流水，也不是测试计划单一信息源，也不是复盘档案。测试计划和环境路由先看 [[projects/development/plan/test-acceptance-planning-model]] 与 [[projects/development/acceptance/README]]；长期学习和机制改进看 [[projects/retrospectives/README]]。本页只记录计划执行后的证据、结果和裁决。测试报告要能说明：

- 验证对象是什么，是 handoff / artifact 包、代码实现、联调闭环、TASK、EP、FP、Issue 还是 Gate 准出。
- 计划来源是什么，是事项页测试计划、轻量检查点还是 `AP-*`。
- 用什么方案验证，覆盖哪些核心用例、非默认值 / 边界值和相关回归。
- 本轮自己做了哪些独立取证动作，而不是只引用子工程 handoff、历史报告或口头结论。
- 哪些失败项、未验证项和人工确认项仍然存在。
- 当前结论能关闭哪一层对象，不能上推到哪里。

Issue 是案件档案，报告是每次庭审记录。同一个 ISSUE 可以有多份报告；新报告改变状态、owner、关闭标准、根因边界或未验证项时，必须回写 [[projects/development/issues/README]] 或对应 issue 档案页。

## 报告规则

- 先声明本次验证对象类型：`handoff / artifact 包`、`代码实现`、`联调闭环` 或 `Gate 准出`。
- 大功能、跨模块功能、Gate 准出和真实数据 / 调度 / 写入 / 权限相关功能必须有完整测试方案。
- 小功能可以轻量化，但不能省略测试结论和未验证边界。
- 跨服务或多组件验收必须区分 `local validation`、`service-side validation` 和 `end-to-end validation`，缺哪一层就写清缺口，不能用局部通过替代用户行为闭环。
- 多工程联调接口验收必须写清请求接收、状态查询、后台副作用和最终 artifact / DB / UI 投影之间的关系。
- 如果本轮涉及参数、配置、profile、feature flag、限流、采样或筛选条件，至少验证一个非默认值或边界值，并证明它真实改变了执行结果。
- 报告必须回链对应 EP / TASK / FP / Gate / ISSUE；对应 EP / TASK / FP / Gate / ISSUE 也要回链最新有效报告。
- 报告必须引用计划来源。没有事项页测试计划或 `AP-*` 的报告只能作为临时观察或排障记录，不能单独作为关闭、准出或发布确认依据。
- 新 bug、漏测、复验失败或合同变化要升级成后续测试项、回归用例或准出守卫。
- 新报告可以覆盖旧结论，但不删除旧报告的证据价值。
- 已发生 bug、Issue 复验失败、用户现场测试未通过、事故或关闭争议，必须设计 bug 反向用例：原始复现路径、同场景代表样本、修复前失败 / 修复后通过或等价证据、漏测原因和回归守卫入驻位置。
- 部署、重启、远程配置、服务组切换、灰度或上线，必须启动服务组验收：代码 / 配置版本、进程或 deployment readback、health、UI/API origin、关键入口 smoke 和回滚边界。
- 异步任务、调度、worker、写库或外部副作用，必须区分引擎状态和业务状态；请求接收、状态查询、worker / 日志、artifact / DB / UI 最终投影缺一不可。
- UI、图片、mask / overlay、看板、人工操作或用户截图参与验收时，必须判断是否保留截图；不保留时写清结构化证据为什么足够。
- Gate 准出不按“代码写完”判断，而按 P0 EP 关闭、必要 TASK 完成、测试报告结论、失败项归口、服务台账事实和剩余风险判断。

## 测试质量指标

定期复盘时至少看：AP 覆盖率、复验失败率、逃逸缺陷、回归守卫入驻率、环境上推违规、未验证风险滞留和人工确认超期。

## 数据、fixture 和 oracle 治理

- 报告引用固定样本时，写明样本来源、版本和可复跑性。
- 没有 oracle 的执行结果只能写成观察，不能写成通过。
- oracle 失效、样本过期或数据来源变化时，回写对应 `AP-*` 或事项页测试计划。

## 验收执行包触发矩阵

| 触发信号 | 必须启动的验收执行包 | 最小证据链 | 不足时状态上限 |
| --- | --- | --- | --- |
| 新功能、参数、配置、profile、feature flag、限流、采样或筛选条件变更 | 参数 / 配置生效包 | 非默认值或边界值输入、执行结果变化、artifact / progress / manifest / SQL / UI 投影之一 | `review / partial` |
| 已发生 bug、ISSUE 复验失败、用户现场测试未通过、事故或实施偏差 | Bug 反向复验包 | 原 bug 真实路径或同路径代表样本、修复前失败 / 修复后通过或等价证据、漏测原因、回归守卫入驻 | `open / partial` |
| 部署、重启、远程配置、服务组切换、灰度或上线 | 服务组验收包 | 代码 / 配置版本、进程或 deployment readback、health、UI/API origin、关键入口 smoke、回滚边界 | `review / gray-only / blocked` |
| 异步任务、调度、worker、写库、外部副作用或队列流转 | 后台效果闭环包 | 请求 / 触发证据、状态查询、worker / 日志、业务状态、artifact / DB / UI 最终投影 | `review / partial` |
| UI、图片、看板、人工操作或用户截图参与验收 | 用户可见证据包 | 可渲染截图或原图未入库原因、操作者入口、API / DB / artifact 交叉证据、视觉结论边界 | `review / 待人工确认` |
| 引用子工程 handoff、README、测试报告记录、状态页或口头结论 | 独立抽查包 | 至少抽查代码、测试、artifact、日志、运行或接口读回之一 | `沿用历史结论，当前未独立复验` |
| 推进 EP / TASK / FP / Gate 状态、关闭 issue、写 `done` 或准出 | 关闭裁决包 | 验收对象、关闭判据、通过项、失败项、未验证项、人工确认项、下游吸收和不上推边界 | 保持原状态或 `review` |

## 最小报告骨架

默认复制 [[templates/development-test-report-template]]，不要在本页维护第二份模板正文。
