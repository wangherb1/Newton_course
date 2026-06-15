# Codex 输入指令 03：整理 Andrew Motte 1729 英文原文资源并完善 `motte_1729` 目录框架

版本：v0.1  
项目路径：`E:\Codex\Newton_course`  
目标目录：`E:\Codex\Newton_course\sources\external\motte_1729`  
任务类型：本地文件整理、资源归档、元数据清单建立、项目状态更新  
执行环境：Windows，本地 Codex，可使用 PowerShell / Python 脚本

---

## 一、任务背景

本项目是“牛顿《自然哲学的数学原理》现代精读 / 开放教材网站”建设项目。网站核心内容将以廖日东老师提供的中文学术翻译和现代微积分解释为主体，同时需要接入 Andrew Motte 1729 年英文译本作为英文原文底本。

目前项目已经在以下路径建立基本框架：

```text
E:\Codex\Newton_course
```

英文原文资源已经从 Internet Archive 下载完成，并分别解压到：

```text
E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_1
E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_2
```

上述两个目录中包含网页端可下载的全部资源，例如 PDF、FULL TEXT、DJVU XML、HOCR、page numbers JSON、scandata、metadata、JP2 zip、EPUB、torrent 等。

现在需要你将这些资源**安全、规范、可追溯地整理到项目目录**：

```text
E:\Codex\Newton_course\sources\external\motte_1729
```

本任务只做资源整理和框架完善，**不要开始制作样板页，不要提取命题1，不要修改课程正文内容**。

---

## 二、核心原则

### 1. 绝对不要删除原始下载目录

不要删除、移动、覆盖以下目录中的任何原始文件：

```text
E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_1
E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_2
```

优先采用“复制”或“硬链接”的方式整理到项目目录。

### 2. 不要无脑复制超大文件

Internet Archive 资源中可能包含 `*_jp2.zip` 等超大图片包，体积可能超过 1GB。对于这类大文件：

- 优先尝试在同一磁盘分区内建立硬链接；
- 如果硬链接失败，不要强行复制；
- 改为在目标目录中创建 `.external_path.txt` 指针文件，记录原始文件路径、大小和用途；
- 不要因为复制超大文件导致磁盘空间快速耗尽。

### 3. 所有整理动作必须可追溯

你必须生成资源清单、整理日志、缺失项检查表和项目状态更新文件。

必须新增或更新：

```text
E:\Codex\Newton_course\sources\external\motte_1729\README.md
E:\Codex\Newton_course\sources\external\motte_1729\MANIFEST_motte_1729.md
E:\Codex\Newton_course\sources\external\motte_1729\MANIFEST_motte_1729.json
E:\Codex\Newton_course\sources\external\motte_1729\logs\organize_motte_1729_log.md
E:\Codex\Newton_course\docs\status\PROJECT_STATUS.md
E:\Codex\Newton_course\docs\status\CHANGELOG.md
E:\Codex\Newton_course\docs\status\TODO.md
E:\Codex\Newton_course\docs\status\ISSUES.md
```

如果这些状态文件尚不存在，请创建；如果已经存在，请追加更新，不要覆盖已有内容。

### 4. 文件命名要建立“规范名”和“原始名”的双重关系

目标目录中核心资源可采用规范名，便于后续脚本调用，例如：

```text
motte_1729_vol1.pdf
motte_1729_vol2.pdf
djvu.txt
djvu.xml
hocr.html
page_numbers.json
scandata.xml
```

但必须在 manifest 中记录对应的 Internet Archive 原始文件名，确保未来能够追溯来源。

### 5. 本任务完成后，Codex 后续应优先读取 OCR 文本，而不是重新 OCR PDF

后续英文原文抽取工作应优先使用：

```text
sources\external\motte_1729\ocr\vol_1\djvu.txt
sources\external\motte_1729\ocr\vol_1\djvu.xml
sources\external\motte_1729\ocr\vol_1\hocr.html
sources\external\motte_1729\page_maps\vol_1\page_numbers.json
sources\external\motte_1729\page_maps\vol_1\scandata.xml
```

不要在后续默认反复对 PDF 执行 OCR。PDF 只作为扫描原件校对依据。

---

## 三、输入路径

### 卷一原始下载目录

```text
E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_1
```

### 卷二原始下载目录

```text
E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_2
```

### 项目目标目录

