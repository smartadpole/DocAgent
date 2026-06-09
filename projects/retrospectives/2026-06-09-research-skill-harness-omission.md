---
type: retrospective
project: wiki
status: active
source_of_truth: false
updated: 2026-06-09
tags: [retrospective, agent-work, harness, research-skill]
---

# 调研技能加固后漏做 Harness 判断复盘

上游：[[concepts/agent-work-retrospective]]、[[harness-evolution]]、[[harness-feedback-ledger]]、[[log]]

关联对象：[[skills/technology-research-router/SKILL]]、[[skills/technical-topic-research/SKILL]]、[[skills/open-source-project-research/SKILL]]、[[skills/industry-ai-research/SKILL]]

沉淀路由：[[harness-feedback-ledger]]、[[log]]

## 复盘对象

- **时间范围**：2026-06-09，本轮“用当前的调研知识储备，武装本工程的调研技能”到后续用户指出“除了更新 log，harness 没有更新吗”的连续对话。
- **对象类型**：Agent 工作。
- **复盘目标**：还原为什么会在技能加固完成后漏做 Harness episode 判断，区分事实、根因和候选改进。
- **不做范围**：不重判调研技能加固本身是否有价值；不把本次复盘直接升级成新硬规则或 sensor；不重写既有 ledger 结论。

## 原始目标

- 目标：把已经沉淀的技术调研知识储备真正装进本工程调研技能，使后续调研工作按对象、证据、成熟度、风险和沉淀合同执行。
- 非目标：不是再补一轮技术调研内容；也不是在未发生明确失守前直接扩一轮 Harness 规则。
- 约束：保持 scope 在调研技能相关页面；不混入无关脏改；收尾要经过知识库检查和提交闭环。
- 验收或成功口径：调研技能得到加强，相关记录沉淀完整，工作区干净，用户能看出本轮提升了什么。

## 实际结果

- 已完成：四个调研技能完成加固并提交；随后在用户指出后补写了 [[harness-feedback-ledger]] episode 和 [[log]]。
- 未完成：第一次提交 `a5187c0` 时，没有同步做 H5 episode 资格判断。
- 偏离或降级：把“是否需要更新 Harness”留在了用户追问之后，而不是在第一次收尾里主动完成。
- 超出预期：补漏后形成了明确的 observed episode，可作为后续是否升级模板字段或 sensor 的依据。
- 遗留风险：如果后续 skill / governance 类改动仍主要依赖人工记忆做 H5 资格判断，同类漏项可能再次发生。

## 关键事实

### 证据地图

- 当前对话上下文：用户先要求武装调研技能，之后追问“工作区干净了吧”“除了更新 log，harness 没有更新吗”“不对，你应该发动复盘技能”。
- log：[[log]] 已记录技能加固、补 ledger，以及当前这次复盘技能补记。
- Issue / 事故 / report：无。
- trace / decision / memory：不适用；本次主要依赖治理页、技能页、git 和当前对话。
- git diff / commit：`a5187c0` 只改了四个技能和 `log.md`；`1040a50` 才补 ledger；本次复盘再落独立复盘档案。
- 检查 / 测试输出：当时 `python3 scripts/check_all.py --only knowledge-linking` 与 `python3 scripts/check_all.py` 都通过，但这只能证明知识库结构和门禁通过，不能替代 H5 资格判断。
- 原始 session / rollout：未读取，当前复盘依赖当前上下文、git、ledger、log 和治理页，足够支撑本次结论。
- 缺口：没有独立的收尾模板字段或 sensor 强制 agent 显式回答“本轮是否形成 H5 episode”。

| 时间 / 节点 | 事实 | 证据 |
| --- | --- | --- |
| 技能加固阶段 | 本轮主交付是强化四个调研技能，使其继承总控 intake、证据等级、成熟度和风险门 | `a5187c0`、[[skills/technology-research-router/SKILL]] |
| 第一次收尾 | 完成 `log + checks + commit`，但没有补 [[harness-feedback-ledger]] | `a5187c0` 的 diff 只含技能和 `log.md` |
| 用户纠偏 | 用户指出“除了更新 log，harness 没有更新吗” | 当前对话上下文 |
| 补漏阶段 | 补写 observed episode 到 [[harness-feedback-ledger]]，并写入 [[log]] | `1040a50`、[[harness-feedback-ledger]] |
| 再次纠偏 | 用户指出这次解释不应只口头说明，而应启动复盘技能 | 当前对话上下文 |

## 偏差与原因

