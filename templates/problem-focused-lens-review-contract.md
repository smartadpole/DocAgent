---
type: template
id: TEMPLATE-PROBLEM-FOCUSED-LENS-REVIEW-CONTRACT-001
status: active
updated: 2026-06-12
tags: [template, lens, problem-focused-lens, review-contract, problem-focused-visual-presentation]
---

# Problem-Focused Lens Review Contract

本模板用于审核 problem-focused lens 是否已经达到“可读、可追溯、可刷新、不可误用”的标准。它适合在生成 HTML、current lens、snapshot、PNG 预览或汇报图前使用。

## A. 关注问题审核

| 检查项 | 通过标准 | 失败时处理 |
| --- | --- | --- |
| primary question | 首屏能直接看出本 lens 回答什么 | 回到关注合同，不先改视觉 |
| reader | 知道读者是用户、工程师、决策者还是复盘者 | 调整术语密度和细节 |
| decision | 知道读者看完要判断什么 | 不给行动卡，只给背景图 |
| not_for | 写清不能用于验收、准出、状态推进或规则裁决的边界 | 添加不上推说明 |
| current/snapshot | 写清是当前视图还是历史快照 | 补 generated_at 和 refresh_trigger |

## B. Source Pack 审核

| 检查项 | 通过标准 | 失败时处理 |
| --- | --- | --- |
| source_pages | 每个关键判断都有来源 | 补来源或降级 |
| source_scope | 读了什么、没读什么写清 | 添加未覆盖边界 |
| source_revision | commit、生成时间或文件版本可追溯 | 补 revision |
| authority | 真相源、证据源、背景源、导出源分开 | 重写 source pack |
| unread critical source | 关键未读源不能支撑 confirmed | 降级 likely / blocked |
| derived source | 导出件不能成为事实源 | 改成 preview |

## C. 证据边界审核

| 等级 | 必须满足 | 常见错误 |
| --- | --- | --- |
| confirmed | 事实链闭合，来源权威，时间边界清楚 | 把接口返回当 DB readback |
| likely | 证据强但缺一段验证 | 写成已确认 |
| possible | 只是候选解释或设计假设 | 放进状态卡 |
| blocked | 缺权限、数据、人工确认或关键页面 | 用美观图遮蔽缺口 |

## D. 视觉审核

| 模块 | 适合场景 | 不适合场景 | 降级方案 |
| --- | --- | --- | --- |
| 状态卡 | 一眼看当前结论 | source pack 不完整 | 写背景框 |
| 热力矩阵 | 多对象缺口比较 | 分数口径不清 | 用缺口表 |
| 时间线 | 演进有明确时间 | 时间证据不完整 | 用阶段列表 |
| 关系图 | 节点和关系明确 | 关系类型模糊 | 用分组清单 |
| 泳道图 | owner / 层级清楚 | owner 未确认 | 用责任边界表 |
| 证据链 | 需要解释为什么 | 缺关键证据 | 用待验证清单 |
| 行动地图 | 下一步明确 | 验收层级不清 | 用问题清单 |

## E. 文案审核

- 标题必须是主题或问题，不写泛泛“可视化报告”。
- 首段先给一眼判断，不先堆元数据。
- 每个颜色或分数都要有口径。
- 每个行动都要有 owner、验证或未确认边界。
- 每个 blocked 都要写解锁条件。
- 每个 snapshot 都要写生成时间。
- 每个 current 都要写刷新触发。
- 每个导出状态都要写是否验证。

## F. 导出审核

| 导出 | 允许用途 | 必须声明 | 禁止 |
| --- | --- | --- | --- |
| HTML | canonical view | source pack / generated_at | 替代真相源 |
| print HTML | 打印 / PDF 源 | print_profile | 改事实 |
| PNG | 聊天预览 | verified / not verified | 当主文档维护 |
| PDF | 分发 | generated from | 后续编辑 |
| SVG | 图形源或导出 | source tool | 和 HTML 分叉 |

## G. Registry 审核

新增或更新持久 lens 后检查：

- registry 是否有 `lens_id`。
- registry path 是否指向 canonical。
- registry 是否写 current / snapshot。
- registry 是否写 source pages。
- registry 是否写 refresh trigger。
- registry 是否写 export status。
- registry 是否写 not source of truth for。
- registry 是否能让后续 agent 找到该 lens。

## H. 十类常见误用

