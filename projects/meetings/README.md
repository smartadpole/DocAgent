---
type: meetings
id: MEET-001
project: PROJ-WIKI-001
status: active
updated: 2026-04-25
tags: [meetings, project]
---

# 会议

这页是项目侧的会议主入口。

当会议很多、而且会前材料、纪要、行动项和回看都需要稳定收口时，就用这里做总入口。
正式会议优先放这里；开发过程里的临时讨论，仍然可以直接记到 [[projects/development/worklog]]。

上游：[[projects/README]]、[[projects/requirements]]、[[projects/design/README]]、[[projects/decisions]]、[[projects/development/README]]、[[WORKFLOW]]  \
下游：[[projects/meetings/worklog]]、[[projects/trace]]、[[projects/decisions]]、[[projects/development/worklog]]、[[projects/memory/README]]

## 这页负责什么

- 统一会议议程、纪要、行动项和回看入口
- 统一正式会议的记录入口
- 统一会后结论和待办状态的回看入口
- 统一会后分流：决策、需求收敛、开发动作和稳定背景
- 统一会议相关的最小规则和流程入口
- 默认一场会不单独生成一个文件，而是在 [[projects/meetings/worklog]] 里写成一条记录；只有特别大的会议才再单独拆页

## 会前共享

- 如果明天这场会要发给对方提前看，优先单独开一页可分享的会前材料 / 议程页，把目标、待确认问题、背景和材料链接写清
- 如果待确认问题本身已经是跨页设计专题，先把专题主正文写到 [[projects/design/topics/README]] 及其子页，再在会议材料里引用
- [[projects/meetings/worklog]] 主要负责会后归档和时间线，不建议把对外预读材料只埋在长时间线里
- 一旦某场会已经有独立会前材料页，这张页就是该会议会前信息的单一信息源；不要再在 [[projects/meetings/worklog]] 里复制第二份议程、节奏、会前材料和预期结果正文
- 会后如果形成结论，再把结果回写到 [[projects/meetings/worklog]]、[[projects/decisions]]、[[projects/trace]] 或 [[projects/development/worklog]]
- 会议记录不是一次性议程快照；会后补结论、owner、时间和待办状态，仍然优先回写原会议记录
- 单条会议记录内部也不应重复：`议题`、`结论`、`行动项`、`分流` 和 `关联链接` 各自只承担一层职责，不为“看起来完整”重复表达同一件事

## 这页不负责什么

- 不放原始录音、截图和外部附件本体，那些优先进 `raw/` 或 `assets/`
- 不替代 [[projects/decisions]] 的拍板正文
- 不替代 [[projects/trace]] 的需求收敛链
- 不替代 [[projects/development/worklog]] 的实现、排障和验证流水
- 不长期承接未拍板但需要持续演化的设计专题；这类内容进入 [[projects/design/topics/README]]，会议只引用
- 不把所有会议的任务清单再汇总到 [[WORKFLOW]] 或入口页；每场会议的结论和待办仍留在各自会议记录里
- 不在独立会议页和 [[projects/meetings/worklog]] 之间并行维护同一场会的完整会前正文；发现重复时，同轮收平到单一信息源

## 固定流程

1. 会前先收集议程、背景、待确认问题和相关链接。
2. 如果待确认问题本身是未决设计专题，先补到 [[projects/design/topics/README]] 对应专题页，再挂进会议材料。
3. 如果这场会拆出了独立会前材料页，`worklog` 里的对应条目只保留链接、会后结论、待办和分流，不再复制完整会前正文。
4. 会中只记录结论、风险、行动项和需要继续确认的问题。
5. 会后按结果分流：
   - 拍板和取舍进 [[projects/decisions]]
   - 需求变化和范围收敛进 [[projects/trace]]
   - 开发动作和验证进 [[projects/development/worklog]]
   - 稳定背景进 [[projects/memory/README]]
6. 会后补写会议结论和待办状态：正式会议不只留下“待会议确认”或动作清单本身；至少把本次实际结论、待办 owner、时间和当前状态补齐。
7. 当 [[projects/decisions]]、[[projects/trace]]、[[projects/development/worklog]]、功能点页或其他承接页推进后，同轮回写对应会议记录里的结论或待办状态；这是显式同步，不是隐藏自动流控。
8. 如果发现独立会议页和 `worklog` 之间出现重复正文，不留到以后再整理；当前这轮就收平成“独立页保留会前正文，`worklog` 保留会后摘要”。
9. 如果单条会议记录内部已经出现“议题 / 结论 / 行动项”互相改写重述、默认分流重复出现、链接成堆但没有新增信息的情况，也要在当前这轮直接收紧，不接受“先保留完整、以后再压缩”的写法。
10. 如果某类会议开始反复出现，再把固定字段继续收紧成 [[templates/meeting-entry-template]] 或索引。

## 当前子页

- [[projects/meetings/worklog]]：按时间顺序记录正式会议
- [[templates/meeting-entry-template]]：正式会议记录模板

## 规则来源

- [[WORKFLOW]]：会议材料怎么收、怎么记、怎么分流
- [[projects/decisions]]：会议里的正式拍板
- [[projects/trace]]：会议里推动的需求收敛
- [[projects/development/worklog]]：会议里推动的实现动作
