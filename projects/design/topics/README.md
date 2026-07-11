---
type: design-topics
id: DES-TOPICS-001
project: wiki
status: optional
stage: design
updated: 2026-07-11
tags: [design, topics]
---

# 设计专题

这页是设计层的重要专题入口。

主入口：[[projects/design/README]]

这里承接两类内容：

- 还没有拍板、但已经需要跨多页持续讨论的设计专题
- 当前不进入完整架构包、但需要长期保留的专项设计储备

## 这页负责什么

- 给重要设计专题提供统一目录
- 给跨页设计问题和后续储备提供稳定落点
- 让这类内容不必混进完整架构包或决策正文里

## 这页不负责什么

- 不替代 [[projects/design/README]] 的完整架构包入口
- 不替代 [[projects/decisions]] 的正式拍板正文
- 不替代会议层承接会前材料和会议纪要

## 当前专题

按需要补充：

### 已采纳专题

- [[projects/design/topics/local-git-branch-and-sync-semantics]]：系统级 Codex 配置方案；配置入口需在当前机器自发现，默认分支由用户指定或主机名推导，并把“git 同步”定义为当前分支、远程当前分支、本地 `master`、远程 `master` 三组关系读回。它不是 wiki 仓库规则或仓库分支操作。

### 待拍板专题

按需要补充。

### 后续储备

- [[projects/design/topics/retrospective-archive-storage-structure]]：复盘 archive root、年份目录、多维索引和文件爆炸控制的结构裁决。

## 使用约束

- 只要某个未定问题已经超出一次临时讨论的范围，开始影响多张设计页，就应该先沉淀成这里的专题页。
- 如果专题已经拍板并稳定收进主设计页，可在这里保留入口，也可在失去主职责后转入 [[archive/README|archive]]。
- 如果会议涉及未定设计问题，会议页只引用这里的专题，不重复维护主正文。
