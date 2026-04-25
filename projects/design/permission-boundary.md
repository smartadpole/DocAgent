---
type: design
id: DES-PERMISSION-001
project: wiki
status: optional
stage: design
updated: 2026-04-25
tags: [design, permission]
---

# 权限边界

主入口：[[projects/design/README]]

这里记录权限真相源、角色可见性、业务授权和前端守卫的职责分层。

## 当前内容

- 权限真相源：
- 角色和可见性：
- 数据底线：
- 业务授权：
- 前端守卫：
- 风险和校验：

## 维护说明

- 权限不只写在前端。
- 如果权限判断影响写操作，回链 [[projects/design/write-boundary]]。
- 如果现实实现和权限设计冲突，回写 [[projects/codebase/conflicts]]。