```text
E:\Codex\Newton_course\sources\external\motte_1729
```

---

## 四、目标目录结构

请将 `motte_1729` 目录整理成如下结构。若目录已存在，请补齐缺失部分，不要破坏已有文件。

```text
E:\Codex\Newton_course\sources\external\motte_1729
│
├─ README.md
├─ MANIFEST_motte_1729.md
├─ MANIFEST_motte_1729.json
│
├─ vol_1
│  ├─ pdf
│  │  └─ motte_1729_vol1.pdf
│  ├─ archive_raw
│  │  ├─ original_file_list.txt
│  │  ├─ archive_metadata_source.txt
│  │  ├─ *_meta.xml
│  │  ├─ *_files.xml
│  │  └─ README.md
│  ├─ derivatives
│  │  ├─ epub
│  │  ├─ kindle
│  │  ├─ torrent
│  │  └─ other
│  └─ large_assets
│     ├─ jp2
│     └─ pointers
│
├─ vol_2
│  ├─ pdf
│  │  └─ motte_1729_vol2.pdf
│  ├─ archive_raw
│  │  ├─ original_file_list.txt
│  │  ├─ archive_metadata_source.txt
│  │  ├─ *_meta.xml
│  │  ├─ *_files.xml
│  │  └─ README.md
│  ├─ derivatives
│  │  ├─ epub
│  │  ├─ kindle
│  │  ├─ torrent
│  │  └─ other
│  └─ large_assets
│     ├─ jp2
│     └─ pointers
│
├─ ocr
│  ├─ vol_1
│  │  ├─ djvu.txt
│  │  ├─ djvu.xml
│  │  ├─ hocr.html
│  │  ├─ hocr_pageindex.json.gz
│  │  ├─ hocr_searchtext.txt.gz
│  │  ├─ abbyy.gz
│  │  ├─ original_names.json
│  │  └─ README.md
│  └─ vol_2
│     ├─ djvu.txt
│     ├─ djvu.xml
│     ├─ hocr.html
│     ├─ hocr_pageindex.json.gz
│     ├─ hocr_searchtext.txt.gz
│     ├─ abbyy.gz
│     ├─ original_names.json
│     └─ README.md
│
├─ page_maps
│  ├─ vol_1
│  │  ├─ page_numbers.json
│  │  ├─ scandata.xml
│  │  ├─ page_map_manual_review.json
│  │  └─ README.md
│  └─ vol_2
│     ├─ page_numbers.json
│     ├─ scandata.xml
│     ├─ page_map_manual_review.json
│     └─ README.md
│
├─ extracted_nodes
│  ├─ vol_1
│  │  └─ README.md
│  └─ vol_2
│     └─ README.md
│
├─ tools
│  ├─ organize_motte_1729.ps1
│  ├─ inspect_motte_ocr.py
│  └─ README.md
│
└─ logs
   ├─ organize_motte_1729_log.md
   ├─ missing_files_report.md
   └─ checksum_report.csv
```

---

## 五、文件分类规则

请先扫描两个原始下载目录，列出全部文件名、大小、扩展名、相对路径，再按以下规则归档。

### 1. PDF 扫描件

匹配：

```text
*_1729_1.pdf
*_1729_2.pdf
```

目标：

```text
vol_1\pdf\motte_1729_vol1.pdf
vol_2\pdf\motte_1729_vol2.pdf
```

注意：如果目标 PDF 已存在，先比较大小和哈希。相同则跳过，不同则不要覆盖，改名为：

```text
motte_1729_vol1_candidate_YYYYMMDD_HHMMSS.pdf
motte_1729_vol2_candidate_YYYYMMDD_HHMMSS.pdf
```

并在日志中说明。

### 2. OCR 文本与结构文件

匹配：

```text
*_djvu.txt
*_djvu.xml
*_hocr.html
*_hocr_pageindex.json.gz
*_hocr_searchtext.txt.gz
*_abbyy.gz
```

目标：

```text
ocr\vol_1\
ocr\vol_2\
```

规范名：

```text
djvu.txt
djvu.xml
hocr.html
hocr_pageindex.json.gz
hocr_searchtext.txt.gz
abbyy.gz
```

同时生成：

```text
ocr\vol_1\original_names.json
ocr\vol_2\original_names.json
```

记录规范名与原始文件名之间的映射。

