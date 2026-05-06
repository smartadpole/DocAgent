---
type: development_plan
id: DEV-WORK-ITEM-SYSTEM-001
project: PROJ-WIKI-001
status: active
source_of_truth: true
updated: 2026-05-06
tags: [development, planning, work-items, traceability]
---

# 需求到事项的系统模型

主入口：[[projects/development/plan/README]]

上游：[[projects/requirements]]、[[projects/trace]]、[[projects/design/README]]  \
横向：[[projects/development/feature-points/README]]、[[projects/development/execution/todo]]、[[projects/development/execution/engineering-feedback-loop]]  \
下游：[[projects/development/reports/README]]、[[projects/status]]

## 这页解决什么

这页回答“需求、目标、功能点、TODO、反馈和验收这些事项之间是什么关系”。

核心目标不是把列表做复杂，而是保证每一个事项都服务于系统化完成一个需求，避免因为局部修复、复验失败或单个工程建议，把原始目标、阶段边界和关闭标准带偏。

## 核心不变量

所有研发事项都必须能回答这 6 个问题：

| 问题 | 目的 | 主落点 |
| --- | --- | --- |
| 它服务哪个需求或目标 | 防止无源任务膨胀 | [[projects/requirements]]、[[projects/trace]]、本页 |
| 它属于哪类事项 | 区分目标、能力、执行、证据、风险或决策 | 本页、[[projects/development/execution/todo]] |
| 它和上游是什么关系 | 判断分解、实现、派生、阻塞、约束或验证 | [[projects/development/execution/todo]]、[[projects/development/execution/engineering-feedback-loop]] |
| 它产出什么可验收结果 | 避免只写主题或过程动作 | TODO、功能点页、测试报告 |
| 什么证据能关闭它 | 避免代码完成、handoff 通过和 Gate 准出混用 | [[projects/development/reports/README]]、[[projects/development/execution/worklog]] |
| 它的反馈要回写到哪 | 避免局部修复改变总目标却没有 trace | [[projects/trace]]、设计页、风险、会议或决策 |

没有上游目标、关系类型和关闭证据的 TODO，不应作为 Gate 准出依据。

## 事项类型

| 类型 | 负责回答 | 不负责什么 |
| --- | --- | --- |
| 需求 / 目标 | 为什么做、做到什么算有价值 | 不直接写代码任务 |
| Gate | 阶段准入和准出条件 | 不替代单功能验收 |
| 功能能力 | 系统需要哪些能力 | 不替代当前下一步 |
| 执行事项 | 下一步做什么、谁主责、交什么 | 不作为第二份需求或第二份设计 |
| 证据事项 | 证明某项做到哪一层 | 不自动关闭上游目标 |
| 控制事项 | 风险、待确认项和拍板问题 | 不承担实现本身 |

## 关系类型

| 关系 | 含义 | 使用时机 |
| --- | --- | --- |
| `decomposes` | 上游目标被拆成能力或子能力 | 需求到功能点、功能点到候选项 |
| `realizes` | 执行事项实现某项能力 | TODO 对应功能能力 |
| `enables` | 一个事项让后续事项可执行 | 基础设施、合同、fixture、配置 |
| `derives_from` | 从反馈、失败或缺口派生补修 | bug、漏测、合同缺口 |
| `constrains` | 一项约束限制另一项实现方式 | 权限、容量、运行模式、外部规则 |
| `validates` | 证据验证事项是否成立 | 测试报告、复验、Gate 报告 |
| `blocks` | 未确认项阻塞关闭或准出 | owner、凭据、业务事实、权限 |
| `feeds_back_to` | 实现反馈反向修正上游 | 合同变化、设计不成立、验收边界变化 |
| `supersedes / absorbs` | 一个事项覆盖或吸收另一个事项的范围 | 重复 TODO、下游吸收 handoff |

关系可以是多条，但必须标主关系。

## 推荐矩阵

```md
| 上游需求 / 目标 | Gate | 功能点 / 候选项 | TODO | 关系类型 | 主责模块 | 当前状态 | 输出物 | 关闭证据 | 反馈回写 | 未确认项 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

## 防跑偏策略

| 新问题类型 | 能否改变需求 / 目标 | 默认处理 |
| --- | --- | --- |
| 实现 bug | 否 | 修实现、补测试、更新 worklog 和测试报告 |
| 合同缺口 | 可能 | 先补设计 / Gate 方案和 TODO，若改变范围再回写 trace |
| 验收缺口 | 否，除非验收标准本身不成立 | 补测试报告、TODO 和相关回归范围 |
| 运行质量缺口 | 可能后置 | 判断是否属于当前 Gate 关闭前置；否则进风险或后续阶段 |
| 业务事实缺失 | 可能阻塞准出 | 进入待人工确认、风险或会议，不让 agent 代拍板 |
| 需求范围变化 | 是 | 先更新 [[projects/requirements]] 和 [[projects/trace]]，必要时进 [[projects/decisions]] |

局部修复不能直接改总目标。只有当新问题被判定为“需求范围变化”或“设计口径不成立”时，才允许从 TODO 反向改需求、trace 或设计。

## 关闭守卫

| 事项类型 | 最小关闭证据 |
| --- | --- |
| 功能能力 | 对应 TODO 已完成、测试证据存在、相关功能回归已处理 |
| TODO | 输出物存在，测试 / 复验证据存在，失败项和待人工确认项已归口，下游吸收关系明确 |
| 派生 TODO | 来源问题已解释，补修结果已验证，对源 TODO 的反向影响已同步 |
| Gate 准出 | 覆盖矩阵、测试报告、风险 / 人工确认项和 owner 决议齐全 |

如果一个 TODO 只是产出 handoff、执行包、字段合同、细化稿或报告草稿，且下游吸收还没完成，默认只能停在 `review`。
