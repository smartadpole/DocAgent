---
type: development_plan
id: DEV-TASK-DESIGN-001
project: PROJ-WIKI-001
status: active
source_of_truth: true
updated: 2026-05-25
tags: [development, planning, task, delivery-contract]
---

# TASK 设计模型

主入口：[[projects/development/plan/README]]

上游：[[projects/development/plan/work-item-system-model]]、[[projects/development/execution/execution-packages/README]]  \
下游：[[projects/development/execution/tasks/README]]、[[projects/development/acceptance/README]]、[[projects/development/reports/README]]、[[projects/development/execution/developer-execution-workflow]]

## 这页解决什么

这页沉淀 TASK 的设计决策：TASK 为什么存在、页面为什么这样组织，以及后续创建或修改 TASK 时必须遵守什么结构。

最终决策：

> TASK 是父级 EP 下的状态化交付合同。它负责把一个功能切片从 `planned` 推到 `done`，并让子工程、主控、联调方和验收方都清楚：谁负责、为什么做、做到什么算 done、怎样接上下游、用什么证据关闭、关闭后能证明什么，以及不能上推关闭什么。

TASK 不是需求页、设计页、issue、risk、测试报告或治理清单。页面里的来源、归属、边界、验证、关系校准和证据记录，都必须服务于同一个目标：确保这个 TASK 的 `done` 是正确、可验收、可追溯、不会误上推的 `done`。

## 设计决策

### 1. TASK 是状态化交付合同

TASK 的默认生命周期是：

```text
planned -> in_progress / implemented -> review -> done
```

例外状态可以是 `blocked`、`archived` 或项目已有兼容状态。任何状态下，正文都要回答“离 done 还差什么”，不能只有 frontmatter 状态。

### 2. Done Contract 是主轴

TASK 页面最核心的是 `Done Contract`，它回答：

- 必交付物是什么。
- 范围内和范围外分别是什么。
- 子工程回传必须包含什么。
- 关闭证据是什么。
- 关闭本 TASK 后能证明什么。
- 不能上推关闭父 EP、FP、Gate 或兄弟 TASK 的什么内容。

测试、验收、关系校准和证据记录都是 Done Contract 的支撑，不能喧宾夺主。

### 3. 归属与责任是一等信息

TASK 要先说明谁负责把它做到 done。`归属与责任` 至少写清：

- 主责模块 / 执行方。
- 协同模块。
- 上游输入方。
- 下游消费方。
- owner、环境、权限或资源待确认项。

### 4. 正确性约束不能丢

TASK 不只是“把功能做出来”，还要把功能正确落地。页面必须显性写出：

- 核心业务 / 技术不变量。
- 参数、配置、权限和运行轨道边界。
- 失败语义。
- fallback、skipped、blocked、retry、dead letter 或人工分流规则。
- 不能静默成功、不能误判成功、不能用默认 happy path 伪造通过的场景。

### 5. 上下游和联调路径要服务交付

TASK 是父 EP 下的一段链路，不是孤立开发项。页面必须写清：

- 上游输入是什么。
- 本任务处理什么。
- 下游输出给谁。
- 前置、后续、兄弟 TASK 是哪些。
- 联调流程如何证明链路接上。

如果上下游不能写清，只能标为 `planned / blocked / 待确认`，不得说开发就绪。

### 6. 验证要求是 done 的证据设计

TASK 的验证要求至少覆盖：

- 开发者自测证据。
- `local validation`。
- `service-side validation`。
- `end-to-end validation`。
- 相关功能回归。
- 计划来源或 `AP-*` / 不适用原因。
- 非默认值 / 边界值。
- readback、artifact、UI、日志或回传包证据。
- 未验证风险。

如果 TASK 关联已发生 ISSUE / Bug，验证要求还必须显式包含 bug 反向用例：原 bug 复现用例、同场景代表性用例、修复前失败 / 修复后通过或等价证据、漏测原因和新增回归守卫。

