# 2026-05-31 Motte 1729 Sample Page Readiness Audit

## 结论

当前英文原始资料已经具备制作“命题1 定理1：扫面积速度恒定”样板页的基本条件。无需继续手动寻找或下载英文底本资源。

## 核心资源检查

- 关键资源检查：24/24 存在。
- 两卷用户提供清晰版 PDF：存在。
- 两卷 Internet Archive 归档 PDF：存在。
- 两卷 DJVU 文本、DJVU XML、HOCR、HOCR 页索引和搜索文本：存在。
- 两卷 `page_numbers.json`、`scandata.xml` 和人工校对文件：存在。
- 两卷 Internet Archive `meta.xml` 和 `files.xml`：存在。

## 非阻塞缺失项

- `ocr/vol_1/abbyy.gz`
- `ocr/vol_2/abbyy.gz`

这两个文件是独立的 ABBYY OCR XML 压缩派生文件，不是 `hocr_pageindex.json.gz` 或 `hocr_searchtext.txt.gz`。已有 DJVU、HOCR 和页码映射，故不影响样板页建设。

## 样板页定位结果

Vol.1 的样板页英文正文已经在 Internet Archive OCR 中定位：

- Book I, Section II
- Proposition I, Theorem I
- IA scan leaf：`102-103`
- IA archive PDF 页码（1-based）：`103-104`
- 1729 版印刷页码：`57-58`

OCR 标题存在损坏：

```text
PROPHOSTLITION I. TRHEOREMu J.
```

正文可识别到：

```text
The areas, which revolving bodies describe ...
```

因此 OCR 只能作为 raw 工作底本，最终英文展示文本必须对照清晰扫描页人工校核。

## 清晰版 PDF 映射要求

- Vol.1 清晰版 PDF：408 页。
- Vol.1 Internet Archive PDF：414 页。
- Vol.2 清晰版 PDF：267 页。
- Vol.2 Internet Archive PDF：543 页。

两套 PDF 页数不同，不能假设固定页偏移。样板页制作前，需要人工确认 Vol.1 清晰版 PDF 中对应 Proposition I, Theorem I 的实际页码，并写回：

```text
sources/external/motte_1729/page_maps/vol_1/page_map_manual_review.json
```

## 下一步

1. 在 Vol.1 `raw_pdf/` 清晰版中人工定位 Proposition I, Theorem I。
2. 回填清晰版 PDF 页码。
3. 提取英文原文 raw 文本。
4. 对照清晰扫描页清洗为 clean 文本。
5. 接入样板页内容节点。
