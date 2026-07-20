---
type: template
id: TEMPLATE-SKILL-TRANSFER-MANIFEST-001
status: active
updated: 2026-06-26
tags: [template, skill-transfer, manifest, transferable-skill-governance]
---

# Skill Transfer Manifest Template

用于高价值通用技能迁移前的源能力清单、边界裁决和目标工程自检。它比 `skill-transfer-contract-template` 更偏源能力归一和迁移边界；真正交给目标工程 agent 执行的任务书仍使用 [[templates/skill-transfer-contract-template]]。

## 基本信息

- **能力名称**：
- **源技能**：
- **适用迁移场景**：
- **不适用场景**：
- **上游归一状态**：ready / source-needs-normalization / target-needs-discovery / blocked
- **矩阵快照 / source_revision**：

## 参考资料路径

- **核心 skill**：
- **TRANSFER**：
- **方法 / concept**：
- **模板**：
- **规则 / workflow**：
- **运行层或档案入口**：
- **检查脚本 / sensor**：

## Project Conformance

- **local_source_of_truth**：
- **allowed_write_scope**：
- **required_profile**：
- **validation_command**：
- **blocked_when_missing**：
- **exceptions**：

## 源能力覆盖矩阵

| 层 | 当前证据 | 可迁移内容 | 不可迁移内容 | 目标工程验证 |
| --- | --- | --- | --- | --- |
| 方法层 |  |  |  |  |
| 技能 / 执行层 |  |  |  |  |
| 模板层 |  |  |  |  |
| 规则 / 治理层 |  |  |  |  |
| sensor / 验证层 |  |  |  |  |
| views / 呈现层 |  |  |  |  |
| 行动分流 / 单一信息源 |  |  |  |  |

## 可以吸收

- 触发条件：
- 事实源分层：
- 执行流程：
- 输出格式：
- 验证方式：
- 回写守卫：
- 禁止项：

## 只能抽象吸收

- 目录形态：
- 项目状态：
- 服务 / 环境：
- 运行 ID / 数据表：
- handoff / 历史 log：
- 一次性验证样例：

## 禁止复制

- 项目事实：
- 业务链路：
- 密钥 / 凭据 / 内网地址：
- 源工程成熟度分数或排行：
- 未确认 owner / 状态 / 验收结论：

## 目标工程结构自检

1. 目标工程已有哪个同名或等价能力？
2. 缺口是真能力缺失、可检测落点缺失，还是 signal-only gap？
3. 目标工程的 `local_source_of_truth` 是哪个入口？
4. `allowed_write_scope` 和只读边界是什么？
5. 需要的 `required_profile`、profile、host、运行环境或人工确认是什么？
6. `validation_command` 或人工 review 清单是什么？
7. 缺少哪些内容时必须 `blocked_when_missing`？
8. 有哪些 `exceptions`，不应强行套完整技能包？

## 目标工程应新增或更新

| 模块 | 新建 / 更新 / 不做 | 最小字段 | 验证 |
| --- | --- | --- | --- |
| skill |  |  |  |
| TRANSFER |  |  |  |
| template |  |  |  |
| governance |  |  |  |
| sensor |  |  |  |
| views / registry |  |  |  |
| README / INDEX / AGENTS |  |  |  |
| log / report / owner page |  |  |  |

## 任务书基线

- **开头命令**：
- **目标定义**：
- **参考资料分组**：
- **目标工程结构自检重点**：
- **必须建立或更新的主题模块**：
- **相近目录防误用规则**：
- **行动分流和单一信息源**：
- **验证和提交要求**：
- **最终回复要求**：

## 验证要求

- **专项 sensor**：
- **完整检查**：
- **手工回看**：
- **负向样例 / 未做原因**：
- **未验证边界**：

## 最终回复要求

- 目标结构读取结果：
- 推荐落位：
- 已新增或更新模块：
- 检查结果：
- commit hash：
- 未吸收内容及原因：
- 未验证边界：
