---
type: design-topic
id: DES-TOPIC-LOCAL-GIT-SYNC-001
project: PROJ-WIKI-001
status: proposed
stage: governance-design
updated: 2026-07-08
tags: [design, agent, git, branch, sync, governance]
---

# 本机 Git 分支与同步语义设计专题

上游：[[projects/design/topics/README]]、[[agent-orchestration]]、[[state-constraint-reasoning]]、[[instruction-adherence]]

关联：[[AGENTS]]、[[harness-feedback-ledger]]、[[log]]

## 设计对象

本专题沉淀两个本机 Codex 工作流设计方案：

1. 本机 Git 工程默认在以本机命名的分支工作；当前本机名为 `macpro`。
2. 用户说“git 同步”时，同步目标默认覆盖当前分支、`master` 分支、它们各自的远程分支状态，以及当前分支与本地 `master` 之间的代码关系。

这两个方案当前只作为 agent 升级 topic 保存，不等价于已经写入 wiki 当前硬规则。

## 非目标

- 不直接修改 [[AGENTS]]、[[POLICY]]、[[WORKFLOW]] 或治理页的生效规则。
- 不要求本轮批量扫描、切换或同步所有本机 Git 仓库。
- 不把一次本机偏好自动上推为所有工程、所有机器或所有远程的通用规则。
- 不允许为了分支切换或同步而重置、覆盖或丢弃用户未提交改动。

## 方案 A：本机命名分支

候选口径：

- 本机工作默认分支按设备名收口；当前设备名是 `macpro`，默认工作分支为 `macpro`。
- 新建、接手或继续本机 Git 工程时，先读当前分支、remote 和 dirty 状态。
- 若用户明确指定其他分支、PR / 远程分支，或仓库级 release / hotfix 规则优先，则按更高优先级执行，并在最终回复说明原因。

待拍板问题：

- 该规则是否只适用于 Codex 本机任务，还是也作为目标工程通用 agent 模板能力。
- 已经长期使用 `master` / `main` / 项目专用分支的仓库，是否需要自动创建 `macpro`，还是仅在新任务中使用。
- 多设备协作时是否使用各设备名分支，还是统一使用任务分支。

## 方案 B：git 同步语义

候选口径：

- “git 同步”不是只 push 当前分支。
- 默认先 `fetch --all --prune`，再分别检查当前分支和 `master` 的 upstream / remote / ahead / behind。
- 当前分支与 `master` 都需要和对应远程分支读回 `0 0`。
- 当前分支与本地 `master` 也必须完成关系判断：是否互相包含、是否分叉、是否存在未解释差异；需要代码一致时，只能用明确且安全的 fast-forward / merge / rebase 策略处理。
- 多远程仓库需要逐一说明同步状态；只读、缺分支、无权限或远程不存在时写为边界或阻塞。
- dirty、diverged、无 upstream、缺少 `master`、当前分支与本地 `master` 冲突或存在未跟踪文件时，优先保护用户改动，并将动作降级为 `conditional / blocked`。

待拍板问题：

- `master` 是否固定为第二同步分支，还是应按仓库默认分支自动识别 `master / main`。
- 多远程同步是否必须覆盖所有 remote，还是只覆盖当前 upstream 和用户指定 remote。
- 当前分支与本地 `master` 的目标是完全一致、互相包含，还是只要求没有未解释差异。
- 对脏工作区是否允许自动 stash，还是必须先请求确认。

本轮确认：

- “git 同步”至少要覆盖三组关系：当前分支 ↔ 远程当前分支、本地 `master` ↔ 远程 `master`、当前分支 ↔ 本地 `master`。
- 若第三组关系不能安全收敛，最终回复必须写清阻塞原因、当前差异和需要用户拍板的合并策略。

## 可能落位

如果后续拍板为 wiki 生效规则，推荐分层落位：

- [[AGENTS]]：只写最短硬约束和触发词。
- [[state-constraint-reasoning]]：承接 branch、remote、upstream、ahead / behind、dirty、diverged 和权限状态判断。
- [[agent-orchestration]]：承接 Subproject Git Preflight 和 Worker / Evaluator 的同步证明边界。
- [[instruction-adherence]]：承接“git 同步”触发矩阵和最终回复证明。
- [[harness-feedback-ledger]]：只在真实失守或规则晋升时记录 episode。

## 采纳条件

- 已确认适用范围：本机偏好、wiki 工程规则、还是跨工程 agent 模板规则。
- 已确认默认分支策略：固定 `macpro`，还是设备名变量。
- 已确认默认同步分支策略：固定 `master`，还是识别仓库默认分支。
- 已确认当前分支与本地 `master` 的同步目标和允许策略。
- 已确认多远程和 dirty 工作区处理策略。
- 已有最小验证：至少一个仓库的 current branch、`master`、remote、branch-to-master 关系和 dirty 状态读回样例。

## 当前裁决

状态：`proposed`。

本专题只保存设计方案和待拍板问题。没有进一步拍板前，不把它写成 wiki 当前生效的 agent 硬规则。
