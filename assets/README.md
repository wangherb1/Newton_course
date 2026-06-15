# Assets

存放主题配置、课程图像、动态演示和图标。正式资产与 `sources/prototypes/` 中的参考材料分开管理。

- `images/heroes/`：节点首端 AI 氛围背景图。
- `images/primary_sources/`：从公开数字原典页面下载的原版插图，保留来源页面记录，并通过 `scripts/sync_web_public_assets.py` 同步到 Web 发布目录。
- `images/teacher_manuscripts/`：从老师 Word 稿件中保守提取的正文插图，保留原始文件内容，并通过 `scripts/sync_web_public_assets.py` 同步到 Web 发布目录。
- `videos/`：课程视频课资产。按 `book*_chapter*/node*` 或命题专属目录存放 MP4，并通过 `scripts/sync_web_public_assets.py` 同步到 Web 发布目录。
