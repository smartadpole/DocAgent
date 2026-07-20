# Transferable Skill Governance Transfer

## 能力目标

让目标工程能把外部成熟度矩阵、源技能和下游经验转成可执行、可验证、可维护的本地能力升级，同时防止复制项目事实、制造平行系统或追逐弱信号。

## 可以吸收

- `true-gap / recognition-gap / signal-only-gap` 三分判断。
- `recognize / complete / upgrade / merge / adapt / defer / reject` 决策枚举。
- 最小耐久落点：`SKILL.md`、`TRANSFER.md`、governance、template、sensor、views 的按需组合。
- 矩阵边界：leader 只代表结构信号强，不等于执行质量。
- 验证边界：sensor 证明 wiring，不能上推为真实运行质量或验收闭环。
- 单一信息源守卫：优先复用目标工程已有结构，不照搬外部目录。
- 通用 skill 前沿维护 review：source-depth、TRANSFER、golden example / review contract、verification-loop、runtime / outcome / external readback 边界、Goodhart guard。
- Agent system 分层裁决：skill、runtime、harness、memory、evaluation、governance、migration 和 intelligence evidence lens 分开判断。
- Matrix adoption manifest：矩阵级吸收必须有 repo-native 清单，写明 source snapshot、source-depth、local_source_of_truth、allowed_write_scope、required_profile、validation_command、blocked_when_missing、exceptions、逐能力裁决和未验证边界；本仓示例为 [[skills/transferable-skill-governance/matrix-adoption-2026-06-26-agent-evidence-v12]]。

## 只能抽象吸收

- 下游工程的目录、handoff 形态、报告结构、检查脚本模式和视图组织方式。
- 某次审计的分数、路径、commit、检查输出和项目状态。
- 源工程的业务名、服务名、运行实例和领域事实只能作为抽象方法来源。
- 项目 / 领域绑定能力的树状编号、关系矩阵、模板字段、服务台账字段和报告写法只能抽象方法；是否落为本地 skill 由目标工程自身结构决定。

## 禁止复制

- 不复制项目事实、业务链路、表名、服务名、运行 ID、真实路径、历史 log、密钥、环境配置或一次性验收结果。
- 不为追矩阵分数创建空技能、空模板、空 view 或大段无执行价值正文。
- 不把外部工程的本地规则、状态页或 handoff 变成本库通用真相源。
- 不把 skill maturity 高分上推成 agent system / intelligence maturity 高分。
- 不把外部 readback 的 blocked / expected impact 写成 passed。

## 目标工程结构自检

1. 目标工程已有哪个本地等价能力？
2. 缺口是真能力缺失、可识别落点缺失，还是弱信号缺口？
3. 哪些源内容是系统层信息，哪些是项目材料？
4. 新增落点会不会形成第二真相源或重复入口？
5. sensor 能证明什么，不能证明什么？
6. 最终回复是否列出拒绝、defer 和未验证边界？
7. 如果是通用 skill，source-depth、TRANSFER、review contract、verification-loop 和 external readback 边界是否齐全？
8. 如果是项目 / 领域绑定能力，是否明确 `transfer_ready: false` 或等价不可通用迁移说明？
9. 如果涉及外部 evaluator，是否填写 Matrix Recognition Capsule 并区分本地检查、expected impact 和 external readback？
10. 如果是矩阵级吸收，是否有 Matrix adoption manifest，并且它没有替代真正 owner 页？

## 验证要求

- 输出逐能力决策表，至少包含原状态、缺口类型、处理方式、落位和剩余边界。
- 矩阵级吸收必须通过 `python3 scripts/check_all.py --only transferable-skill-baseline` 或目标工程等价检查。
- 新增或更新的 skill 必须进入 `skills/README.md` 并通过 `skill-maturity`。
- 新增 sensor 必须接入目标工程统一检查入口或说明没有总检查时的替代验证。
- 最终回复必须区分结构 wiring、矩阵状态和真实运行质量。
- agent-system / intelligence maturity 任务必须列出七层对象、八维 evidence lens、仍为 `insufficient-evidence` 的维度和 external readback blocked / passed 状态。
