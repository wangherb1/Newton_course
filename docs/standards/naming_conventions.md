# 命名规范

## 文件与目录

- 代码、JSON 键和稳定目录使用小写英文、数字和下划线。
- 原始资料副本保留原始中文文件名，便于追溯。
- 章节目录使用 `chapter_00`、`chapter_01`、`chapter_02`。
- 内容目录使用 `book1_chapter02` 形式。

## 节点 ID

节点 ID 使用稳定、可排序的英文标识：

```text
principia-book1-chapter02-prop001-theorem001
```

显示编号单独保存在 `display_id`：

```text
命题1 定理1
```

不要把显示文本作为文件系统主键。

## 主题键

主题键使用 `chapterNN_topic`：

```text
chapter02_centripetal_force
```

## 状态记录

- 大任务状态文件：`docs/status/YYYY-MM-DD_task_name.md`
- 技术决策：`docs/decision_log/DECISION_YYYY-MM-DD_short_name.md`