1. 把成熟度矩阵颜色当作能力本身，忽略诊断里的 missing signals。
2. 把 HTML 当作项目状态源，忘记回写项目主页或 owning page。
3. 把截图当作已验证导出，未检查真实文件。
4. 把 snapshot 放在 current 路径，导致读者误判。
5. 把未读来源放进 confirmed。
6. 把 issue 分析图当成 issue 案件档案。
7. 把 research 图当成调研结论，缺证据等级。
8. 把服务拓扑图当成 service registry。
9. 把模板示例当成真实字段。
10. 把 lens 里的行动项当成正式 TASK。

## I. 交付前确认

```markdown
- [ ] 关注问题明确
- [ ] source pack 完整
- [ ] evidence boundary 分级
- [ ] current / snapshot 清楚
- [ ] registry 已同步
- [ ] 导出状态诚实
- [ ] 真相源未被替代
- [ ] 专项 sensor 已通过
- [ ] log 已记录本轮真实意图
```

## J. 二阶反思

如果 lens 审核失败，不只修当前图，还要判断失败类型：

- source pack 总漏：补模板字段或 sensor。
- registry 总漏：补 views 规则。
- 导出总误报：补导出验证步骤。
- 状态总上推：补 governance 不上推规则。
- 矩阵总遮蔽原因：补诊断详情入口。

## K. 详细复核清单

### K1. 矩阵类 lens

矩阵类 lens 最容易把颜色误当结论。复核时逐项确认：

- 行和列是否都是稳定对象，而不是混合了项目、能力、状态、证据和建议。
- 每个格子的颜色是否有一致口径。
- 分数是否来自同一来源、同一时间、同一算法。
- 如果矩阵来自外部诊断，是否链接详情页或 Markdown 诊断。
- 是否把“缺少信号”写成缺少哪些文件、路径、模板、sensor 或治理接线。
- 是否避免把领先工程的项目事实复制到目标工程。
- 是否把项目绑定能力和通用可迁移能力分开。
- 是否在矩阵下方给出优先修复列表。
- 是否有“本轮不吸收”的清单。
- 是否标记生成时间和 source revision。

### K2. 状态类 lens

状态类 lens 容易替代项目主页。复核时确认：

- 状态来源是否回到项目主页、事项页、报告或服务台账。
- lens 是否只是展示，不承接下一次状态维护。
- `done`、`pending acceptance`、`blocked`、`risk` 是否和主入口一致。
- 是否写清哪些状态来自人工确认，哪些来自脚本。
- 是否避免把子工程通过写成主控闭环。
- 是否避免把一次报告结论写成长期状态。
- 是否写清下一步由谁吸收。

### K3. Issue / 事故类 lens

Issue lens 必须保护原始现象：

- 是否保留用户看到的问题。
- 是否区分现象、影响、期望、证据、候选根因和 confirmed 根因。
- 是否避免用推测根因改写标题。
- 是否把日志、API、DB、UI、报告和 agent 过程分层。
- 是否写清最小根因链的证据强度。
- 是否把修复、复验、关闭裁决分开。
- 是否回链正式 Issue 案件页或说明没有建案。

### K4. Research 类 lens

Research lens 必须保护证据等级：

- 是否区分 L1 一手事实、L2 权威分析、L3 产业信号、L4 线索、L5 推论、L6 建议。
- 是否写清哪些事实需要当前联网查证。
- 是否避免用单篇媒体稿支撑采用建议。
- 是否避免把 PoC 成功写成生产可用。
- 是否写出 Adopt / Trial / Assess / Hold / Blocked 的行动等级。
- 是否有刷新触发，例如 release、价格、政策、CVE、benchmark。
- 是否回链 research report 或 concept / article。

### K5. 迁移类 lens

迁移 lens 必须保护源项目和目标项目边界：

- 是否先源能力归一，再目标迁移。
- 是否只吸收触发条件、事实源分层、输出格式、回写守卫和验证方式。
- 是否明确禁止复制业务链路、服务名、运行 ID、数据表和本地 handoff。
- 是否检查目标工程已有同名能力。
- 是否写清目标工程结构自检，而不是直接指定目录。
- 是否要求目标工程最终提交和验证。

### K6. 导出复核

导出前后都要复核：

- HTML 是否能独立打开或通过本地服务打开。
- CSS 是否适合打印。
- 宽屏和移动视口是否不重叠。
- PNG 是否来自当前 HTML，而不是旧缓存。
- PDF 是否分页可读。
- registry 是否记录导出状态。
- `.gitignore` 是否忽略导出缓存。

### K7. 最终回复复核

最终回复必须让用户知道：

