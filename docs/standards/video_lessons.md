# 视频课模块规范

## 模块位置

视频课模块用于承载老师线下讲课视频。内容页中若启用该模块，应放在“英文原文 / Primary English source”模块之前。

## 资产目录

项目内 canonical 视频资产放在：

```text
assets/videos/<chapter>/<node>/
```

视频文件使用 Git LFS 跟踪，不直接作为普通 Git blob 提交。当前规则写在根目录
`.gitattributes`：

```text
assets/videos/**/*.mp4 filter=lfs diff=lfs merge=lfs -text
assets/videos/**/*.mov filter=lfs diff=lfs merge=lfs -text
assets/videos/**/*.avi filter=lfs diff=lfs merge=lfs -text
```

命题1定理1当前目录为：

```text
assets/videos/book1_chapter02/prop001_theorem001/
```

网页发布副本由 `scripts/sync_web_public_assets.py` 同步到：

```text
web/public/assets/videos/<chapter>/<node>/
```

`web/public/assets/videos/` 是同步副本，保持在 `.gitignore` 中，不手动提交。

页面端引用路径使用：

```text
/assets/videos/<chapter>/<node>/<filename>.mp4
```

## 命名规则

- 文件名使用 ASCII 小写、下划线或连字符，不使用中文文件名。
- 推荐命名：

```text
teacher_lecture.mp4
teacher_lecture_v1.mp4
feynman_equal_area_example.mp4
```

## 样板页当前视频

当前样板页示例视频：

```text
assets/videos/book1_chapter02/prop001_theorem001/feynman_equal_area_example.mp4
web/public/assets/videos/book1_chapter02/prop001_theorem001/feynman_equal_area_example.mp4
```

该视频仅用于演示视频课模块。正式发布前应替换为已确认授权的老师课程视频。

## 替换老师视频流程

1. 将老师 MP4 放入节点目录，例如：

```text
assets/videos/book1_chapter02/prop001_theorem001/teacher_lecture.mp4
```

2. 运行：

```text
python scripts\sync_web_public_assets.py
```

3. 在页面中将 `<video src="...">` 指向：

```text
/assets/videos/book1_chapter02/prop001_theorem001/teacher_lecture.mp4
```

4. 运行：

```text
npm.cmd run build
```

5. 使用浏览器截图确认桌面端和窄屏端视频模块正常显示。

## 版权与发布

- 未确认授权的视频只能作为内部样板页占位或开发演示。
- 正式发布前必须确认视频来源、讲授者授权、剪辑版本和公开发布边界。
- 页面说明应避免把占位视频写成正式课程视频。
