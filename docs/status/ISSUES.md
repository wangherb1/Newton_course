# ISSUES

## Motte 1729 资源风险

- OCR 可能存在长 s、旧式拼写、断行、页眉页脚混入等问题。
- Internet Archive OCR 与扫描页码之间可能不完全对应。
- 1729 版 Motte 文本与 1846 版、Gutenberg 文本可能存在差异。
- 不应将现代修订本误作为 1729 原始底本。
- 大文件不要重复复制，避免项目体积失控。
- 两卷下载资源中均未提供 `abbyy.gz`。它们是独立 ABBYY OCR XML 派生文件，不是 `hocr_pageindex.json.gz` 或 `hocr_searchtext.txt.gz`；后续优先使用已存在的 DJVU 和 HOCR。
- `vol_*/raw_pdf/` 中用户提供的 PDF 是重新排版参考版，不是 IA 1729 扫描页的高清替代件。Vol.1 封面显示为高等教育出版社 2016 版，并标明 Florian Cajori 修订与历史说明。不得将其页码或修订内容混入 1729 节点底本。
- 页码映射、OCR 对照、英文切片、引用核验和必要时的补充 OCR 必须使用逐页匹配 IA OCR 的 `vol_*/pdf/motte_1729_vol*.pdf`。
