# 2026-05-31 PDF Source Alignment

## 任务目标

评估 Internet Archive 下载 PDF 与用户提供 PDF 的页序、OCR 和 page map 对齐关系，确定后续英文节点抽取的默认底本。

## 结论

后续页码映射、OCR 对照、英文节点切片、引用核验和必要时的补充 OCR，统一使用：

```text
sources/external/motte_1729/vol_1/pdf/motte_1729_vol1.pdf
sources/external/motte_1729/vol_2/pdf/motte_1729_vol2.pdf
```

`vol_*/raw_pdf/` 中用户提供的 PDF 是重新排版参考版，不是 IA 1729 扫描页的高清替代件，仅用于辅助阅读。

## 证据

| Volume | IA PDF pages | User PDF pages | page_numbers | scandata | DJVU XML | HOCR page index | IA image dimensions matching scandata |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 414 | 408 | 414 | 414 | 414 | 414 | 414/414 |
| 2 | 543 | 267 | 543 | 543 | 543 | 543 | 543/543 |

## 视觉核验

- 用户提供 Vol.1 PDF 封面显示为高等教育出版社 2016 版。
- 封面标明翻译经过修订，并包含 Florian Cajori 的历史与说明附录。
- 用户提供版本为重新排版版式，不是 IA 1729 原始扫描页。

## 产物

- `sources/external/motte_1729/PDF_SOURCE_PRIORITY.md`
- `sources/external/motte_1729/pdf_source_priority.json`
- `sources/external/motte_1729/logs/pdf_source_alignment_report.md`
- `sources/external/motte_1729/logs/pdf_source_alignment_report.json`
- `sources/external/motte_1729/tools/assess_pdf_alignment.py`
