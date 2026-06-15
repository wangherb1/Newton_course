# 命题1 定理1主体四模块样板范式留档

## 任务目标

在继续审阅动态图和思考题之前，固化已经基本敲定的样板页主体正文范式，并生成可追溯的阶段留档和下一线程续接摘要。

## 已确认主体模块

1. Hero 首端封面。
2. Andrew Motte 1729 英文原文。
3. 中译版。
4. 现代微积分证明：极坐标方法。

详细规则见 `docs/standards/sample_page_body_baseline.md`。

## 保留待审阅模块

- 图示与动态演示。
- 思考题。
- 命题网络。
- 评论 / 讨论区。
- 署名与版权说明。

## 留档位置

`archive/2026-06-01_prop001_theorem001_body_baseline/`

留档采用引用清单和 SHA-256，不复制项目主资产或老师源稿二进制。

## 验证

- `python scripts/sync_web_public_assets.py`
- `python scripts/check_content_status.py`
- `npm.cmd run build`
- HTTP `200`：`http://127.0.0.1:4321/nodes/book1-chapter02/prop001-theorem001/`
- 构建产物包含现代证明图题，不包含 `[公式待校对]` 或 `[图2.1待重绘]`
- 已生成并人工检查桌面与窄屏留档截图：
  - `exports/screenshots/prop001_theorem001_sample/body_baseline_archive_v1.png`
  - `exports/screenshots/prop001_theorem001_sample/body_baseline_archive_v1_mobile.png`
