---
type: structure
project: wiki
status: active
updated: 2026-05-09
---

# 项目层结构

这页只回答四件事：

- `projects/` 应该怎么组织
- 常见文件应该放哪
- 文件之间怎么依赖
- 项目推进时先读什么、后写什么

详细操作顺序看 [[WORKFLOW]]；硬约束看 [[AGENTS]]；治理层总边界看 [[governance/README]]；这页只做项目层的结构主说明。

## 1. 设计原则

- 一个文档库只服务一个项目，所以 `projects/` 本身就是这个项目的运行层。
- 项目层只放当前项目直接相关的需求、设计、会议、决策、过程、记忆和发布信息。
- 可复用知识最终回写到 `articles/`、`concepts/`、`indexes/`，不要长期堆在项目层。
- 需求、trace、设计和决策共同定义主工程口径；[[projects/codebase/README]] 只负责现实实现审计、冲突收口和复用边界，不反向定义主工程。
- 单一信息源优先：同一类信息只保留一个主文件，其他页面链接它，不重复抄写。
- [[BRAIN]]、[[POLICY]] 和 `projects/memory/` 是显式分层，不再混成一页正文。
- 先有目录和职责，再决定是否需要模板。

## 2. 推荐结构

项目层结构不是一刀切。

- 已经形成多文件职责的模块，继续保留子目录。
- 只有一个 `README.md` 的子目录，默认优先收平成单文件。
- 现有内容优先保留，不为了“结构更整齐”就重写或打散已有信息。

```text
projects/
  README.md
  STRUCTURE.md
  status.md
  service-registry.md
  codebase/
    README.md
    source-code-audit-workflow.md
    page-map.md
    schema-map.md
    infra.md
    conflicts.md
    reuse-boundary.md
  requirements.md
  trace.md
  design/
    README.md
    tech-selection.md
    architecture.md
    backend-frontend-structure.md
    permission-boundary.md
    write-boundary.md
    database.md
    deployment.md
    runtime-quality.md
    topics/
      README.md
    memory/
      README.md
      tools.md
  decisions.md
  development/
    README.md
    plan/
      README.md
      work-item-system-model.md
    execution/
      README.md
      todo.md
      developer-execution-workflow.md
      engineering-feedback-loop.md
      worklog.md
    gates/
      README.md
    implementation/
      README.md
    reports/
      README.md
    risks/
      README.md
    feature-points/
      README.md
      FP-001.md
      FP-002.md
      FP-003.md
  meetings/
    README.md
    worklog.md
  releases.md
  incidents/
    README.md
    2026-04-09-example.md
  memory/
    README.md
    shared.md
    policy-links.md
```

项目层之外还有几页要一起看：

- [[governance/README]]：治理层入口和总边界
- [[BRAIN]]：共享背景
- [[POLICY]]：规则、优先级和自动沉淀边界
- [[log]]：主题化的历史记录

这不是要求一次性建全，而是推荐的扩展方向。

- 极简项目：只保留 [[projects/README]]
- 新应用探索期：如果还在比较多个候选方向，先留在 `inbox/`、`raw/`、`articles/`、`concepts/`；只有方向已经成为当前项目，才进入 [[projects/README]]、[[projects/requirements]] 和 [[projects/trace]]
- 小项目：优先平铺单文件；只有明显会长成多文件模块时再建子目录
- 复杂项目：再细分到 `architecture.md`、`backend-frontend-structure.md`、`permission-boundary.md`、`write-boundary.md`、`database.md`、`deployment.md`、`runtime-quality.md`、`worklog.md`、`shared.md` 等子页

## 3. 文件职责

### 3.1 项目主入口

- `projects/README.md`
- 回答：项目现在在做什么、当前状态是什么、下一步是什么
- 这里只放摘要、状态、关键链接和跳转，不承载大段设计正文

### 3.1.1 状态页

- `projects/status.md`
- 回答：当前状态、当前阶段、下一步、阻塞项、功能点双轴状态镜像和当前主入口
- 这是项目主页的状态镜像页，适合后续自动化读取

### 3.1.2 服务实例台账

- `projects/service-registry.md`
- 回答：真实服务现在在哪里运行、怎样健康检查、运行代码版本是什么、配置 profile 和数据目录如何定位
- 这里只记录脱敏后的运行实例事实，不替代 [[projects/design/deployment]] 的部署原则、密钥治理、发布和回滚
- 同一个代码工程 / 部署上下文下的 API、UI、scheduler、worker 或 sidecar 默认先作为一个服务组记录，再把进程写成组件

