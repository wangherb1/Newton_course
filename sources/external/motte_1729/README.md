# Andrew Motte 1729 English Translation Resources

本目录保存 Andrew Motte 1729 年英文译本两卷本的 Internet Archive 外部资源，用于英文原文底本校核、页码映射、疑难段落核查和扫描图像检查。

后续日常英文提取主工作流已经迁移到 `../principia_english/`，数字主源为 Wikisource 1846 页面；英文译文归属仍为 Andrew Motte 1729 英译本。本目录保留为历史扫描校核库，不删除、不重复大规模复制，也不再作为常规节点抽取入口。

## 来源

- 卷一下载目录：`E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_1`
- 卷二下载目录：`E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_2`

下载目录中的原始文件不得删除、移动、覆盖或重命名。项目内资源由 `tools/organize_motte_1729.ps1` 复制、硬链接或记录为外部指针。

## 资源类型

- `vol_1/pdf/`、`vol_2/pdf/`：Internet Archive 下载得到的 1729 扫描 PDF。它们与 OCR、HOCR、页码 JSON 和 scandata XML 逐页匹配，是页码映射、OCR 对照、英文切片和引用核验的默认底本。
- `vol_1/raw_pdf/`、`vol_2/raw_pdf/`：用户提供的重新排版参考版 PDF。Vol.1 封面显示为高等教育出版社 2016 版，并标明 Florian Cajori 修订与历史说明。仅用于辅助阅读，不作为 1729 页码或英文节点底本。
- `vol_1/archive_raw/`、`vol_2/archive_raw/`：Internet Archive 元数据和原始文件清单。
- `vol_1/derivatives/`、`vol_2/derivatives/`：EPUB、torrent 和其他派生文件。
- `vol_1/large_assets/`、`vol_2/large_assets/`：JP2 高分辨率图像包和必要时的外部路径指针。
- `ocr/vol_1/`、`ocr/vol_2/`：DJVU 文本、DJVU XML、HOCR 和相关 OCR 派生文件。
- `page_maps/vol_1/`、`page_maps/vol_2/`：Internet Archive 页码数据、扫描数据和人工校对占位。
- `extracted_nodes/`：后续人工核验后的命题切片。本次整理任务不生成节点内容。
- `logs/`：整理日志、校验报告、缺失项报告和 OCR 检查报告。

## 后续使用原则

1. 日常英文原文抽取优先使用 `../principia_english/wikisource_1846_primary/`。
2. 本目录 OCR 仅用于扫描底本核查、疑难段落比对和页码映射，不再作为默认提取来源。
3. 不要默认对 PDF 反复执行 OCR。需要扫描原件校对或补充识别时，使用与 IA OCR 逐页匹配的 `vol_*/pdf/motte_1729_vol*.pdf`。
4. OCR 可能包含长 s、旧式拼写、断行、页眉页脚混入等问题，页面展示前必须对照扫描页人工校核。
5. 页码映射必须在 `page_maps/vol_*/page_map_manual_review.json` 中人工审核。
6. 后续公开使用的英文节点统一放入 `../principia_english/wikisource_1846_primary/extracted_nodes/`，并记录本目录中实际核对过的扫描页。

PDF 选择规则另见 `PDF_SOURCE_PRIORITY.md` 和 `pdf_source_priority.json`。

PDF 对齐评估另见 `logs/pdf_source_alignment_report.md`。

## 版权初步判断

Andrew Motte 1729 年英文文本属于历史文本，可按公共领域文本处理；但 Internet Archive 扫描件和数字化资源仍需保留具体来源说明。不得将现代修订本、Cajori 版本或其他现代文本混入本目录。

## 大文件策略

超过 500MB 的 JP2 压缩包优先建立硬链接，避免重复占用磁盘空间。硬链接失败时，整理脚本会在 `large_assets/pointers/` 中创建 `.txt` 指针文件，不强行复制。

硬链接与下载目录中的原始文件共享同一份数据。项目内 JP2 压缩包只允许只读使用，不要编辑或覆盖；如需更新资源，应重新下载并按整理脚本重新归档。

## 清单

- 人工可读清单：`MANIFEST_motte_1729.md`
- 机器可读清单：`MANIFEST_motte_1729.json`
- 校验报告：`logs/checksum_report.csv`
- OCR 检查：`logs/ocr_inspection_report.md`
