---
name: work-item-auto-decomposition
description: 项目 / 领域绑定的研发事项自动拆解技能；用于本仓需求、Gate、FP、EP、TASK、risk、issue、test、验收关系不完整时，按 wiki 自己的研发事项模型生成候选拆解、关系节点和关闭证据。
maturity: adopted
evidence_signals: [skill, README entry, governance, template, sensor, report]
transfer_ready: false
sensor: python3 scripts/check_all.py --only work-item-matrix,agent-system-maturity
---

# Work Item Auto Decomposition

## 定位

本技能把当前 wiki 的研发事项拆解固定为一个项目 / 领域绑定能力。它只服务本仓已经采用的 `Gate -> FP -> EP -> TASK` 主链，以及 risk / issue / test / 验收 / 报告 / 服务台账关系节点。

它不是通用可迁移 skill。跨工程只可抽象“先读目标工程事项模型、关系节点、模板和关闭守卫”的方法，不能把 wiki 的目录、编号、状态或当前项目事实复制到别的工程。

## 适用场景

- 用户要求自动拆解需求、Gate、FP、EP、TASK、risk、issue、test 或验收关系。
- 发现需求、trace、设计、Gate、FP、EP、TASK、risk、issue、报告或 service registry 之间关系不完整。
- 代码工程或子工程回传了新事实，需要判断是否派生 TASK、risk、issue、测试报告或验收计划。
- 外部矩阵指出 `work-item-auto-decomposition` 缺口，但本仓只能做项目绑定能力，不能硬升通用技能。

## 边界

- 事实源以 [[projects/development/plan/work-item-system-model]]、[[projects/development/plan/task-design-model]]、[[projects/development/plan/test-acceptance-planning-model]]、[[projects/development/execution/execution-packages/README]]、[[projects/development/execution/tasks/README]]、[[projects/development/issues/README]]、[[projects/development/reports/README]]、[[projects/service-registry]]、[[projects/trace]] 和当前授权材料为准。
- 本技能只输出候选拆解、关系矩阵、关闭证据和回写建议；正式状态推进仍回到对应 Gate / FP / EP / TASK / issue / report owner。
- 没有父 EP 的 TASK 只能作为关系校准候选，不能直接派发为正式编码任务。
- 已发生 bug、偏差、验收失败或用户可见问题必须进入 Issue；未发生风险只写 `risk:` 和 `issue-trigger:`，不预建 issue。
- TASK done 只能作为父 EP 输入证据，不能自动关闭父 EP、FP 或 Gate。

## 成熟度与证据信号

- `maturity`：`adopted`，已接入本仓事项模型、技能入口、矩阵模板和专项 sensor。
- `governance`：主规则在 [[projects/development/plan/work-item-system-model]]，TASK 细节在 [[projects/development/plan/task-design-model]]。
- `template`：矩阵输出参考 [[templates/development-work-item-matrix-template]]；EP / TASK / Issue / report 使用对应模板。
- `sensor`：`python3 scripts/check_all.py --only work-item-matrix,agent-system-maturity` 检查树状编号、关系节点、关闭证据和不上推边界的 wiring。
- `transfer_ready`：`false`。这是项目 / 领域绑定能力，不作为所有工程默认通用 skill。
- `evidence boundary`：本技能产出的候选矩阵不代表事项已创建、状态已关闭、测试已通过或外部 evaluator 已认可。

## 工作流

1. 读取本轮目标和授权范围，确认是需求拆解、执行包拆解、issue 派生、验收补齐还是外部矩阵 recognition。
2. 按最小相关事实源读取：requirements / trace / design / Gate / FP / EP / TASK / risk / issue / report / service registry / handoff。
3. 判断当前缺口类型：
   - `true-gap`：确实缺父级、关系节点、输出物、关闭证据、回归守卫或测试计划。
   - `recognition-gap`：已有事项关系，但模板、入口或 sensor 不可识别。
   - `signal-only-gap`：只影响矩阵标记，不值得制造空 TASK / EP / skill。
4. 输出候选 `Gate -> FP -> EP -> TASK` 树，不越级创建正式事项。
5. 为每一行补齐主责模块、输出物、关闭证据、回归守卫、反馈回写和 `risk:`、`test:`、`验收:`、`issue-trigger:`。
6. 标注不能上推的关闭边界，尤其是 TASK done、局部报告通过、handoff 通过和结构检查通过。
7. 给出应回写的 owner：需求 / trace / design / Gate / FP / EP / TASK / risk / issue / AP / report / service registry / log。
8. 运行或要求运行 `work-item-matrix` 专项检查；涉及 agent system external recognition 时再运行 `agent-system-maturity`。

## 输出格式

```markdown
**拆解对象**
- 来源：
- 当前目标：
- 授权范围：

**缺口分类**
| 缺口 | 类型 | 证据 | 处理 |
| --- | --- | --- | --- |

**候选事项矩阵**
| 树状编号 | 上游需求 / 目标 | Gate | 功能点 / 候选项 | EP | TASK | 子工程增量 | 关系类型 | 主责模块 | 当前状态 | 输出物 | 关闭证据 | 回归守卫 | 关系节点覆盖 | 反馈回写 | 未确认项 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

**关闭边界**
- TASK：
- EP：
- FP / Gate：
- Issue / risk：
- 外部 evaluator：

**回写建议**
- owner 页面：
- 验证命令：
- 未验证边界：
```

## 禁止项

- 不把本技能硬升为所有工程通用 skill。
- 不为矩阵分数创建空 EP、空 TASK、空 risk、空 issue 或平行看板。
- 不把未发生风险预建成 issue；只写 `issue-trigger:`。
- 不把小任务误升 EP，不绕过父 EP，不让 TASK 直接代表 Gate 准出。
- 不让测试报告替代测试计划，不用默认 happy path 代替边界值 / 非默认值验证。
- 不把 `check_all.py` 通过、本地结构 green 或 Worker 自述写成外部 evaluator readback。