### 3. 页码映射与扫描数据

匹配：

```text
*_page_numbers.json
*_scandata.xml
```

目标：

```text
page_maps\vol_1\page_numbers.json
page_maps\vol_1\scandata.xml
page_maps\vol_2\page_numbers.json
page_maps\vol_2\scandata.xml
```

并生成初始人工校对文件：

```text
page_maps\vol_1\page_map_manual_review.json
page_maps\vol_2\page_map_manual_review.json
```

初始内容建议：

```json
{
  "volume": 1,
  "status": "not_reviewed",
  "source_files": {
    "page_numbers": "page_numbers.json",
    "scandata": "scandata.xml"
  },
  "notes": [
    "This file is reserved for manual mapping between scan page index, printed page number, and Principia nodes.",
    "Do not rely only on OCR page numbering before manual review."
  ],
  "review_items": []
}
```

卷二同理，`volume` 改为 2。

### 4. Internet Archive 元数据

匹配：

```text
*_meta.xml
*_files.xml
*_archive.torrent
*_meta.sqlite
```

其中：

`*_meta.xml` 和 `*_files.xml` 放入：

```text
vol_1\archive_raw\
vol_2\archive_raw\
```

`torrent` 放入：

```text
vol_1\derivatives\torrent\
vol_2\derivatives\torrent\
```

`meta.sqlite` 如果存在，放入：

```text
vol_1\archive_raw\
vol_2\archive_raw\
```

### 5. EPUB / Kindle / 其他派生格式

匹配：

```text
*.epub
*.mobi
*.azw3
*.pdf_meta.xml
*.sqlite
```

按类型放入：

```text
vol_1\derivatives\epub\
vol_1\derivatives\kindle\
vol_1\derivatives\other\
vol_2\derivatives\epub\
vol_2\derivatives\kindle\
vol_2\derivatives\other\
```

### 6. JP2 / 高分辨率图像包 / 超大资源

匹配：

```text
*_jp2.zip
*.zip
```

如果文件大小大于 500MB：

1. 第一选择：尝试建立硬链接到：

```text
vol_1\large_assets\jp2\
vol_2\large_assets\jp2\
```

2. 第二选择：如果硬链接失败，创建指针文件：

```text
vol_1\large_assets\pointers\jp2_zip_external_path.txt
vol_2\large_assets\pointers\jp2_zip_external_path.txt
```

指针文件至少包含：

```text
original_path:
file_name:
file_size_bytes:
reason:
suggested_usage:
```

