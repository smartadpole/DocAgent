# Page Paradigm Library

本页给 `problem-focused-visual-presentation` 提供页面范式选择，不承接项目事实。

## 使用规则

- 先按 focus contract 选择范式，再写 HTML。
- 每个持久 lens 至少声明一个 `page_paradigm` 和 slot schema。
- 范式可以组合，但首屏只能有一个视觉主角。
- 不要用通用卡片堆叠替代概念图、证据链、边界图、时间线或矩阵。

## 范式

### current-status-dashboard

用于 `status / issue / acceptance`。

- slots：一眼判断、状态带、证据边界、阻塞点、不可上推范围、追溯入口。
- visual anchor：状态控制台或证据仪表盘。
- failure mode：把状态绿灯当成 owner 页面裁决。

### decision-comparison

用于 `decision / plan / resource`。

- slots：判断目的、选项矩阵、取舍标准、证据强度、待确认项、owner 回写。
- visual anchor：对比矩阵或取舍地图。
- failure mode：评分没有口径，或把偏好写成结论。

### evidence-chain

用于 `issue / acceptance / risk / timeline`。

- slots：原始现象、证据层、推断层、验证层、不可上推层、行动分流。
- visual anchor：证据链路或泳道。
- failure mode：只凭单条日志推断全局结论。

### concept-map / concept map

用于 `knowledge / resource / owner`。

- slots：核心概念、关系类型、边界、入口、证据等级、未覆盖区。
- visual anchor：脑图、概念图、关系图或分层地图。
- failure mode：把知识页摘要成列表，没有关系。

### timeline

用于 `timeline / status / plan`。

- slots：时间点、状态变化、触发事件、证据来源、未确认段、刷新触发。
- visual anchor：路径图或阶段带。
- failure mode：把历史快照冒充 current。

### matrix

用于 `acceptance / risk / issue / decision`。

- slots：概览、轴定义、整格状态、下沉证据、不可上推范围、owner 回写。
- visual anchor：状态矩阵或热力矩阵。
- failure mode：长说明塞进格子，颜色替代诊断。

### boundary-map

用于 `risk / issue / acceptance / resource`。

- slots：内外边界、权限、证据可达性、阻塞、单一信息源、行动分流。
- visual anchor：结构边界图。
- failure mode：把不可证明范围写成 confirmed。

### operations-map

用于 `plan / acceptance / issue / status`。

- slots：source truth、content contract、visual strategy、renderer、export QA、owner 回写。
- visual anchor：从事实源到导出验证的 operations map。
- failure mode：只画流程，不记录证据边界和导出检查。

### resource-map

用于 `resource / owner / plan`。

- slots：资源类型、可用性、owner、更新条件、风险、追溯入口。
- visual anchor：资源地图库或 owner 分布图。
- failure mode：把临时资源状态写成长期事实。
