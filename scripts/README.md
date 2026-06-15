# Scripts

## 网站图片同步

```powershell
python scripts\sync_web_public_assets.py
```

将 `assets/images/heroes/`、`assets/images/primary_sources/` 和 `assets/images/teacher_manuscripts/` 中的项目主资产同步到 `web/public/assets/`，供 Astro 网站直接发布。不要直接编辑发布副本。

## 老师稿件截图裁剪

```powershell
powershell -ExecutionPolicy Bypass -File scripts\crop_teacher_manuscript_image.ps1 `
  -InputPath assets\images\teacher_manuscripts\book1_chapter02\prop001_theorem001_geometry_proof.png `
  -OutputPath assets\images\teacher_manuscripts\book1_chapter02\prop001_theorem001_geometry_proof_cropped.png `
  -X 520 -Y 175 -Width 900 -Height 810
```

Word 稿件中的图片可能是包含浏览器界面或页面边缘的截图。保留直接提取的溯源原图，另生成裁剪后的网页资产；页面只引用裁剪版。

## DOCX 文本抽取

```powershell
python scripts\extract_docx_text.py
```

默认扫描 `sources/raw/liao_teacher/` 中的 `.docx`，将纯文本副本写入 `sources/processed/text_extracts/`。脚本不会覆盖原始文件；遇到 Word 公式时会写入人工校核标记。

老师稿件目录中如同时存在 `- latex.docx` 配套稿件，应优先使用该版本录入网页公式。该版本中的公式以 `\[...\]` LaTeX 文本保存，可由抽取脚本直接保留。原始 `.docx` 仍用于核对插图、相对位置和公式视觉效果；网页交付前必须复核 KaTeX 渲染结果。

## 目录种子生成

```powershell
python scripts\build_outline_seed.py
```

从 `原理概要.docx` 保守提取疑似目录行，覆盖更新 `content/metadata/principia_outline.seed.json`。输出必须人工校核。

## 内容状态扫描

```powershell
python scripts\check_content_status.py
```

扫描 `content/nodes/` 下正式 `.mdx` 节点，生成 `exports/status/content_status.json` 和 `exports/status/content_status.md`。