如果文件小于 500MB，可以复制到 `large_assets\jp2\` 或 `derivatives\other\`，但仍需在 manifest 中登记。

### 7. 无法识别的文件

无法归类的文件不要丢弃，放入：

```text
vol_1\derivatives\other\
vol_2\derivatives\other\
```

并在：

```text
logs\missing_files_report.md
```

中记录。

---

## 六、需要生成的工具脚本

请在以下目录创建脚本：

```text
E:\Codex\Newton_course\sources\external\motte_1729\tools
```

### 1. `organize_motte_1729.ps1`

这个脚本应完成资源整理工作。要求：

1. 支持参数：

```powershell
-SourceVol1 "E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_1"
-SourceVol2 "E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_2"
-TargetRoot "E:\Codex\Newton_course\sources\external\motte_1729"
-Mode "Copy"
-LargeFilePolicy "HardLinkOrPointer"
```

2. 默认不删除源文件。
3. 执行前打印计划，执行后生成日志。
4. 文件已存在时要判断哈希，不要直接覆盖。
5. 大文件优先硬链接，否则生成指针。
6. 生成 `MANIFEST_motte_1729.json` 和 `MANIFEST_motte_1729.md`。
7. 生成 `checksum_report.csv`，至少包含：

```text
volume,category,canonical_path,original_path,file_size_bytes,sha256,action
```

8. 可重复运行。重复运行时不应造成重复文件泛滥。

### 2. `inspect_motte_ocr.py`

这个脚本暂时只做轻量检查，不做命题抽取。要求：

1. 检查以下文件是否存在：

```text
ocr\vol_1\djvu.txt
ocr\vol_1\djvu.xml
ocr\vol_1\hocr.html
page_maps\vol_1\page_numbers.json
page_maps\vol_1\scandata.xml
ocr\vol_2\djvu.txt
ocr\vol_2\djvu.xml
ocr\vol_2\hocr.html
page_maps\vol_2\page_numbers.json
page_maps\vol_2\scandata.xml
```

2. 输出每个 OCR 文本的字符数、行数、文件大小。

3. 在 `ocr\vol_1\djvu.txt` 中尝试搜索以下关键词并记录命中情况：

```text
PROPOSITION I
THEOREM I
centripetal
equal areas
```

4. 仅生成检查报告，不要修改 OCR 内容。

输出报告：

```text
logs\ocr_inspection_report.md
```

---

## 七、README 与 MANIFEST 内容要求

### 1. `README.md`

请在 `motte_1729\README.md` 中说明：

1. 本目录用途：保存 Andrew Motte 1729 年英文译本相关外部资源；
2. 卷一和卷二来源路径；
3. 资源类型说明；
4. 后续使用原则：优先读取 OCR，不反复 OCR PDF；
5. 英文原文版权初步判断：1729 年文本属于公共领域，但扫描文件来源和现代数字化资源需保留来源说明；
6. 大文件处理策略；
7. 后续命题切片文件将放入 `extracted_nodes`。

### 2. `MANIFEST_motte_1729.md`

请生成适合人工阅读的资源清单。至少包含：

- 卷号；
- 资源类别；
- 规范文件路径；
- 原始文件路径；
- 文件大小；
- 是否复制 / 是否硬链接 / 是否仅记录外部路径；
- SHA256；
- 备注。

### 3. `MANIFEST_motte_1729.json`

请生成机器可读清单，建议结构：

```json
{
  "project": "Newton_course",
  "source": "Andrew Motte 1729 English translation of Newton's Principia",
  "volumes": {
    "vol_1": {
      "source_dir": "...",
      "files": [
        {
          "category": "ocr",
          "canonical_name": "djvu.txt",
          "canonical_path": "...",
          "original_name": "...",
          "original_path": "...",
          "size_bytes": 0,
          "sha256": "...",
          "action": "copied|hardlinked|pointer|skipped_existing",
          "notes": ""
        }
      ]
    },
    "vol_2": {
      "source_dir": "...",
      "files": []
    }
  }
}
```

---

## 八、项目状态文件更新要求

请更新或创建以下文件：

```text
E:\Codex\Newton_course\docs\status\PROJECT_STATUS.md
E:\Codex\Newton_course\docs\status\CHANGELOG.md
E:\Codex\Newton_course\docs\status\TODO.md
E:\Codex\Newton_course\docs\status\ISSUES.md
```

### 1. `PROJECT_STATUS.md`

追加或更新一节：

```text
## Motte 1729 英文原文资源整理状态

状态：进行中 / 已完成

已完成：
- 已接收卷一、卷二 Internet Archive 下载资源；
- 已整理 PDF、OCR、HOCR、页码映射和元数据；
- 已生成 manifest 和校验报告。

当前问题：
- 页码映射尚未人工校对；
- 命题节点尚未提取；
- 命题1定理1英文原文尚未切片。

