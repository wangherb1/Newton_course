# Codex 输入指令 04：调整英文原文数据源，改用 Wikisource 1729 作为主数据库

版本：v0.1  
项目路径：`E:\Codex\Newton_course`  
任务类型：项目数据源重构 + 英文原文抓取流程建立 + 命题1样板页前置准备  
执行对象：Codex 本地项目智能体  
重要程度：高  
执行顺序：应在“命题1 定理1样板页制作”之前完成

---

## 0. 本次任务背景

当前项目 `E:\Codex\Newton_course` 已经建立了基本框架。此前曾计划将 Internet Archive 下载的 Andrew Motte 1729 年《The Mathematical Principles of Natural Philosophy》扫描资源、OCR、HOCR、页码文件等整理成本地英文原文资源库。

但经过重新评估，完全依靠本地 OCR 资源库存在以下问题：

1. 文件体量很大，卷一、卷二完整下载资源庞杂。
2. OCR 质量不稳定，需要大量人工校对。
3. 命题、引理、推论的精确切片工作量大。
4. 项目后续维护困难，容易出现页码、段落、命题编号错位。
5. 网上已有更成熟的公开数字文本资源，可以直接作为主数据库。

因此，本项目英文原文的主数据源调整为：

```text
Wikisource 1729 Andrew Motte 版
https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1729)
```

该页面为 Andrew Motte 英译本，基于 Newton 1726 年第三版拉丁本，且已经将 Volume 1 的 Definitions、Axioms、Book I 各 Section 拆分为独立页面。后续应优先从 Wikisource 1729 页面提取英文原文。

---

## 1. 本次任务目标

请你在 `E:\Codex\Newton_course` 项目中完成以下工作：

1. 调整英文原文数据源策略。
2. 新建 `sources\external\principia_english` 数据源目录。
3. 将 Wikisource 1729 设置为英文原文主源。
4. 将 Wikisource 1846 和 Project Gutenberg 1846 设置为备用源。
5. 保留已下载的 1729 扫描资源作为底本校核源，但不再作为主工作流。
6. 编写脚本，用于抓取、缓存、解析 Wikisource 1729 分章节页面。
7. 以 `Book 1 / Section 2` 为第一测试对象，提取 “PROPOSITION I. THEOREM I.” 英文原文。
8. 生成英文原文提取报告。
9. 更新项目状态文件和 README，明确后续英文原文统一使用该工作流。
10. 不要立即制作最终网页样板页。本任务只做英文数据源准备和样板页前置数据整理。

---

## 2. 新的数据源优先级

从现在开始，英文原文提取优先级固定如下。

### 2.1 第一优先级：Wikisource 1729 主源

```text
https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1729)
```

用途：

- 主力提取英文原文。
- 优先用于 Definitions、Axioms、Book I 各 Section。
- 优先用于命题、引理、推论的节点化切片。
- 当前样板页 “命题1 定理1：扫面积速度恒定” 必须从该源提取。

样板页目标页面：

```text
https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1729)/Book_1/Section_2
```

### 2.2 第二优先级：Wikisource 1846 备用源

```text
https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1846)
```

用途：

- 当 Wikisource 1729 某部分缺失、转录未完成或格式异常时，用作备用校对。
- 不作为默认主源。
- 提取内容时必须标记来源为 `wikisource_1846_backup`。

### 2.3 第三优先级：Project Gutenberg 1846 全文备份源

```text
https://www.gutenberg.org/ebooks/76404
https://www.gutenberg.org/cache/epub/76404/pg76404-images.html
```

用途：

- 全文备份。
- 跨源校对。
- 当 Wikisource 页面抓取失败时，作为文本比对来源。
- 不作为命题切片主源，因为它是长篇单页 HTML，不如 Wikisource 分章节页面适合自动切分。

### 2.4 第四优先级：Internet Archive 1729 扫描底本

本地已下载目录：

```text
E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_1
E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_2
```

项目已有或计划目录：

```text
E:\Codex\Newton_course\sources\external\motte_1729
```