### 3.1.3 代码基线分析入口

- `projects/codebase/README.md`
- 回答：当前现实实现或既有工程是什么、页面怎么分、schema 怎么对、基础设施怎么跑、哪里有冲突、哪些能复用
- 这是现实实现审计与复用边界的主入口，但它不是项目主工程入口
- 子页：
  - `projects/codebase/source-code-audit-workflow.md`
  - `projects/codebase/page-map.md`
  - `projects/codebase/schema-map.md`
  - `projects/codebase/infra.md`
  - `projects/codebase/conflicts.md`
  - `projects/codebase/reuse-boundary.md`

### 3.2 需求层

- `projects/requirements.md`
- 回答：为什么做、做给谁、范围是什么、验收怎么算通过
- 适合放：问题定义、用户场景、目标、非目标、约束、验收标准

### 3.2.1 需求演进链

- `projects/trace.md`
- 回答：一轮需求怎样从原始意图、约束变化和修补性需求一路收敛到当前实现口径
- 适合放：原始意图、收敛后的可执行需求、关键决策变化、最终范围、关联页面、迭代块
- 不适合放：逐句对话历史、完整设计正文、完整开发流水

### 3.3 设计层

设计层只有一层，不是“两份设计”。

- `projects/design/README.md` 是设计主入口
- 它回答：整体方案是什么、涉及哪些模块、怎样实现
- 这里先放设计总览：模块划分、接口、数据流、依赖、主要风险，以及指向技术选型、架构、数据库等子页的入口
- `projects/design/topics/README.md` 是设计专题目录
- 重要但尚未拍板、或当前不进入完整架构包的专项设计，优先挂到 `topics/`
- 如果设计会影响记忆路由或规则接线，也要在这里留入口
- 如果会议涉及未定设计问题，会议页只引用这里的专题，不在会议层重复承载主正文

如果某一块设计继续长大，再从这个主入口往下拆子页：

- `projects/design/tech-selection.md`
  这是技术选型子页
  适合放候选方案、比较维度、最终选择和不选原因
- `projects/design/architecture.md`
  这是架构子页，不是第二份设计
  适合放系统架构、模块关系、接口边界、调用链
- `projects/design/backend-frontend-structure.md`
  这是工程结构子页
  适合放前后端模块拆分、目录边界、接口约定和代码落点
- `projects/design/permission-boundary.md`
  这是权限专题页
  适合放权限真相源、业务后端和前端守卫的职责分层、数据可见性矩阵、权限风险与校验边界
- `projects/design/write-boundary.md`
  这是写操作边界专题页
  适合放平台层轻量写白名单、必须进入业务后端的红线、页面动作映射、codebase 风险与改造优先级
- `projects/design/database.md`
  这是数据库子页，也属于设计层
  适合放表结构、字段约束、索引、迁移策略、读写路径
- `projects/design/deployment.md`
  这是部署子页
  适合放环境、运行拓扑、上传链路、发布和回滚
- `projects/service-registry.md`
  这是服务实例台账
  适合放已经确认的运行实例事实、健康检查、版本、配置 profile、数据目录、日志定位和更新方式；不放真实密钥或一次性排障流水
- `projects/design/runtime-quality.md`
  这是运行质量子页
  适合放监控、告警、幂等、重试、补偿、限流和稳定性口径
- `projects/design/topics/README.md`
  这是设计专题入口
  适合放未拍板但需要持续推进的设计专题，以及当前不进入完整架构包、但要长期保留的专项储备
- `projects/design/memory/README.md`
  这是记忆研究层入口
  适合放分层方案讨论、工具调研和运行层设计草稿
- `projects/design/memory/tools.md`
  这是记忆工具调研子页
  适合放 `Mem0`、`Zep`、`Letta` 等工具路线

### 3.4 决策层

- `projects/decisions.md`
- 回答：为什么选这个方案、不选另一个、当时约束是什么
- 适合放关键取舍和 ADR 风格记录
- 默认单页结构：顶部 `当前生效决策摘要`，中段 `正式决策记录`，底部 `已覆盖 / 历史决策`
- 顶部摘要默认用数字编号条目写成“主题：决策。影响：摘要”，`主题` 直接链接到同页正式条目的标题
- 正式决策记录和历史决策记录默认直接使用稳定的一句话标题，不额外加正文编号
- 摘要区的 `影响` 只写影响摘要，不罗列影响文件清单
- 新决策默认骨架：`**背景**`、`**要决策什么**`、`**可选项**`、`**最终决策**`、`**影响**`、`**各自优劣**`、`**风险点**`
- 如果使用“标签：内容”展开式，冒号前标签统一加粗；`**最终决策**` 和 `**影响**` 放在比较和风险之前

