---
type: design-topic
id: DES-TOPIC-LOCAL-GIT-SYNC-001
project: PROJ-WIKI-001
status: adopted-for-system-codex-config
stage: governance-design
updated: 2026-07-14
tags: [design, agent, git, branch, sync, codex-config]
---

# 本机 Codex Git 分支与同步语义配置方案

上游：[[projects/design/topics/README]]

关联：[[log]]

## 目标一句话

本方案的目标是升级当前机器的**系统级 Codex 配置**，让后续该机器上的 Codex 任务默认遵守：

1. 默认本机工作分支名由本轮用户指定；如果用户没有指定，则从当前主机名推导。
2. 用户说“git 同步”时，必须按三组关系读回和收敛，默认完成态是当前分支、`master`、远程当前分支和远程 `master` 指向同一个 commit。

配置目标不是当前 wiki 仓库，也不是任一业务仓库。

## 目标配置位置

本方案不写死配置路径，必须先在当前机器上自发现 Codex home 和全局指令入口。推荐发现顺序：

1. 读取环境变量 `CODEX_HOME`。
2. 如果没有 `CODEX_HOME`，使用当前用户 home 下的 `.codex`，例如 macOS / Linux 的 `~/.codex`，Windows 的 `%USERPROFILE%\.codex`。
3. 在候选 Codex home 中确认 `config.toml`、`AGENTS.md`、`rules/default.rules` 等实际存在情况。
4. 如当前机器存在多份 Codex home，优先使用当前 Codex 进程实际读取的那一份；无法确认时停止并说明候选路径，不凭惯性写入。

本方案只允许落到这些系统级位置：

- `<CODEX_HOME>/AGENTS.md`：Codex 全局行为规则。默认分支和“git 同步”语义必须写在这里。
- `<CODEX_HOME>/rules/default.rules`：命令级 allow 规则。只在需要放通固定命令时更新，例如 `git fetch --all --prune`。
- 当前用户的全局 Git 配置：只用于 `init.defaultBranch = <default-local-branch>`，不承接 Codex 行为语义。

其中，默认分支和同步语义的单一主落位是当前机器自发现到的 `<CODEX_HOME>/AGENTS.md`，不是固定的某台机器路径。

## 明确非目标

- 不修改当前 wiki 仓库的 [[AGENTS]]、[[WORKFLOW]]、[[POLICY]] 或治理页，把它们伪装成系统级 Codex 配置。
- 不在当前 wiki 仓库或任意业务仓库创建默认本机分支。
- 不创建或删除远程默认本机分支。
- 不执行仓库同步、merge、rebase、reset、stash、push 或 force push。
- 不把默认本机分支当成 GitHub 默认分支、发布分支、PR 分支或所有机器统一分支。
- 不把一台机器的配置路径、主机名或默认分支自动上推为 SmartMacPro、Windows 或其他机器的配置。

如果后续 agent 因为本方案开始操作仓库分支、远程分支或 wiki 治理页，说明执行目标已经走偏，应立即停止并回到本页。

## 配置规则 A：默认本机分支

先确定 `default-local-branch`：

1. 用户本轮明确指定默认分支名时，使用用户指定值，例如 `macmini`。
2. 用户没有指定时，从当前主机名推导：读取 `hostname -s`、macOS 的 `scutil --get LocalHostName` / `scutil --get ComputerName` 或 Windows 的 `%COMPUTERNAME%`，选取最能代表当前机器的短名。
3. 将主机名归一化为可用 Git 分支名：转小写，去掉空格和不适合分支名的标点，保留清晰可读的机器名；归一化前后需要在最终回复里读回说明。
4. 如果主机名为空、明显是临时容器名、或多台机器身份混淆，停止并要求用户指定，不自动猜测。

写入 `<CODEX_HOME>/AGENTS.md` 的语义应当是：

- 默认本机分支是 `<default-local-branch>`。
- 创建、切换或接手仓库前，先检查当前分支、upstream、remote、dirty / untracked、local-only、本地 `master` 和远程关系。
- 用户没有指定其他分支，且仓库没有更高优先级的 release / hotfix / PR / 项目专用分支规则时，优先切换或创建 `<default-local-branch>`。
- 如果需要创建 `<default-local-branch>`，只能在不会覆盖用户改动、不会改写历史、不会破坏仓库既有分支策略时执行。
- 不默认使用 `codex/`、随机任务名前缀或一次性临时分支来替代本机工作分支，除非用户明确要求或项目级规则要求。
- 已经长期使用 `master`、`main`、项目专用分支或 PR 分支的仓库，不因本规则自动改名或强制迁移。

## 配置规则 B：git 同步语义

写入 `<CODEX_HOME>/AGENTS.md` 的语义应当是：

用户说“git 同步”“同步 git”“同步到远程”“和远程 master 同步”“做好同步”或同类请求时，默认覆盖三组关系：

1. 当前分支与远程当前分支。
2. 本地 `master` 与远程 `master`。
3. 当前分支与本地 `master`。

默认执行顺序：

