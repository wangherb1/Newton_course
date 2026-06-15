# 2026-06-03 命题1定理1等面积演示融合版

## 范围

- 样板页：`/nodes/book1-chapter02/prop001-theorem001/`
- 网页挂载组件：`web/src/components/demos/AreaLawDemo.tsx`
- 独立演示文件：`web/public/demos/book1_chapter02/prop001_theorem001/equal_area_demo.html`
- 参考优化文件：`web/public/demos/book1_chapter02/prop001_theorem001/equal_area_optimized.html`

## 本次结论

本轮将优化版演示的主体内容吸收到课程页正式演示中，但不直接照搬其白底工具页风格。最终版本保留课程页面的深色图框、金色扇形、纸本文本区和 iframe 挂载方式，同时采用优化版的命题陈述、交互控制、几何与面积检验、力心连线特征对比、图例、读图要点和 Canvas 等面积建模。

## 核心展示点

- 固定力心位于椭圆焦点 `S`。
- 以平近点角 `M = E - e sin E` 的等间隔表示相等时间。
- 相等时间段对应的焦点扇形面积相等。
- 近点处连线较短而转角较大；远点处连线较长而转角较小。
- 默认展示全轨道等面积扇区，使读者首先看到定律整体结构，而不是只看到局部动画。
- 右侧面板提供可核验的数据表，而不仅是图形说明。

## 版面要求

- 演示语言面向正式课程读者，避免“交互演示”“给用户看”等内部制作语气。
- 右侧面板保留优化版主体结构：命题陈述、交互控制、几何与面积检验、近远焦点对比、图例和读图要点。
- 桌面端左侧图框固定，右侧文字面板独立滚动；移动端采用上图下文，面板独立滚动。
- 移动端避免横向裁切；按钮、滑条、表格和图框标签必须完整可读。
- 独立 HTML 文件与网页端显示保持同一文件来源，便于后续人工直接修改。
- 等时间分段数上限为 `36`。

## 验证记录

- `npm.cmd run build`：通过，生成 3 个静态页面。
- 桌面截图：`exports/screenshots/prop001_theorem001_sample/equal_area_demo_fusion_desktop_final2.png`
- 移动截图：`exports/screenshots/prop001_theorem001_sample/equal_area_demo_fusion_mobile_final2.png`
- 网页嵌入截图：`exports/screenshots/prop001_theorem001_sample/equal_area_demo_fusion_page_final.png`
