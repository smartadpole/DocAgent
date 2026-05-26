---
type: governance
id: GOV-EXECUTION-CONTRACT-SEMANTICS-001
scope: shared
status: active
source_of_truth: true
truth_scope: execution_contract_semantics
updated: 2026-05-26
tags: [governance, execution-contract, semantics, harness]
---

# 执行合同语义

这页是执行类信息的语义真相源。它治理一种常见口径漂移：

> 执行合同语义污染，就是把参考性规则、条件路由、证据解释或非目标说明写进具体执行裁决里，导致本该单值的“现在要不要做 / 做到哪算关闭”变成隐形待办。

这类污染会出现在 TASK、issue、AP、EP、FP、Gate、模块职责、子工程 handoff、测试报告、风险、状态页和会议行动项里。

## 信息层级

| 层级 | 回答的问题 | 典型落点 | 不能做什么 |
| --- | --- | --- | --- |
| 参考规则层 | 什么情况下怎么判 | [[POLICY]]、[[WORKFLOW]]、[[projects/development/plan/work-item-system-model]]、[[projects/development/plan/test-acceptance-planning-model]]、本页 | 不能替具体事项给出本轮状态 |
| 路由层 | 这类事归谁、去哪验、证据往哪上推 | FP、EP、Gate、acceptance plans、模块页、流程页 | 不能在下层事项里复制成条件待办 |
| 执行合同层 | 当前对象本轮要做什么、不要做什么、什么证据关闭 | TASK、issue、AP、handoff、报告目标包、状态页行动项 | 裁决必须单值，不能写成“默认不需要，但如果……” |
| 证据记录层 | 实际做过什么、证据来自哪里、结论覆盖哪一层 | 测试报告、worklog、截图 / 日志证据、服务台账 readback | 不能反向改写执行合同 |

## 六类污染

1. **裁决不单值**：执行页应该回答 `做 / 不做 / blocked 待裁决`。
2. **上层规则下沉**：发布策略、准出规则、模块职责或 Gate 路由属于参考规则层 / 路由层；具体 issue / TASK 只写本对象怎么验。
3. **非目标变潜在任务**：当前对象不承接的内容，只能命名或链接父级入口，不展开后续步骤、另归流程或验证细节。
4. **伪 optional**：`可选`、`视情况`、`只在需要时`、`后续可能`、`optional` 不能出现在执行裁决字段里；真实产品开关要写成明确参数 / 模式 / feature flag，并说明本轮取哪个值。
5. **证据层级回流**：local、service-side、gray、production、Gate 准出、人工确认是不同证据面；上层证据不能回写成普通 issue / TASK 的隐形关闭条件。
6. **辅助证据改写问题本体**：日志、API、DB、代码 diff 和发布反馈只能支持判断，不能改写用户原始现象、issue 标题、当前执行对象或关闭标准。

## 执行类页面硬规则

- **当前裁决单值**：`当前状态`、`done 还差什么`、`下一步`、`环境路由`、`关闭裁决`、`未验证风险`、`子工程回传要求` 和 `会议行动项` 必须能读出唯一当前动作。
- **条件规则上移**：如果一句话需要解释“什么情况下需要 X”，放到父级 EP / Gate、规则页、AP 或模块路由页；本页只写当前对象是否需要 X。
- **非目标只命名不展开**：可以写“非目标：发布节点验收”，不得继续写后续如何发布、归谁、怎么测、不作为关闭条件等防御性闭包。
- **证据只对本层有效**：报告或事项页写清证据覆盖对象和层级，禁止用局部通过外推上层准出。
- **模板占位不算裁决**：模板里的“如需 / 可选 / 后续补齐 / 视情况”落地时必须替换成 `适用 / 不适用 / blocked`。
- **历史可保留，当前合同要改正**：旧报告可以保留当时语境；当前 issue / TASK / AP / 状态页若仍承接执行，就必须按本页改成单值合同。

## Sensor 口径

`scripts/check_execution_contract_semantics.py` 负责三类可机器检查的红灯：

- 执行合同入口是否都链接本页。
- 具体 issue / TASK / AP 是否出现非目标环境的防御性闭包、条件式路由或伪 optional。
- 治理入口、工作项入口、测试入口、报告入口和回传入口是否共同承接本页规则。

该 sensor 只能拦截可见文本模式，不能替代人工语义判断。凡用户指出“这让不需要的东西变成隐形待办”，即使命中不了脚本，也必须按本页和 [[harness-evolution]] 进入 episode / sensor 升级。
