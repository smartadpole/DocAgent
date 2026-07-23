---
name: cross-project-governance-audit
description: 跨工程治理审计技能；用于按需读取多个工程的关键治理文件，对照平台级标准评估成熟度、漂移、共性缺口和可执行 handoff 边界。
maturity: mature
evidence_signals: [skill, README entry, governance, sensor, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only harness-governance,skill-maturity
---

# Cross-Project Governance Audit

## 定位

本技能把多个工程的 agent / harness / governance 状态对照同一组抽象标准做审计，输出漂移、缺口、共性模式和可执行建议。

它吸收上游知识治理库的跨工程治理审计能力，但适配本库边界：本库可以审计和生成建议，不默认维护外部工程注册表，也不直接修改其他工程。wiki 作为对外统一模板时，只输出工程角色、source archetype、capability pack 和证据边界，不把内部工程名写成模板概念。

## 适用场景

- 用户说“审计某工程治理”“看这个工程治理成熟度”“生成漂移报告”。
- 用户要求比较多个工程的 AGENTS、响应路由、harness ledger、sensor、模板反哺或技能成熟度。
- 用户要求把跨工程治理经验吸收到本库模板、规则、技能或 sensor。
- 用户说“举一反三”“所有工程都需要吸收”“不只是某个工程”或等价要求时，必须按内部 source registry 或等价登记面逐工程审计；不能用最强样本、旧矩阵摘要、能力覆盖集或本机路径扫描替代注册表全集；输出到 wiki 模板面时必须匿名化为 source archetype / capability pack。
- 周期性检查当前 wiki 自身治理 wiring 是否仍然完整。

## 边界

- 不直接修改其他工程文件，除非用户明确授权进入目标工程执行。
- 不把外部工程分数、排名、状态或提交记录写成本库事实。
- 不把一次审计建议等同于规则升级；可复用缺口按 [[harness-evolution]]、[[template-feedback-rules]] 和 [[POLICY]] 路由。
- 不用审计报告替代目标工程验收、CI、PR review 或人工拍板。

## 成熟度与证据信号

- `maturity`：`mature`。本技能已有技能正文、README 入口、治理接线、可用 sensor 和迁移边界。
- `template`：跨工程治理审计报告和 handoff-ready 任务书见 [[templates/cross-project-governance-audit-contract-template]]；它承接 source-depth、Drift Report、Transfer Manifest、verification-loop 和 no runtime validation 边界。
- `governance`：本库自查使用 [[response-mode-routing]]、[[harness-evolution]]、[[harness-feedback-ledger]]、[[template-feedback-rules]] 和 [[POLICY]]。
- `TRANSFER`：迁移边界见 [[skills/cross-project-governance-audit/TRANSFER]]。
- `source-depth`：审计必须说明读取了哪些根规则、治理页、技能、模板、sensor、检查输出或 handoff；只读单一入口时只能给轻量判断。
- `evidence boundary`：审计结论代表本轮文件证据信号和 no runtime validation 边界，不代表目标工程运行质量、业务交付或验收状态。
- `drift report`：审计必须把缺口分成 true-gap / recognition-gap / signal-only-gap，并说明是否 handoff-ready；矩阵、文件存在和 sensor 通过都不能替代 runtime validation。

| Benchmark marker | 用途 |
| --- | --- |
| `YYYY-MM-DD` | 审计日期 |
| `YYYY-MM` | 审计月份 |
| `cross-project-governance-audit` | 技能识别 |
| `Cross-Project` | 跨工程范围 |
| `Project Governance Audit` | 审计类型 |
| `git remote -v` | 远端读回 |
| `source-depth` | 读取深度 |
| `handoff-ready` | 可执行任务书 |
| `skill-transfer` | 技能迁移关系 |
| `Transfer Manifest` | 迁移清单 |
| `non-reference` | 不反哺材料 |
| `verification-loop` | 验证闭环 |

## 工作流

### 1. 判断审计模式

- 单工程审计：只读指定工程。
- 多工程对比：读多个工程，输出共性和差异。
- 本库自查：对当前 wiki 的治理 wiring 跑专项 sensor。
- handoff 生成：把审计缺口转换成目标工程可执行任务书，但不执行。

### 2. 建审计基线

默认维度：

1. 执行约束入口：AGENTS / README / project rules。
2. 响应分流机制：快速诊断、沉淀、验收、规则升级、实现回传等模式。
3. Harness 反馈机制：episode、ledger、晋升 / 降级、重复失守处理。
4. Sensor / 自动检查：check_all、专项检查、负向样例或 CI。
5. 模板与技能成熟度：模板字段、技能 frontmatter、TRANSFER、证据边界。
6. 跨工程协作规则：主控 / 子工程写权限、handoff、回传和不复制项目事实。

若本轮是全登记工程吸收，额外固定四个字段：

1. `registry_project`：工程来自哪张登记表，是否属于全集。
2. `system-layer capability`：可抽象吸收的 agent / workflow / memory / harness / skill / evaluation / governance / template / migration 能力。
3. `wiki landing / guard`：进入哪个本仓 owner / skill / sensor；或为什么只 `recognize / adapt / reject`。
4. `project-bound fact`：哪些路径、服务、数据、模型、运行 ID、业务事实或一次性 handoff 不上推。
5. `template-facing name`：输出给 wiki 对外模板时使用工程角色或能力包名，不使用 source project 名称。

### 3. 读取证据

优先读：

- 根 `AGENTS.md` 或等价入口。
- `git remote -v`、`git fetch --all --prune` 和 ahead / behind / diverged 读回；只读审计也要说明是否读取 Git preflight。
- `governance/response-mode-routing.md` 或等价响应路由。
- `governance/harness-feedback-ledger.md`、`harness-evolution` 或等价机制。
- `governance/template-feedback-rules.md` 或跨项目反哺规则。
- `skills/README.md`、`templates/skill-template.md` 和技能目录。
- `scripts/check_all.py`、`scripts/check_*.py` 或 CI 检查。
- 最近相关 `log.md`、commit、PR 或审计报告。

### 4. 打分和定性

每个维度按证据写：

- `confirmed`：文件存在且内容能支撑该机制。
- `partial`：有入口但缺模板、sensor、迁移边界或执行字段。
- `missing`：未见等价机制。
- `blocked`：路径、权限或证据不可读。

成熟度只说明治理信号，不说明项目业务质量。

### 5. 生成漂移和 handoff

输出：

- 整体结论。
- 逐维度证据。
- 主要缺口。
- 已有优势。
- Drift Report：true-gap / recognition-gap / signal-only-gap。
- 可复用共性模式。
- 全登记工程吸收矩阵：每个 registry project 一行；轻量仓也要写最小治理 profile 或 no-op 理由。
- 不反哺项目材料。
- 建议动作和 owner 页面。
- 如果需要，生成目标工程任务书：范围、逐条操作、verification-loop、Transfer Manifest、验证、禁止项和最终回复。
- `handoff-ready` 只表示建议足够交给目标工程 agent 执行；它不是目标工程已修复、已提交、已验证或已验收。
- `non-reference` 材料必须单列：项目事实、业务状态、一次性检查、旧 source revision、排行榜或路径不能进入平台标准。

## 输出格式

```markdown
**审计对象**
- 工程：
- 模式：
- 本轮不做：

**审计基线**
| 维度 | 结论 | 证据 | 缺口 |
| --- | --- | --- | --- |

**Drift Report**
- true-gap：
- recognition-gap：
- signal-only-gap：
- source-depth：
- handoff-ready：
- no runtime validation：
- Transfer Manifest：
- skill-transfer：
- non-reference：
- verification-loop：

**共性模式**
- 可反哺：
- 不反哺：

**handoff 候选**
- 文件：
- 操作：
- 验证：
- 禁止项：

**证据边界**
- 未读：
- blocked：
- 不能上推：
```

## 禁止项

- 不把其他工程的排名、分数或具体状态写成本库规则。
- 不把审计建议自动变成目标工程改动。
- 不用文件存在替代内容质量判断。
- 不把 sensor 通过写成治理完全成熟。
- 不复制外部工程的业务事实、本地路径、服务实例或一次性 handoff。