用途：

- 作为底本校核。
- 用于疑难段落、页码、图版、扫描页核对。
- 不再作为日常英文提取主工作流。
- 不要删除，也不要重复大规模复制。

---

## 3. 请建立新的目录结构

在项目中建立：

```text
E:\Codex\Newton_course\sources\external\principia_english
```

建议完整结构如下：

```text
sources\external\principia_english
│
├─ README.md
├─ source_strategy.md
├─ urls.json
├─ manifest.json
│
├─ wikisource_1729_primary
│  ├─ README.md
│  ├─ urls.json
│  ├─ raw_html
│  │  ├─ book_1_section_2.html
│  │  └─ ...
│  ├─ raw_wikitext
│  │  ├─ book_1_section_2.wikitext
│  │  └─ ...
│  ├─ cleaned_text
│  │  ├─ book_1_section_2_clean.txt
│  │  └─ ...
│  ├─ extracted_nodes
│  │  ├─ book1_section2_prop01_theorem01_en_raw.md
│  │  ├─ book1_section2_prop01_theorem01_en_clean.md
│  │  ├─ book1_section2_prop01_theorem01_metadata.json
│  │  └─ ...
│  └─ logs
│     ├─ fetch_log.md
│     ├─ extraction_log.md
│     └─ validation_report.md
│
├─ wikisource_1846_backup
│  ├─ README.md
│  ├─ urls.json
│  ├─ raw_html
│  ├─ cleaned_text
│  ├─ extracted_nodes
│  └─ logs
│
├─ gutenberg_1846_backup
│  ├─ README.md
│  ├─ source_url.txt
│  ├─ raw_html
│  ├─ full_text
│  └─ logs
│
├─ motte_1729_scan_backup
│  ├─ README.md
│  ├─ local_paths.json
│  └─ notes.md
│
└─ tools
   ├─ fetch_wikisource.py
   ├─ extract_wikisource_node.py
   ├─ validate_extracted_node.py
   └─ README.md
```

如果项目已有类似目录，请在不破坏已有文件的前提下合并。

---

## 4. 请写入 urls.json

在：

```text
sources\external\principia_english\urls.json
```

写入如下结构：

```json
{
  "primary_source": {
    "name": "Wikisource 1729 Andrew Motte edition",
    "base_url": "https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1729)",
    "notes": "Primary source for English text extraction. Use this source first whenever possible."
  },
  "sample_source": {
    "node_id": "book1_section2_prop01_theorem01",
    "title": "PROPOSITION I. THEOREM I.",
    "url": "https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1729)/Book_1/Section_2"
  },
  "backup_sources": [
    {
      "name": "Wikisource 1846 Motte-Chittenden edition",
      "base_url": "https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1846)",
      "use_case": "Backup and comparison when Wikisource 1729 is incomplete or abnormal."
    },
    {
      "name": "Project Gutenberg 1846 electronic text",
      "base_url": "https://www.gutenberg.org/ebooks/76404",
      "html_url": "https://www.gutenberg.org/cache/epub/76404/pg76404-images.html",
      "use_case": "Full-text backup and cross-checking."
    }
  ],
  "scan_backup": {
    "name": "Internet Archive 1729 scan backup",
    "local_vol_1": "E:\\Download\\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_1",
    "local_vol_2": "E:\\Download\\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_2",
    "use_case": "Historical scan verification only. Do not use as routine extraction source."
  }
}
```

---

## 5. 请建立 source_strategy.md

在：

```text
sources\external\principia_english\source_strategy.md
```

写明以下原则：

1. 英文原文主源为 Wikisource 1729。
2. Wikisource 1729 的文本优先级高于 1846 版。
3. 1846 Wikisource 与 Project Gutenberg 只作为备用与比对。
4. Internet Archive 1729 扫描件保留为底本核对，不再作为日常主工作流。
5. 所有抓取内容必须本地缓存，避免每次重复请求网页。
6. 所有提取节点必须记录来源 URL、抓取时间、提取规则、是否人工校对。
7. 如果 1729 与 1846 文本存在差异，默认保留 1729 文本，并在 metadata 中记录差异。
8. 如果引用整段英文原文用于公开网页，必须保留来源说明和公共领域说明。
9. 不允许在没有记录来源的情况下手动粘贴英文原文。
10. 后续所有英文节点统一放入 `wikisource_1729_primary\extracted_nodes`。

