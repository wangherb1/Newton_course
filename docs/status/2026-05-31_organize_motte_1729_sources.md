# 2026-05-31 Organize Motte 1729 Sources

## 任务目标

按 `docs/codex_prompts/03_organize_motte_1729_sources.md` 整理 Andrew Motte 1729 两卷 Internet Archive 资源，不制作样板页，不切片命题正文。

## 执行结果

- 下载目录仍完整保留：Vol.1 共 23 个文件，Vol.2 共 22 个文件。
- 生成 45 条 manifest 记录。
- 核心 PDF、DJVU、HOCR、page numbers 和 scandata 均存在。
- 两个 JP2 大包采用硬链接：Vol.1 为 1,483,125,258 bytes，Vol.2 为 2,004,175,245 bytes。
- 下载资源未提供两卷 `abbyy.gz`，已写入缺失项报告。
- OCR 检查完成：Vol.1 文本 528,160 字符，Vol.2 文本 813,302 字符。
- Vol.1 关键词命中：`PROPOSITION I` 1 次、`THEOREM I` 1 次、`centripetal` 134 次、`equal areas` 2 次。
- 整理脚本已重复运行验证，未产生 `_candidate_` 冲突文件。
- 已完成 PDF 对齐评估并修正来源优先级：后续页码映射、OCR 对照、英文切片、引用核验和补充 OCR 使用 `vol_*/pdf/motte_1729_vol*.pdf`；`vol_*/raw_pdf/` 为重新排版辅助阅读参考。
- `abbyy.gz` 与现有 HOCR 压缩包不是同一种派生文件；其缺失不阻塞后续工作。

## PDF 对齐评估

- Vol.1：IA PDF、page numbers、scandata、DJVU XML 和 HOCR 页索引均为 414 页；IA PDF 图像尺寸与 scandata 414/414 精确匹配。用户提供参考版为 408 页。
- Vol.2：IA PDF、page numbers、scandata、DJVU XML 和 HOCR 页索引均为 543 页；IA PDF 图像尺寸与 scandata 543/543 精确匹配。用户提供参考版为 267 页。
- 用户提供参考版标题页显示为重新排版版本，Vol.1 封面标明高等教育出版社 2016 版和 Florian Cajori 修订说明。

## 主要产物

- `sources/external/motte_1729/MANIFEST_motte_1729.md`
- `sources/external/motte_1729/MANIFEST_motte_1729.json`
- `sources/external/motte_1729/logs/checksum_report.csv`
- `sources/external/motte_1729/logs/missing_files_report.md`
- `sources/external/motte_1729/logs/ocr_inspection_report.md`
- `sources/external/motte_1729/tools/organize_motte_1729.ps1`
- `sources/external/motte_1729/tools/inspect_motte_ocr.py`

## 下一步

人工校对 Vol.1 page map，定位并切片 Book I, Section II, Proposition I, Theorem I。
