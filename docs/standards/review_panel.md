# 内容页审阅状态面板范式

## 目标

每一个内容页在建设和人工校对阶段都必须显示审阅状态面板。该面板用于清晰呈现内容进度、来源接入情况和待校对事项，不属于正式教材正文。

正式发布时只隐藏面板展示，不删除节点源文件中的状态记录。

## 显示规则

面板是否显示由两层开关共同决定：

1. 全站开关：`assets/theme/site_config.json` 中的 `reviewPanel.visible`。
2. 节点开关：节点 MDX 中的 `review_panel.visible`。

只有两个开关都为 `true` 时，页面才显示审阅状态面板。

新节点默认使用：

```yaml
review_panel:
  visible: true
  mode: internal_review
```

正式公开发布前，将全站配置改为：

```json
{
  "reviewPanel": {
    "visible": false,
    "mode": "hidden_for_release"
  }
}
```

节点源文件中的 `status`、`source_status` 和 `review_panel` 字段继续保留，供后续维护和内部追踪使用。

## 面板内容

审阅状态面板至少应包含：

1. 所属章节。
2. 节点类型。
3. 原书位置。
4. 内容状态。
5. 英文原文状态。
6. 中文译文状态。
7. 现代解释状态。
8. 图示或动态演示状态。

状态表述必须具体，例如“已从 Wikisource 1846 数字页面提取，译文归属 Motte 1729，待人工校对”，不得只写含义不明确的“处理中”。

## 页面接入

Web 页面使用 `NodeMetaPanel.tsx` 统一渲染。新页面必须通过全站开关和节点开关计算是否显示，不得删除状态数据或在正式发布时手工删掉组件源文件。