- lens 文件在哪里。
- 本轮读了哪些 source。
- 哪些导出已验证。
- 哪些边界未覆盖。
- 哪些项目状态没有被 lens 改写。
- 哪些后续动作已经写回主入口。

## L. 示例判读表

| lens 类型 | 可写成 confirmed 的条件 | 只能写 likely 的条件 | 必须 blocked 的条件 |
| --- | --- | --- | --- |
| 技能成熟度矩阵 | 已读矩阵数据、诊断页和目标工程命中文件 | 只读截图，未读 JSON 或诊断 | 目标工程不可读 |
| 研发状态图 | 项目主页、事项页、报告一致 | 报告通过但状态页未更新 | 缺验收或人工确认 |
| Issue 证据链 | 原始现象、日志、代码、复验闭合 | 有日志和候选根因，缺复验 | 缺复现或关键证据 |
| 研究结论图 | 有 L1 来源、风险门和行动等级 | 有资料但缺 PoC 或当前查证 | 关键来源不可访问 |
| 服务拓扑图 | service registry 和运行检查一致 | 只有旧记录或局部健康检查 | 端口 / profile 未确认 |
| 知识关系图 | 入口、上位、邻接、回链都存在 | 只有入口，缺反向回链 | 新页孤立 |
| 迁移任务图 | 源 TRANSFER 和目标入口都读过 | 源已读，目标结构未核 | 用户未授权目标工程 |
| 验收缺口图 | AP、report、issue、TASK 都对应 | 局部验证通过 | 缺关键验证层级 |
| 会议材料图 | 独立会议页或 worklog 明确 | 只有议题，缺行动项 | 会议目标未定 |
| 复盘图 | 事实、偏差、原因、行动、沉淀齐全 | 只有过程总结 | 缺可复用学习资产 |

## M. Lens 变更分类

| 变更 | 是否需要更新 registry | 是否需要更新 log | 是否需要提交 |
| --- | --- | --- | --- |
| 新建 current HTML | yes | yes | yes |
| 新建 snapshot HTML | yes | yes | yes |
| 只生成 PNG 预览缓存 | no，除非 registry 记录导出状态 | 通常 no | no |
| 修改 source pack | yes | yes | yes |
| 修改视觉样式不改事实 | maybe | yes if persistent | yes |
| 修正证据边界 | yes | yes | yes |
| 删除过期 lens | yes | yes | yes |
| 临时聊天内 Mermaid | no | no，除非形成长期知识 | no |

## N. 手工浏览器检查

持久 HTML 交付前，建议做：

- desktop viewport：确认首屏可读、没有横向遮挡、矩阵标题不重叠。
- mobile viewport：确认卡片和表格可滚动，长词不会撑破容器。
- print preview：确认分页、背景、颜色和链接说明可接受。
- screenshot：确认 PNG 不是旧缓存。
- link check：确认 source links 能回到本库页面。
- dark / light：若页面有主题，确认对比度。

未做浏览器检查时，最终回复要写“HTML 已生成，视觉导出未验证”。

## O. 上推边界速查

| lens 中看到的内容 | 不能上推成 | 必须回到 |
| --- | --- | --- |
| 矩阵满分 | 能力已长期领先 | skill、TRANSFER、sensor、template、governance、views 本地证据 |
| 单项绿色 | 整体项目完成 | 项目主页、报告、验收页 |
| HTML 可打开 | 导出已验证 | 浏览器截图、print preview、导出文件检查 |
| PNG 存在 | canonical 已更新 | HTML source 和 registry |
| 报告通过 | Issue 关闭 | Issue 案件页和关闭裁决 |
| 子工程 handoff | 主控吸收完成 | 主控 report / TASK / risk / status |
| 服务 health OK | 端到端成功 | service-side 和 e2e validation |
| 研究图有结论 | 采用已拍板 | decision / design / owner 确认 |
| 关系图有链接 | 知识已完整沉淀 | 入口、上位、邻接、反向回链 |

## P. 更新后回看

更新 lens 后按顺序回看：

1. 主题是否仍然是同一个关注问题。
2. 新增来源是否改变证据等级。
3. 删除来源是否让 confirmed 降级。
4. 导出缓存是否需要刷新。
5. registry 的 source_revision 是否需要更新。
6. log 是否需要新增同一主题记录。
7. 是否因为 lens 发现了规则或模板缺口。
8. 是否应该停止在呈现层，而不是继续扩需求。

## Q. 细粒度审查项

以下清单用于复杂 lens 的最终人工回看。不是每个 lens 都要展示这些条目，但生成者必须知道这些风险存在。

