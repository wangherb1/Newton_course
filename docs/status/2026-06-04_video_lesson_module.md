# 2026-06-04 样板页视频课模块

## 范围

- 样板页：`/nodes/book1-chapter02/prop001-theorem001/`
- 页面入口：`web/src/pages/nodes/book1-chapter02/prop001-theorem001.astro`
- 视频规范：`docs/standards/video_lessons.md`
- 视频资产目录：`assets/videos/book1_chapter02/prop001_theorem001/`

## 本次修改

- 在样板页新增“视频课：等面积定律讲解”模块。
- 模块位置：章节导读之后，英文原文模块之前。
- 当前使用一段费曼相关讲解视频作为样板演示占位。
- 视频文件已复制为 ASCII 文件名：

```text
assets/videos/book1_chapter02/prop001_theorem001/feynman_equal_area_example.mp4
```

- 发布副本路径：

```text
web/public/assets/videos/book1_chapter02/prop001_theorem001/feynman_equal_area_example.mp4
```

## 后续老师视频放置位置

命题1定理1老师讲课视频应放入：

```text
assets/videos/book1_chapter02/prop001_theorem001/
```

推荐命名：

```text
teacher_lecture.mp4
teacher_lecture_v1.mp4
```

放入后运行：

```text
python scripts\sync_web_public_assets.py
```

然后将页面 `<video>` 的 `src` 更新为：

```text
/assets/videos/book1_chapter02/prop001_theorem001/teacher_lecture.mp4
```

## 范式结论

- 视频课模块是可选内容模块，但页面框架已预留。
- 若存在老师线下讲课视频，优先放在英文原文模块之前。
- 未确认授权的视频只能用于内部样板页或开发演示；正式发布前必须替换为授权确认后的课程视频。