---

## 6. 请编写抓取脚本 fetch_wikisource.py

在：

```text
sources\external\principia_english\tools\fetch_wikisource.py
```

编写 Python 脚本。要求如下：

### 6.1 功能

脚本应支持输入 URL 和输出路径，下载 Wikisource 页面并保存：

- raw HTML
- 可选 raw wikitext
- 简单清洗后的正文文本

### 6.2 技术建议

优先使用普通 `requests + BeautifulSoup` 抓 HTML。

同时建议支持 MediaWiki API 获取 wikitext，例如：

```text
https://en.wikisource.org/w/api.php?action=parse&page=The_Mathematical_Principles_of_Natural_Philosophy_(1729)/Book_1/Section_2&prop=wikitext&format=json
```

注意：实际脚本中需要对 page title 进行 URL 编码。

### 6.3 脚本要求

1. 不要写死只能处理 Section 2。
2. 支持命令行参数：
   - `--url`
   - `--page-title`
   - `--out-dir`
   - `--slug`
   - `--sleep`
   - `--force`
3. 如果本地已经存在 raw_html，默认不重复下载，除非传入 `--force`。
4. 设置 User-Agent，标明这是课程资料整理用途。
5. 每次抓取后写入 `logs\fetch_log.md`。
6. 捕获网络错误，失败时不要中断整个项目。
7. 输出 UTF-8 编码文件。

### 6.4 首次测试对象

运行目标：

```text
URL:
https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1729)/Book_1/Section_2

slug:
book_1_section_2
```

输出：

```text
sources\external\principia_english\wikisource_1729_primary\raw_html\book_1_section_2.html
sources\external\principia_english\wikisource_1729_primary\raw_wikitext\book_1_section_2.wikitext
sources\external\principia_english\wikisource_1729_primary\cleaned_text\book_1_section_2_clean.txt
```

---

## 7. 请编写节点提取脚本 extract_wikisource_node.py

在：

```text
sources\external\principia_english\tools\extract_wikisource_node.py
```

编写脚本，用于从已经缓存的 Section 页面中提取单个命题/引理节点。

### 7.1 当前第一目标节点

```text
node_id: book1_section2_prop01_theorem01
source_page: book_1_section_2
title_en: PROPOSITION I. THEOREM I.
title_zh: 命题1 定理1：仅受向心力作用的物体与固定力心的连线扫面积速度恒定
section: Book I, Section II
source_url: https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1729)/Book_1/Section_2
```

### 7.2 提取范围

从：

```text
PROPOSITION I. THEOREM I.
```

开始，提取到下一个主要节点开始之前。

对于样板页，本次应至少包含：

- Proposition I. Theorem I.
- 英文命题正文
- 英文证明
- Corollary 1
- Corollary 2
- Corollary 3
- Corollary 4
- Corollary 5
- Corollary 6

如果脚本难以精确判断下一个主要节点，可以先提取到：

```text
PROPOSITION II. THEOREM II.
```

之前。

### 7.3 输出文件

输出到：

```text
sources\external\principia_english\wikisource_1729_primary\extracted_nodes
```

文件名：

```text
book1_section2_prop01_theorem01_en_raw.md
book1_section2_prop01_theorem01_en_clean.md
book1_section2_prop01_theorem01_metadata.json
```

### 7.4 metadata JSON 要求

`book1_section2_prop01_theorem01_metadata.json` 至少包含：

