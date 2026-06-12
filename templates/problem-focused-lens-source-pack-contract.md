---
type: template
id: TEMPLATE-PROBLEM-FOCUSED-LENS-SOURCE-PACK-001
status: active
updated: 2026-06-12
tags: [template, lens, problem-focused-lens, source-pack, problem-focused-visual-presentation]
---

# Problem-Focused Lens Source Pack Contract

本模板用于补齐 `problem-focused-visual-presentation` 的 source pack。它不替代 [[templates/problem-focused-lens-template]]，而是把“这张 lens 到底读了什么、没读什么、能证明什么、不能上推什么”写成可复查合同。

## 1. 关注合同

- `lens_id`：
- `focus_object`：
- `judgement_purpose`：看懂 / 比较 / 行动 / 验收 / 追责 / 回顾 / 学习 / 沉淀
- `primary_question`：
- `reader`：
- `expected_decision`：
- `not_for`：
- `current_or_snapshot`：
- `refresh_trigger`：

## 2. Source Pack 清单

| 来源 | 类型 | 已读程度 | 支撑判断 | 权威层 | 更新时间 / revision | 风险 |
| --- | --- | --- | --- | --- | --- | --- |
|  | README / project / issue / report / template / governance / data / screenshot / code / log | full / partial / referenced / unread |  | truth / evidence / context / derived |  |  |

填写规则：

- `full` 表示本轮读完目标页或目标段落。
- `partial` 表示只读了相关段落，必须写明未覆盖范围。
- `referenced` 表示被其他页面引用但本轮未直接展开。
- `unread` 表示已知相关但未读，不能支撑 confirmed。
- `truth` 是当前事实单一信息源。
- `evidence` 是支撑某次判断的证据。
- `context` 是背景，不直接证明结论。
- `derived` 是导出件、图、缓存、摘要或 lens 本身。

## 3. 证据边界

### confirmed

| 判断 | 证据 | 来源 | 不能上推到 |
| --- | --- | --- | --- |
|  |  |  |  |

### likely

| 判断 | 依据 | 缺少的确认 | 降级原因 |
| --- | --- | --- | --- |
|  |  |  |  |

### possible

| 候选 | 为什么可能 | 必需验证 | 不得写成 |
| --- | --- | --- | --- |
|  |  |  |  |

### blocked

| 阻塞 | 缺少什么 | 影响范围 | 解锁动作 |
| --- | --- | --- | --- |
|  |  |  |  |

## 4. 单一信息源守卫

| 事实类型 | 真相源 | lens 只允许做什么 | 禁止 |
| --- | --- | --- | --- |
| 项目状态 | `projects/README.md` 或 owning status page | 摘要和链接 | 直接推进状态 |
| 验收关闭 | acceptance / report / issue / TASK / EP / FP / Gate | 展示证据层级 | 把局部通过写成完整关闭 |
| 服务运行 | service registry / runtime evidence | 呈现拓扑和健康摘要 | 维护密钥、临时日志或真实状态 |
| 规则裁定 | `governance/` | 摘要适用规则 | 新增未生效规则 |
| 技能流程 | `skills/` | 展示能力地图 | 改写技能正文 |
| 模板字段 | `templates/` | 展示字段覆盖 | 让 lens 成为模板 |
| 导出件 | `.exports` / cache | 预览 | 成为事实源 |

## 5. 视觉结构合同

| 视觉模块 | 回答的问题 | 数据来源 | 字段 | 交互 / 导出 | 降级规则 |
| --- | --- | --- | --- | --- | --- |
| 状态卡 | 现在怎么样 |  | status / owner / next |  | 缺状态源则只写背景 |
| 热力矩阵 | 哪些缺口最大 |  | row / column / score / missing |  | 缺评分口径则不用颜色 |
| 证据链 | 为什么这样判断 |  | step / evidence / boundary |  | 缺链路则用列表 |
| 行动地图 | 下一步做什么 |  | owner / action / dependency / validation |  | 缺 owner 则写角色 |
| 时间线 | 怎么演进到现在 |  | date / event / source |  | 缺日期则不用时间线 |
| 关系图 | 页面或对象如何连接 |  | node / edge / relation |  | 缺关系类型则不用图 |

## 6. 导出合同

- `canonical_html`：
- `print_profile`：
- `default_auto_exports`：
- `conversation_png_preview`：
- `pdf_status`：
- `png_status`：
- `svg_status`：
- `export_cache_path`：
- `export_verified_by`：

导出声明规则：

- 没生成就写 `not generated`。
- 生成但未打开检查就写 `generated, not visually verified`。
- 浏览器截图或 canvas 检查通过后才能写 `verified`。
- PDF / PNG / SVG 不提交为事实源；只作为预览或分发缓存。

## 7. Registry 字段

同步 [[views/lens-registry]] 时至少记录：

- `lens_id`
- `title`
- `path`
- `type`
- `current_or_snapshot`
- `source_pages`
- `source_revision`
- `generated_at`
- `refresh_trigger`
- `exports`
- `owner`
- `not_source_of_truth_for`

## 8. 读者首屏检查

- 首屏是否能回答 primary question：
- 是否没有把 metadata 放在最醒目位置：
- 是否有一眼判断：
- 是否有下一步：
- 是否有风险 / 缺口：
- 是否能进入证据细节：
- 是否能回到真相源：
- 是否写清不能上推到哪里：

## 9. 失败模式自检

| 失败模式 | 表现 | 修正 |
| --- | --- | --- |
| 视觉先行 | 先选图，后找问题 | 回到关注合同 |
| 证据缺席 | 有结论无来源 | 补 source pack 或降级 |
| 快照冒充 current | 旧页面无生成时间 | 标 snapshot 和 refresh_trigger |
| 导出冒充交付 | PNG / PDF 未验证 | 改写导出状态 |
| 二次事实源 | lens 复制主页面正文 | 删除重复，保留链接 |
| 分数遮蔽原因 | 矩阵只有颜色 | 补缺口和下一步 |
| 验收上推 | 局部 green 写成关闭 | 回到报告 / Gate |
| 孤立 HTML | 未登记 registry | 补 registry |

## 10. 最终回复片段

```markdown
本轮 lens 的 canonical 文件是：
- path:
- source pack:
- registry:
- exports:
- verified:
- not source of truth for:
```
