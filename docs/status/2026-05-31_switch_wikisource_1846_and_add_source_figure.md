# 英文数字主源切换与原版插图接入

## 决策

- 日常英文文本提取、节点切片和原版插图定位改用 Wikisource 1846 数字页面。
- 页面可见引用继续保留 Andrew Motte 1729 英译本归属。
- Wikisource 1729 缓存保留为比对记录；IA 1729 扫描库继续承担公开发布前底本校核。

## 样板页改动

- 核心定理句独立加粗斜体展示。
- 英文证明开头由错误提取的 `OR suppose` 修正为 `For suppose`。
- 原版图 `Principia1846-105.png` 下载到 `assets/images/primary_sources/book1_chapter02/`，并同步到 Web 发布目录。
- 插图在第一段证明后进入正文，桌面端右浮动，窄屏整行显示。

## 主源缓存

- 页面：`https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1846)/BookI-II`
- HTML：`sources/external/principia_english/wikisource_1846_primary/raw_html/book_i_section_ii.html`
- Wikitext：`sources/external/principia_english/wikisource_1846_primary/raw_wikitext/book_i_section_ii.wikitext`
- Clean text：`sources/external/principia_english/wikisource_1846_primary/cleaned_text/book_i_section_ii_clean.txt`
- 节点：`sources/external/principia_english/wikisource_1846_primary/extracted_nodes/book1_section2_prop01_theorem01_en_clean.md`

## 验证

- 1846 页面抓取：通过。
- Proposition I / Theorem I 自动提取：通过。
- Cor. 1-6 完整且未越界到 Proposition II：通过。
- Astro 静态构建：通过。
- IA 1729 扫描人工校核：仍待完成。
