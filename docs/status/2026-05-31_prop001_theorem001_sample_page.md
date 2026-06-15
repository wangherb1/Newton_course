# 命题1 定理1样板页建设状态

## 本次任务目标

建设“命题1 定理1：扫面积速度恒定”标准样板页，验证统一内容模型、统一视觉风格、页面组件、英文主源缓存、老师稿件接入、动态演示、图谱、思考题、讨论区占位和署名模块。

## 已完成内容

- 新增样板页路由：`/nodes/book1-chapter02/prop001-theorem001/`。
- 新增统一节点 MDX：`content/nodes/book1_chapter02/prop001_theorem001.mdx`。
- 接入老师第2章稿件的章节导读、几何证明和现代微积分证明。
- 接入 Wikisource 1729 Prop. I / Theorem I 英文展示切片。
- 新增 8 个可复用页面模块和 `AreaLawDemo` SVG 互动原型。
- 更新节点图谱、outline 确认项、Schema、节点模板和内容模型文档。
- 生成浏览器截图：`exports/screenshots/prop001_theorem001_sample/page.png`。
- 生成 Hero AI 单层范式桌面截图：`exports/screenshots/prop001_theorem001_sample/hero_ai_only_v1.png`。
- 生成 Hero AI 单层范式窄屏截图：`exports/screenshots/prop001_theorem001_sample/hero_ai_only_v1_mobile.png`。
- 生成 Hero 意境优先范式 `v2` 桌面截图：`exports/screenshots/prop001_theorem001_sample/hero_ai_only_v2.png`。
- 生成 Hero 意境优先范式 `v2` 窄屏截图：`exports/screenshots/prop001_theorem001_sample/hero_ai_only_v2_mobile.png`。
- 生成内部审阅状态面板截图：`exports/screenshots/prop001_theorem001_sample/review_panel_internal_v1.png`。

## 新增/修改文件

主要新增文件：

- `content/nodes/book1_chapter02/prop001_theorem001.mdx`
- `web/src/pages/nodes/book1-chapter02/prop001-theorem001.astro`
- `web/src/data/prop001Theorem001.ts`
- `web/src/components/NodeHero.tsx`
- `web/src/components/NodeMetaPanel.tsx`
- `web/src/components/SourceBlock.astro`
- `web/src/components/TeacherTextBlock.tsx`
- `web/src/components/ModernExplanationBlock.tsx`
- `web/src/components/NodeGraphLinks.tsx`
- `web/src/components/QuestionBlock.tsx`
- `web/src/components/demos/AreaLawDemo.tsx`

## 内容来源

- 中文主源：`sources/raw/liao_teacher/chapters/chapter_02/牛顿自然哲学的数学原理第2章.docx`
- 中文抽取文本：`sources/processed/text_extracts/chapters/chapter_02/牛顿自然哲学的数学原理第2章.txt`
- 英文主源：Wikisource 1729 Andrew Motte 英译本，Book I, Section II。
- 思考题来源：`sources/raw/liao_teacher/questions/思考题.docx` 的第2章方向，并由助教按本命题结构拆分。

## 英文原文提取情况

- 页面展示切片从 `PROPOSITION I. THEOREM I.` 开始，在 `Cor. 1.` 之前结束。
- 未混入 Proposition II、导航菜单或 Wikisource 页面模板。
- 推论 I-VI 已定位，仅在样板页中显示折叠占位。
- 当前状态：`extracted_from_primary_pending_review`。

## Wikisource 1729 缓存文件

- `sources/external/principia_english/wikisource_1729_primary/raw_html/book1_section2.html`
- `sources/external/principia_english/wikisource_1729_primary/extracted_sections/book1_section2.md`
- `sources/external/principia_english/wikisource_1729_primary/extracted_nodes/book1_section2_prop001_theorem001_en_raw.md`
- `sources/external/principia_english/wikisource_1729_primary/extracted_nodes/book1_section2_prop001_theorem001_en_clean.md`
- `sources/external/principia_english/wikisource_1729_primary/extracted_nodes/book1_section2_prop001_theorem001_source.json`

## 公式与图示校对状态

- 已使用老师提供的 `牛顿自然哲学的数学原理第2章 - latex.docx` 核对现代证明公式文本；原 Word 公式对象 `image3.wmf` 至 `image16.wmf` 保留为视觉回查底本。
- 网页端使用 KaTeX 排版现代证明公式，不再显示 `[公式待校对]` 占位或整理者校核旁注。
- 已从老师稿件提取并接入带图题的图2.1静态插图，与 `AreaLawDemo` SVG 互动原型区分用途。
- 现代证明公式仍需对照老师原稿人工校对；Wikisource 节点仍需对照 IA Vol.1 scan leaf `102-103` 人工校对。

## 视觉与交互待改进项

- Hero 已升级为 AI 单层范式：同一张 AI 位图连续呈现左侧留白、右侧椭圆轨道、偏心力心和两组扫掠区域，首端不再叠加第二套 SVG。
- Hero `v2` 进一步收敛为意境优先范式：正文承担精确说明，首端背景只保留主题弱语义；人工检查确认微光位于椭圆内部并沿长轴偏离中心。
- 页面视觉复核后，当前 Hero 已回退至用户选定的 `v1`；`v2` 仅保留为未采用历史候选。
- 原“元信息”模块已固定为内部审阅状态面板：内容建设期显示，正式发布时通过全站开关隐藏，节点源文件中的状态字段继续保留。
- 节点级 Hero 配置位于 `assets/theme/hero_visuals.json`，规范位于 `docs/standards/hero_visual_assets.md`。
- `AreaLawDemo` 当前使用圆轨道离散冲击原型，以清晰展示等时间、等三角形和等面积逻辑。
- 后续可在正文图示区加入更接近牛顿原图的字母标注和 SVG 导出功能。
- 老师稿件图2.1已作为独立静态图接入现代证明模块，不与互动原型混淆。

## 构建/测试结果

- `npm.cmd install`：通过，依赖已是最新状态。
- `npm.cmd run build`：通过，Astro 成功生成 2 个静态页面。
- `python scripts/check_content_status.py`：通过，识别到 1 个 `sample_draft` 节点。
- JSON 语法检查：通过。
- 节点必填字段检查：通过。
- 浏览器 HTTP 检查：通过，样板页返回 `200`。
- 审阅状态面板双模式构建检查：通过，`internal_review` 构建包含面板，`hidden_for_release` 构建不包含面板。
- 浏览器截图：通过，已人工查看长页截图。
- `lint` / `test`：`web/package.json` 当前未配置对应脚本。
- JSON Schema 引擎：Python 环境未安装 `jsonschema`，本次未执行第三方 Schema 引擎校验。
- Windows 说明：直接运行 `npm run build` 会被 PowerShell 执行策略拦截 `npm.ps1`；使用 `npm.cmd run build` 可正常构建。

## 下一步建议

1. 对照 IA 扫描页人工校核 Wikisource 英文切片。
2. 结合桌面与窄屏渲染结果继续人工校对现代证明公式。
3. 保留并继续审阅动态图、思考题、命题网络、评论区和署名模块。
4. 按主体四模块样板范式逐步扩展其他节点。
