---
type: development_acceptance_plans
id: DEV-ACCEPTANCE-PLANS-001
project: PROJ-WIKI-001
status: active
source_of_truth: true
updated: 2026-05-26
tags: [development, acceptance, testing, plans]
---

# AP 验收计划索引

主入口：[[projects/development/acceptance/README]]

`AP-*` 是复杂验收的测试前承接文件。它回答“本轮按什么计划验、在哪个证据面验、报告落到哪里、什么不能上推”，不记录执行后的证据流水。

## AP 覆盖审计

| 覆盖项 | 要求 |
| --- | --- |
| L2 | 普通 issue / Bug、跨组件 TASK、真实服务组、DB / artifact / UI readback、灰度验证需要 AP，除非已有等价 AP |
| L3 | Gate、FP 准出、EP 聚合、生产发布、业务发布必须有 AP |
| AP 缺失 | 写明不适用原因，不能静默跳过 |
| 目标事项未回链 | AP frontmatter 或正文必须声明 target_items，目标事项也要能回到 AP |
| 报告没有计划来源 | 报告只能作为临时观察，不能作为关闭证据 |
| 环境路由把环境写成错误层级 | 必须回到事项对象和证据需求重新裁决 |
| release checklist | 发布 AP 必须覆盖版本、配置 readback、health、监控、回滚、观察窗口 |

## AP 编号

- `AP-TASK-*`：复杂 TASK 验收。
- `AP-ISSUE-*`：已发生问题修复闭环。
- `AP-EP-*`：多组件或模块级验收。
- `AP-FP-*`：能力级验收。
- `AP-GATE-*`：阶段准出。
- `AP-RELEASE-*`：上线 / 发布确认。

## 模板

默认复制 [[templates/development-acceptance-plan-template]]，不要在本页维护第二份模板正文。
