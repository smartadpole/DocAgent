---
name: documentation-maintenance
description: 检查并修正本次公开行为、结构、规则或入口变化引起的文档漂移；按实际影响读取，普通内部修改不触发全库治理。
maturity: leading
evidence_signals: [skill, README entry, governance, sensor, TRANSFER]
transfer_ready: true
sensor: python3 scripts/check_all.py --only documentation-maintenance,skill-maturity
---

# Documentation Maintenance

以当前 diff 或事实变化定位受影响文档。用户要求报告时只报告；修改任务已经授权且文档同步属于必要范围时，直接完成修正。

## 影响判断

关注读者、维护者或 agent 会使用的 API、CLI、配置、默认值、行为、目录、命令、职责及规则。纯内部重排、提交动作本身不要求文档改动。先找到实际变化和文档上下文，再判 stale、missing、broken example 或无需修改；不要制造发现。

对治理变化同时检查重复正文、多个 owner、过厚入口、thin adapter 漂移和方案落错层。方案尚未裁决时留在既有 design owner，不写成已生效规则。规则已有但没执行时，修正执行或反馈机制，不通过增加常驻文字补偿。

## 保守修正

优先改已有 owner，其他入口短链引用。保留准确内容和本地风格，避免无关重写。Generated HTML、导出缓存、API reference 等改源文件或生成器；不能把“文件可写”当成手改授权。

AGENTS 保留必要边界和入口，条件细节进入对应 owner；thin adapter 不复制正文。按实际影响同步 README、INDEX、skill、template、sensor 或导航，不逐目录巡检。

检查受影响链接、示例/命令和格式，运行相关检查；日志、完整门禁和提交按工程收尾规则执行。结果说明改了什么、依据和未覆盖边界，无需固定报告模板。

规则 owner：[[governance/documentation-maintenance-rules]]。专项验证：`python3 scripts/check_all.py --only documentation-maintenance`；它证明维护接线，不证明代码行为已经验收。迁移见 [[skills/documentation-maintenance/TRANSFER]]。