### 3.5 开发层

#### 3.5.0 职责分层

- `projects/README.md`
  这是项目主入口，偏首席技术官 / 项目负责人视角
  负责定方向、边界、优先级和最终拍板
- `projects/development/README.md`
  这是研发推进主入口，偏研发经理视角
  负责整体推进、状态镜像、阻塞协调和下一步
- `projects/development/plan/README.md`
  这是研发执行总控页
  负责当前阶段、执行入口、目录职责和支撑文件分组
- `projects/development/plan/work-item-system-model.md`
  这是事项关系模型页
  负责需求、目标、功能点、TODO、反馈和证据之间的关系类型、关闭守卫和防跑偏策略
- `projects/development/execution/README.md`
  这是执行控制入口
  负责待办、编码交接、反馈纠偏和过程记录的入口分流
- `projects/meetings/README.md`
  这是会议主入口，偏项目协作视角
  负责正式会议材料、纪要、行动项和会后分流
- `projects/development/feature-points/README.md` 和其下实体页
  这是功能点执行层，偏工程师视角
  负责单个功能点的实现、验证、结果和状态更新

#### 3.5.1 研发推进主入口

- `projects/development/README.md`
- 回答：当前研发推进状态、活跃功能点入口、卡在哪里、下一步做什么
- 偏研发经理视角

#### 3.5.2 研发执行总控

- `projects/development/plan/README.md`
  适合放当前阶段、当前主入口、支撑文件分组和开发层目录职责
- `projects/development/plan/work-item-system-model.md`
  适合放事项类型、关系类型、TODO 关闭守卫、反馈回写和证据矩阵

#### 3.5.3 执行控制目录

- `projects/development/execution/README.md`
  适合放待办、编码交接、反馈纠偏和过程记录的入口
- `projects/development/execution/todo.md`
  适合放当前可执行待办和关闭证据
- `projects/development/execution/developer-execution-workflow.md`
  适合放编码任务执行单、代码工程回传包和受控回写规则
- `projects/development/execution/engineering-feedback-loop.md`
  适合放实现偏差、测试失败、待确认项和设计反馈的分流规则
- `projects/development/execution/worklog.md`
  适合放复杂排障、联调过程、验证过程和时间顺序的实现记录

#### 3.5.4 阶段门、实现、报告和风险

- `projects/development/gates/README.md`
  适合放阶段门、准入准出、冻结对象和 Gate 报告入口
- `projects/development/implementation/README.md`
  适合放服务 / 模块实现指导和候选功能点池
- `projects/development/reports/README.md`
  适合放测试方案、测试用例、测试结论、相关回归和准出报告
- `projects/development/risks/README.md`
  适合放风险、卡点、待确认项和会议归口

#### 3.5.5 功能点执行目录

- `projects/development/feature-points/README.md`
  这是功能点实体目录，一页一个功能点
  适合放当前活跃、完成待发布和已发布功能点的索引与执行规则
  偏工程师视角

#### 3.5.6 功能点实体页

- `projects/development/feature-points/FP-001.md`
  这是功能点实体页
  适合放一个功能点的 frontmatter、目标、范围、验收、阻塞、过程和结果
- `projects/development/feature-points/FP-002.md`
  这是完成待发布的功能点实体页
- `projects/development/feature-points/FP-003.md`
  这是已发布的功能点实体页

### 3.6 会议层

- `projects/meetings/README.md`
  这是会议主入口
  适合放会前材料、会议规则、纪要入口和会后分流口径
- `projects/meetings/worklog.md`
  这是正式会议的时间线记录页
  适合放按时间顺序整理的会议纪要、行动项和回看链接
- 会议层负责把正式会议里的拍板送到 [[projects/decisions]]，把需求变化送到 [[projects/trace]]，把实现动作送到 [[projects/development/execution/worklog]]
- 如果某个待确认问题本身已是未决设计专题，会议层只引用 [[projects/design/topics/README]] 下的专题页，不重复维护主正文

### 3.7 发布层

- `projects/releases.md`
- 回答：这次发了什么、怎么验证、出了问题怎么回滚

### 3.8 事故层

