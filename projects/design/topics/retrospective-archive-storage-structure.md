---
type: design-topic
id: DES-TOPIC-RETROSPECTIVE-STORAGE-001
project: PROJ-WIKI-001
status: implemented
stage: governance
updated: 2026-06-25
tags: [design, retrospective, archive, structure]
---

# 复盘档案存放结构设计

上游：[[projects/design/topics/README]]、[[projects/retrospectives/README]]、[[projects/STRUCTURE]]

关联：[[skills/retrospective-capability/SKILL]]、[[templates/project-retrospective-template]]、[[log]]

## 设计对象

本专题只处理复盘文件已经落库之后如何存放、索引和检查。

它不处理：

- 复盘是否应该启动。
- 多个待复盘信号如何聚合成一篇复盘。
- 复盘正文的证据判断、结论写法或行动分流。
- Issue、事故、报告、ledger、log 或 handoff 的主档案职责。

这些问题由 [[skills/retrospective-capability/SKILL]]、[[projects/retrospectives/README]]、[[harness-evolution]] 和各 owner 页面承接。

## 当前结构裁决

采用**年度物理分区 + 多维索引页**。

```text
projects/retrospectives/
  README.md
  indexes/
    by-year.md
    by-theme.md
    by-type.md
  2026/
    README.md
    YYYY-MM-DD-topic.md
```

`projects/retrospectives/` 是 archive root，只保留入口、索引目录和年份目录；标准 / 深度复盘正文进入对应年份目录。当前仓库没有旧复盘正文需要迁移，本轮只建立结构和检查闭环。

## 设计理由

- 年份是最稳定的物理分区，和 `YYYY-MM-DD-<topic>.md` 命名天然匹配。
- 主题和类型经常重叠，适合用索引表达，不适合用目录强迫单选。
- archive root 保持短入口，避免随着复盘数量增长变成长历史列表。
- Issue、事故、报告、ledger、log 和 handoff 不被镜像进复盘目录，保持单一信息源。

## 文件爆炸控制

- 同类轻量信号先聚合；没有形成标准 / 深度复盘合同前，不预建空正文。
- 同一机制缺口优先合并为一篇专题复盘；只有目标、证据链或 owner 不同才拆分。
- 新增正文必须同步 [[projects/retrospectives/indexes/by-year]]；主题或类型稳定时同步对应索引。
- 当某年目录或某索引段膨胀时，优先回检合并、拆分索引或归档旧年，不回退成根目录平铺。

## 验收口径

- archive root 只包含 `README.md`、`indexes/` 和年份目录。
- 至少存在一个年份目录，且年份目录有入口页。
- `indexes/by-year.md` 收录所有年份目录和已存在复盘正文。
- 模板保留首轮目标、用户纠偏、行动兑现回检、行动分流、上层抽象、治理自演进和未验证边界。
- 显式复盘请求默认标准复盘并落档，显式深度复盘必须包含证据计划和举一反三。
- 复盘行动项分流到 owner 页面，不在复盘目录形成平行看板。
- `python3 scripts/check_all.py --only retrospective-system` 通过。
