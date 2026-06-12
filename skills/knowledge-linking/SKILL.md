---
name: knowledge-linking
description: 新增、调研或大改长期知识页时，用于判断分层落位、入口、上位 / 邻接关系、反向回链和验证方式，避免知识成为孤岛。
maturity: mature
evidence_signals: [skill, README entry, governance, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only skill-maturity
---

# Knowledge Linking

## 定位

本技能把“新增知识”收敛成能被后续检索、学习、复用和维护的知识网络节点。

它吸收 AcknowledgeBase 的知识关联方法，但适配本库现状：当前没有独立 `knowledge-linking` sensor，因此先用技能流程和收尾检查守住入口、上位关系、邻接关系和 `log.md` 记录；后续若重复出现孤岛页，再升级专项 sensor。

## 适用场景

- 用户要求“沉淀知识”“做成参考”“新增概念”“新增文章”“调研后沉淀”。
- 新增或大改 `articles/`、`concepts/`、`indexes/`、`governance/`、`skills/` 或 `templates/`。
- 发现某个知识只存在于最终回复、`[[log]]` 或孤立页面，缺少入口和回链。
- 跨项目吸收技能、规则或模板时，需要确认它落在正确层级。

## 边界

- 不为了通过形式检查堆无意义链接；每条链接必须表达上位、邻接、案例、规则、模板、技能或证据关系。
- `[[log]]` 是历史记录，不是知识入口；新增知识不能只靠 `[[log]]` 被发现。
- 外部事实需要调研或可能变化时，必须查证来源，不能凭记忆写成稳定结论。
- 技能只提供执行方法，不替代 [[POLICY]]、[[response-mode-routing]]、[[template-feedback-rules]] 或目标页面的单一信息源。

## 成熟度与证据信号

- `maturity`：`mature`。本技能已有技能正文、README 入口、迁移边界和治理接线；暂未接入独立链接 sensor。
- `template`：知识页本身按目标层已有页面结构写；本技能不维护第二份 article / concept 模板。
- `governance`：分层落位和跨项目反哺回到 [[POLICY]] 与 [[template-feedback-rules]]；过程记录回到 [[log]]。
- `TRANSFER`：迁移边界见 [[skills/knowledge-linking/TRANSFER]]；迁移时吸收落位判断、关系画像和验证要求，不复制具体知识图谱。
- `evidence boundary`：本技能只能证明知识落位和关系维护质量，不能证明外部事实已经永久有效。

## 工作流

### 1. 判定沉淀模式

- 快速补链：已有页面缺入口、上位页或邻接关系。
- 标准知识沉淀：用户给出稳定经验，需要新增或更新概念 / 文章 / 入口。
- 调研沉淀：需要先查外部资料，再形成知识资产。
- 机制升级：需要新增或更新规则、模板、技能或 sensor。

### 2. 做内外校准

调研或大改时至少区分：

- 外部依据：官方文档、作者原文、论文、标准、法规或项目仓库。
- 内部历史：现有 `articles/`、`concepts/`、`governance/`、`skills/`、`templates/` 和 `log.md`。
- 已验证事实、方法论启发、设计推论、仍未验证边界。

### 3. 分层落位

按职责选择主落位：

- 原始资料或导出物：`raw/`、`inbox/`、`assets/`。
- 单篇材料摘要：`articles/`。
- 可复用概念、方法或实体：`concepts/`。
- 执行规则、路由或裁定：`governance/`。
- 可复用 agent 流程：`skills/`。
- 可复制骨架：`templates/`。
- 过程记录：`log.md`。

如果一个主题跨多个层级，先确定单一信息源，再让其他页面只引用和补上下文。

### 4. 建关系画像

每个新增或大改知识页都要确认：

- 所属层级。
- 主入口。
- 上位概念或 owning page。
- 至少一个邻接页面。
- 是否需要反向回链。
- 是否需要 `log.md` 记录。
- 应跑的检查命令。

### 5. 写入和验证

最小验证：

- 更新对应 README / INDEX / registry 或上位入口。
- 回看新增页是否有来源、适用边界和非 `[[log]]` 入链。
- 规则、技能、模板或入口变化后运行 `python3 scripts/check_all.py --only skill-maturity` 或相关专项检查；收尾前按本库规则运行完整检查。

## 输出格式

```markdown
**知识落位**
- 模式：
- 主落位：
- 单一信息源：

**关系画像**
- 主入口：
- 上位：
- 邻接：
- 反向回链：
- 来源：
- 适用边界：

**验证**
- 检查命令：
- 未覆盖边界：
```

## 禁止项

- 不把新增知识只写进最终回复或 `[[log]]`。
- 不把同一段正文复制到多个入口页。
- 不把项目事实、运行状态、服务路径或一次性结论写成通用概念。
- 不用空泛“相关链接”替代可解释的关系。
- 不因为暂时没有 sensor 就跳过入口、上位、邻接和回链自检。
