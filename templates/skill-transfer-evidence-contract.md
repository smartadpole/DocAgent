---
type: template
id: TEMPLATE-SKILL-TRANSFER-EVIDENCE-CONTRACT-001
status: active
updated: 2026-06-12
tags: [template, skill-transfer, skill-adoption, evidence-contract, cross-project-skill-adoption-prompt]
---

# Skill Transfer Evidence Contract

本模板用于 `cross-project-skill-adoption-prompt` 的迁移证据合同。它回答：源能力哪些内容真的可迁移，目标工程需要建立哪些证据，哪些内容必须拒绝复制。

## 1. 源能力证据

| 证据 | 路径 | 可迁移内容 | 不可迁移内容 | 备注 |
| --- | --- | --- | --- | --- |
| SKILL.md |  | 触发、流程、输出、禁止项 | 项目事实 |  |
| TRANSFER.md |  | 吸收边界 | 源项目状态 |  |
| template |  | 字段骨架 | 示例事实 |  |
| governance |  | 裁定条件 | 本地规则细节 |  |
| sensor |  | 检查思想 | 路径硬编码 |  |
| views / reports |  | 呈现方式 | 当前数据 |  |

## 2. 目标工程证据

| 目标证据 | 是否存在 | 读取结果 | 决定 |
| --- | --- | --- | --- |
| 根 AGENTS |  |  |  |
| 最近 owning AGENTS |  |  |  |
| skills 目录 |  |  |  |
| templates 目录 |  |  |  |
| governance / rules |  |  |  |
| scripts/check_all |  |  |  |
| views / reports |  |  |  |
| README / INDEX |  |  |  |

## 3. 吸收裁定

### 可以直接吸收

- 触发条件：
- 事实源分层：
- 输出格式：
- 质量门：
- sensor 入口：

### 只能抽象吸收

- 目录名：
- 业务对象：
- 服务边界：
- 运行证据：
- 项目状态：

### 禁止吸收

- 密钥、凭据、账号、内网地址：
- 源项目一次性 handoff：
- 源项目具体运行 ID：
- 源项目成熟度排行：
- 未经目标工程确认的 owner / 状态：

## 4. 目标落位裁定

| 模块 | 新建 / 更新 / 不做 | 理由 | 验证 |
| --- | --- | --- | --- |
| skill |  |  |  |
| TRANSFER |  |  |  |
| governance |  |  |  |
| template |  |  |  |
| sensor |  |  |  |
| entry |  |  |  |
| log |  |  |  |

## 5. 迁移完成定义

迁移完成必须同时满足：

- 目标工程入口能发现能力。
- 目标工程 agent 知道触发条件。
- 目标工程有迁移边界。
- 目标工程有验证方式。
- 目标工程没有复制源项目事实。
- 最终回复写明未吸收内容和原因。
- 如果产生文件变化，按目标工程规则检查和提交。

## 6. 未完成边界

- 没跑 sensor：
- 目标工程缺权限：
- 结构冲突未裁定：
- 用户只要求任务书：
- 源能力自身还未归一：
- 目标工程不允许回写：
