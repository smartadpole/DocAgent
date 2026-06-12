# Problem-Focused Visual Presentation Transfer

## 能力目标

让目标工程具备把复杂文档、主题、状态、风险、计划、验收或证据链转成问题聚焦图文 lens 的能力，并守住来源、证据边界、持久化和导出一致性。

## 可以吸收

- 关注合同：对象、粒度、目的、载体、持久性、导出需求。
- source pack：已读、未读、更新时间、证据和推断。
- 背景框：上位、来源、历史、关系、使用边界。
- 证据边界：confirmed、likely、possible、blocked。
- 图文结构选择：状态卡、矩阵、时间线、关系图、证据链、行动地图。
- 持久化守卫：canonical HTML / source、snapshot、ignored exports、导出一致性、同源一致性、[[views/lens-registry]] 或等价 registry。

## 只能抽象吸收

- 源工程的 `views/` 结构、导出目录、registry、lens 字段和 CSS 只能作为参考。
- 目标工程已有报告、dashboard、artifact 或 docs site 时，应映射到既有呈现层。
- 没有持久视图需求时，只迁移聊天内 lens 方法，不强行建 `views/`；一旦目标工程要生成持久 lens，必须建立或绑定等价 current / snapshot / registry / ignored exports。

## 禁止复制

- 不复制源工程具体 HTML、矩阵数据、项目状态、路径、排行、source revision 或截图。
- 不把 PDF / PNG / slide 写成第二份事实源。
- 不把图文呈现替代验收、关闭、准出、决策或人工确认。

## 目标工程结构自检

迁移前检查：

1. 是否已有 `views/`、`reports/`、dashboard、artifact、docs site 或等价呈现层。
2. 是否已有导出目录和 `.gitignore` 规则。
3. 是否需要 current / snapshot / temporary 三类视图。
4. 是否有 source manifest、registry、render pipeline 或截图 / PDF 工具。
5. 如果没有持久需求，只建立技能，不新增呈现目录。

## 验证要求

- 用一个真实主题生成聊天内 lens 或持久 lens 干跑。
- 检查 source pack、背景框、证据边界和不可上推范围是否完整。
- 若生成持久 HTML，验证导出件和 canonical 源的一致性，并确保导出件不会作为重复事实源提交。
- 若建立持久呈现层，验证 `views/current/`、`views/snapshots/`、`views/lens-registry` 或等价入口已经接线。
- 最终回复写清呈现落位、来源、导出状态、检查结果和未覆盖边界。