| 偏差 | 类型 | 证据等级 | 原因判断 | 影响 |
| --- | --- | --- | --- | --- |
| 技能加固后第一次收尾漏做 H5 episode 资格判断 | Agent 工作 / 收尾 | confirmed | 收尾阶段把注意力集中在技能交付、检查和提交闭环，遗漏了“skill / governance 类改动后是否形成 Harness episode”的判断步骤 | 让 Harness 更新依赖用户追问，削弱了自演进闭环的主动性 |
| 把“不要过度治理”理解成“这轮可以先不判断 Harness” | 阶段判断 / 路由 | likely | 过于强调资格判断的“不要无条件仪式化”，但没有先做 yes/no 判断再决定不落地 | 造成规则在执行层短暂掉到 L0，靠记忆而不是流程触发 |
| 门禁通过被误当成收尾完成度足够高 | 验证 | likely | `check_all.py` 覆盖的是结构门禁，不覆盖“本轮是否需要新增 episode”这一人工语义判断 | 容易让收尾显得完整，但对 Harness 自演进仍有盲区 |

## Agent 工作回看

- 目标理解：对“武装调研技能”的主目标理解是对的，没有把任务做成再补一轮调研文章。
- 阶段判断：前半段判断为技能升级是对的；后半段收尾时，没有把“技能升级可能触发 Harness 补记”视为同轮必要判断。
- 上下文读取：读到了总控技能、分支技能、skill-creator 约束；第一次收尾时没有再回看 [[harness-evolution]] 和 [[instruction-adherence]]。
- 工具使用：读取、patch、检查、提交链路是稳定的。
- 执行策略：主交付推进顺畅，但收尾 checklist 少了一项 H5 资格判断。
- 验证质量：结构检查充分，治理语义判断不完整。
- 沟通节奏：技能加固过程中的进度同步正常，但第一次最终回复没有主动说明 “harness: no update, reason=...”。
- 权限和边界控制：scope 控制是好的，没有混入无关文件。
- 沉淀路由：第一次只落了 `log`，第二次才补 `ledger`，说明沉淀路由存在收尾漏项。
- 收尾和提交质量：提交边界和工作区清理是好的，但 Harness 自演进闭环第一次没有完整关闭。

## 保留做法

- 主任务阶段先把调研技能本体做扎实，再处理治理补记，没有把技能加固和更大范围规则改造混成一轮。
- 提交边界控制是清楚的，第一次和第二次提交都没有混入无关改动。
- 用户指出缺口后，能够迅速把问题降级为 observed episode，而不是直接上升成新硬规则。

## 改进行动

| 行动 | owner | 落点 | 完成口径 | 检查方式 |
| --- | --- | --- | --- | --- |
| 对 skill / governance / template 类改动，收尾时显式回答一次 `harness: updated / no-episode` | agent workflow | 候选进入 [[harness-feedback-ledger]] 后继续观察 | 后续同类任务的最终回复或复盘正文里可见这一判断 | 历史抽样复盘 |
| 若再次出现同类漏项，再把 H5 资格判断提升为模板字段或 sensor 候选 | harness evolution | [[harness-feedback-ledger]] | 出现第二次相似失守后，从 `observed` 晋升为更高层动作 | [[harness-evolution]] 周期复盘 |

## 沉淀路由

- 项目记忆：不写入。
- trace：不写入。
- 决策：不写入。
- 设计：不写入。
- 研发事项：不写入。
- Issue / 事故：不写入。
- 会议 / 跨 owner 协调：不需要。
- 模板 / skill：本轮不直接改模板或技能，先保留为复盘结论。
- 治理规则 / sensor：本轮只记录为 observed episode，不直接升级。
- 暂不落地：是否把 `harness: updated / no-episode` 变成模板字段或 sensor，等待重复样本。

## 治理自演进判断

- 单次表现，继续观察：是。这次先作为单次收尾资格判断失守处理。
- 重复失守，进入 harness ledger：已进入 [[harness-feedback-ledger]]。
- 可模板化：有可能，但当前证据不足以直接升级。
- 可技能化：当前复盘技能已经足够，本轮不改。
- 可脚本化：暂时不适合，因核心仍是语义资格判断。
- 影响 WORKFLOW：暂不改。
- 影响 AGENTS：暂不改。
- 影响 POLICY：暂不改。

## 未验证边界

- 没有抽样更多历史 skill / governance 类提交来判断这是不是更广泛的重复模式。
- 当前结论主要基于本次对话、治理页、git 和 ledger，没有展开读取原始 rollout。
