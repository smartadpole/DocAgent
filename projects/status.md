---
type: status
id: STATUS-001
project: PROJ-WIKI-001
status: active
stage: design
source_of_truth: true
updated: 2026-07-23
next_action: apply-implementation-project-profile-to-next-target-repo
current_entry: projects/README.md
blockers:
  - remaining-page-normalization
  - wider-sensor-coverage
  - behavior-intelligence-evidence
tags: [status]
---

# 项目状态

这页是 [[projects/README]] 的状态镜像，适合给人和 agent 快速读取当前阶段、下一步、阻塞项和活跃功能点。

## 当前状态

- 状态：active
- 阶段：design
- 当前主入口：[[projects/README]]
- 当前定位：Template Kernel + Project Profile Overlay + Capability Pack 的模板母体工程；入口见 [[projects/design/topics/implementation-engineering-template-system]] 和 [[templates/implementation-project-profile-template]]

## 下一步

- 基于 [[projects/development/plan/work-item-system-model]] 观察后续研发任务是否能稳定按 `Gate -> FP -> EP -> TASK` 拆解，并把 Issue、risk、test、验收和服务台账关系补齐
- 继续把 Markdown / wikilink、frontmatter 和更大范围模板完整性检查扩展成 `scripts/check_all.py` 下的 feedback sensor；技能成熟度已补 `skill-maturity` sensor，研发事项矩阵已升级为结构化字段 / 表头 / 章节检查
- 通用 agent 技能体系已有矩阵级吸收清单 [[skills/transferable-skill-governance/matrix-adoption-2026-06-26-agent-evidence-v12]]、实现类工程 profile overlay / capability pack 模板 [[templates/implementation-project-profile-template]] 和 `implementation-template-system` sensor；下一步是在新目标工程接入时用 profile 真实填一次，并继续等待 runtime / intelligence 行为证据，不为矩阵分数补空壳
- 定期做规则减肥：合并重复入口、删除过期补丁，把可执行约束迁到模板或检查脚本

## 功能点镜像

功能点正文以 [[projects/development/feature-points/README]] 和实体页为准，这里只放当前状态镜像。

## 功能点状态维护

- 这页只保留全局状态镜像，不展开所有功能点细节
- 整体推进看 [[projects/development/README]]
- 研发总控和当前执行入口看 [[projects/development/plan/README]]
- 正式事项主链看 [[projects/development/plan/work-item-system-model]]
- EP 执行包看 [[projects/development/execution/execution-packages/README]]
- TASK 交付合同看 [[projects/development/execution/tasks/README]]
- Issue 案件看 [[projects/development/issues/README]]
- 当前待办和关闭证据看 [[projects/development/execution/todo]]
- 测试方案和准出证据看 [[projects/development/reports/README]]
- 功能点模板看 [[templates/development-feature-point-template]]，活跃实体清单看 [[projects/development/feature-points/README]]
- 过程流水看 [[projects/development/execution/worklog]]
- 正式会议看 [[projects/meetings/worklog]]
- 功能点用 `status` + `phase` 双轴管理
- `status` 看生命周期：`planned`、`active`、`blocked`、`done`、`released`、`archived`
- `phase` 看串联步骤：`design`、`implementation`、`verification`、`release`
- 旧的 `in_progress` 口径以后统一拆成 `status=active + phase=*`
- 功能点实体页一页一个功能点，`status` 和 `phase` 写在各自页的 frontmatter
- 被取消或被替代的功能点，分别标成 `canceled` 或 `superseded`
- 切状态时，先更新功能点实体页，再回看发布、事故和记忆是否需要同步

### 进行中

- [[projects/development/feature-points/FP-001]]：active / implementation

### 完成待发布

- [[projects/development/feature-points/FP-002]]：done / release

### 已发布

- [[projects/development/feature-points/FP-003]]：released / release

## 维护说明

- 状态变化前先读 [[projects/README]]。
- 功能点状态变化时，同步对应功能点页、[[projects/development/README]] 和这里。
- 如果状态变化反映了需求范围、设计口径或决策变化，再同步 [[projects/trace]] 和 [[projects/decisions]]。

## 阻塞项

- 还没有把更大范围的页面批量规范化
- Harness H5、`harness-governance`、`skill-maturity`、`transferable-skill-baseline`、`implementation-template-system` 和结构化 `work-item-matrix` sensor 已完成吸收，但更大范围的文档结构 sensor 仍未覆盖；agent intelligence 行为证据仍需外部 evaluator 或正负样本 readback。
