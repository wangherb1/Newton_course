# Codex 输入指令 01：建立 Newton_course 项目初步基本框架

版本：v0.1  
建议保存位置：`E:\Codex\Newton_course\docs\codex_prompts\01_project_scaffold.md`  
使用时机：Codex 当前对该项目一片空白，需要从零建立项目目录、项目规范、内容数据结构、网站技术骨架、状态管理文件。

---

## 一、你的角色与总任务

你现在是我的本地 Codex 项目工程助理。请在 Windows 本地目录：

```text
E:\Codex\Newton_course
```

中建立一个长期可维护的数字课程项目初步框架。

本项目名称暂定为：

```text
牛顿《自然哲学的数学原理》现代精读开放课程
Newton Principia Modern Reading Course
```

项目目标不是简单做几篇文章，而是把廖日东老师多年整理的牛顿《自然哲学的数学原理》讲义、中文翻译、现代微积分解释、图示、动态演示、思考题和未来互动讨论，整理成一套可长期维护、可公开发布、可课程教学、可课程改革申奖、未来可反向整理为书稿的开放教材型网站。

请你完成的不是全部内容生产，而是先建立项目骨架、标准规范、内容模型和网站初始工程。后续我们会以“命题1 定理1：扫面积速度恒定”为第一个样板页，单独打磨。

---

## 二、项目核心原则

### 2.1 内容原则

1. 内容主体来自廖日东老师已有稿件，必须尽量保留老师原意。
2. 不得随意改写导师中文翻译和现代解释。
3. 如需整理，只做结构化、格式化、拆分、索引、注释位置标记，不做未经授权的实质性改写。
4. 不得凭空补充牛顿英文原文。
5. 英文原文采用 Andrew Motte 1729 英文译本，两卷本。若本地尚未提供 OCR 或页码范围，先建立占位和待办，不要自行乱填。
6. 现代修订版、现代出版社版本、现代注释版、现代导言等文本不得默认公开使用。
7. 所有原始材料先作为本地原始资料保存，不要直接公开发布，不要自动提交到公开 Git 仓库。

### 2.2 工程原则

1. 先建立框架，不要一开始批量生成全书所有命题页面。
2. 先做一个标准样板页，确认范式后再批量复制。
3. 所有页面必须由统一内容模型驱动，不能每页临时设计。
4. 视觉风格必须统一，但必须可配置、可替换、可整体换皮。
5. 评论/互动功能先预留接口和占位组件，不要第一阶段自建复杂后端。
6. 每次任务完成后，必须更新项目状态文件，记录完成内容、当前问题、待办事项和下一步。
7. 不得删除、移动用户原始材料；如需纳入项目，只能复制。
8. 任何无法确认的内容，写入 TODO 或 issue，不要假装已经完成。

---

## 三、推荐技术路线

除非我另行指定，请采用以下轻量、内容优先的静态网站技术路线：

```text
Astro + React + TypeScript + MDX + CSS Variables / theme.json
```

理由：

1. Astro 适合开放教材、文档站、静态内容和后续部署。
2. MDX 适合把讲义文本、公式、图示组件和互动演示组件放在同一页面中。
3. React 适合制作局部互动组件，如轨道、面积速度、偏离量、滑块演示等。
4. 静态站便于部署到 GitHub Pages、Vercel、Netlify 或学校服务器。
5. 当前阶段不需要数据库和复杂后端。

如果本地 Node.js 或 npm 环境不可用，请不要强行安装失败后中断整个项目。请先建立纯文件夹框架、文档规范和占位文件，并在 `PROJECT_STATUS.md` 中明确记录依赖缺失问题。

---

## 四、已有材料与放置位置

我当前已有的老师材料位于：

```text
C:\Users\wang_\Desktop\视频号\知乎：数学物理思想及应用\牛顿\廖老师稿件
```

请先检查该目录是否存在。如果存在，请把材料复制到项目的 `sources/raw/liao_teacher/` 下。不要移动原文件，不要删除原文件。

建议放置方式如下：

