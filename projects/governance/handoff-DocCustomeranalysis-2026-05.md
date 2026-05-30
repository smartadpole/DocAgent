---
type: governance-handoff
target: DocCustomeranalysis
source: AcknowledgeBase 治理中控
issue: Issue Intake 耗时过长（21 分钟）
root-cause: 自主复现默认触发 + doc-only intake 检查链偏重
generated: 2026-05-30
status: ready
---

# 治理 handoff：DocCustomeranalysis — Issue Intake 效率

## 诊断依据

来源：2026-05-30 ISSUE-024 归档实录（21 分 16 秒）

**不是路由问题**：agent 正确进入了 Issue Intake 快路径，checkpoint 声明了 allowed_write_roots/forbidden_roots，分层执行逻辑完整。

**真实耗时分布**：

| 阶段 | 估计用时 | 性质 |
|---|---|---|
| 定位 / 路由 / checkpoint | ~2 分钟 | 必要成本 |
| 浏览器自主复现 | ~6-8 分钟 | **可优化**：用户已提供截图，复现不是默认必须 |
| 写 issue + 档案 + 索引 | ~3 分钟 | 必要成本 |
| work-item-matrix + project-docs + 全量 check_all | ~3-4 分钟 | **可优化**：doc-only intake 不需要全量检查 |
| finalizer 外部脏改重跑 | ~2-3 分钟 | 独立问题，不在本 handoff 范围 |

---

## 本次治理范围

只改 `governance/response-mode-routing.md` 两处。不改 AGENTS.md、WORKFLOW、POLICY 或任何项目文档。

---

## 操作一：Issue Intake 快路径——补"证据充分跳过自主复现"判定

**文件**：`governance/response-mode-routing.md`

**问题**：Issue Intake 快路径没有区分"用户已提供截图+明确入口+期望行为"和"只有文字描述"两种情形，agent 对两种情形都默认执行浏览器复现。

**定位**：找到 `Issue Intake 分三层执行：` 段落，在它**之前**插入以下内容（紧接在 "首次 checkpoint 必须先回答两件事……" 段落之后）：

---

插入内容（新增段落，放在首次 checkpoint 段落和"Issue Intake 分三层执行"之间）：

```
进入三层执行前，先做证据充分性判定：用户已同时提供截图、可见入口路径和期望行为时，浏览器复现不需要做——直接进入最小落档层。只有用户描述模糊、入口不清或截图缺失时，才在最小落档层之前做最小范围复现（只验证"现象是否能稳定触发"，不做全交互流程演示）。复现产出的截图存入 assets，复现过程本身不计入 issue 正文。
```

---

**验证**：改完后问自己：下次用户提 issue 同时附上截图 + 入口 + 期望行为，agent 是否会直接写 issue，完全不打开浏览器？

---

## 操作二：Issue Intake 同步预算——补 doc-only 轻检查链规则

**文件**：`governance/response-mode-routing.md`

**问题**：同步预算段落没有区分"doc-only intake（无代码变更、无 EP/TASK 状态变更）"和"涉及状态回退的 intake"，导致两种情形都跑全量 check_all.py。

**定位**：找到以下原文段落（第 51 行附近）：

```
同步预算默认只包含：issue 页面、必要的图片证据文件、必要的单次报告或沟通包、issue 索引、报告索引、`log.md`。TASK / EP / FP / risk / status 只有在本 issue 改变它们的当前裁决、关闭状态、阻塞关系、责任归口或必须建立 backlink 时才同步；如果只是新 issue 归档，不为了"看起来完整"批量改上游状态页。
```

**在这段末尾追加（不替换原文，直接在段落后新起一段）**：

```
检查链同样按影响分层。doc-only issue intake（只写 issue 页面 + 证据文件 + 索引 + log，没有改 EP / TASK / FP 状态）：只跑 `python3 scripts/check_all.py --only project-docs`，再跑 `agent_finalizer`，不默认跑全量 check_all.py 或 work-item-matrix。涉及 TASK / EP 状态回退（如把 TASK 从 done 拉回 review）：补跑 `python3 scripts/check_all.py --only project-docs,work-item-matrix`。只有本轮同时涉及规则变更、结构变更或多模块同步时，才升级到全量 check_all.py。
```

---

**验证**：改完后问自己：下次纯 issue 归档（不改 TASK 状态），检查链是否只跑 `project-docs` + finalizer？

---

## 预期收益

| 场景 | 改前 | 改后 |
|---|---|---|
| 用户附截图提 issue，无状态变更 | ~21 分钟 | ~8-10 分钟 |
| 用户附截图提 issue，涉及 TASK 状态回退 | ~21 分钟 | ~12-14 分钟 |
| 用户无截图提 issue | ~21 分钟 | ~15-18 分钟（仍需最小复现） |

---

## 不做的事

- 不改 AGENTS.md 正文结构
- 不改 WORKFLOW
- 不处理 finalizer 外部脏改问题（独立 ledger episode，单独跟进）
- 不改 issue 模板或 check_all.py 脚本本身

---

## 执行后回传

执行完成后，在 DocCustomeranalysis 的 harness-feedback-ledger 补一条 episode：

```
| 2026-05-30 | Issue Intake 自主复现和检查链偏重 | AcknowledgeBase 治理中控分析 ISSUE-024 实录 | 规则升级 | 可优化成本 | 补证据充分性判定 + doc-only 轻检查链规则 | response-mode-routing.md | promoted |
```
