---
name: cross-project-skill-adoption-prompt
description: 跨工程技能迁移任务书生成技能；用于把已沉淀技能或能力抽象成可交给目标工程 agent 执行的提示词、资料清单、吸收边界、落位步骤和验证要求。
maturity: mature
evidence_signals: [skill, README entry, governance, template, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only skill-maturity
---

# Cross-Project Skill Adoption Prompt

## 定位

本技能把“某个工程已经沉淀好的能力”转换成目标工程 agent 可直接执行的迁移任务书。这里的能力可以是单项 skill，也可以是更上层的 Agent System Capability Package；后者必须覆盖 skill、runtime、harness、memory、evaluation、governance、migration 和 intelligence evidence lens，不能退回成只迁移 `SKILL.md`。

它吸收 AcknowledgeBase 的 meta-skill 思路：先上游归一，再目标迁移。若某个下游工程的技能比源技能更成熟，必须先把通用增量抽象回本库源能力或标成待确认参考；不要从下游 A 直接复制到目标 B。

## 适用场景

- 用户要求“把某个技能迁移到其他工程”。
- 用户要求“生成一段提示词”，让目标工程 agent 升级某项能力。
- 用户要求把复盘、issue 分析、调研、图文呈现、治理审计、文档维护、Goal Contract 或 Harness 治理扩散到其他工程。
- 用户要求目标工程被外部矩阵、agent-system maturity diagnostics、CI、public readback 或独立 evaluator 识别。
- 用户要求升级 agent system / intelligence maturity，而不只是补单项技能。
- 用户明确要求附上已有知识、模板、本机路径、吸收边界和验证要求。

## 边界

- 本技能默认只生成任务书，不直接修改目标工程，除非用户明确授权当前轮进入目标工程执行。
- 不整库复制，不原样搬运项目事实、运行 ID、服务实例、业务链路、一次性 handoff、排行或分数。
- 通用迁移不变量是任务书骨架；主题内容必须来自源 `SKILL.md`、`TRANSFER.md`、模板或规则，不从其他样例借字段。
- 目标工程结构自检写进任务书，由目标工程 agent 执行；本技能不预设目标工程目录。

## 成熟度与证据信号

- `maturity`：`mature`。本技能已有技能正文、README 入口、迁移边界和治理接线；如源工程或本库维护 golden examples / golden baseline，生成任务书必须按 `generated >= baseline` 做产物级对照。
- `template`：源能力归一清单见 [[templates/skill-transfer-manifest-template]]；可复制任务书骨架见 [[templates/skill-transfer-contract-template]]，证据和审核分别见 [[templates/skill-transfer-evidence-contract]]、[[templates/skill-transfer-review-contract]]；最终产物仍必须按目标工程结构自检后裁剪。
- `governance`：跨项目反哺和项目事实剥离回到 [[template-feedback-rules]]；写入目标工程前必须确认授权。
- `TRANSFER`：迁移边界见 [[skills/cross-project-skill-adoption-prompt/TRANSFER]]。
- `frontier maintenance`：任务书必须写清 source-depth、`skill-name`、true-gap / recognition-gap / signal-only-gap、Matrix Recognition Capsule、verification-loop、runtime / outcome / external readback 边界；有 golden baseline 时必须保持 `generated >= baseline`。
- `evidence boundary`：本技能生成的是迁移任务书，不代表目标工程已经完成迁移、通过验收或被外部 evaluator 读回。

## 工作流

### 1. 判执行合同

先确定：

- 用户要的是任务书、源技能维护、还是直接执行迁移。
- 本次迁移的能力名称。
- 源能力路径：`SKILL.md`、`TRANSFER.md`、模板、治理页、sensor 或报告。
- 是否存在用户提供的强样稿、golden baseline、版本锚点或禁止项。

### 2. 抽取源能力

从源材料抽取：

- 能力目标和触发场景。
- 事实源 / 证据源。
- 必备模块和字段。
- 工作流和输出格式。
- 禁止项、相近材料边界和不上推边界。
- 验证方式、sensor、检查命令或人工自检。

如果源技能没有 `TRANSFER.md`，先生成一次性任务书，同时建议补迁移边界。

源能力归一时先形成 source-depth 判断：源 `SKILL.md`、`TRANSFER.md`、模板、治理页、sensor、views / registry 和 owner 页面分别提供什么证据，哪些只是历史样例或项目事实。高价值通用技能应优先填 [[templates/skill-transfer-manifest-template]] 的能力目标、可吸收、只能抽象吸收、禁止复制、目标工程结构自检、验证要求和任务书基线；缺少 manifest 时，任务书只能标为 `source-needs-normalization` 或一次性迁移建议。

如果迁移对象是 agent system / intelligence maturity，源能力抽取必须额外读取或要求目标 agent 自查等价 owner：

- Agent system owner：七层对象、system profile、snapshot、blocked reason 和不上推边界。
- Intelligence evidence：八维 `dimension_scores`、positive / negative / missing evidence、cap reason、evaluator provenance。
- Matrix Recognition Capsule：candidate files / scanned surfaces、baseline、true-gap、recognition-gap、signal-only-gap、Goodhart guard、external readback / blocked。
- Tight loop：baseline -> patch -> evaluate -> diagnose -> patch -> re-run -> stop；外部 evaluator 由主控持有，目标 agent 只回传 evidence + limits。

### 3. 判断是否要先归一源能力

如果候选增量来自下游工程，先分类：

- 项目事实、业务路由、服务实例、运行路径、一次性状态：不吸收。
- 可复用触发、事实源分层、输出结构、模板字段、回写守卫、导出策略、检查方式：先归一到源能力。
- 本轮未授权改源能力：在任务书里标为“待人工确认参考”，不能伪装成已吸收标准。

### 4. 展开任务模块

每个模块至少写：

- 目标。
- 必写字段 / 判断项。
- 落位候选或结构自检规则。
- 反模式 / 禁止项。
- 验证点。

### 5. 生成任务书

任务书按目标 agent 执行顺序组织：

1. 直接命令。
2. 背景和目标。
3. 参考资料。
4. 吸收边界。
5. 目标工程结构自检和落位。
6. 需要建立或更新的模块。
7. 技能 / 模板 / 规则 / sensor 接入要求。
8. 行动分流和单一信息源。
9. 验证和提交要求。
10. 最终回复要求。

### 6. 失败模式审查

输出前检查：

- 目标 agent 是否知道第一步读什么。
- 每个模块是否到字段级，而不是只有模块名。
- 哪些相近页面不能替代本能力是否写清。
- 没有对应目录时如何保守落位是否写清。
- 验证、提交、未验证边界和最终回复是否写清。
- 是否误带具体目标工程事实、源工程排行或未确认提交锚点。

### 7. Golden baseline 对照

当用户提供手写样稿、旧提示词、参考任务书，或源工程存在 `examples/` golden 样例时，先把样稿拆成 baseline rubric，再生成。baseline 至少检查：

- 开头命令是否明确升级 `<能力名称>`，而不是只新增目录、模板或说明页。
- 目标定义是否说明长期问题和应反哺的流程、规则、模板、验证或 agent 工作方式。
- 参考资料是否覆盖源 `SKILL.md`、`TRANSFER.md`、相关 concept / docs、template、governance、sensor 或检查脚本。
- 吸收边界是否写清可以吸收、只能抽象吸收和禁止复制。
- 目标工程结构自检是否要求先读目标工程入口，再按既有 docs / projects / skills / templates / reports / governance / scripts 落位。
- 主题模块是否来自当前源 skill / `TRANSFER.md`，并展开到目标、必填字段 / 判断项、反模式和验证点。
- 入口同步、验证、提交和最终回复是否让目标 agent 能照单完成并回传证据。

如果生成稿比 baseline 更短、更抽象、缺少字段级模块、缺少禁止项或更像说明文而不是任务书，判定为失败并重写。通用化只能删除具体工程事实，不能删除任务书主干、章节顺序、字段粒度、验证和最终交付要求。

### 8. 任务书质量门

生成迁移任务书前，逐项检查：

- `直接命令` 是否让目标 agent 知道第一步读目标工程入口规则，而不是直接写文件。
- `参考资料` 是否区分源 skill、TRANSFER、template、governance、sensor 和目标工程入口。
- `吸收边界` 是否明确可以吸收、只能抽象吸收和禁止复制。
- `结构自检` 是否让目标工程自行判断已有 skill / template / governance / sensor / views，而不是预设目录。
- `模块要求` 是否到字段级，能让目标 agent 直接执行。
- `验证要求` 是否包含专项 sensor、总检查、手工回看和未验证边界。
- `最终回复` 是否要求交代已更新文件、检查结果、未吸收内容和 commit。
- `Transfer Manifest` 是否说明了 source-depth、taskbook-ready、harness-governance 接线和不复制项目事实。
- `Matrix Recognition Capsule` 是否说明 evaluator、candidate files、baseline、true-gap、recognition-gap、signal-only-gap、Goodhart guard 和 external readback / blocked。
- `Agent System Capability Package` 是否覆盖 skill、runtime、harness、memory、evaluation、governance、migration 和 intelligence evidence lens。
- `Golden baseline` 如存在，生成稿是否 `generated >= baseline`，没有弱化章节顺序、字段粒度、禁止项、验证和最终回复要求；如果没有本地 baseline，要在任务书里说明按源 `TRANSFER.md` 和目标工程结构自检补齐。

如果缺任一项，先补任务书，不急着迁移目标工程。

## 输出格式

```markdown
请升级目标工程的 <能力名称> 体系。

## 背景和目标

## 参考资料
- <本机路径或目标 agent 可读路径>

## 吸收边界
- 可以吸收：
- 只能抽象吸收：
- 禁止复制：

## 目标工程结构自检与落位

## 需要建立或更新的模块

## 技能 / 模板 / 规则 / sensor 接入要求

## 行动分流和单一信息源

## 验证和提交要求

## 最终回复要求
- 已更新的落位、检查结果、commit hash、未验证边界和后续建议
```

## 禁止项

- 不把提示词写成泛泛迁移说明；必须是可执行任务书。
- 不用某个主题的字段污染所有技能迁移。
- 不复制下游工程的业务事实、服务名、表名、运行 ID、本地路径或提交规则。
- 不预设目标工程结构；让目标工程 agent 自检并保守落位。
- 不把迁移任务书当成目标工程已经完成迁移。
- 不在缺少 source-depth、Transfer Manifest 或等价自检时声称任务书已经 `taskbook-ready`。
- 不把 skill maturity 高分上推成 agent system / intelligence 高分。
- 不用本地检查通过、Worker 自述或 expected impact 替代外部 evaluator readback。
- 不把 golden baseline 压缩成更短、更抽象的说明文；只能做通用化补丁和边界增强。