```json
{
  "node_id": "book1_section2_prop01_theorem01",
  "work": "The Mathematical Principles of Natural Philosophy",
  "edition": "1729 Andrew Motte English translation",
  "source": "Wikisource",
  "source_priority": "primary",
  "source_url": "https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1729)/Book_1/Section_2",
  "source_page_slug": "book_1_section_2",
  "book": "Book I",
  "section": "Section II",
  "section_title": "Of the invention of centripetal forces",
  "node_type": "proposition_theorem",
  "node_number": "Proposition I. Theorem I.",
  "title_en": "The areas, which revolving bodies describe by radii drawn to an immovable centre of force, do lie in the same immovable planes, and are proportional to the times in which they are described.",
  "title_zh": "仅受向心力作用的物体与固定力心的连线扫面积速度恒定",
  "contains": [
    "proposition",
    "proof",
    "corollary_1",
    "corollary_2",
    "corollary_3",
    "corollary_4",
    "corollary_5",
    "corollary_6"
  ],
  "extraction_status": "auto_extracted_pending_manual_review",
  "manual_review_status": "not_reviewed",
  "created_at": "",
  "updated_at": "",
  "notes": "Extracted from Wikisource 1729. Must be manually compared with page scan before final public release."
}
```

时间字段由脚本自动写入 ISO 格式。

---

## 8. 请编写验证脚本 validate_extracted_node.py

在：

```text
sources\external\principia_english\tools\validate_extracted_node.py
```

功能：

1. 检查 `book1_section2_prop01_theorem01_en_clean.md` 是否存在。
2. 检查是否包含以下关键词：
   - `PROPOSITION I. THEOREM I.`
   - `Cor. 1`
   - `Cor. 2`
   - `Cor. 3`
   - `Cor. 4`
   - `Cor. 5`
   - `Cor. 6`
   - `PROPOSITION II. THEOREM II.` 不应出现在最终 clean 文件中。
3. 输出验证报告：
   ```text
   sources\external\principia_english\wikisource_1729_primary\logs\validation_report.md
   ```
4. 如果提取结果包含 Proposition II，则标记为失败。
5. 如果缺少任意 Corollary，则标记为需要人工检查。

---

## 9. 请建立 README 文件

### 9.1 总 README

在：

```text
sources\external\principia_english\README.md
```

说明：

- 本目录用途。
- 当前主数据源。
- 备选数据源。
- 本地扫描资源的角色。
- 如何抓取页面。
- 如何提取节点。
- 如何验证节点。
- 后续如何扩展到其他命题和引理。

### 9.2 Wikisource 1729 README

在：

```text
sources\external\principia_english\wikisource_1729_primary\README.md
```

说明：

- Wikisource 1729 是主源。
- 当前已经缓存哪些页面。
- 当前已经提取哪些节点。
- 哪些节点已人工校对，哪些未校对。
- 后续命题切分规则。

### 9.3 scan backup README

在：

```text
sources\external\principia_english\motte_1729_scan_backup\README.md
```

说明：

- 本地 1729 扫描资源不删除。
- 当前扫描资源在 `E:\Download\...`。
- 仅用于历史底本核查。
- 不作为主提取流程。
- 如需校对，应记录具体扫描页码和文件名。

---

## 10. 请更新项目状态文件

如果项目已有：

```text
docs\project_status.md
docs\planning\project_status.md
PROJECT_STATUS.md
```

请选择项目当前实际使用的状态文件进行更新。若不存在，请新建：

```text
E:\Codex\Newton_course\PROJECT_STATUS.md
```

追加如下内容：

```markdown
## 英文原文数据源策略调整

日期：自动填写当前日期

### 决策

英文原文主数据源由本地 OCR/扫描资源调整为 Wikisource 1729 Andrew Motte 版。

主源：
https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1729)

样板页节点源：
https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1729)/Book_1/Section_2

### 原因

1. Wikisource 1729 已经按章节结构化。
2. 与项目既定的 Motte 1729 英文底本一致。
3. 比自行维护 OCR 资源库更高效、更稳定。
4. 有利于后续批量提取命题、引理、推论。
5. 本地扫描资源继续作为底本校核源。

### 当前任务

- [ ] 建立 `sources\external\principia_english`
- [ ] 缓存 Wikisource 1729 Book I Section II 页面
- [ ] 提取 `book1_section2_prop01_theorem01`
- [ ] 生成 metadata
- [ ] 完成自动验证
- [ ] 进入命题1样板页制作阶段
```

