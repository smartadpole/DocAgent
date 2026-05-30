---
type: article
id: ARTICLE-AGENT-GOVERNANCE-REFLECTION-DOCCUSTOMER-20260530
status: active
updated: 2026-05-30
tags: [agent, governance, harness, reflection, doccustomer, case-study]
---

# Agent 治理反思：以 DocCustomer 为例

相关：[[concepts/agent-governance]]、[[harness-feedback-ledger]]、[[governance/harness-evolution]]、[[governance/instruction-adherence]]、[[governance/execution-contract-semantics]]、[[articles/2026-05-29-finalizer-write-scope-case]]、[[articles/2026-05-25-agent-response-efficiency-governance-reflection]]

## 来源

本页来自 2026-05-30 对 DocCustomer 主控工程 agent 治理体系的整体反思，结合 [[harness-feedback-ledger]] 已积累的 episode、sensor backlog 和 rule prune queue，归纳当前治理体系的结构性问题并提出方向建议。不是执行计划，不产生新 issue，结论作为后续演进的参考基准。

## 一句话总结

DocCustomer 的治理体系在快速迭代期积累了一套可运作的规则闭环，但存在**规则只增不减的正反馈陷阱、角色边界模糊、分流链路过重、状态层次冗余和门禁兜底掩盖前置失效**五类系统性问题，建议从减负、硬隔离和精简层次三个方向分步改进。

---

## 八个结构性问题

### 1. 规则入口是「只增不减」的正反馈陷阱

最核心的问题：每次 agent 犯错，系统就往 AGENTS.md / WORKFLOW / governance 里加规则。Feedback Ledger 里 30+ 条 episode 几乎全是"应避免成本 → 规则升级"，但规则越长，agent 读取成本越高，遗漏概率越大，于是又犯错，于是又加规则。系统自己也观察到这个问题（2026-05-28 "Harness 结构臃肿"），但打补丁的方式仍然是加规则（新增复杂度预算要求）。

AGENTS.md 当前超过 360 行，几乎没有任何空白行，密度极高。这不是 agent 能稳定执行的格式。

**根因**：Rule Prune Queue 是 backlog 不是执行动作，没有人或机制来触发它。

### 2. Agent 角色边界模糊

这套系统里「agent」同时指：AI 模型（Codex/Claude 在跑任务）、治理系统本身（Harness）、各种 sensor 脚本。三者的职责边界模糊。没有一张表回答「哪类任务 agent 可以自主完成，哪类必须人工确认」。现有 POLICY.md 定义了晋升规则，但没有定义执行授权层级。结果是：每次 agent 面对新情况，都要从头推导，容易在推导中漂移。

### 3. 响应模式分流本身需要读 4+ 个文件才能执行

AGENTS.md 第一条是「先读 response-mode-routing」，response-mode-routing 里又引用 POLICY、AGENTS、WORKFLOW、instruction-adherence……一个简单任务，光是找到「当前该走哪个模式」就需要跨 5 个文件做推导。这个设计假设 agent 有无限上下文且能完美执行交叉引用，但实际上 agent 在复杂依赖链下容易在某一步短路。

### 4. 验收/状态层次过多，传播规则容易冲突

EP → FP → TASK → risk → issue → Gate → AP，七层工作项每层有自己的状态、关闭标准、证据层级和向上传播规则。Feedback Ledger 里有多条 episode 指向这里的混淆：「证据角色回流污染」、「Goal 验收维度与全量执行目标混淆」、「非目标环境防御性说明污染」。层次多不是问题，但缺少「哪层的状态谁能修改」的权限矩阵，导致 agent 经常误写。

### 5. Finalizer 逃生舱越来越多，说明前置流程不可靠

`agent_finalizer.py` 设计为最后一道门禁，但现在已经有 `--allow-residual`、`--allow-external-residual`、`--scope-base`、`--allowed-path`、`--scope-manifest` 等多个例外参数。一个设计良好的最终门禁不该有这么多例外路径。这些参数的出现表明前置的写入白名单和模式分流没有可靠运行，门禁在兜住本该更早发现的问题。详见 [[articles/2026-05-29-finalizer-write-scope-case]]。

### 6. 子工程写入边界反复失守

Ledger 里有至少 3 条 episode 关于主控 agent 误改子工程（"外部子工程写入边界失守"、"验收反馈误执行为子工程代码补丁"）。每次的修复方案是：加规则、加 sensor、加白名单 proof。但根本问题是：**当前工作区路径 ≠ 写入权限**这个判断，靠自然语言规则让 agent 在每轮开头自我声明是不可靠的。这应该是工具层/系统层的硬隔离，而不是让 agent 靠读 AGENTS.md 记住。

### 7. log.md 的治理精力投入与实际价值不对等

系统对 log.md 的规则极其复杂（AGENTS.md 里约 20 条专项规则），包括：同一天不同意图不能合并、标题不加前缀、记录人只能是 git config 值等。但 log.md 是「时间降序的过程记录」，不是决策文件也不是主入口。这个精力投入和文件的实际读者价值不成比例。

### 8. 治理层自参照风险

修改规则的规则（"规则改动守卫"）本身也是规则，由同一个 agent 执行。这意味着：agent 如果执行失误，它也有可能错误地修改了用于约束它自身的规则，然后在没有发现错误的情况下提交。系统没有为治理层规则设计独立的人工审核卡口，只有 `scripts/check_harness_governance.py` 做格式检查，但格式正确不等于语义正确。

---

## 改进方向

| 问题 | 建议方向 |
|---|---|
| 规则只增不减 | 把 Rule Prune Queue 变成硬性季度执行动作，而不是 backlog；每次规则升级同时标记一条候选清理 |
| 入口密度过高 | AGENTS.md 只保留 P0 硬约束和跳转，细节全部移到 owning page；目标是 100 行以内 |
| 子工程隔离靠规则 | 用系统层机制（worktree 隔离、工具层路径检查）替代自然语言声明，规则只作为补充说明 |
| 响应模式分流太重 | 默认只走一个模式（快速诊断），需要切模式时显式声明，而不是每轮都判断 8 个模式 |
| 工作项层次过多 | 对当前项目阶段，精简到 3 层（Gate → EP → TASK），其余归入注释或软关联 |
| 门禁例外参数膨胀 | 收紧 finalizer 例外参数数量；凡是需要新增例外参数的场景，先问「前置流程哪里可以更早拦截」 |
| log.md 规则过重 | 把 log.md 规则精简到 3 条硬约束（格式、唯一性、来源），其余变为约定说明，不进入 sensor |
| 治理层自参照 | 治理层任何实质性变更在 commit 中标注 `[GOVERNANCE]`，并由用户 review 后方可合并 |

---

## 与已有案例的关联

- **Finalizer 写入范围失守**（[[articles/2026-05-29-finalizer-write-scope-case]]）是问题 5 和 6 的具体实例，揭示了 scope proof 缺口。
- **响应效率治理反思**（[[articles/2026-05-25-agent-response-efficiency-governance-reflection]]）是问题 3 的早期观察，已部分转化为 [[response-mode-routing]]，但分流链路本身的重量尚未被解决。
- **DocCustomeranalysis Harness 反哺**（ledger 2026-05-25 条目）是当前体系主要治理规则的来源，本页是对那次升级效果的回看。

## 执行建议

本页不产生 issue，不修改 AGENTS.md。后续可作为下一次 [[templates/harness-evolution-review-template]] 复盘的输入基准，对照上述 8 个问题逐项评估是否有新 episode 覆盖或可晋升的规则变更。
