---
type: development_workflow
id: DEV-FEEDBACK-LOOP-001
project: PROJ-WIKI-001
status: active
updated: 2026-05-06
tags: [development, feedback, correction, validation]
---

# 工程反馈纠偏闭环

主入口：[[projects/development/execution/README]]

上游：[[projects/development/plan/README]]、[[projects/development/execution/developer-execution-workflow]]、[[projects/development/execution/todo]]、[[projects/development/reports/README]]  \
下游：[[projects/development/execution/worklog]]、[[projects/trace]]、[[projects/decisions]]、[[projects/meetings/worklog]]

## 这页解决什么

这页回答编码过程中信息如何回流，以及出现偏差、错误、疑惑和验收失败时怎么及时修正。

核心原则：

- 工程师不需要维护整套文档系统。
- 工程师只需要按固定格式反馈代码改动、测试结果、偏差和阻塞。
- Codex / 文档维护者负责把反馈路由到待办、功能点、测试报告、设计、trace、决策或会议。

## 正向链路和反向链路

```text
正向：需求 -> trace -> 设计 -> 功能点 -> TODO -> 实现 / 测试
反向：实现 / 测试 -> TODO / 测试报告 -> FP -> 设计 -> trace -> 需求
```

反馈必须回到它影响的最上游层级，不能只改当前 TODO。

## 反馈路由

| 反馈发现 | 最远回写层级 | 说明 |
| --- | --- | --- |
| 实现 bug | TODO / worklog / 测试报告 | 需求和设计不变，只修实现和测试 |
| 测试方案 / 测试用例缺失 | 测试报告 / TODO / FP | 补测试方案、用例或检查点，不改需求范围 |
| 相关功能回归缺失 | 测试报告 / TODO / FP | 把受影响的相邻功能、上下游合同、共享配置或写入路径补进回归范围 |
| 字段、接口、状态、错误码不清 | 设计 / Gate 方案 / FP | 先补合同，再继续实现 |
| 功能点粒度不够 | 候选 backlog / FP / TODO | 重新拆候选项或提升实体页 |
| Gate 准出不成立 | Gate 方案 / status / 风险 / TODO | 阻止阶段推进，生成补齐任务 |
| 用户纠偏范围或验收 | requirements / trace / design / FP / TODO | 从需求层重新传播 |
| 架构取舍变化 | decisions / design / trace | 先形成取舍，再改执行项 |

## 最小反馈格式

```md
- 任务 / 候选 ID：
- 改动代码位置：
- 新增或修改的接口 / 表 / 状态 / 配置：
- 跑过的测试：
- 测试结果：
- 发现的问题：
- 需要判断或协调的事项：
```

“需要判断或协调的事项”不是闲聊，而是正式回传内容。涉及接口、数据、验收、平台增强边界或业务 owner 判断不清时，都要写出来并分流。

## 完成定义

一个开发任务完成，不只看代码合并，还要满足：

- 功能点或待办状态更新。
- 测试结果已记录。
- 失败和阻塞已归口。
- 设计变化已同步。
- Gate 级测试报告已更新或说明无需更新。
