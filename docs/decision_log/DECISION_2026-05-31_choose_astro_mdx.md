# Decision: Choose Astro + React + TypeScript + MDX

日期：2026-05-31

## 决策

网站采用 Astro + React + TypeScript + MDX，并通过 CSS Variables 和 JSON 主题配置控制视觉风格。

## 理由

- Astro 适合内容优先的静态教材网站。
- MDX 可在同一页面组织讲义、公式、图示和局部互动组件。
- React 只用于需要交互的局部组件。
- 当前阶段无需数据库和复杂后端。

## 边界

- 不批量生成全书页面。
- 不建立真实评论后端。
- 不自动公开部署。