- 如果 lens 使用颜色，必须确认颜色不承接唯一语义；色盲或黑白打印时仍能看懂。
- 如果 lens 使用排序，必须写清排序字段和排序方向。
- 如果 lens 使用分组，必须说明分组依据来自源页面还是本轮推断。
- 如果 lens 使用分数，必须说明分数是否可加总、可比较、可跨时间复用。
- 如果 lens 使用状态词，必须对齐项目主入口或事项模型里的状态词。
- 如果 lens 使用 owner，必须说明 owner 是人工确认、页面字段还是推断角色。
- 如果 lens 使用时间，必须说明时间是事件发生、记录生成、文件更新还是截图时间。
- 如果 lens 使用截图，必须说明截图是否是当前状态、历史证据还是展示示例。
- 如果 lens 使用外部数据，必须说明数据更新时间和刷新触发。
- 如果 lens 使用运行日志，必须说明日志覆盖的服务、环境、profile 和时间窗口。
- 如果 lens 使用 API 返回，必须说明它证明的是请求层、服务层还是持久化层。
- 如果 lens 使用 DB readback，必须说明查询条件、样本范围和时间窗口。
- 如果 lens 使用测试报告，必须说明报告能关闭哪一层，不能关闭哪一层。
- 如果 lens 使用 issue，必须保留原始现象和后续根因分层。
- 如果 lens 使用复盘，必须区分事实复盘、原因复盘和改进行动。
- 如果 lens 使用研究材料，必须写出证据等级和当前性。
- 如果 lens 使用模板字段，必须说明模板字段不是事实。
- 如果 lens 使用技能成熟度矩阵，必须同时引用矩阵和诊断，不只看颜色。
- 如果 lens 使用跨工程材料，必须说明哪些是系统层信息，哪些是项目材料。
- 如果 lens 使用子工程 handoff，必须说明主控是否已经吸收。
- 如果 lens 使用服务台账，必须说明台账是否是当前确认事实。
- 如果 lens 使用浏览器截图，必须说明是否来自目标 URL 和目标 viewport。
- 如果 lens 使用导出件，必须说明导出件是否由 canonical 生成。
- 如果 lens 使用 Mermaid，必须确认它是小流程而不是大型架构图替代物。
- 如果 lens 使用 Excalidraw 或 Diagrams.Net，必须链接源文件和预览。
- 如果 lens 有行动项，必须说明行动项是否已经写入正式任务系统。
- 如果 lens 有风险，必须说明风险是否已进入 risk 页面。
- 如果 lens 有决策，必须说明决策是否已进入 decisions 页面。
- 如果 lens 有需求变化，必须说明 trace 是否同步。
- 如果 lens 有规则变化，必须说明 governance 是否同步。
- 如果 lens 有模板变化，必须说明 templates/README 是否同步。
- 如果 lens 有技能变化，必须说明 skills/README 和 skill-maturity 是否同步。
- 如果 lens 有项目状态变化，必须说明 projects/README 是否同步。
- 如果 lens 有知识沉淀，必须说明 knowledge-linking 是否完成。
- 如果 lens 有文件新增，必须说明路径归类是否符合 AGENTS。
- 如果 lens 有检查命令，必须说明命令结果和未覆盖边界。
- 如果 lens 有 commit，必须说明 commit 只包含同一主题。
- 如果 lens 没有 commit，必须说明是否只是缓存或临时预览。
- 如果 lens 有未读来源，必须说明哪些判断因此降级。
- 如果 lens 有 blocked 项，必须说明解锁条件。
- 如果 lens 有 follow-up，必须说明它是不是正式任务。
- 如果 lens 用于用户聊天预览，必须避免把内部维护字段放在首屏。
- 如果 lens 用于分发，必须加打印 / 导出说明。
- 如果 lens 用于治理审计，必须把评分、证据和建议分开。
- 如果 lens 用于验收，必须把 local、service-side、end-to-end 和人工确认分开。
- 如果 lens 用于调研，必须把事实、推论、建议和刷新触发分开。
- 如果 lens 用于迁移，必须把源能力、目标结构、吸收边界和验证分开。
- 如果 lens 用于复盘，必须把保留做法和改进行动分开。
- 如果 lens 用于状态同步，必须把当前状态和历史快照分开。
- 如果 lens 用于会议，必须把会前材料、结论和行动项分开。
- 如果 lens 用于服务运行，必须把服务组、组件、profile、日志和健康检查分开。
- 如果 lens 用于 agent 规则，必须把规则裁定、执行约束和检查证明分开。

## R. 完成判定

