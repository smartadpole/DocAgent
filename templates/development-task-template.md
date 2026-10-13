# TASK 任务模板

使用位置：[[projects/development/execution/tasks/README]]；阶段规则：[[projects/development/plan/task-design-model]]。只复制最小登记，条件字段按实际影响填写。

## 最小登记

```yaml
---
type: task
id: TASK-001
parent_ep: EP-001
project:
contract_profile: staged-v1
status: planned
owner:
impact: [local]
updated:
---
```

# TASK-001 | 任务名称

## 任务合同

- 父 EP：
- 目标：
- 范围：
- 不做项：
- 待确认：

## Done Contract

- 完成条件：
- 验证计划：
- 关系覆盖：risk / test / 验收 / issue-trigger；可引用父项，不复制正文。

## 按阶段补齐

执行时补 `授权依据`（本地动作也须明确当前用户授权）、`执行范围`、`下一动作`。关闭时补 `验证结果: passed`、`证据`、`回归守卫`、`不上推边界`；失败或未测不能写 done。

## 条件扩展

`impact` 取实际涉及的 `local / interface / cross_repo / service / production / data_write / irreversible / long_run`，可多选；未知用 `unknown` 阻塞执行。服务端、生产或跨仓影响不得用 local 掩盖。

- 跨仓：external_ref、source_branch、执行 owner、Git preflight 与回传入口。
- 接口 / 服务：上游 Gate / FP、local validation、service-side validation、end-to-end validation、参数边界、失败语义与联调证据；service-side validation、end-to-end validation、非默认值 / 边界值各以 `passed: 证据引用` 记录已通过结果。
- 生产 / 数据 / 不可逆：动作授权、资源范围、恢复方法、service registry 和现场 pre_action_check，以 `allowed: 当前动作 / 目标 / 证据` 记录；blocked 不能执行。
- 长时：Current Execution Contract 的 current_slice、first_core_action、expected_delta、pre_core_limit、minimum_safe_gates、on_budget_exhausted；引用当前 owner 或已启用 Goal，不额外创建或复制完整模板。
