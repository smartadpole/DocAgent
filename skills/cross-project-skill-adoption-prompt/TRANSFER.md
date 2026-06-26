# Cross-Project Skill Adoption Prompt Transfer

## 能力目标

让目标工程具备把任意已沉淀技能转换成可执行迁移任务书的能力，支持源能力抽取、吸收边界、目标结构自检、模块落地、验证和最终回复。

## 可以吸收

- 先上游归一、再目标迁移的策略。
- 任务书结构：背景目标、参考资料、吸收边界、结构自检、模块落地、治理 / sensor 接入、验证提交、最终回复。
- 源能力覆盖矩阵：目标、事实源、模块、输出、禁止项、验证。
- Transfer Manifest：用 [[templates/skill-transfer-manifest-template]] 先归一 source-depth、可吸收 / 只能抽象 / 禁止复制、目标工程自检和任务书基线，再生成执行任务书。
- 失败模式审查：是否可执行、是否字段级、是否无项目事实偷渡。
- 对 `TRANSFER.md` 的依赖：transfer-ready 技能优先从迁移清单生成任务书。
- Golden baseline 质量门：如果用户给出强样稿或已有 golden，生成稿必须保持章节顺序、字段粒度、禁止项、验证和最终回复要求，达到 `generated >= baseline`。

## 只能抽象吸收

- 源工程的迁移样稿、历史提示词和 golden baseline 只能抽象任务书质量门。
- 具体能力的模块清单必须来自目标源技能，不能在 meta skill 里写死。
- 目标工程结构读取由目标工程 agent 完成，本技能只传递自检要求。
- 矩阵中的 leader、score、source revision 和项目路径只能作为 source-depth 线索，不写成目标工程完成事实。

## 禁止复制

- 不复制任何项目事实、业务链路、运行 ID、服务实例、下游路径、排行分数或一次性 handoff。
- 不让某个下游工程成为平行源；下游强化版要先抽象归一。
- 不把任务书生成结果写成目标工程已完成改造。

## 目标工程结构自检

迁移本 meta skill 时，目标工程先检查：

1. 是否已有 agent 技能目录和 README 入口。
2. 是否已有跨项目反哺、模板反馈或外部能力采纳规则。
3. 是否已有技能模板、迁移清单或成熟度 sensor。
4. 是否已有提交、检查和最终回复规则。
5. 若缺少以上结构，先建立最小 `SKILL.md` 与 README 入口，不铺完整治理体系。

## 验证要求

- 用一个已有技能生成一次迁移任务书，检查是否可直接交给目标 agent。
- 用 [[templates/skill-transfer-manifest-template]] 或等价 manifest 先做一次源能力归一，确认任务书不低于 `taskbook-ready` 标准。
- 确认任务书没有复制项目事实或预设目标工程结构。
- 如果目标工程已有 skill-maturity sensor，确保本技能和 TRANSFER 通过检查。
- 最终回复写清生成样例、检查结果和未验证边界。