| 原始文件 | 项目内建议位置 | 用途 |
|---|---|---|
| `原理概要.docx` | `sources/raw/liao_teacher/outline/原理概要.docx` | 全书目录骨架，定义、定律、引理、命题、推论的总索引 |
| `作者给读者的序言-1210.docx` | `sources/raw/liao_teacher/preface/作者给读者的序言-1210.docx` | 第一版序言、作者导读、课程引入 |
| `牛顿自然哲学的数学原理第0章-2026.docx` | `sources/raw/liao_teacher/chapters/chapter_00/牛顿自然哲学的数学原理第0章-2026.docx` | 引言、定义、运动定律、绝对时空观 |
| `牛顿自然哲学的数学原理第1章-2026.docx` | `sources/raw/liao_teacher/chapters/chapter_01/牛顿自然哲学的数学原理第1章-2026.docx` | 第一章：初始比与最终比法，引理1到引理11 |
| `牛顿自然哲学的数学原理第2章.docx` | `sources/raw/liao_teacher/chapters/chapter_02/牛顿自然哲学的数学原理第2章.docx` | 第二章：向心力的确定，命题1到命题10 |
| `附录.docx` | `sources/raw/liao_teacher/appendices/附录.docx` | 圆锥曲线、开普勒定律、二体问题等数学工具库 |
| `思考题.docx` | `sources/raw/liao_teacher/questions/思考题.docx` | 精读目标、思考题、作业题和讨论题来源 |

如果还有前期知乎专栏材料、HTML 动态演示、GIF、封面图等，请放入：

```text
sources/prototypes/zhihu_limit_column/
```

这些材料仅作为视觉风格和交互样例参考，不作为本项目正式权威内容。

建议包括：

```text
sources/prototypes/zhihu_limit_column/articles/第一期内容.md
sources/prototypes/zhihu_limit_column/articles/牛顿番外.md
sources/prototypes/zhihu_limit_column/demos/极限思想动态演示.html
sources/prototypes/zhihu_limit_column/demos/牛顿偏离量模型.html
sources/prototypes/zhihu_limit_column/assets/封面.png
sources/prototypes/zhihu_limit_column/assets/割圆术.gif
sources/prototypes/zhihu_limit_column/assets/牛顿偏离量.gif
```

Andrew Motte 1729 英文译本材料后续放置为：

```text
sources/external/motte_1729/vol_1/raw_pdf/
sources/external/motte_1729/vol_2/raw_pdf/
sources/external/motte_1729/ocr/
sources/external/motte_1729/page_maps/
sources/external/motte_1729/extracted_nodes/
```

注意：70MB 级 PDF 和扫描图像默认不提交到 Git。请在 `.gitignore` 中排除 `sources/raw/**`、`sources/external/**/raw_pdf/**`、`sources/external/**/scans/**` 等原始资料目录。若后续需要版本管理，另行考虑私有仓库或 Git LFS。

---

## 五、请建立的项目目录结构

请在 `E:\Codex\Newton_course` 下建立如下目录和基础文件：

```text
Newton_course/
├─ README.md
├─ PROJECT_STATUS.md
├─ CHANGELOG.md
├─ TODO.md
├─ .gitignore
├─ docs/
│  ├─ planning/
│  │  └─ README.md
│  ├─ codex_prompts/
│  │  └─ README.md
│  ├─ standards/
│  │  ├─ content_model.md
│  │  ├─ naming_conventions.md
│  │  ├─ visual_style.md
│  │  ├─ copyright_and_attribution.md
│  │  ├─ workflow.md
│  │  └─ comments_and_interaction.md
│  ├─ status/
│  │  └─ README.md
│  ├─ decision_log/
│  │  └─ README.md
│  └─ qa/
│     └─ README.md
├─ sources/
│  ├─ raw/
│  │  ├─ README.md
│  │  └─ liao_teacher/
│  │     ├─ outline/
│  │     ├─ preface/
│  │     ├─ chapters/
│  │     │  ├─ chapter_00/
│  │     │  ├─ chapter_01/
│  │     │  └─ chapter_02/
│  │     ├─ appendices/
│  │     └─ questions/
│  ├─ external/
│  │  ├─ README.md
│  │  └─ motte_1729/
│  │     ├─ README.md
│  │     ├─ vol_1/
│  │     ├─ vol_2/
│  │     ├─ ocr/
│  │     ├─ page_maps/
│  │     └─ extracted_nodes/
│  ├─ processed/
│  │  └─ README.md
│  └─ prototypes/
│     └─ zhihu_limit_column/
├─ content/
│  ├─ README.md
│  ├─ metadata/
│  │  ├─ principia_outline.seed.json
│  │  ├─ chapters.seed.json
│  │  └─ node_schema.json
│  ├─ nodes/
│  │  ├─ README.md
│  │  ├─ _template.mdx
│  │  └─ book1_chapter02/
│  ├─ graph/
│  │  ├─ nodes.v0.json
│  │  └─ edges.v0.json
│  └─ questions/
│     └─ README.md
├─ assets/
│  ├─ README.md
│  ├─ theme/
│  │  ├─ theme.json
│  │  └─ chapter_themes.json
│  ├─ images/
│  │  ├─ backgrounds/
│  │  ├─ covers/
│  │  └─ diagrams/
│  ├─ demos/
│  └─ icons/
├─ scripts/
│  ├─ README.md
│  ├─ extract_docx_text.py
│  ├─ build_outline_seed.py
│  └─ check_content_status.py
├─ web/
│  ├─ README.md
│  └─ astro_project_here
├─ exports/
│  ├─ README.md
│  ├─ docx/
│  ├─ pdf/
│  └─ screenshots/
├─ tests/
│  └─ README.md
└─ archive/
   └─ README.md
```