1. 先读 `git status --short --branch`、当前分支、upstream、remote、dirty / untracked 和 local-only 状态。
2. 再执行 `git fetch --all --prune`，不要用陈旧 tracking ref 判断“已经最新”。
3. 分别读回当前分支 ↔ 远程当前分支、本地 `master` ↔ 远程 `master`、当前分支 ↔ 本地 `master` 的 ahead / behind / diverged 关系。
4. 如果三组关系能通过 fast-forward 或普通 merge 安全收敛，按用户目标执行并读回验证。
5. 如果出现 dirty、diverged、无 upstream、缺远程分支、缺本地 `master`、冲突、无权限、可能改写历史，或需要 stash / rebase / reset / force push，必须降级为 `conditional / blocked / ask-human`，并写清当前差异和需要用户拍板的策略。

完成口径：

- 默认完成态不是“差异可解释”，而是本地当前分支、本地 `master`、远程当前分支、远程 `master` 指向同一个 commit。
- 多 remote 且都可写时，完成态覆盖每一个相关远程的当前分支和 `master`；任一远程缺分支、只读或无权限时，必须在最终回复中列为 `blocked` 或边界。
- 只有当前分支、本地 `master`、远程当前分支、远程 `master` 四个面都读回清楚，且所有要求覆盖的 ref 都达到同一 commit，才能说同步完成。
- 如果当前分支已经包含 `master`，安全策略通常是把本地 `master` fast-forward 到当前分支，再推送当前分支和 `master` 到所有要求覆盖的远程，最后重新 fetch 并用 `rev-list --left-right --count` 与 `for-each-ref` 读回。
- 如果 `master` 包含当前分支，安全策略通常是把当前分支 fast-forward 到 `master`，再推送并读回。
- 如果当前分支与 `master` 分叉，或任何一步需要非 fast-forward、冲突解决、rebase、reset、force push、stash 或丢弃未提交改动，不能自行假装同步完成；必须停下说明分叉和可选策略。
- 不允许为了完成同步而自动 reset、overwrite、force push、删除分支、丢弃未提交改动或把未跟踪文件当成可以清理的垃圾。
- 多 remote 仓库至少说明当前 upstream 和用户指定 remote 的状态；如果仓库有多个已配置且可写的远程，默认覆盖所有这些远程，除非用户目标明确排除或权限 / 成本形成阻塞。

## 对照样本

SmartMacPro 的只读检查结论：

- `<SmartMacPro CODEX_HOME>/config.toml` 不承接分支和 git 同步语义，只承接插件、项目 trust level、MCP 等运行配置。
- `<SmartMacPro CODEX_HOME>/AGENTS.md` 承接默认分支和“git 同步”语义。
- `<SmartMacPro CODEX_HOME>/rules/default.rules` 只承接命令级 allow 规则，不承接语义规则。

因此，不同机器都必须按同样结构配置，但路径和默认分支值要在各自机器上自发现或由用户指定，不能把某台机器的 `/Users/...` 路径或 `macmini` / `macpro` 直接复制到另一台机器。

## 验证方式

完成本方案时，只验证系统级配置。先读回当前机器的 `CODEX_HOME` 和 `default-local-branch`，再替换下列占位：

```bash
sed -n '1,120p' <CODEX_HOME>/AGENTS.md
rg -n "Git 分支规则|Git 同步规则|<default-local-branch>|git fetch --all --prune" <CODEX_HOME>/AGENTS.md
git config --global --show-origin --get init.defaultBranch
```

如果检查命令级 allow 规则，只读：

```bash
rg -n "git fetch --all --prune|git merge --no-ff" <CODEX_HOME>/rules/default.rules
```

不需要、也不应该用创建仓库分支或推送远程分支来验证本方案。

## 失败模式与纠偏

| 走偏表现 | 为什么错 | 正确纠偏 |
| --- | --- | --- |
| 去改 wiki 的 [[AGENTS]] / [[WORKFLOW]] / [[POLICY]] | 这些是 wiki 项目规则，不是系统级 Codex 配置 | 自发现当前机器的 `<CODEX_HOME>/AGENTS.md` |
| 写死 `/Users/hai/.codex/AGENTS.md` | 该路径只适合某些 macOS 用户，不适合不同用户名、Windows 或 remote host | 先读 `CODEX_HOME`，否则按当前用户 home 发现 |
| 写死 `macmini` | 默认分支会随机器变化；用户未指定时应使用主机名 | 用户指定优先，否则从当前主机名归一化 |
| 在 wiki 仓库创建默认本机分支 | 把配置目标误解成仓库状态 | 删除误建分支，回到系统配置 |
| 创建远程默认本机分支 | 把本机工作分支偏好误解成远程发布目标 | 删除误建远程分支 |
| 只改 `git config --global init.defaultBranch` | 只影响新仓库初始分支，不影响 Codex 行为语义 | 同步写入 `<CODEX_HOME>/AGENTS.md` |
| 把规则写进 `config.toml` | `config.toml` 不是语义规则主入口 | 使用 `<CODEX_HOME>/AGENTS.md` |

## 当前裁决

状态：`adopted-for-system-codex-config`。

本方案已经明确：配置对象是当前机器自发现到的系统级 Codex 配置；默认分支由用户指定或当前主机名推导；它不是 wiki 仓库治理升级，也不是仓库分支操作方案。