下一步：
- 运行 OCR 检查；
- 建立卷一 page map 初版；
- 提取命题1定理1英文原文 raw / clean；
- 制作命题1定理1样板页。
```

### 2. `CHANGELOG.md`

追加一条记录，记录本次整理时间、范围和主要产物。

### 3. `TODO.md`

增加后续任务：

```text
- [ ] 人工校对 Vol.1 扫描页码与书籍页码关系
- [ ] 定位 Book I, Section II, Proposition I, Theorem I 在 Motte 1729 Vol.1 中的页码范围
- [ ] 提取 Prop.1 Theorem.1 英文原文 raw 文本
- [ ] 清洗 Prop.1 Theorem.1 英文原文 clean 文本
- [ ] 将英文原文接入样板页内容节点
```

### 4. `ISSUES.md`

记录潜在问题：

```text
- OCR 可能存在长 s、旧式拼写、断行、页眉页脚混入等问题；
- Internet Archive OCR 与扫描页码之间可能不完全对应；
- 1729 版 Motte 文本与 1846 版 / Gutenberg 文本可能存在差异；
- 不应将现代修订本误作为 1729 原始底本；
- 大文件不要重复复制，避免项目体积失控。
```

---

## 九、执行步骤建议

请按以下步骤执行，不要跳步。

### Step 1：检查目录

确认以下路径存在：

```text
E:\Codex\Newton_course
E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_1
E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_2
```

如果不存在，停止并报告。

### Step 2：扫描源目录

生成源目录文件清单：

```text
vol_1\archive_raw\original_file_list.txt
vol_2\archive_raw\original_file_list.txt
```

清单至少包含：

```text
relative_path
file_name
extension
size_bytes
last_write_time
```

### Step 3：建立目标目录结构

按第四节目标目录结构创建所有目录。

### Step 4：执行文件整理

使用分类规则复制、硬链接或生成指针文件。

### Step 5：生成校验信息

计算关键文件 SHA256。

必须计算：

```text
pdf
djvu.txt
djvu.xml
hocr.html
page_numbers.json
scandata.xml
meta.xml
files.xml
```

超大文件可只记录大小和路径；如果计算 SHA256 耗时过长，可在报告中说明未计算。

### Step 6：生成 README / MANIFEST / 日志

完成文档生成。

### Step 7：运行 OCR 检查脚本

运行：

```powershell
python .\sources\external\motte_1729\tools\inspect_motte_ocr.py
```

生成：

```text
logs\ocr_inspection_report.md
```

### Step 8：更新项目状态

更新 `docs\status` 下的四个文件。

### Step 9：输出执行总结

最后在 Codex 回复中给出：

1. 已创建/更新的目录；
2. 已整理的关键文件数量；
3. PDF、OCR、page map 是否完整；
4. 是否存在缺失文件；
5. 是否存在大文件未复制，仅生成指针；
6. 下一步建议。

---

## 十、验收标准

本任务完成后，应满足以下条件：

### 1. 目录完整

以下目录必须存在：

```text
sources\external\motte_1729\vol_1\pdf
sources\external\motte_1729\vol_2\pdf
sources\external\motte_1729\ocr\vol_1
sources\external\motte_1729\ocr\vol_2
sources\external\motte_1729\page_maps\vol_1
sources\external\motte_1729\page_maps\vol_2
sources\external\motte_1729\extracted_nodes\vol_1
sources\external\motte_1729\extracted_nodes\vol_2
sources\external\motte_1729\tools
sources\external\motte_1729\logs
```

### 2. 核心文件完整

至少应存在：

```text
vol_1\pdf\motte_1729_vol1.pdf
vol_2\pdf\motte_1729_vol2.pdf
ocr\vol_1\djvu.txt
ocr\vol_1\djvu.xml
ocr\vol_1\hocr.html
ocr\vol_2\djvu.txt
ocr\vol_2\djvu.xml
ocr\vol_2\hocr.html
page_maps\vol_1\page_numbers.json
page_maps\vol_1\scandata.xml
page_maps\vol_2\page_numbers.json
page_maps\vol_2\scandata.xml
```

如果某个文件在源目录中确实不存在，应在 `missing_files_report.md` 说明。

### 3. 文档完整

必须存在：

```text
README.md
MANIFEST_motte_1729.md
MANIFEST_motte_1729.json
logs\organize_motte_1729_log.md
logs\checksum_report.csv
logs\ocr_inspection_report.md
```

### 4. 状态文件已更新

必须更新：

```text
docs\status\PROJECT_STATUS.md
docs\status\CHANGELOG.md
docs\status\TODO.md
docs\status\ISSUES.md
```

### 5. 不应破坏源文件

源目录：

```text
E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_1
E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_2
```

必须仍然保留，不得删除，不得移动，不得重命名。

---

## 十一、重要提醒

1. 本次只整理 Motte 1729 英文底本资源，不做样板页。
2. 不要将 Project Gutenberg、Cajori 版本或其他现代修订文本混入本目录。
3. 目录中的 OCR 文本只能作为初步工作底本，最终用于页面展示的英文原文需要与 PDF 扫描页人工校核。
4. `extracted_nodes` 暂时只建立空目录和 README，不要急于填充。
5. 所有项目状态必须更新，因为这是长期项目，后续恢复上下文、继续开发、交给其他智能体，都依赖这些状态文件。
6. 如果发现文件命名和本 prompt 预设不同，请不要失败退出，应根据扩展名、文件大小和文件内容进行合理归类，同时在日志中说明判断依据。
7. 所有脚本和文档应使用 UTF-8 编码。
