# Hero 插图资产范式

## 目标

每一个定义、定律、引理、命题、推论和附注页面都可以拥有与节点内容对应的 Hero 背景图。首端插图用于建立章节气氛和直观印象，必须统一风格，并在视觉层面保持与节点主题相关的弱语义。

Hero 插图采用 AI 位图单层范式：

1. AI 位图独立承担 Hero 背景视觉，不在首端叠加第二套科学图、SVG 标注或公式。
2. `assets/theme/hero_visuals.json` 负责节点与插图资产之间的映射。
3. `NodeHero.tsx` 与 `HeroVisual.tsx` 负责统一渲染。
4. 严格的符号、文字标注和可交互演示进入正文图示区，与 Hero 背景图分工。

AI 位图不是可引用的精确科学插图，不要求完整呈现正文中的具体内容、符号或推导。生成时必须用明确约束排除常识性错误；验收时必须检查图中保留的科学元素。不得在 Hero AI 图中生成文字、字母、公式或数字。

## 文件位置

项目主资产：

```text
assets/images/heroes/<chapter_id>/<node_number>_hero_ai_vN.png
```

网站发布副本：

```text
web/public/assets/heroes/<chapter_id>/<node_number>_hero_ai_vN.png
```

首页封面使用独立资产，不复用任何单一节点 Hero：

```text
assets/images/heroes/principia_main/homepage_hero_ai_vN.png
web/public/assets/heroes/principia_main/homepage_hero_ai_vN.png
```

首页封面必须表达《原理》整体体系：几何思维、运动、力、宇宙引力与现代数学重述。不得把某个命题的单一图示直接放大作为首页故事。

节点级配置：

```text
assets/theme/hero_visuals.json
```

## 新节点制作流程

1. 阅读节点标题、核心命题、证明方法和章节主题。
2. 明确 Hero 只需传达的单一核心视觉意象，以及必须排除的科学错误。
3. 按固定模板编写详细生成指令，用内置 `image_gen` 生成无文字 AI 背景图。
4. 检查底图是否满足：左侧留白、右侧主体、视觉连续、保留的科学元素不存在常识错误、无错误文字、无水印、颜色统一、不过度拥挤。
5. 将通过验收的图片复制到项目主资产。
6. 运行同步脚本，将主资产复制到网站发布目录。
7. 在 `hero_visuals.json` 中新增节点配置。
8. 在节点 MDX 的 `visual.cover_image` 与 `visual.hero_visual_mode` 中记录资产。
9. 使用开发服务器检查桌面端和窄屏显示效果。
10. 运行 `npm.cmd run build` 并保存截图。

网站发布副本通过脚本同步：

```powershell
python scripts\sync_web_public_assets.py
```

不要直接编辑 `web/public/assets/heroes/` 下的副本。需要修改或替换图片时，先更新 `assets/images/heroes/` 下的主资产，再运行同步脚本。

## 固定生成模板

每张图都必须明确写出以下信息：

1. 页面节点与核心概念。
2. 横幅用途、左侧文字留白和右侧视觉主体。
3. 允许弱化表达的内容意义。
4. 必须避免的常识性错误，以及逐项人工检查清单。
5. 无文字、无公式、无水印约束。
6. 统一的深蓝、古金和羊皮纸色调。

## 命题1 定理1生成指令

使用模式：内置 `image_gen`。

```text
Use case: scientific-educational
Asset type: full-width decorative hero background for a Newton Principia modern reading course website
Primary request: create a refined, restrained astronomical-geometric illustration for Newton's equal areas law under a centripetal force. The image itself must form one visually coherent hero background. It should suggest orbital motion and swept-area meaning, while remaining an atmospheric decorative concept image rather than a labeled textbook figure.
Scene/backdrop: deep midnight navy scientific field, subtle fine Cartesian grid, faint orbital arcs and delicate star-track traces, a quiet classical-science observatory mood, subtle parchment-gold highlights, no horizon and no photographic scenery
Subject: one and only one elegant elliptical orbit on the right side. Place one modest warm-gold focal glow clearly at one geometric focus: visibly offset from the ellipse center along the major axis, never at the center. Add only a very subtle translucent suggestion of swept-area motion radiating from that same offset focus toward the orbit, atmospheric rather than diagrammatic.
Style/medium: polished editorial scientific illustration, minimal, premium textbook website hero, classical celestial mechanics blended with modern data visualization, flat-to-soft digital illustration, not photorealistic, not fantasy
Composition/framing: wide landscape banner. Keep the left 42 percent mostly empty dark navy for webpage title text. Continue the background grid and navy field seamlessly across the full width. Place the visual interest on the right 58 percent. Keep the main ellipse fully inside the right side with generous padding.
Lighting/mood: low-key, scholarly, calm, precise, elegant
Color palette: deep navy #0B1F3A and near-black blue; restrained antique gold #C8A24A; faint parchment #F4E8C1; very low-opacity blue-grey grid lines
Constraints: one ellipse only; one focal glow only; the focal glow must be visibly offset from the ellipse center along the major axis and remain inside the ellipse; any swept-area suggestion must radiate from that same offset focus; no second orbit diagram layered over the first; no disconnected radial lines; no impossible geometry; no bright central sun; no crowded starfield; no important detail on the left side; no thick lines; no generic glowing sci-fi interface; no text; no letters; no numbers; no equations; no labels; no watermark; no logo
Avoid: duplicate diagrams, multiple competing ellipses, centered focal glow, swept-area suggestions attached to different centers, sectors floating outside the orbit, inaccurate geometry, fantasy planets, colorful nebulae, photorealistic space, spaceship imagery, excessive lens flares, large luminous objects, hard infographic labels, visual clutter
```

## 质量验收

- 风格符合“古典科学 + 数学几何 + 宇宙秩序 + 现代交互”。
- Hero 是一张连续背景图，不出现左右割裂或重复叠图。
- 图中只出现一条主要椭圆轨道和一个位于椭圆内部、明显偏离中心的力心微光。
- 如果保留扫掠区域或径向纹理，它们必须从同一个偏心力心出发，并保持弱化表达。
- 左侧文字区有足够留白和对比度。
- 右侧插图不能抢夺标题视觉层级。
- 图中不出现文字、字母、数字、公式、水印或 Logo。
- 精确标注和教学演示放在正文图示区，不塞入 Hero。
