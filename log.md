# 活动记录

> 历史不重写；新记录按时间降序插在前面。

## 记录原则

- `[[log]]` 记录的是这轮在解决什么主题，不是对话逐句转录。
- 记录用户提问时，先提炼用户意图，再记录对应动作和影响。
- 同一轮里多个细碎问题，如果服务同一主题，合并成一条记录。
- 每条记录优先回答四件事：主题、用户意图、关键动作、受影响页面。

## 2026-04-11

### 主题：重构 `[[log]]` 的记录模型

- 用户意图：让 `[[log]]` 不再只记“改了什么”，而是能回看用户这轮真正想解决的问题；记录顺序改为时间降序；提问内容按主题提炼，不机械抄写所有问句。
- 关键动作：重写 `[[log]]` 的说明和历史条目结构，把记录口径收成“主题 + 用户意图 + 关键动作 + 受影响页面”。
- 关键动作：同步更新 [[README]]、[[INDEX]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/memory/README]] 对 `[[log]]` 的职责描述。
- 影响页面：[[log]]、[[README]]、[[INDEX]]、[[BRAIN]]、[[POLICY]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/README]]、[[projects/STRUCTURE]]、[[projects/memory/README]]。

## 2026-04-10

### 主题：把项目运行层收口到更清晰的状态与功能点模型

- 用户意图：让项目状态、功能点推进、角色分层和运行层入口的口径一致，减少“进行中”这类模糊状态在不同页面里互相污染。
- 关键动作：补齐项目状态页、运行层到规则层的桥接页，以及 Markdown 引用校验约束，让入口、状态镜像和规则边界更稳定。
- 关键动作：把功能点从单字段推进改成 `status + phase` 双轴模型，并把模板、示例、工作日志、状态页、决策页和项目记忆一起对齐。
- 关键动作：把功能点示例拆成真实实体页，把 `projects/development/README.md` 收口为研发经理看板，把工程师视角集中到 [[projects/development/feature-points/README]]。
- 关键动作：进一步收紧语言与分层边界，统一入口层中文表达，并把“框架级说明不下放到 `projects/`”沉淀成全局约束。
- 影响页面：[[projects/status]]、[[projects/memory/README]]、[[projects/memory/policy-links]]、[[projects/development/README]]、[[projects/development/worklog]]、[[projects/development/feature-points/README]]、[[projects/README]]、[[projects/STRUCTURE]]、[[WORKFLOW]]、[[POLICY]]、[[BRAIN]]、[[AGENTS]]。

## 2026-04-09

### 主题：把文档库从“文件集合”收口成有上下文模型和 memory 分层的系统

- 用户意图：让后续更新不再只盯着当前文件，而是先判断模式、阶段、主入口、上下游和受影响页面，并把规则、背景、项目记忆分层放稳。
- 关键动作：补出全局背景优先、上下文模型、最小读取集、结构变更同步和提交治理规则，避免结构变化后入口页和约束页脱节。
- 关键动作：把项目层结构说明抽到 [[projects/STRUCTURE]]，并补齐需求、设计、决策、开发、发布、事故等运行层主页面与子页面。
- 关键动作：引入 [[BRAIN]]、[[POLICY]] 和 [[projects/memory/README]] 这一组分层入口，明确共享背景、规则优先级和项目级稳定记忆的边界。
- 关键动作：统一内部链接约束，禁止长期文档继续写本机绝对路径，并把可复用设计研究迁回 `articles/` 和 `concepts/`。
- 影响页面：[[README]]、[[INDEX]]、[[WORKFLOW]]、[[AGENTS]]、[[projects/STRUCTURE]]、[[projects/README]]、[[BRAIN]]、[[POLICY]]、[[projects/memory/README]]、[[articles/2026-04-09-obsidian-doc-system-design]]、[[concepts/document-os]]。

## 2026-04-08

### 主题：搭建 `wiki` 文档库底座并补齐最小维护流程

- 用户意图：先把这套库从零搭起来，让资料有入口、有层次、有维护动作，后续不管是知识沉淀还是研发推进都有可落脚的主结构。
- 关键动作：初始化 `wiki` vault，配置 `Obsidian`、`Codex CLI`、`workspace-filesystem`、`workspace-memory`，并建立根入口、模板层、知识层与日志层。
- 关键动作：明确 `raw/`、`inbox/`、`assets/`、`archive/` 和 `projects/` 的边界，把“README 先行、模板按需、极简项目默认单主页”收成基础维护规则。
- 关键动作：把新建目录、新建文件、修改文件、目录复用、入口跳转和日志留痕这些高频判断前置到入口页和流程页，避免系统刚起步就散成文件堆。
- 影响页面：[[README]]、[[INDEX]]、[[WORKFLOW]]、[[projects/README]]、[[log]]、`templates/`、`articles/`、`concepts/`、`indexes/`。
