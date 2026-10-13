# Issue 案件模板

使用位置：[[projects/development/issues/README]]。已发生问题先最小登记，未知根因不阻止建档；未发生的风险不创建 Issue。

## 最小登记

```yaml
---
type: issue
id: ISSUE-001
related_task: TASK-001
project:
contract_profile: staged-v1
status: open
severity:
owner:
updated:
---
```

# ISSUE-001 | 问题标题

## 原始现象

- 用户可见症状：保留用户触发入口与表面现象。
- 期望行为：
- 影响范围：
- 证据：直接证据或明确观察缺口。
- 责任 / 待确认：

## 按调查进展补齐

确认后补复现路径、直接事实、已排除项、候选根因和根因边界；先最小可区分实验，再决定扩样。external_ref、source_branch、EP、TASK、risk、服务台账只关联实际对象，不为了表单创建整条链。

## 修复与复验

修复前确认授权与影响；执行合同复用 TASK 或当前授权。进入修复阶段补 impact（取值同 TASK）、授权依据、执行范围、下一动作；高风险补 `pre_action_check: allowed: 当前动作 / 目标 / 证据` 与恢复方法，跨仓补 Git preflight 与回传入口。服务相关关闭补 service-side validation、end-to-end validation、非默认值 / 边界值的 `passed: 证据引用`。引用也要能定位对应字段。关闭时填写：

- 最新有效报告：
- 验证结果：passed / failed / untested
- 反向复验：原始复现修复前后对照或等价证据。
- 回归守卫：
- 未验证边界：
- 关闭结论：本次能关闭哪一层，不自动关闭 EP / Gate。
