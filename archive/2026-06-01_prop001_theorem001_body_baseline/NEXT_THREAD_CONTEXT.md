# 下一线程续接摘要

## 当前页面

- 开发地址：`http://127.0.0.1:4321/nodes/book1-chapter02/prop001-theorem001/`
- 页面入口：`web/src/pages/nodes/book1-chapter02/prop001-theorem001.astro`
- 页面数据：`web/src/data/prop001Theorem001.ts`
- 节点 MDX：`content/nodes/book1_chapter02/prop001_theorem001.mdx`

## 已基本敲定的主体四模块

### Hero 首端封面

- 仅使用 AI 单层背景图。
- 当前固定为 `assets/images/heroes/book1_chapter02/prop001_theorem001_hero_ai_v1.png`。
- 不叠加 SVG，不追求精确符号；精确图示进入正文。

### 英文原文

- 日常数字主源：Wikisource 1846 页面。
- 译本归属：Andrew Motte 1729 英译本。
- 证明开头已修正为 `For suppose`。
- 核心句独立加粗斜体。
- 已按原文相对位置接入 `Principia1846-105.png`。
- 原版图无必要时不添加图号、图注或单图链接。

### 中译版

- 标题：“中译版”；英文小标题：`Chinese translation`。
- 页面内不重复显示稿件来源。
- 核心句独立加粗斜体。
- 已使用裁剪版 `prop001_theorem001_geometry_proof_cropped.png`。
- 原始截图继续保留用于溯源。

### 现代微积分证明

- 标题：“现代微积分证明：极坐标方法”。
- 英文小标题：`Modern calculus proof in polar coordinates`。
- 页面内不重复显示稿件来源。
- 式（2.1）至（2.6）使用 KaTeX 排版。
- 已接入图2.1和图题：“图2.1 仅受向心力作用的物体的运动”。
- 老师已提供 `牛顿自然哲学的数学原理第2章 - latex.docx`。后续公式优先读取 `- latex.docx`，原 Word 用于视觉回查，最终必须执行 KaTeX 与双端截图复核。

## 保留待审阅模块

- 动态图：当前保留 `AreaLawDemo`，下一轮优先审阅。
- 思考题：当前保留，下一轮审阅。
- 命题网络、评论区、署名与版权说明：继续保留待审阅。

## 规范入口

- 主体四模块基线：`docs/standards/sample_page_body_baseline.md`
- 内容模型：`docs/standards/content_model.md`
- Hero：`docs/standards/hero_visual_assets.md`
- 英文原版插图：`docs/standards/primary_source_illustrations.md`
- 工作流：`docs/standards/workflow.md`

## 最近验证

- `python scripts/sync_web_public_assets.py`
- `python scripts/check_content_status.py`
- `npm.cmd run build`
- HTTP 页面返回 `200`
- 构建产物包含图题，不包含 `[公式待校对]` 或 `[图2.1待重绘]`

## 下一步

从动态图模块开始继续按页面从上到下审阅。不要回退主体四模块已确认范式。
