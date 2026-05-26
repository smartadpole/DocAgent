# 验收计划模板

使用位置：[[projects/development/acceptance/plans/README]]

```md
---
type: acceptance_plan
id: AP-XXX
target_items: []
status: planned
updated: YYYY-MM-DD
---

# AP-XXX 标题

## 基本信息

- 验收对象：
- 对象类型：TASK / ISSUE / EP / FP / Gate / Release
- 计划来源：
- 报告落点：
- 当前裁决：适用 / 不适用 / blocked

## 验收目标

- 要证明什么：
- 用户可见或系统可观察结果：
- 非目标：

## 环境路由

- 开发 / local：
- CI：
- 集成 / service-side：
- 预发 / 灰度：
- 生产 / release：
- 外部依赖 / 读回源：

## 测试方案

- 测试维度：
- 核心路径：
- 失败路径：
- 非默认值 / 边界值：
- 历史能力回归：

## Fixture / Oracle

- 固定样本：
- 预期结果 / oracle：
- 数据来源：
- 版本：
- 失效条件：

## 人工确认

- 需要人工确认项：
- owner / 角色：
- 未确认前状态上限：

## 报告要求

- 必须保留的截图 / 日志 / API / DB / artifact 证据：
- 子工程回传证据：
- 执行偏差处理：

## 上推边界

- 本计划通过能关闭什么：
- 只能作为上游输入什么：
- 不能上推关闭什么：
```
