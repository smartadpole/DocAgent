---
type: template
id: TEMPLATE-RUN-CAPSULE-EXTENSIONS-001
status: active
updated: 2026-10-14
tags: [template, harness, conditional, evaluator]
---

# Run Capsule 条件扩展

入口见 [[templates/run-capsule-template]]。Goal 与 Loop 可以引用本页中适用的专业合同，不需为引用而额外创建 Run Capsule。

## 多角色合流

**触发**：已获授权的多个执行者、主控与子工程或独立验收者需要合流；本页不提供委派与写入授权。

- **Agent Topology**：Orchestrator、Worker、Acceptance / evaluator owner、execution posture（direct-execution / orchestrator-only / worker-assisted / evaluator-required / blocked）；实际采用的 worktree / 仓库 / 只读研究隔离、并行理由与不可并行部分。
- **Worker Ownership**：每个 Worker 的 Scope、Allowed writes、Required evidence、输出入口、limits、Stop condition。
- **继承边界**：引用实际存在的 Goal / Parent Loop Contract / Run Capsule / AGENTS / owning page 约束，不让 Worker 全读无关或不存在的合同。
- **Evaluator**：合流规则、冲突处理、passed / partial / blocked / failed 条件与最终裁决 owner；Worker 只交证据，不关闭整体任务。缺少 limits、未声明不能上推的证据或把局部通过当整体闭环的回传不得用于关闭。
- **Closeout Proof**：已采纳 / 缺失的 Worker 证据、evaluator 结论、检查结果、仍需人工确认项；不能用回传齐全替代验证充分。

## 外部仓库现场检查

**触发**：操作子工程代码、handoff 或外部仓库。在实际操作前刷新，记录可链接的现场输出，不能缓存安全事实。

- **Subproject Git Preflight**：directory、branch / upstream、remotes、fetch state（not-run / fetched / blocked）、fetch 后 ahead / behind / diverged、dirty / untracked、local-only risk、授权的更新策略。
- **更新边界**：默认不 pull / merge / rebase / reset；只有用户授权且 fast-forward safe 才更新。保护未提交内容，跨仓写入仍需 allowed write roots；fetch 失败或未做时如实记录，不声称远端已核对。

## 分层证据

**触发**：功能 / 服务 / 端到端多层验证、参数效果、相关回归或人工确认影响完成判定。

| 验证面 | 证据链接与结果 | 缺口 / limits |
| --- | --- | --- |
| 仅列本轮完成判定需要的层级 |  |  |

层级选自 code-level / unit、functional / business-flow、service-side、end-to-end、non-default / boundary、related regression、manual-confirmation。涉及参数时必须证明非默认值 / 边界值改变实际结果，不能只看回显。删去不适用层级，但必要层级缺测必须保留缺口；写清辅助证据为何不能上推至父项 / Gate。

## 循环回传

**触发**：本 run 消费持久 Loop 的队列项。

- **Parent Loop Contract / Input discovery item**：实际合同、队列项与本轮 consumed inputs；不要链接模板冒充运行合同。
- **State transition**：queued / running / passed / partial / blocked / failed / skipped 的前后状态、持久化位置与真实读回。
- **Next-run recommendation**：stop / rerun / retry-after / split / escalate / wait-human / schedule-next，触发条件与接手 owner。
- **Process Record**：关键命令、文件变更、决策和失败项的证据位置；不把流水复制成项目事实源。最终状态由 Loop 的独立 evaluator 采纳，不由 Worker 自述上推。

## 沉淀与复盘

**触发**：影响未来理解的新事实、用户纠偏 / 检查失败 / 重复失守、稳定背景、可复用流程，或用户明确要求复盘。普通完成无新增信息不生成路由表或 no-op 证明。

| 实际信号 | 落点与边界 |
| --- | --- |
| 需要回看的过程变化 | [[log]]；不替代事实 owner |
| 用户纠偏、模式偏差或重复失守 | [[harness-feedback-ledger]]；先有 episode，按 [[harness-evolution]] 决定是否晋升 |
| 稳定背景 | [[BRAIN]] / [[projects/memory/README]] |
| 可复用流程 / 字段 / 机器可检查约束 | skill / template / sensor；记录 Reuse entry proof 和实际入口，不能因生成文件就声称效果已验证 |
| 改变规则或权限 | 回到 [[POLICY]] / [[AGENTS]] 的授权和裁定流程 |
| 显式复盘或已有长期学习信号 | [[skills/retrospective-capability/SKILL]]；Agent 工作对象使用 [[skills/historical-dialogue-retrospective/SKILL]] |

只记录实际沉淀路径与理由。标准 / 深度复盘要形成档案和索引，显式请求不得被自动 no-op 降级；Worker 可回传复盘信号，evaluator 按证据裁决深度，不用“多 agent / 长 Goal / Loop”标签强制复盘仪式。复盘不替代 Issue、报告、handoff、trace 或事项关闭。
