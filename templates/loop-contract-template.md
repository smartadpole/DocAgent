---
type: template
id: TEMPLATE-LOOP-CONTRACT-001
status: active
updated: 2026-10-14
tags: [template, loop, harness, orchestration, evaluator]
conditional_sources: [templates/loop-contract-extensions.md]
---

# Loop Contract 模板

仅在需要跨 run 发现源、去重持久队列与调度恢复时建立。普通长任务、多 agent 或“直到闭环”不自动启用，未启用时不生成表单。

Loop Contract 只定义发现输入、分派执行、验证、持久化与下一轮决策；复用 [[templates/goal-contract-template]]、[[templates/run-capsule-template]] 和原事项 owner，不替代 Issue、TASK、报告、服务台账或 memory。

## 最小生效核心

- **Owner / Objective**：用户目标、期望最终状态、成功判定与不做项；链接原 owner。
- **Loop 模式与授权**：discovery-only / assisted-patch / structured-auto-fix / not-ready；允许写入范围和人工确认边界。
- **Discovery Source**：发现源、读取方式、输入标识与去重规则、优先级、噪音 / 误报处理。
- **Trigger / Schedule**：触发方式与调度 owner / 位置；实际频率或事件、并发上限、重试与退避上限。
- **Run Queue And State**：state store、状态 schema、当前 iteration、已消费输入、next-run marker；queued / running / passed / partial / blocked / failed / skipped 在持久队列记录，合同引用队列，不再复制数量看板。
- **Evaluator Oracle**：负责裁决的独立 oracle、所需证据与通过条件、失败 / 冲突处理；Worker 自述不能充当 evaluator。
- **Budget And Safety**：适用的累计时间 / token / 成本与轮次上限，停止 / blocked 条件，写入失败时恢复或 rollback 方式。
- **本轮读回与下一轮**：证据和失败项落点、队列实际状态、evaluator 结论、下一轮动作及触发条件；stop / rerun / retry-after / split / escalate / wait-human / schedule-next。

## 不可越过的边界

Loop 不新建平行研发看板，不自动合并、发布、生产写入、关闭 Gate / FP / EP / TASK / Issue 或修改高优先级规则。未经独立 evaluator 采纳的 Worker 回传不能上推为整体闭环；回传必须保留 limits、证据层级和未验证边界。权限、证据或预算不支持继续时持久化真实状态，不能写成 passed。

## 条件扩展

在 [[templates/loop-contract-extensions]] 中，自动调度命中“调度恢复”；多个角色或外部仓库命中“协作与现场检查”；修复 / 验收循环命中“Evaluator 细化”；发现研发事项命中“研发落位”；有可复用或复盘信号命中“沉淀”。只读命中的章节，不生成未触发的空字段或 no-op 证明。