TASK 级测试通过只能作为父 EP 输入证据，不能自动关闭父 EP、FP 或 Gate。

### 7. 体系关系后置但不能省略

体系关系负责防止小功能误升为 EP，或把已发生问题误写成 TASK。至少写：

- 父级 EP。
- 对应 FP / 候选项。
- 关联 risk / issue。
- `issue-trigger`：没有已发生 issue 时，写清什么失败条件会创建或复用 issue。
- 主关系类型。
- 为什么是 TASK，不是 EP / FP / risk / issue。
- 对父级状态的影响。

### 8. 证据记录区分历史和当前裁决

`证据记录` 承接最新验收、子工程 handoff、历史修正和后续回归守卫。历史报告不能删除或改写成不存在；最新有效报告才是当前裁决。证据不完整时，TASK 只能保持 `review`、`blocked` 或未关闭。

## 标准结构

后续新增或重写活跃 TASK 时，默认采用这个顺序：

```md
# TASK-xxx 标题

> 一句话定位：这是父 EP 下哪个功能切片，最终要完成什么。

## 出发点和目标

- 来源：
- 服务的需求 / Gate / FP / 父 EP：
- 为什么需要这个 TASK：
- 本 TASK 要完成的功能切片：

## 当前状态

- 状态：
- 当前结论：
- done 还差什么：
- 下一步：
- 阻塞 / 待确认：

## 归属与责任

- 主责模块：
- 执行方：
- 协同模块：
- 上游输入方：
- 下游消费方：
- owner / 环境 / 权限待确认：

## Done Contract

- 必交付物：
- 范围内：
- 范围外：
- 子工程回传要求：
- 关闭证据：
- 关闭本 TASK 后能证明什么：
- 不能上推关闭什么：

## 功能边界和正确性约束

- 核心不变量：
- 参数 / 配置 / 权限边界：
- 失败语义：
- fallback / skipped / blocked / retry 规则：
- 不能静默成功或误判成功的场景：

## 上下游和联调路径

- 上游输入：
- 本任务处理：
- 下游输出：
- 联调流程：
- 前置 / 后续 / 兄弟 TASK：

## 验证要求

- 开发者自测证据：
- 测试计划来源 / AP：
- local validation：
- service-side validation：
- end-to-end validation：
- 相关功能回归：
- 已发生 Bug / ISSUE 反向用例：
- 非默认值 / 边界值：
- readback / artifact / UI / 日志证据：
- 未验证风险：

## 体系关系

- 父级 EP：
- 结构链路：
- 对应 FP / 候选项：
- 关联 risk / issue：
- issue-trigger：
- 主关系类型：
- 为什么是 TASK，不是 EP / FP / risk / issue：
- 对父级状态的影响：

## 相关页面 / 文件入口

- 父级 EP：
- 相关 FP / Gate / risk / issue：
- 设计 / 接口 / 数据合同：
- 验证入口：
- 子工程回传入口：

## 证据记录

- 最新验收：
- 子工程 handoff：
- 历史修正：
- 后续回归守卫：
```

## 状态填充规则

- `planned`：必须写清出发点、归属与责任、Done Contract、功能边界、验证要求和待确认项；缺这些内容时不得写“开发就绪”。
- `in_progress / implemented`：必须更新已落地交付物、联调路径变化、失败语义变化、子工程回传路径和新增未验证风险。
- `review`：必须写当前已有证据、失败项、复验缺口、done 还差什么，以及最新有效报告是否覆盖旧报告。
- `done`：必须固化关闭证据、回归守卫、父级上推边界和后续吸收入口；不能只写“已完成”。
- `archived`：必须写清替代 TASK、为何不再作为活跃执行入口，以及历史证据是否仍可引用。

## 模板残留规则

TASK 页面允许先用模板搭骨架，但不能把模板占位句当成最终内容。后续新增、批量生成或重写 TASK 时，必须把模板字段改成任务特定内容。确实无法确认时，也要写成具体待确认项和归口入口，而不是泛化句。