---

## 11. 请不要做的事情

本次任务禁止：

1. 不要删除已经下载的 1729 扫描资源。
2. 不要继续大规模复制 JP2、PDF、OCR 到项目内，除非用户明确要求。
3. 不要把 1846 版当成主源。
4. 不要把 Project Gutenberg 单页 HTML 当成主源。
5. 不要直接修改最终网页样板页。
6. 不要改动导师中文译文和现代解释稿。
7. 不要在没有 metadata 的情况下输出英文原文节点。
8. 不要让提取脚本只适配一个页面，必须考虑后续可扩展到其他 Section。
9. 不要在未缓存网页的情况下每次重复联网抓取。
10. 不要过于频繁请求 Wikisource。抓取脚本应支持 sleep 和本地缓存。

---

## 12. 本次任务完成后的验收标准

完成后，项目中至少应出现以下文件：

```text
sources\external\principia_english\README.md
sources\external\principia_english\source_strategy.md
sources\external\principia_english\urls.json
sources\external\principia_english\manifest.json

sources\external\principia_english\wikisource_1729_primary\raw_html\book_1_section_2.html
sources\external\principia_english\wikisource_1729_primary\raw_wikitext\book_1_section_2.wikitext
sources\external\principia_english\wikisource_1729_primary\cleaned_text\book_1_section_2_clean.txt

sources\external\principia_english\wikisource_1729_primary\extracted_nodes\book1_section2_prop01_theorem01_en_raw.md
sources\external\principia_english\wikisource_1729_primary\extracted_nodes\book1_section2_prop01_theorem01_en_clean.md
sources\external\principia_english\wikisource_1729_primary\extracted_nodes\book1_section2_prop01_theorem01_metadata.json

sources\external\principia_english\wikisource_1729_primary\logs\fetch_log.md
sources\external\principia_english\wikisource_1729_primary\logs\extraction_log.md
sources\external\principia_english\wikisource_1729_primary\logs\validation_report.md

sources\external\principia_english\tools\fetch_wikisource.py
sources\external\principia_english\tools\extract_wikisource_node.py
sources\external\principia_english\tools\validate_extracted_node.py
```

并且：

1. `book1_section2_prop01_theorem01_en_clean.md` 中必须包含 Proposition I 和 Corollary 1–6。
2. `book1_section2_prop01_theorem01_en_clean.md` 中不应包含 Proposition II。
3. metadata 中必须记录 source URL 和 extraction status。
4. PROJECT_STATUS.md 必须更新。
5. README 中必须说明 1729 Wikisource 为主源，1846 和 Gutenberg 为备源，本地扫描为校核源。

---

## 13. 完成后请输出总结

任务完成后，请在 Codex 回复中输出：

1. 实际创建或修改了哪些目录。
2. 实际创建或修改了哪些文件。
3. 是否成功抓取 Wikisource 1729 Section II。
4. 是否成功提取 Proposition I Theorem I。
5. 是否通过验证脚本。
6. 是否存在需要人工检查的问题。
7. 下一步是否可以进入“命题1 定理1样板页制作”。

---

## 14. 后续下一步

本任务完成并通过验收后，下一步任务才是：

```text
基于 book1_section2_prop01_theorem01 英文原文节点，
结合导师中文译文和现代解释，
制作“命题1 定理1：扫面积速度恒定”标准样板页。
```

样板页必须包括：

- 统一页面布局
- 统一标题格式
- 英文原文区
- 导师中文译文区
- 现代解释区
- 图示与动态演示区
- 思考题区
- 评论/互动区占位
- 命题依赖网络区
- 视觉风格与主题配置
- 署名和版权说明
- 页面元数据结构

本次任务只完成英文原文数据源重构，不进入样板页正式制作。
