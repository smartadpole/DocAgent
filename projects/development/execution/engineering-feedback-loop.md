---
type: development_workflow
id: DEV-FEEDBACK-LOOP-001
project: PROJ-WIKI-001
status: active
updated: 2026-05-25
tags: [development, feedback, correction, validation]
---

# 工程反馈纠偏闭环

主入口：[[projects/development/execution/README]]

上游：[[projects/development/plan/README]]、[[projects/development/plan/work-item-system-model]]、[[projects/development/execution/developer-execution-workflow]]、[[projects/development/execution/tasks/README]]、[[projects/development/issues/README]]、[[projects/development/reports/README]]  \
下游：[[projects/development/execution/worklog]]、[[projects/development/execution/execution-packages/README]]、[[projects/trace]]、[[projects/decisions]]、[[projects/meetings/worklog]]

## 这页解决什么

这页回答编码过程中信息如何回流，以及出现偏差、错误、疑惑和验收失败时怎么及时修正。

核心原则：

- 工程师不需要维护整套文档系统。
- 工程师只需要按固定格式反馈代码改动、测试结果、偏差和阻塞。
- Codex / 文档维护者负责把反馈路由到 TASK、父 EP、Issue、测试报告、服务台账、设计、trace、决策或会议；TODO 只保留为轻量兼容入口。

## 正向链路和反向链路

```text
正向：需求 -> trace -> 设计 -> Gate -> FP -> EP -> TASK -> 实现 / 测试
反向：实现 / 测试 -> TASK / 报告 / Issue -> EP -> FP -> Gate -> 设计 -> trace -> 需求
```

反馈必须回到它影响的最上游层级，不能只改当前 TASK 或轻量 TODO。

## 反馈路由

| 反馈发现 | 最远回写层级 | 说明 |
| --- | --- | --- |
| 实现 bug | TASK / Issue / worklog / 测试报告 | 需求和设计不变，只修实现和测试；已发生问题进入 Issue |
| 测试方案 / 测试用例缺失 | 测试报告 / TASK / EP / FP | 补测试方案、用例或检查点，不改需求范围 |
| 相关功能回归缺失 | 测试报告 / TASK / EP / FP | 把受影响的相邻功能、上下游合同、共享配置或写入路径补进回归范围 |
| 字段、接口、状态、错误码不清 | 设计 / Gate 方案 / FP / EP | 先补合同，再继续实现 |
| 功能点粒度不够 | 候选 backlog / FP / EP / TASK | 重新拆候选项、父 EP 或 TASK；TODO 只作过渡 |
| Gate 准出不成立 | Gate 方案 / status / 风险 / EP / TASK | 阻止阶段推进，生成补齐任务 |
| 用户纠偏范围或验收 | requirements / trace / design / FP / EP / TASK | 从需求层重新传播 |
| 架构取舍变化 | decisions / design / trace | 先形成取舍，再改执行项 |

## 最小反馈格式

默认复制 [[templates/engineering-feedback-template]]，不要在本页维护第二份模板正文。

“需要判断或协调的事项”不是闲聊，而是正式回传内容。涉及接口、数据、验收、平台增强边界或业务 owner 判断不清时，都要写出来并分流。

## 完成定义

一个开发任务完成，不只看代码合并，还要满足：

- 功能点或待办状态更新。
- TASK 和父 EP 状态、证据和不上推边界已更新。
- 测试结果已记录。
- 失败和阻塞已归口。
- 设计变化已同步。
- Gate 级测试报告已更新或说明无需更新。