如果采用 Astro，请在 `web/` 下初始化工程。不要把网页源码直接和原始资料混在一起。

---

## 六、必须建立的状态管理文件

这是长期项目，状态记录比一次性代码更重要。

### 6.1 `PROJECT_STATUS.md`

必须包含以下栏目：

```markdown
# PROJECT_STATUS

## 当前项目版本
- 当前阶段：Phase 0 / Phase 1 / Phase 2 ...
- 最近更新时间：YYYY-MM-DD HH:mm
- 当前负责人：YAO / Codex
- 当前任务：

## 项目总目标

## 当前已有材料

## 当前目录结构状态

## 当前已完成事项

## 当前正在进行事项

## 当前未完成事项

## 当前阻塞问题

## 版权与公开发布风险

## 下一步建议

## 最近一次 Codex 操作记录
- 时间：
- 执行任务：
- 修改文件：
- 成功事项：
- 失败事项：
- 需要用户确认：
```

### 6.2 `TODO.md`

按优先级维护：

```markdown
# TODO

## P0 必须立即处理
## P1 近期处理
## P2 中期处理
## P3 远期设想
```

### 6.3 `docs/status/`

每次较大任务后新建一个状态文件，例如：

```text
docs/status/2026-05-30_project_scaffold.md
```

内容包括：任务目标、执行步骤、生成文件、未解决问题、下一步。

### 6.4 `docs/decision_log/`

重要技术选择、内容结构选择、版权策略、评论系统选择等，都要记录为 decision log，例如：

```text
docs/decision_log/DECISION_2026-05-30_choose_astro_mdx.md
```

---

## 七、内容节点模型

请在 `docs/standards/content_model.md` 中写清楚本项目的内容节点模型。

本项目的基本内容单元不是普通文章，而是《原理》中的：

```text
定义 / 定律 / 引理 / 命题 / 问题 / 定理 / 推论 / 附注 / 附录知识点
```

每个节点都应该有统一元数据。建议字段如下：

```yaml
id: principia-book1-chapter02-prop001-theorem001
book: 1
chapter_id: book1_chapter02
chapter_title: 第二章 向心力的确定
node_type: proposition_theorem
node_number: prop001_theorem001
display_id: 命题1 定理1
title_cn: 仅受向心力作用的物体与固定力心的连线扫面积速度恒定
title_en: Bodies under a centripetal force sweep out equal areas in equal times
short_title: 扫面积速度恒定
status: draft | reviewed | published | missing_source | pending_teacher_review
source_status:
  english_motte_1729: pending
  teacher_translation: available
  modern_explanation: available
  figures: available_or_pending
  demo: pending
source_files:
  teacher_docx: sources/raw/liao_teacher/chapters/chapter_02/牛顿自然哲学的数学原理第2章.docx
  english_source: sources/external/motte_1729/extracted_nodes/...
visual:
  theme_key: chapter02_centripetal_force
  cover_image: null
  demo_component: AreaLawDemo
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
  attribution: 廖日东，北京理工大学
  public_release_status: internal_draft
last_updated: YYYY-MM-DD
```

---

## 八、页面统一布局规范

请在 `docs/standards/content_model.md` 和 `content/nodes/_template.mdx` 中体现每个节点页面的标准结构。

每个命题/引理页面必须预留以下模块：

