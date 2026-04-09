# 项目层结构

这页只回答四件事：

- `projects/` 应该怎么组织
- 常见文件应该放哪
- 文件之间怎么依赖
- 项目推进时先读什么、后写什么

详细操作顺序看 [[WORKFLOW]]；硬约束看 [[AGENTS]]；这页只做项目层的结构主说明。

## 1. 设计原则

- 一个 `wiki` 只服务一个项目，所以 `projects/` 本身就是这个项目的运行层。
- 项目层只放当前项目直接相关的需求、设计、决策、过程和发布信息。
- 可复用知识最终回写到 `articles/`、`concepts/`、`indexes/`，不要长期堆在项目层。
- 单一信息源优先：同一类信息只保留一个主文件，其他页面链接它，不重复抄写。
- 先有目录和职责，再决定是否需要模板。

## 2. 推荐结构

项目层结构不是一刀切。

- 已经形成多文件职责的模块，继续保留子目录。
- 只有一个 `README.md` 的子目录，默认优先收平成单文件。
- 现有内容优先保留，不为了“结构更整齐”就重写或打散已有信息。

例如：

- `design/` 里如果已经有 `README.md`、`architecture.md`、`database.md`，就继续保留目录。
- `releases/` 如果现在只有一个 `README.md`，而且短期内不会继续长文件，就更适合平铺成 `releases.md`。

```text
projects/
  README.md
  STRUCTURE.md
  requirements/
    README.md
  design/
    README.md
    architecture.md
    database.md
  decisions/
    README.md
  execution/
    README.md
    worklog.md
  releases/
    README.md
  incidents/
    README.md
```

这不是要求一次性建全，而是推荐的扩展方向。

- 极简项目：只保留 `projects/README.md`
- 小项目：优先平铺单文件；只有明显会长成多文件模块时再建子目录
- 复杂项目：再细分到 `architecture.md`、`database.md`、`worklog.md`、`releases/README.md`、`incidents/README.md`

如果你更喜欢平铺文件，也可以用统一前缀，例如：

```text
projects/
  README.md
  req-overview.md
  design-architecture.md
  design-database.md
  decision-log.md
  exec-worklog.md
  release-notes.md
  incident-review.md
```

当前系统默认规则是：

- 多文件模块保留目录
- 单文件模块优先平铺
- 先保留已有内容，再优化结构

## 3. 文件职责

### 3.1 项目主入口

- `projects/README.md`
- 回答：项目现在在做什么、当前状态是什么、下一步是什么
- 这里只放摘要、状态、关键链接和跳转，不承载大段设计正文

### 3.2 需求层

- `projects/requirements/README.md`
- 回答：为什么做、做给谁、范围是什么、验收怎么算通过
- 适合放：问题定义、用户场景、目标、非目标、约束、验收标准

### 3.3 设计层

- `projects/design/README.md`
- 回答：整体方案是什么、涉及哪些模块、怎样实现
- 适合放：模块划分、接口、数据流、依赖、技术选型、风险

如果设计内容继续增长，再拆：

- `projects/design/architecture.md`
  适合放系统架构、模块关系、接口边界、调用链
- `projects/design/database.md`
  适合放表结构、字段约束、索引、迁移策略、读写路径

### 3.4 决策层

- `projects/decisions/README.md`
- 回答：为什么选这个方案、不选另一个、当时约束是什么
- 适合放关键取舍和 ADR 风格记录

### 3.5 执行层

- `projects/execution/README.md`
- 回答：最近在推进什么、卡在哪里、下一步做什么
- `projects/execution/worklog.md`
  适合放复杂排障、联调过程、验证过程

### 3.6 发布层

- `projects/releases/README.md`
- 回答：这次发了什么、怎么验证、出了问题怎么回滚

### 3.7 事故层

- `projects/incidents/README.md`
- 回答：发生了什么、影响是什么、根因是什么、怎么修、如何防再发

## 4. 文件依赖

项目层依赖关系建议固定成这条主链：

`projects/README.md -> requirements -> design -> decisions -> execution -> releases -> incidents`

具体来说：

- 项目主页依赖所有活跃页面的摘要结果
- 需求页向下驱动设计和决策
- 设计页依赖需求，并向下驱动实现
- 决策页依赖需求和设计，记录关键判断
- 执行页依赖设计和决策，记录实际推进过程
- 发布页依赖设计、决策和验证结果
- 事故页依赖发布记录、执行记录和证据

数据库设计不是独立于架构设计存在的，它默认属于设计层：

- 如果数据库只是局部实现细节，放在 `design/README.md`
- 如果数据库已经成为独立主题，再拆成 `design/database.md`

## 5. 默认读取顺序

### 5.1 做一个新功能时

1. 先读 `projects/README.md`
2. 再读 `requirements/README.md`
3. 再读 `design/README.md`
4. 有关键取舍时再读 `decisions/README.md`
5. 实施复杂时再读 `execution/worklog.md`

### 5.2 做发布或排障时

1. 先读 `projects/README.md`
2. 再读 `design/README.md`
3. 再读 `decisions/README.md`
4. 发布看 `releases/README.md`
5. 故障看 `incidents/README.md` 和 `execution/worklog.md`

## 6. 什么时候建新文件

- 某一类内容已经明显变成长期主话题
- 同一类信息会反复被查
- 一页已经装不下，而且继续写会破坏可读性
- 该内容需要独立历史和独立链接

## 7. 什么时候先不拆

- 只是一次性记录
- 当前信息量很少
- 拆出去后还需要频繁回到原页才能看明白
- 还没形成稳定职责

## 8. 和知识库层的关系

- `projects/` 回答“当前项目正在推进什么”
- `articles/` 回答“某份来源材料稳定得出了什么”
- `concepts/` 回答“哪些概念和方法是可复用的”
- `indexes/` 回答“这些稳定页面怎么被导航到”

项目推进过程中产出的稳定结论，应该从 `projects/` 提升到知识库层，而不是一直留在项目层。
