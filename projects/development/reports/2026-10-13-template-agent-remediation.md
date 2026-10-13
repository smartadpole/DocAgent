---
type: test-report
id: REPORT-TEMPLATE-AGENT-20261013
project: PROJ-WIKI-001
status: verified-local
updated: 2026-10-13
tags: [agent, template, governance, validation]
---

# 模板 Agent 执行基线整改

设计 owner：[[projects/design/topics/agent-workflow-memory-harness-skill-landing|模板执行基线]]。计划来源为本轮模板治理委托与该 owner 的要求映射；本报告只证明本轮范围，不关闭其他 Gate、EP 或运行层事项。

## 对象与取舍

源能力为已校准的单一入口、按需加载、原生技能发现、独立 Goal / Loop 触发、阶段合同和证据不可覆盖语义。源版本与私有跨仓 preflight 留在授权的私有记录；公开模板只保存去标识能力、原生实现和验证方法。

根规则保留 P0 融合问候、公开安全、权限、证据与提交 guard，专业细则从原根页迁至四个唯一条件 owner。原 `.codex/AGENTS.md` 的重复规则删除，仅保留根导入；新增 Claude 导入。18 个现有技能以相对链接提供发现，无技能正文副本。研究、复盘、知识结构、图文与业务绑定事项技能保留。

Goal、Loop、Run Capsule 在 Skill、workflow、路由、模板和 ledger 的当前裁决上同步替换。TASK / Issue 以最小登记开始，按影响 / 阶段补执行与关闭证据；沿用 parent_ep 和本地编号。当前无旧事项实例；新实例遗漏 profile、重复字段、失败结果覆盖、缺授权或只用 local 证据关闭服务事项会失败。

## 验证面

- 静态与功能回归：9 个入口 / 相对技能链接回归、23 个阶段 / 影响回归，含真实模板抽取并实例化的最小 TASK / Issue；30 项完整门禁通过，记录随本次提交封存。
- 配置发现：Codex 原生 `skills/list` 强制刷新，返回 18 个 repo 技能、errors 为空。此项证明项目发现和当前路径，不证明所有模型都会正确使用。
- 模板移植：隔离目录复制相对链接与隐藏入口后运行入口、阶段与事项检查；负向删除 adapter 导入、移除技能链接、篡改合同应被拒绝。四项隔离检查退出 0，三个破坏性负例均退出 1，随后恢复候选副本。
- 模型行为 / service-side / end-to-end：未对所有平台和模型做真实任务对照；本任务没有业务服务变更，不宣称生产或长期 token 收益已验证。
- 公开安全：机器检查与人工 diff 复核；不写入私有工程身份、绝对本机路径、内部 remote 或运行凭据。

## 收尾与回退

本轮在既有工作分支实施，初始工作区干净；只提交本轮明确文件，读回 commit、staged 与剩余 dirty，未推送。提交身份由包含本报告的 Git commit 给出，避免自引用 hash 导致重复补交。

回退需审阅后整体 revert 此次提交，同时恢复入口、条件页、技能链接、模板与 sensor；不能只恢复旧触发句。后续派生工程在自身采纳边界校准身份、权限、分支与能力包，不能继承模板维护者的机器身份或私有事实。

Persistence Decision：artifact-needed，落在现有设计 owner、本报告与 [[log]]；上游只吸收模板继承 / 移植验证的系统层增量。文件缩短、结构门禁和原生技能发现均不能上推为整个 Agent 体系运行效果已完成。
