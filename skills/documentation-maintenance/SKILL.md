---
name: documentation-maintenance
description: 文档维护技能；用于代码、结构、规则或公开行为变化后，保守检查文档是否过期、缺失或不准确，并产出修正报告或受控文档改动。
maturity: mature
evidence_signals: [skill, README entry, governance, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only skill-maturity
---

# Documentation Maintenance

## 定位

本技能把“代码 / 结构 / 规则变了，文档要不要同步”收敛成可审计、可保守执行的维护流程。

它吸收 fetch-adapter / prefect 的 `document-changes`、`AGENTS.md sync` 和写作文档技能中的通用方法，但不复制其产品文档、Mintlify 组件、仓库路径、提交规则或 CI 细节。

## 适用场景

- 用户要求检查文档是否需要更新、是否过期、是否和代码 / 规则不一致。
- 当前分支改了公开 API、CLI、配置、行为、目录结构、agent 规则、模板或检查脚本。
- 准备提交、PR、发布、合并后复查或规则同步。
- 本轮发现文档中的命令、路径、状态、职责、入口、模板字段或 AGENTS 约束已经漂移。

## 边界

- 默认先报告，再在用户授权或本库规则要求时做受控修改。
- 只修正确实过期、缺失或错误的文档；不为了风格偏好重写准确内容。
- 自动生成文档、导出件、API reference、examples 或目标工程声明的 generated 文件不手改。
- 不把代码仓库的产品文档规范原样搬进本库；只吸收 diff 驱动、公开面识别、保守修正、质量门和 AGENTS 层级同步方法。

## 成熟度与证据信号

- `maturity`：`mature`。本技能已有技能正文、README 入口、迁移边界和治理接线；暂未建立独立 doc-maintenance sensor。
- `template`：输出报告格式即最小骨架；若后续频繁生成文档维护报告，再抽模板。
- `governance`：文档同步、log、提交和规则升级回到 [[response-mode-routing]]、[[POLICY]]、[[AGENTS]] 和 [[template-feedback-rules]]。
- `TRANSFER`：迁移边界见 [[skills/documentation-maintenance/TRANSFER]]。
- `evidence boundary`：本技能证明文档和当前 diff / 事实源的一致性检查，不代表代码行为已经验收。

## 工作流

### 1. 判模式

- 报告模式：默认本地交互，只输出发现和建议。
- 编辑模式：用户明确授权、本库规则要求同步，或收尾必须修正文档漂移。
- AGENTS 同步模式：代码结构、命令、模块职责或 agent 约束发生变化。
- 规则 / 模板同步模式：治理页、模板、skill、sensor 变化，需要更新入口和检查说明。

### 2. 确定 diff 或事实变化

按场景获取变化：

- 当前分支：`git diff <base>...HEAD --name-status` 和目标文件 diff。
- 本轮文档库改动：`git diff --name-only` 和受影响入口。
- 指定 commit / PR：读取用户指定范围。
- 非 git 变化：使用用户给出的变更说明和直接文件证据。

跳过锁文件、缓存、导出件、自动生成文件和与用户可见行为无关的纯内部重排。

### 3. 提取用户可见变化

重点看：

- 公开 API、CLI、参数、配置、默认值、环境变量。
- 行为、错误信息、状态机、生命周期、权限、写入边界。
- 目录结构、入口、模块职责、命令、测试方式。
- agent 规则、技能、模板、sensor、提交或验收要求。
- 删除、重命名或替换的页面、文件、命令和概念。

纯内部重构不一定需要文档；只有影响读者理解、使用、维护或 agent 执行时才标记。

### 4. 映射到文档

搜索相关文档并读取上下文：

- `README`、`INDEX`、`AGENTS`、`WORKFLOW`、`governance/`。
- `skills/`、`templates/`、`projects/`、`articles/`、`concepts/`。
- 目标工程 docs、nav、runbook、handoff 或 API 文档。

分类：

- `Stale`：文档写了旧行为、旧参数、旧路径、旧命令或旧规则。
- `Missing`：新公开能力、入口或规则没有文档入口。
- `Broken example`：示例代码、命令或链接已经不可用。
- `No changes needed`：已检查但无需改。

### 5. 保守修正

编辑时只改必要位置：

- 保留现有 frontmatter、标题层级、语气和链接风格。
- 优先更新已有页，不新建重复页。
- 如果新内容需要独立页，先确认主入口和单一信息源。
- 修改代码块时确认语法、命令和测试说明。
- 更新 AGENTS 时遵守层级：共享知识放最浅共同入口，特定模块规则放最近 owning 文件。

### 6. 验证和收尾

至少：

- 回看受影响入口是否同步。
- 跑相关专项 sensor；收尾前按本库规则跑完整检查。
- `git diff --check` 或 `scripts/check_all.py` 覆盖格式问题。
- 更新 `log.md` 并提交同一主题改动。

## 输出格式

```markdown
**文档维护模式**
- 模式：
- 变化范围：
- 不检查：

**发现**
| 类型 | 文档 | 证据 | 建议 |
| --- | --- | --- | --- |

**已修改**
- 文件：
- 变更：

**验证**
- 检查：
- 未覆盖边界：
```

## 禁止项

- 不制造发现；只有读过 diff 和文档上下文后才标记 stale / missing。
- 不为了风格重写准确文档。
- 不手改自动生成文档、导出缓存或目标工程禁止手改的文件。
- 不把每个内部 helper 都要求写文档；只关注用户、维护者或 agent 会遇到的公开面。
- 不让 AGENTS 变成文件清单；它应承接隐藏约束、职责边界、惯例和坑点。
