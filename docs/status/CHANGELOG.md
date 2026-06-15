# CHANGELOG

## 2026-05-31 13:54 Motte 1729 资源整理

- 整理两卷 Internet Archive 下载目录。
- 生成 45 条 manifest 记录。
- 核心 PDF、DJVU、HOCR、page numbers 和 scandata 完整。
- 两个 JP2 大包使用硬链接。
- 记录缺失的 `ocr/vol_1/abbyy.gz` 和 `ocr/vol_2/abbyy.gz`。
- 新增可重复运行整理脚本和 OCR 检查脚本。
- 完成 PDF 对齐评估并修正来源优先级：`vol_*/pdf/motte_1729_vol*.pdf` 与 IA OCR、HOCR、page map 和 scandata 逐页匹配，设为默认底本；`vol_*/raw_pdf/` 为重新排版参考版，仅用于辅助阅读。
- 完成样板页英文资源就绪审计：关键资源 24/24 存在，无需额外下载；定位 Vol.1 IA leaf `102-103`、印刷页 `57-58`。

## 2026-05-31 15:03 Wikisource 1729 英文主源工作流

- 建立 `sources/external/principia_english/` 统一入口。
- 将 Wikisource 1729 Andrew Motte 版设为日常英文提取主源。
- 将 Wikisource 1846、Project Gutenberg 1846 设为备用来源。
- 将 `motte_1729/` 调整为扫描底本校核库。
- 新增通用抓取、提取、验证脚本。
- 缓存 Book I Section II，提取 `book1_section2_prop01_theorem01`，并通过自动验证。
