# Codex Local Adapter

本文件是当前 wiki 的 Codex 本地入口适配层。完整维护约束仍以根目录 [[AGENTS]]、[[WORKFLOW]]、[[POLICY]]、[[response-mode-routing]]、[[proactive-dialogue-system]]、[[instruction-adherence]]、[[execution-contract-semantics]] 和 [[harness-evolution]] 为准。

## 每轮启动

- 先读根目录 `AGENTS.md`。
- 再按 [[response-mode-routing]] 判断响应模式：快速诊断、引导式设计、知识沉淀、Issue 分析 + 沉淀、验收关闭、规则升级、子工程实现 / 回传或批处理。
- 如果用户要求设计新系统、新工具、把粗糙想法想完整，或只给出“更智能 / 更前沿 / 更高效”目标，读 [[proactive-dialogue-system]]，并用 [[templates/guided-discovery-session-template]] 承接轻量 discovery。
- 如果涉及 Harness 自演进、用户纠偏、检查失败、模式切换或规则反哺，再读 [[harness-evolution]] 和 [[harness-feedback-ledger]]。
- 如果涉及规则已有但没有执行，读 [[instruction-adherence]]。
- 如果涉及 TASK、issue、AP、报告目标包、handoff、状态页或会议行动项的当前裁决，读 [[execution-contract-semantics]]。
- 如果用户要求持续推进、直到完成、反复尝试或跨多轮跟进，先按 [[concepts/codex-goals]] 判断是否需要 Goal Contract；模板见 [[templates/goal-contract-template]]。
- 如果用户要求复盘阶段、专题、交付链、Issue / 事故后经验或 Agent 工作流，读 [[concepts/project-retrospective]]、[[projects/retrospectives/README]]；历史对话和 Agent 工作复盘使用 [[skills/historical-dialogue-retrospective/SKILL]]。

## 工作阶段检查

- 工作阶段优先跑专项 sensor：`python3 scripts/check_all.py --only harness-governance`。
- 技能页、技能入口或技能模板改动跑：`python3 scripts/check_all.py --only skill-maturity`。
- 知识关联 skill 或落位规则改动跑：`python3 scripts/check_all.py --only knowledge-linking`。
- 问题聚焦式图文呈现、`views/`、lens 模板或导出守卫改动跑：`python3 scripts/check_all.py --only problem-focused-visual-presentation`。
- H5 ledger 或指令遵循改动跑：`python3 scripts/check_all.py --only harness-feedback-ledger,instruction-adherence`。
- 入口、wikilink 或治理元数据改动跑：`python3 scripts/check_all.py --only project-docs`。
- 测试计划 / AP / 报告计划来源改动跑：`python3 scripts/check_all.py --only testing-system-maturity`。
- 执行合同语义、非目标或环境路由改动跑：`python3 scripts/check_all.py --only execution-contract-semantics`。
- 复盘体系、复盘模板或复盘 skill 改动跑：`python3 scripts/check_all.py --only retrospective-system`。
- 收尾或提交前跑完整门禁：`python3 scripts/check_all.py`。
- `scripts/check_all.py` 是本库本地门传真相源；CI 或平台配置只是适配层。

## 写入边界

- 当前库是模板级 Harness，只吸收系统层规则、流程、模板、技能和自动化契约。
- 从下游工程反哺时，不复制项目事实、业务名、运行实例、具体状态或一次性测试证据。
- episode 先写入 [[harness-feedback-ledger]]，不要因为单次纠偏直接新增硬规则。
