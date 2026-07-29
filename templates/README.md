# 模板层

这里放可复制的笔记模板。

Harness 相关模板默认按 [[response-mode-routing]] 先判响应模式；引导式设计和主动对话看 [[proactive-dialogue-system]]。如果模板使用中暴露重复偏差，再按 [[harness-evolution]] 判断是否写入 episode、升级 sensor 或调整模板字段。

## 用法

- 新文章先复制 [[templates/article-template]]
- 新概念先复制 [[templates/concept-template]]
- 新日志记录可以参考 [[templates/log-entry-template]]
- 新正式会议记录可以复制 [[templates/meeting-entry-template]]
- 新需求演进链可以参考 [[templates/trace-entry-template]]
- 新正式决策可以参考 [[templates/decision-entry-template]]
- 新研发项目可以复制 [[templates/project-template]]，也可以直接手写项目主页；极简小项目不必先用模板
- 新功能点实体可以复制 [[templates/development-feature-point-template]]
- 新研发事项矩阵可以参考 [[templates/development-work-item-matrix-template]]；自动候选拆解先看 [[skills/work-item-auto-decomposition/SKILL]]，矩阵里的 `树状编号`、`risk:`、`test:`、`验收:`、`issue-trigger:` 和不上推边界必须保留
- 新 EP 执行包可以复制 [[templates/development-execution-package-template]]
- 新 TASK 任务可以复制 [[templates/development-task-template]]
- 新 Issue 案件可以复制 [[templates/development-issue-template]]
- 新研发待办可以参考 [[templates/development-todo-template]]
- 新阶段门可以参考 [[templates/development-gate-template]]
- 新复杂验收计划可以参考 [[templates/development-acceptance-plan-template]]
- 新测试或准出报告可以参考 [[templates/development-test-report-template]]
- 新项目、阶段、交付链、Issue / 事故后或 Agent 工作复盘可以参考 [[templates/project-retrospective-template]]；复盘合同先看 [[skills/retrospective-capability/SKILL]]，正文进入 `projects/retrospectives/<year>/` 并同步索引，软件研发交付链看 [[skills/delivery-retrospective/SKILL]]，Agent 工作回看按对象启用
- 新研发风险登记可以参考 [[templates/development-risk-template]]
- 新开发过程记录可以参考 [[templates/development-worklog-entry-template]]
- 新编码任务执行单可以参考 [[templates/developer-task-brief-template]]
- 新代码工程回传包可以参考 [[templates/code-handoff-template]]
- 新工程反馈可以参考 [[templates/engineering-feedback-template]]
- 新主控、子工程、runtime service、知识库、数据 / 模型工程、运维 agent 或 hybrid 工程接入 wiki 作为模板母体时，先参考 [[templates/implementation-project-profile-template|实现类工程 Profile]]；它必须写清 Template Kernel、Project Profile Overlay、Capability Packs、required / optional / forbidden packs、project_bound_facts、owner surfaces、agent system layers、control plane、implementation boundaries、evidence contract、Template Adoption 和 Closeout Proof。
- 新 Agent System 从结构接线推进到行为智能评估时，使用 [[templates/agent-intelligence-evaluation-template]] 收集 positive / negative behavior corpus、八维 intelligence dimensions、evaluator provenance、Goodhart guard、external readback 和 `agent_intelligence_score` 阻塞边界。
- 新 wiki 治理体系全面整改、跨 agent / workflow / memory / harness / skill / evaluation / governance / template / topic / migration 的系统升级时，使用 [[templates/governance-system-upgrade-contract-template|Governance System Upgrade Contract]] 固定 source coverage、ability extraction、system layer landing、sensor / evaluator、persistence routing 和 closeout proof；完成定义以 [[wiki-governance-system-contract.v1]] 为准。
- 新服务实例台账条目可以参考 [[templates/service-registry-template]]
- 新源码工程审计报告可以参考 [[templates/source-code-audit-report-template]]
- 新项目内 agent 技能可以参考 [[templates/skill-template]]
- 新主题呈现使用 [[templates/topic-presentation-template]]；持久 current/snapshot 同步 [[views/lens-registry]]，填写 subject/source、关系图、三轴、五门 evaluator 和同源 PDF / PNG 合同
- 新主题呈现的 source pack、交付前审核和五门边界统一使用 [[templates/topic-presentation-template]]
- 新 HTML 公开发布 profile 可以参考 [[templates/public-html-publication-template]]；发布验证闭环可以参考 [[templates/public-html-publication-contract-template]]；真实发布仍以 [[views/publication]] 和 live readback 为准。
- 新技术、开源工程、行业 / AI、产品或 PoC 调研启动前，可以参考 [[templates/technology-research-contract-template]]；正式研究结果可以参考 [[templates/technology-research-report-template]]、[[templates/technology-research-evidence-matrix-template]] 和 [[templates/technology-research-adoption-contract-template]]
- 新外部技术材料、论文、repo、社区讨论或产品更新进入研究流程前，可以参考 [[templates/research-intake-template]]；它只承接 intake 和 source package，不替代正式研究报告。
- 新跨工程技能迁移源能力清单可以参考 [[templates/skill-transfer-manifest-template]]；新跨工程技能迁移任务书可以参考 [[templates/skill-transfer-contract-template]]、[[templates/skill-transfer-evidence-contract]] 和 [[templates/skill-transfer-review-contract]]
- 矩阵级或多能力吸收清单必须额外写 project conformance、source snapshot、逐能力分类和未验证边界；本仓当前样例是 [[skills/transferable-skill-governance/matrix-adoption-2026-06-26-agent-evidence-v12]]，检查为 `python3 scripts/check_all.py --only transferable-skill-baseline`
- 新 Cross-Project / Project Governance Audit 可以参考 [[templates/cross-project-governance-audit-contract-template]]；报告必须写 source-depth、handoff-ready、Transfer Manifest、verification-loop、git remote -v / git fetch --all --prune 读回和 no runtime validation 边界。
- 新规则页可以复制 [[templates/policy-template]]
- 新项目记忆页可以复制 [[templates/memory-template]]
- 新长时任务需要防跑偏、防证据漂移、防无限探索时，可以参考 [[templates/goal-contract-template]]
- 新引导式设计、主动对话或轻量 discovery 可以参考 [[templates/guided-discovery-session-template]]
- 新系统、主控仓库或子工程接入 Agent Harness 可以参考 [[templates/harness-adoption-template]]
- 新单次 Harness episode 可以参考 [[templates/harness-episode-package-template]]
- 新周期性 Harness 演进复盘可以参考 [[templates/harness-evolution-review-template]]
- 新持续 agent 循环控制面可以参考 [[templates/loop-contract-template]]；单轮多 agent / Worker 回传可以参考 [[templates/run-capsule-template]]，并按 [[agent-orchestration]] 做 Orchestrator / Worker / Evaluator 和 Subproject Git Preflight 分工。
- 如果你启用了 Obsidian 的 Templates 插件，这个目录可以直接作为模板目录
