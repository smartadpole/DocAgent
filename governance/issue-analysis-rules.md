---
type: governance
id: GOV-ISSUE-ANALYSIS-001
scope: shared
status: active
source_of_truth: true
updated: 2026-06-12
tags: [governance, issue-analysis, incident-analysis]
---

# Issue Analysis Rules

本页是 `issue-analysis` 的治理裁定页。[[skills/issue-analysis/SKILL]] 负责执行问题分析；本页负责决定何时进入完整 Issue 分析，何时停在快速根因链，何时转验收、规则升级或知识沉淀。

## 模式边界

| 用户意图 | 默认模式 | 不能越界 |
| --- | --- | --- |
| “为什么 / 在哪 / 先分析” | 快速根因链 | 不自动新建 Issue、TASK、Gate |
| “记录问题 / 设定目标” | intake / 目标冻结 | 不展开排障 |
| “修 / 验收 / 关闭 / 准出” | 修复或验收关闭 | 不把根因分析当关闭证据 |
| “这个规则又没执行” | 规则执行失守分析 | 不只加一句更严厉规则 |
| “沉淀经验” | 知识沉淀或复盘 | 不伪装成现场 issue |

如果中途切换模式，必须告诉用户当前阶段和切换原因。

## 完整 Issue 分析的准入

只有满足以下至少一项，才进入完整 issue-analysis：

- 问题已经影响项目状态、验收、发布、服务运行、数据可信度或跨工程分工。
- 需要裁定 owner、协同方、验证层级或主控吸收方式。
- 已发生 bug、偏差、验收失败或用户可见问题，需要保留原始现象。
- 用户明确要求 issue / incident 分析、案件档案、联测方案或问题闭环。

否则先输出快速 checkpoint：现象、最可信原因、证据、置信度、待确认项。

## 证据分层

Issue 结论必须标注事实源层级：

- `requirements`：需求、设计、Gate、TASK、FP、验收标准。
- `runtime`：服务、调度、worker、日志、状态查询。
- `persistence`：DB readback、manifest、artifact、ledger。
- `presentation`：UI、报告、截图、导出件。
- `agent_process`：本轮操作、漏读、越界、未验证、提交状态。

不要把某一层的通过上推成完整闭环。例如接口返回成功不能等于数据库写入，报告生成不能等于用户验收，子工程 handoff 不能等于主控关闭。

## 原始现象守卫

正式 Issue 案件必须保留用户看到的原始现象：

- 不用推测根因改写问题标题。
- 不用日志错误替代用户现象。
- 不把“可能原因”写成“已发生事实”。
- 不把子工程内部判断直接写成主控裁决。

根因、修复、验证和关闭裁决在后续字段分层记录。

## 输出闭环

完整 issue-analysis 至少输出：

- 问题框。
- 事实源地图。
- 最小根因链。
- 责任边界。
- 分工或修复建议。
- 验证方案。
- 主控文档吸收路径。
- 不能关闭或不能上推的边界。

快速根因链可以短，但也必须区分 `confirmed / likely / possible / blocked`。

## 禁止项

- 不把所有问题都升级成重治理。
- 不把用户只要记录的问题展开成诊断。
- 不把验收报告当 Issue 主档案。
- 不把 reference rule 下沉成下层任务。
- 不用“已分析”替代修复、复验或关闭裁决。