- `projects/incidents/README.md`
- 回答：当前事故总览、整体状态、索引和共性改进项
- 每一个具体事故单独成文，放在 `projects/incidents/` 目录下

### 3.9 项目记忆层

- `projects/memory/README.md`
- `projects/memory/shared.md`
- `projects/memory/policy-links.md`
- 回答：这个项目长期有效的背景、路由和稳定事实
- 这里放的是项目级记忆，不是全局规则，也不是项目拍板

### 3.10 共享规则层

- [[POLICY]]
- 回答：什么可以自动沉淀、什么必须人工确认、优先级怎么排
- 这是全局规则层，不是项目层正文

## 4. 文件依赖

项目层依赖关系建议固定成这条主链：

`[[projects/README]] -> codebase -> requirements -> trace -> design -> decisions -> development -> releases -> incidents`

具体来说：

- 项目主页依赖所有活跃页面的摘要结果
- `projects/codebase/` 依赖当前代码工程事实、迁移、脚本和页面结构，向上提供代码基线结论
- `projects/status.md` 依赖 `projects/README.md` 和 `projects/development/README.md`，保留当前阶段和功能点双轴状态镜像
- 需求页向下驱动设计和决策
- trace 页把需求、设计、决策和开发串成同一条演进链
- 设计页依赖需求，并向下驱动实现
- 决策页依赖需求和设计，记录关键判断
- 开发页依赖设计和决策，记录实际推进过程
- 会议页横向连接需求、设计、决策、开发和记忆，承接正式会议材料和会后分流
- 发布页依赖设计、决策和验证结果
- 事故目录依赖发布记录、开发记录和证据

横向依赖也要固定：

- [[projects/memory/README]] 依赖 [[BRAIN]]、[[POLICY]] 和 [[projects/decisions]]
- [[POLICY]] 依赖 [[AGENTS]]、[[WORKFLOW]] 和相关决策
- 如果设计或决策改变了记忆路由或规则边界，就要同步更新 `projects/memory/`、[[BRAIN]] 和 [[POLICY]]

数据库设计不是独立于设计层存在的，它默认属于设计主入口或其子页：

- 如果数据库只是局部实现细节，放在 `design/README.md`
- 如果数据库已经成为独立主题，再拆成 `design/database.md`

完整软件架构包默认由下面几页组成：

- [[projects/design/tech-selection]]
- [[projects/design/architecture]]
- [[projects/design/backend-frontend-structure]]
- [[projects/design/permission-boundary]]
- [[projects/design/write-boundary]]
- [[projects/design/database]]
- [[projects/design/deployment]]
- [[projects/design/runtime-quality]]

如果某个主题已经明确后置、但已有长期保留价值的详细方案，可以另挂设计储备页；这类页面不自动进入当前完整架构包和默认查看顺序。

## 5. 默认读取顺序

### 5.1 做一个新功能时

1. 先读 [[projects/README]]
2. 再读 [[projects/status]]
3. 再读 [[projects/requirements]]
4. 再读 [[projects/trace]]
5. 再读 [[projects/design/README]]
6. 再读 [[projects/design/tech-selection]] 和 [[projects/design/architecture]]
7. 涉及代码落点时再读 [[projects/design/backend-frontend-structure]] 和 [[projects/design/permission-boundary]]
8. 涉及写动作收口时再读 [[projects/design/write-boundary]]
9. 涉及状态、字段和迁移时再读 [[projects/design/database]]
10. 涉及运行、发布和稳定性时再读 [[projects/design/deployment]] 和 [[projects/design/runtime-quality]]
11. 有关键取舍时再读 [[projects/decisions]]
12. 如果涉及记忆或规则，再读 [[projects/memory/README]] 和 [[POLICY]]
13. 实施复杂时再读 [[projects/development/execution/worklog]]

### 5.2 做记忆 / 规则改动时

1. 先读 [[projects/README]]
2. 再读 [[projects/STRUCTURE]]
3. 再读 [[governance/README]]
4. 再读 [[BRAIN]]
5. 再读 [[POLICY]]
6. 再读 [[projects/memory/README]]
7. 需要拍板时再读 [[projects/decisions]]

### 5.3 做发布或排障时

1. 先读 [[projects/README]]
2. 再读 [[projects/design/README]]
3. 再读 [[projects/decisions]]
4. 发布看 [[projects/releases]]
5. 故障看 [[projects/incidents/README]] 和 [[projects/development/execution/worklog]]

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
