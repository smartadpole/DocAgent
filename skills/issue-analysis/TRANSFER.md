---
type: skill-transfer-manifest
skill: issue-analysis
status: active
updated: 2026-06-12
tags: [skill, transfer, issue-analysis]
---

# Issue Analysis Transfer Manifest

## 能力目标

把模糊问题、联调失败、验收争议、跨工程阻塞或证据冲突，收敛成可裁决、可分工、可联测、可回写的问题分析结果。

## 源资料路径

- `skills/issue-analysis/SKILL.md`
- `skills/README.md`
- `templates/development-issue-template.md`
- `templates/development-test-report-template.md`
- `templates/code-handoff-template.md`
- `templates/developer-task-brief-template.md`
- `governance/response-mode-routing.md`
- `governance/execution-contract-semantics.md`
- `governance/template-feedback-rules.md`
- `scripts/check_skill_maturity.py`

## 可以吸收

- 响应模式判断：先区分快速诊断、完整 Issue 分析、验收关闭和规则升级。
- 问题框：现象、业务影响、期望行为、触发入口、范围、当前证据和主控问题。
- 事实源分层：直接证据、上下文证据、反证 / 排除项、未知项。
- 权威层判断：需求 / 设计、编排、服务合同、服务内部、业务单位、持久化、展示和 agent 过程。
- 最小根因链：先找最早知道真实状态的层，再找传播、展示、副作用或文档口径缺口。
- 责任边界：代码、文档、服务、数据和流程边界分开写。
- 跨工程分工：主责、协同、输入依赖、交付物、验收方式、阻塞和主控吸收方式。
- 联测方案：local validation、service-side validation、end-to-end validation、非默认值 / 边界值、相关回归和证据落点。

## 只能抽象吸收

- 本库的 `Gate -> FP -> EP -> TASK` 事项体系。
- 本库的 `projects/`、`templates/`、`skills/`、`governance/` 命名方式。
- 本库的 `[[wikilink]]`、log 记录、sensor 接线和提交规则。

## 禁止复制

- 不复制本库项目状态、功能点、任务编号、报告结论、服务实例、运行 ID 或一次性问题事实。
- 不复制某个子工程的业务链路、仓库路径、handoff 路径、提交规则或本地环境规则。
- 不把 Issue 分析输出当成目标工程的正式状态关闭、验收通过或发布准出。

## 目标工程结构自检

- 如果目标工程已有 issue / incident / bug / postmortem / handoff / test report 体系，先映射到已有入口，不新建平行问题体系。
- 如果目标工程有主控文档库和子工程，主控侧负责裁决目标、证据和关闭；子工程侧负责实现、验证和回传证据。
- 如果目标工程没有正式事项系统，先把本技能落成 agent 工作流和输出格式；不要强行照搬 `Gate -> FP -> EP -> TASK`。
- 如果目标工程没有 sensor 框架，先写明检查要求；只有已有 `check_all` 或等价脚本时再接入自动检查。

## 验证要求

- 用一个模糊问题样本验证是否能输出问题框、事实源地图和 `confirmed / likely / possible / blocked`。
- 用一个跨工程阻塞样本验证是否能拆出主责、协同、交付物、验收方式和主控吸收位置。
- 用一个验收争议样本验证是否能区分分析结论、测试报告、人工确认和状态关闭。
- 跑目标工程已有检查；如果接入 sensor，补专项检查并纳入统一门禁。
- 最终回复必须说明吸收落位、验证命令、未验证边界和不复制的项目事实。