1. 页面顶部 Hero 区：章节、编号、标题、短标题、视觉背景。
2. 元信息区：节点类型、所属章节、状态、来源、依赖节点、是否已校对。
3. 核心导读区：简要说明本命题要解决什么问题。注意该区可由助教整理，但必须标注为“导读”，不能冒充导师原文。
4. 英文原文区：Andrew Motte 1729 英文原文；若尚未接入，则显示“待接入”。
5. 导师中文译文区：来自廖老师稿件，尽量原样保留。
6. 现代数学物理解释区：来自廖老师稿件，尽量原样保留。
7. 图示与动态演示区：静态图、SVG、Canvas 或 React 互动演示。
8. 关键概念区：如“向心力”“扫面积速度”“力心”“极坐标”等。
9. 思考题区：来自 `思考题.docx` 或后续整理。
10. 命题网络区：前置依赖、后续引用、相关命题。
11. 评论/讨论区：第一阶段只做可控占位，不开放真实评论。
12. 署名与版权说明区。
13. 页面状态区：内部可见或开发模式可见，显示待校对问题。

---

## 九、视觉风格系统

请在 `docs/standards/visual_style.md`、`assets/theme/theme.json`、`assets/theme/chapter_themes.json` 中建立可配置视觉系统。

### 9.1 总体风格

目标风格：

```text
古典科学 + 数学几何 + 宇宙秩序 + 现代交互
```

关键词：

```text
深蓝、金色、羊皮纸、墨绿色、星轨、椭圆轨道、几何图形、手稿、坐标网格、力心、轨道、比例、极限
```

### 9.2 字体原则

1. 中文优先使用宋体类字体，如 `SimSun`, `Songti SC`, `STSong`。
2. 英文、公式旁文字优先使用 `Times New Roman` 或 serif。
3. 不要在仓库中打包或分享字体文件。
4. 通过 CSS font-family 设置字体栈。

### 9.3 主题配置示例

请建立 `assets/theme/theme.json`，示例：

```json
{
  "brand": {
    "siteTitle": "牛顿《原理》现代精读",
    "subtitle": "几何思想与现代微积分重述",
    "teacher": "廖日东，北京理工大学"
  },
  "colors": {
    "deepBlue": "#0B1F3A",
    "gold": "#C8A24A",
    "parchment": "#F4E8C1",
    "inkGreen": "#123D35",
    "paper": "#FBF7EC",
    "text": "#1E1E1E"
  },
  "fonts": {
    "chinese": "SimSun, Songti SC, STSong, serif",
    "english": "Times New Roman, Georgia, serif",
    "math": "Times New Roman, Georgia, serif"
  },
  "components": {
    "buttonRadius": "12px",
    "cardRadius": "18px",
    "lineWidth": 2
  }
}
```

请建立 `chapter_themes.json`，至少包含：

```json
{
  "chapter01_limits": {
    "label": "第一章：初始比与最终比法",
    "symbol": "极限 / 割线 / 曲边图形",
    "primaryColor": "#123D35"
  },
  "chapter02_centripetal_force": {
    "label": "第二章：向心力的确定",
    "symbol": "力心 / 面积速度 / 轨道",
    "primaryColor": "#0B1F3A"
  },
  "chapter03_conics_focus": {
    "label": "第三章：环绕焦点的圆锥曲线运动",
    "symbol": "圆锥曲线 / 焦点 / 平方反比律",
    "primaryColor": "#2B2142"
  }
}
```

---

## 十、版权、署名与公开发布说明

请在 `docs/standards/copyright_and_attribution.md` 中写入初版原则。

必须包含：

1. 牛顿原著与 Andrew Motte 1729 英文译本属于历史文本，后续可作为公共领域文本处理，但仍需标注来源、版本、卷数和页码。
2. 现代整理版、现代修订版、出版社新版、现代导言、现代注释等不可默认公开转载。
3. Internet Archive / HathiTrust / Project Gutenberg 等公开资源可作为校核来源，但需要记录具体来源。
4. 廖日东老师中文翻译和现代解释是本项目核心原创内容，必须保留署名。
5. 公开发布前需确认导师授权边界和学校署名规范。
6. 原始 Word 稿件、PDF 扫描件、内部讨论材料默认不公开。

署名占位建议：

```text
中译版与现代解释：廖日东，北京理工大学
数字化整理与交互演示建设：WYL / 项目助教团队
原典来源：Isaac Newton, Philosophiae Naturalis Principia Mathematica; English translation by Andrew Motte, 1729.
```

---

## 十一、评论与互动策略

请在 `docs/standards/comments_and_interaction.md` 中写入初版策略。

当前阶段：

1. 不自建真实评论后端。
2. 每个命题/引理页面预留讨论区组件。
3. 讨论区显示为“评论功能规划中，当前版本暂未开放”。
4. 后续可选方案包括：Canvas/MOOC 平台讨论区、GitHub Discussions + Giscus、Utterances、Remark42、Commento 或自建审核后台。
5. 若未来启用公开评论，必须支持删除、审核、关闭、置顶、防广告、防不良信息。

