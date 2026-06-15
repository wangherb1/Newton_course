# 内容节点模型

## 基本原则

本项目的内容单元不是普通文章，而是《自然哲学的数学原理》中的定义、定律、引理、命题、问题、定理、推论、附注和附录知识点。所有页面必须由统一元数据和统一页面模块驱动。

内容整理以保留廖日东老师原意为前提。允许结构化、格式化、拆分、索引和注释位置标记，不得未经授权实质改写。Andrew Motte 1729 英文原文在来源和页码尚未确认时只显示“待接入”。

## 节点元数据

```yaml
id: principia-book1-chapter02-prop001-theorem001
book: 1
part: 第一卷 物体的运动
chapter_id: book1_chapter02
chapter_title: 第二章 向心力的确定
node_type: proposition_theorem
node_number: prop001_theorem001
display_id: 命题1 定理1
title_cn: 仅受向心力作用的物体与固定力心的连线扫面积速度恒定
title_en: Bodies under a centripetal force sweep out equal areas in equal times
short_title: 扫面积速度恒定
status: sample_draft
sample_page: true
review_panel:
  visible: true
  mode: internal_review
chapter_intro:
  visible: true
  source: teacher_manuscript
source_status:
  english_wikisource_1846: extracted_from_primary_pending_review
  english_wikisource_1729_reference: retained_for_comparison
  english_gutenberg_1846_backup: not_used
  motte_1729_scan_backup: not_used_for_page
  teacher_translation: extracted_from_teacher_docx_pending_review
  modern_explanation: extracted_from_teacher_docx_pending_review
  figures: reconstructed_or_pending_review
  demo: standalone_html_equal_area_pending_review
source_files:
  teacher_docx: sources/raw/liao_teacher/chapters/chapter_02/牛顿自然哲学的数学原理第2章.docx
  teacher_latex_docx: sources/raw/liao_teacher/chapters/chapter_02/牛顿自然哲学的数学原理第2章 - latex.docx
  english_primary_url: https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1846)/BookI-II
visual:
  theme_key: chapter02_centripetal_force
  cover_image: null
  hero_visual_mode: ai_image_only
  demo_component: AreaLawDemo
  demo_html: web/public/demos/book1_chapter02/prop001_theorem001/equal_area_demo.html
  demo_prompt: web/public/demos/book1_chapter02/prop001_theorem001/equal_area_demo.prompt.md
  teacher_translation_figure: assets/images/teacher_manuscripts/book1_chapter02/prop001_theorem001_geometry_proof.png
graph:
  depends_on:
    - principia-law-001
    - principia-law-corollary-001
    - principia-book1-chapter01-lemma003-corollary004
  used_by: []
  related_nodes: []
questions:
  - qid: q_ch2_prop1_001
comments:
  enabled: false
  provider: placeholder
rights:
  teacher_attribution: 廖日东，北京理工大学
  digital_editor: WYL / 项目助教团队
  english_source_license_note: Wikisource 1846 digital transcription of the Andrew Motte translation, public-domain source, pending project-level citation normalization
  public_release_status: internal_sample_pending_review
last_updated: YYYY-MM-DD
```

字段约束由 `content/metadata/node_schema.json` 提供。正式节点应使用该 Schema 校验。

## 状态定义

- `draft`：已开始整理，尚未完成校对。
- `sample_draft`：标准样板页已经形成，可用于内部审阅和范式验证。
- `reviewed`：内容已完成内部校对。
- `published`：已通过授权和发布检查。
- `missing_source`：关键来源缺失。
- `pending_teacher_review`：等待老师确认。

## 标准页面模块

每个命题、引理及同类节点页面必须预留以下模块：

1. Hero 区：章节、编号、标题、短标题、视觉背景。
2. 审阅状态区：节点类型、所属章节、状态、来源和校对状态。内容建设期默认显示，正式发布时隐藏，源数据保留。
3. 章节导读区：条件模块。仅每章第一个命题页显示，内容直接摘自廖老师稿件；其他命题、定理和推论页不得渲染或复制本区。
4. 助教导读 / 学习提示区：可选编辑模块，正式节点默认不启用。如使用，必须明确标注为整理者导读，不得冒充导师原文。
5. 视频课区：可选但预留的课程讲解模块。若存在老师线下讲课视频，置于英文原文区之前；无视频时可隐藏。
6. Andrew Motte 1729 英文原文区：来源未接入时显示“待接入”。
7. 导师中文译文区：来自廖老师稿件，尽量原样保留。
8. 现代数学物理解释区：来自廖老师稿件，尽量原样保留。
9. 图示与动态演示区：静态图、SVG、Canvas 或 React 组件。演示必须围绕节点核心展示点设计，不能只提供装饰性轨迹动画。
10. 关键概念区。
11. 思考题区。
12. 命题网络区：前置依赖、后续引用、相关命题。
13. 评论/讨论区：第一阶段只使用占位组件。
14. 署名与版权说明区。
15. 页面状态区：开发模式显示待校对问题。

## 样板页主体基线

`principia-book1-chapter02-prop001-theorem001` 已形成首个主体正文样板页。后续扩展节点时，优先复用并保持以下四个主体模块的结构和质量标准：

