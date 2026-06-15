# 2026-06-03 命题1定理1样板页阶段范式留档

## 范围

- 样板页：`/nodes/book1-chapter02/prop001-theorem001/`
- 页面入口：`web/src/pages/nodes/book1-chapter02/prop001-theorem001.astro`
- 页面数据：`web/src/data/nodes/prop001Theorem001.ts`
- 动态演示目录：`web/public/demos/book1_chapter02/prop001_theorem001/`

## 当前阶段结论

命题1定理1样板页的主体结构已经形成阶段基线。后续节点应优先复用本页确认过的模块结构、来源处理方式、动态图示接口和署名规则；仍待审阅的模块不得提前视为最终范式。

## 已确认模块

1. Hero 首端封面  
   使用 AI 单层背景图，精确科学图示不进入 Hero。

2. Andrew Motte 英文原文  
   页面展示 Andrew Motte 1729 英译本归属；Wikisource 1846 数字页面作为日常文本与插图定位主源，来源定位保留在英文原文模块。

3. 视频课  
   视频课模块置于英文原文模块之前。后续老师线下讲课视频放入 `assets/videos/<chapter>/<node>/`，再同步到 `web/public/assets/videos/<chapter>/<node>/`。样板页当前使用示例视频占位，正式发布前应替换为授权确认后的课程视频。

4. 中译版  
   标题使用“中译版”，正文不重复显示稿件来源说明；老师稿件来源和提取状态保留在元数据及内部审阅状态中。

5. 现代微积分证明  
   标题使用“现代微积分证明：极坐标方法”；公式优先从 `- latex.docx` 配套稿件录入，原始 Word 负责视觉回查，公式使用 KaTeX。

6. 图示与动态演示  
   使用独立 HTML 文件，并保留同目录 prompt 文档。命题1定理1当前接口为：
   - `equal_area_demo.prompt.md`
   - `equal_area_demo.html`
   - `equal_area_optimized.html` 可作为外部或人工优化稿保留

   演示 HTML 应包含命题陈述、交互控制、几何与面积检验、近远焦点对比、图例和读图要点。图框区固定，文字面板独立滚动。

7. 署名与版权说明  
   页面展示文本固定为：

   ```text
   中译版与现代解释：廖日东，北京理工大学
   数字化整理与交互演示建设：WYL / 项目助教团队
   原典来源：Isaac Newton, Philosophiae Naturalis Principia Mathematica; English translation by Andrew Motte, 1729.
   当前页面状态：样板草稿，待校对与授权确认。
   ```

   英文数字主源不在署名区单列；应保留在英文原文模块、节点元数据或内部状态记录中。

## 仍待审阅模块

- 思考题。
- 命题网络。
- 评论 / 讨论区。
- 公开发布授权边界与学校署名规范。

## 已同步规范文件

- `docs/standards/sample_page_body_baseline.md`
- `docs/standards/content_model.md`
- `docs/standards/copyright_and_attribution.md`
- `content/nodes/_template.mdx`

## 验证要求

每次更新样板页后至少执行：

```text
python scripts\sync_web_public_assets.py
python scripts\check_content_status.py
npm.cmd run build
```

并检查页面路径与关键独立演示路径返回 `200`。