请创建一个占位组件，例如：

```text
web/src/components/DiscussionPlaceholder.tsx
```

内容包括：

```text
本节讨论区暂未开放。后续将支持读者提问、课程讨论与教师/助教精选答疑。为保证学术讨论质量，评论区将采用审核和管理机制。
```

---

## 十二、脚本与自动化

请建立以下脚本占位或初版实现：

### 12.1 `scripts/extract_docx_text.py`

用途：从 docx 中提取纯文本，输出到 `sources/processed/text_extracts/`。  
要求：不要覆盖原始文件；遇到公式提取失败时做标记。

### 12.2 `scripts/build_outline_seed.py`

用途：尝试从 `原理概要.docx` 中抽取目录，生成 `content/metadata/principia_outline.seed.json`。  
要求：先做保守抽取；如果结构不稳定，生成部分结果，并在状态文件中说明。

### 12.3 `scripts/check_content_status.py`

用途：扫描 `content/nodes/` 中所有节点，生成内容完成状态表，写入 `exports/status/content_status.json` 或 Markdown 表格。

---

## 十三、Git 与仓库规则

如果当前目录尚不是 Git 仓库，可以初始化本地 Git，但不要自动推送到远程。

请建立 `.gitignore`，至少包含：

```gitignore
# dependencies
node_modules/
.astro/
dist/
.next/

# local raw source materials, not for public commit by default
sources/raw/**
sources/external/**/raw_pdf/**
sources/external/**/scans/**
sources/external/**/downloaded_archives/**

# local/generated large files
*.zip
*.7z
*.rar
*.tmp
*.bak

# OS/editor
.DS_Store
Thumbs.db
.vscode/
.idea/

# env
.env
.env.*
```

如果需要保留目录结构，请用 `.gitkeep` 或 README 文件占位。

---

## 十四、第一阶段验收标准

本次任务完成后，至少应达到以下状态：

1. `E:\Codex\Newton_course` 项目目录存在。
2. 基本目录结构完整。
3. `README.md` 说明项目目标和当前阶段。
4. `PROJECT_STATUS.md` 已创建并记录本次操作。
5. `TODO.md` 已创建并列出 P0/P1/P2/P3。
6. `docs/standards/` 下已有内容模型、命名规范、视觉风格、版权署名、工作流、评论互动规范。
7. `assets/theme/theme.json` 和 `chapter_themes.json` 已创建。
8. `content/nodes/_template.mdx` 已创建，包含标准页面模块。
9. `content/metadata/node_schema.json` 已创建。
10. `sources/raw/` 等目录已建立，原始材料如存在则已复制到对应位置。
11. 若 Astro 环境可用，`web/` 下已有最小可运行网站；若不可用，已在状态文件说明原因。
12. 未开始批量生成所有命题页面。
13. 未伪造英文原文。
14. 未自建真实评论后端。
15. 已明确下一步是执行“命题1 定理1”标准样板页建设。

---

## 十五、执行方式

请按如下步骤执行：

1. 检查并创建 `E:\Codex\Newton_course`。
2. 建立目录结构。
3. 创建基础文档和标准规范。
4. 尝试复制已有材料；若路径不存在，记录问题，不要报错终止。
5. 初始化网站工程；若环境缺失，记录问题。
6. 创建主题配置、内容模板、元数据 schema。
7. 创建脚本占位。
8. 更新 `PROJECT_STATUS.md`、`TODO.md` 和 `docs/status/YYYY-MM-DD_project_scaffold.md`。
9. 输出最终执行摘要，包括：完成了什么、修改了哪些文件、哪些材料找到了、哪些材料未找到、下一步如何执行样板页 prompt。

执行过程中请注意：

- 不要删除原始材料。
- 不要移动桌面文件夹中的材料。
- 不要一次性生成全书内容。
- 不要自动公开发布网站。
- 不要向 GitHub 推送。
- 不要把原始 PDF / Word 稿件提交到公开仓库。
- 遇到不确定事项，写入 `PROJECT_STATUS.md` 的“当前阻塞问题”。

---

## 十六、本次任务结束后必须输出给我的摘要

请在任务结束时，用中文输出：

```text
1. 已建立的项目目录
2. 已创建的关键文件
3. 已复制或未找到的原始材料
4. 当前网站工程是否可运行
5. 当前状态文件位置
6. 当前最重要的未解决问题
7. 下一步应执行的 Codex Prompt：命题1 定理1样板页建设
```