1. Hero 首端封面：单层 AI 背景图，不叠加第二套 SVG；左侧保留标题空间，右侧提供章节主题弱语义。
2. Andrew Motte 1729 英文原文区：Wikisource 1846 数字页面作为日常文本与插图定位主源，Andrew Motte 1729 作为译本归属；核心句独立突出，原版插图按原文相对位置接入。
3. 中译版区：保守接入老师稿件，标题为“中译版”，英文小标题为 `Chinese translation`；核心句独立突出，稿件插图按相对位置接入。
4. 现代微积分证明区：保守接入老师稿件，优先使用 `- latex.docx` 配套稿件录入公式，原始 Word 负责视觉回查；使用 KaTeX 排版，并保持插图、图题和正文图号引用一致。

动态图示模块和署名模块已按样板页当前结论固化为可复用范式；思考题、命题网络和评论区继续保留为扩展模块待审阅状态。未经新一轮审阅，不应把待审阅扩展模块的当前形态当作后续节点的最终范式。

视频课模块作为新增可选模块纳入页面框架。样板页当前使用示例视频占位，正式发布前应替换为已确认授权的老师课程视频。

## 图示与动态演示规则

- 每个动态图示必须先写清核心展示点，再选择 SVG、Canvas 或 React 交互形式。
- 合格动态图示应同时给出形象结构和可核查证据：关键几何对象、变量变化和结论提示必须互相对应。
- 命题1定理1的动态图示核心是等面积定律：椭圆轨道、固定焦点力心、不同长度的焦点连线、相等时间段和相等扫过面积必须同时可见。
- 不得用圆轨道等特殊情形替代一般性的核心展示，除非正文明确讨论的就是圆周运动。
- 动态图示完成后必须检查桌面和窄屏截图，确认核心对象没有遮挡，且标题、说明和正文引用一致。
- 每个动态演示必须保留一个可独立打开的 HTML 文件，并由页面端直接挂载同一个文件。样板页路径为 `web/public/demos/book1_chapter02/prop001_theorem001/equal_area_demo.html`。
- 每个动态演示 HTML 的同目录必须保留一份生成指令 prompt 文档，用于记录核心展示点、数学模型、视觉要求、交互要求和验收标准。样板页路径为 `web/public/demos/book1_chapter02/prop001_theorem001/equal_area_demo.prompt.md`。
- 页面语言必须面向正式课程读者，采用客观学术叙述，不得使用内部制作说明语气。
- 如果动态图示涉及物理或数学定律，视觉取样方法必须与定律一致。命题1定理1不得使用等角速度取样；椭圆轨道示例应按 `M = E - e sin E` 等间隔取点，使相等时间对应相等扫过面积。

完整基线见 `docs/standards/sample_page_body_baseline.md`。

## 中译版模块规则

- 页面标题暂用“中译版”，英文小标题使用 `Chinese translation`。
- 页面正文不重复显示稿件来源说明；来源路径、提取状态和校对状态保留在节点元数据及内部审阅状态中。
- 命题或定理核心句应独立突出显示。
- 老师 Word 稿件中存在对应插图时，应从 DOCX 原始媒体中保守提取，并尽量保持稿件中的相对插入位置。
- DOCX 原始媒体如果包含浏览器界面、任务栏、页面边缘或无关内容，应保留直接提取的溯源原图，另生成裁剪后的网页资产。页面只引用裁剪版。
- 中译版插图沿用英文原版插图布局：桌面端右浮动并允许正文绕排，宽度控制在正文区域约 `43%`；窄屏改为整行显示。
- 稿件插图项目主资产存放在 `assets/images/teacher_manuscripts/`，通过 `scripts/sync_web_public_assets.py` 同步到 Web 发布目录。
- 老师稿件插图的公开发布仍受讲义授权边界约束。

## 现代数学物理解释模块规则

- 页面标题暂用“现代微积分证明：极坐标方法”，英文小标题使用 `Modern calculus proof in polar coordinates`。
- 页面正文不重复显示稿件来源说明；来源路径、提取状态和校对状态保留在节点元数据及内部审阅状态中。
- 公式整理优先读取老师提供的 `- latex.docx` 配套稿件中的 LaTeX 文本，以提高录入效率；原始 Word 内嵌公式对象继续作为视觉回查底本。
- LaTeX 文本不得未经检查直接发布。必须经过公式语义核对、KaTeX 渲染、桌面与窄屏截图复核；复杂公式或可疑转义仍需回看原始 Word。
- 公式必须回填到正文相对位置，不得在正式网页中保留 `[公式待校对]` 占位或整理者校核用旁注。
- 老师 Word 稿件中存在对应插图时，应按稿件相对位置插入现代证明模块；正文引用使用图号时，插图必须显示一致的图题。桌面端复用正文插图右浮动布局，窄屏改为整行显示。
- 现代证明公式与插图仍受老师稿件校对和公开发布授权边界约束。

## 章节导读规则

- 节点元数据使用 `chapter_intro.visible` 控制章节导读是否显示。
- 每章仅允许第一个命题页设置 `chapter_intro.visible: true`，并设置 `chapter_intro.source: teacher_manuscript`。
- 其余节点必须保持 `chapter_intro.visible: false` 和 `chapter_intro.source: null`。
- 章节导读与“助教导读 / 学习提示”是不同模块，不得互相替代。

## 内容存放

- 元数据与页面正文：`content/nodes/`
- 关系图：`content/graph/`
- 思考题：`content/questions/`
- 原始资料副本：`sources/raw/`
- 处理后中间文件：`sources/processed/`
