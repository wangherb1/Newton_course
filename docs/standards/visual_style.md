# 视觉风格规范

## 总体方向

目标风格：古典科学 + 数学几何 + 宇宙秩序 + 现代交互。

关键词：深蓝、金色、羊皮纸、墨绿色、星轨、椭圆轨道、几何图形、手稿、坐标网格、力心、轨道、比例、极限。

## 配置原则

- 全站基础主题由 `assets/theme/theme.json` 管理。
- 章节差异由 `assets/theme/chapter_themes.json` 管理。
- 页面组件使用 CSS Variables，不在单个页面散落硬编码色值。
- 视觉系统必须可整体替换，不将前期原型直接视为最终设计。
- Hero 节点插图遵循 `docs/standards/hero_visual_assets.md`：AI 位图独立承担连续背景视觉，首端不叠加第二套科学图或文字标注。
- 节点与 Hero 资产之间的映射由 `assets/theme/hero_visuals.json` 管理。
- 精确符号、文字标注和交互演示进入正文图示区，不与 Hero 背景图混用。

## 字体

- 中文优先：`SimSun, Songti SC, STSong, serif`
- 英文优先：`Times New Roman, Georgia, serif`
- 数学旁文优先：`Times New Roman, Georgia, serif`
- 不在仓库中打包或分享字体文件。

## 可访问性

- 正文与背景保持足够对比度。
- 交互演示不能只用颜色表达状态。
- 动画应提供静态说明或降级展示。