一个 problem-focused lens 可以交付，不代表它关闭了源问题。交付口径固定为：

- `ready for reading`：source pack、registry、首屏判断和证据边界完整。
- `ready for sharing`：在 ready for reading 基础上，导出和视觉检查完成。
- `ready for decision support`：在 ready for sharing 基础上，所有行动等级、风险和不上推边界明确。
- `not ready`：缺 source pack、缺 registry、缺关键来源、导出未验证却要分发，或把 lens 当真相源。

最终回复使用这些词，比“已完成图文”更清楚。

## S. 失败判定表

出现以下任一情况，lens 必须判为 `not ready`：

- 没有 source pack。
- 没有 evidence boundary。
- 没有 current / snapshot 标记。
- 持久 HTML 没有 registry。
- 导出件未生成却声称已导出。
- PNG / PDF 来自旧缓存。
- 把 lens 写成项目状态源。
- 把 lens 写成验收关闭证据。
- 把未读来源写成 confirmed。
- 把候选根因写成根因。
- 把调研线索写成采用建议。
- 把子工程结果写成主控吸收完成。
- 把模板字段写成真实事实。
- 把静态截图写成当前服务状态。
- 把视觉美化放在证据前面。
- 把行动项留在 lens 里，不回到任务或风险入口。
- 把规则候选写成已生效规则。
- 把 source revision 漏掉。
- 把 refresh trigger 漏掉。
- 把未覆盖边界漏掉。

补充失败项：

- 没有说明读者是谁。
- 没有说明当前动作是什么。
- 没有说明 blocked 如何解锁。
- 没有说明颜色含义。
- 没有说明排序口径。
- 没有说明数据窗口。
- 没有说明截图来源。
- 没有说明人工确认边界。
- 没有说明检查命令。
- 没有说明检查未覆盖项。
- 没有说明文件是否提交。
- 没有说明导出是否忽略。
- 没有说明是否影响 trace。
- 没有说明是否影响 risk。
- 没有说明是否影响 decision。
- 没有说明是否影响 service registry。
- 没有说明是否影响 knowledge-linking。
- 没有说明是否影响 documentation-maintenance。
- 没有说明是否需要二阶反思。
- 没有说明是否停止扩展范围。

最终补充失败项：

- 没有把读者下一步写清。
- 没有把判断目的写清。
- 没有把 source pack 和视觉模块对应起来。
- 没有把详情页和总览页对应起来。
- 没有把缓存文件和 canonical 文件分开。
- 没有把人工判断和脚本判断分开。
- 没有把长期入口和一次性预览分开。
- 没有把历史快照和当前事实分开。
- 没有把局部证据和全局结论分开。
- 没有把“建议”与“已执行”分开。

确认交付前再问自己：这个 lens 如果半年后被另一个 agent 打开，它能不能知道当时的来源、判断目的、导出状态、刷新条件和不能上推的范围。不能回答这些问题，就还不是合格的持久 lens。

持久 lens 的价值是降低后续理解成本，而不是制造新的维护面。任何让后续 agent 更难判断真相源、更难发现过期、更难区分证据和推论的视觉处理，都应该退回模板和 source pack 重新整理。

如果用户只是需要快速理解，优先给短答或聊天内结构图；如果用户需要长期复看，才进入 current / snapshot；如果用户需要分发，才进入导出验证。三者不能混成同一个默认动作。

当 lens 发现源页面本身有缺口时，先把缺口记录到 owning page、risk、issue、template 或 governance；lens 只能显示缺口，不能把“显示了缺口”误写成“缺口已经修复”。

如果 lens 的读者必须靠追问才知道数据从哪里来、下一步做什么、哪些结论不能用来关闭事项，这个 lens 就应该判为 needs-work，而不是交付。

合格 lens 必须让读者少追问、少误用、少回头翻源文件；做不到这一点，就先改 source pack。
如果为了看懂 lens 必须重新阅读所有来源，说明 lens 没有完成压缩和导读职责。
如果读者看完仍不知道该相信什么、不该相信什么、下一步在哪里发生，也说明 lens 尚未完成。
合格 lens 的最小承诺是：减少误读、减少重复查证、减少错误上推。
因此，reviewer 应优先审查 source pack、evidence boundary、registry 和不上推边界，而不是优先评价配色、布局或视觉风格。
视觉风格只在证据合同成立之后再优化。
若两者冲突，证据合同优先。
Review priority: evidence first, visual polish second, export convenience third, and never the reverse.
Stop if evidence is unclear.
Evidence remains the gate.
No exception.
Do not ship unclear evidence.
