# PROJECT_STATUS

## Principia 英文原文资源整理状态

状态：已完成

更新时间：2026-05-31 15:03

### 已完成

- 已接收卷一、卷二 Internet Archive 下载资源。
- 已整理 PDF、OCR、HOCR、页码映射、元数据和派生文件。
- 已生成 `MANIFEST_motte_1729.md`、`MANIFEST_motte_1729.json` 和校验报告。
- 已运行 OCR 轻量检查，10 个检查项全部存在。
- 两个 JP2 大包已使用硬链接，避免重复复制约 3.48GB 数据。
- 已重复运行整理脚本，45 条记录全部识别为已有文件，没有产生冲突副本。
- 已完成 PDF 对齐评估：`vol_*/pdf/motte_1729_vol*.pdf` 与 IA OCR 体系逐页匹配，后续页码映射、OCR 对照、英文切片和引用核验使用该版本。
- 已生成 `logs/pdf_source_alignment_report.md` 和 JSON 报告。
- 已完成样板页英文资源就绪审计：关键资源 24/24 存在，无需额外下载英文底本。
- 已定位样板页 IA 入口：Vol.1 leaf `102-103`，IA PDF 第 `103-104` 页，印刷页 `57-58`。
- 已建立 `sources/external/principia_english/`，将 Wikisource 1729 固化为日常英文提取主源。
- 已将 Wikisource 1846 和 Project Gutenberg 1846 固化为备份来源，将 `motte_1729/` 固化为扫描底本校核库。
- 已缓存 Wikisource 1729 Book I Section II。
- 已提取 `book1_section2_prop01_theorem01` raw、clean 和 metadata。
- 自动验证通过：Cor. 1-6 完整，未越界到 Proposition II。

### 当前问题

- 两卷下载资源中均未提供 `abbyy.gz`。它们是独立 ABBYY OCR XML 派生文件，不是现有两个 HOCR 压缩包；已有 DJVU 和 HOCR，故不阻塞后续工作。
- 页码映射尚未人工校对。
- 清晰版 Vol.1 PDF 与 IA PDF 页数不同，需人工确认样板页在 `raw_pdf/` 中的实际页码。
- 命题1定理1节点已自动提取，但尚未对照 IA 1729 扫描页人工校核。
- `vol_*/raw_pdf/` 是重新排版参考版，不是 1729 扫描页的高清替代件，仅用于辅助阅读。

### 下一步

- 对照 IA 1729 扫描页人工校核 Wikisource 节点。
- 人工校对 Vol.1 page map，并回填参考版 PDF 实际页码。
- 校核完成后制作命题1定理1样板页。

项目总状态另见根目录 `PROJECT_STATUS.md`。
