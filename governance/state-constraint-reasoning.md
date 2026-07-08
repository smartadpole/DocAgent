---
type: governance
id: GOV-STATE-CONSTRAINT-REASONING-001
scope: shared
status: active
source_of_truth: true
updated: 2026-07-08
tags: [governance, harness, state, constraints]
---

# State Constraint Reasoning

这页回答“当前状态允许做什么”。它用于防止 agent 在权限、远程、预算、证据和人工确认状态、文件脏改动、用户确认或外部环境不满足时，把不可执行动作写成普通计划。

## 触发条件

- 动作依赖权限、网络、凭据、远程仓库、浏览器 profile、外部服务、人工确认或生产写入。
- 工作区存在 dirty / diverged / local-only / generated 文件保护等约束。
- 计划会改变状态：提交、推送、发布、关闭事项、改规则、写服务台账、启动持续调度。
- 证据层级可能被上推：local 结果、health、自述或日志被当作 service-side / end-to-end。

## 状态变量

| Variable | 示例 |
| --- | --- |
| workspace | 当前目录、目标仓库、用户指定路径 |
| git | branch、upstream、remote、ahead / behind / diverged、dirty |
| permission | 用户授权、写入边界、生产写入、人工确认 |
| evidence | local / service-side / end-to-end / manual-confirmation |
| budget | 读取、问题、检查、时间、成本、轮次 |
| tool state | 浏览器 profile、端口、服务可用性、凭据存在性 |
| owner | 主控、子工程、Worker、Evaluator、人工 reviewer |

## Git 状态约束

Git 相关动作必须先把 branch、remote、upstream、ahead / behind、dirty、diverged 和 local-only 风险拆开判断，不能合并成一句“已同步 / 未同步”。

- 默认本机工作分支：当前本机名是 `macpro`，本机 Git 工程默认优先在 `macpro` 分支工作；用户明确指定其他分支、指定 PR / 远程分支，或仓库级 release / hotfix 规则优先时才切到其他分支。
- `git 同步` 语义：默认同时覆盖当前分支与 `master` 分支；先 `fetch --all --prune`，再分别判断当前分支和 `master` 对应远程分支的 ahead / behind。
- 多远程语义：如果仓库存在多个已配置且可写远程，逐一确认当前分支和 `master` 在各远程的同步状态；只读、缺分支或无权限的远程必须作为边界写出。
- 脏工作区保护：未提交改动、未跟踪文件、生成物或用户预存脏改动存在时，不得为了 pull / merge / rebase / reset / checkout / push 覆盖或丢弃；只能选择安全暂存、保留原状、请求确认或标记 blocked。
- 完成证明：只有当前分支和 `master` 对应远程分支读回 ahead / behind 为 `0 0`，且多远程边界已说明，才能回答“git 同步完成”。

## 约束传播

1. 先列出会限制行动的状态变量。
2. 判断每个动作是 `executable / conditional / blocked / ask-human`。
3. 把约束传播到计划、模板字段、验证口径和最终回复。
4. 对 conditional 动作写清前置条件；对 blocked 动作写清缺少的事实或权限。
5. 如果约束只影响证据层级，必须写明不能上推到哪一层。

## 输出口径

```markdown
- Target action:
- State variables:
- Constraint:
- Decision: executable / conditional / blocked / ask-human
- Allowed next step:
- Evidence boundary:
- Required owner / confirmation:
```

## 禁止项

- 不把需要授权的 pull / merge / rebase / reset / publish / production write 写成默认动作。
- 不在 remote、branch、dirty 或 upstream 未确认时承诺已经完成同步。
- 不把只推当前分支、只看本地 commit、只看缓存的 `origin/*` 或只同步 `master` 包装成完整 `git 同步`。
- 不把 local check 通过写成 end-to-end 验收。
- 不把“可后续考虑”自动变成当前任务或阻塞项。
