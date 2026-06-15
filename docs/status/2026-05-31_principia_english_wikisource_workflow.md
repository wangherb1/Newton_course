# 2026-05-31 Principia English Wikisource Workflow

## 目标

将英文原文日常工作流从本地 IA OCR 调整为 Wikisource 1729 Andrew Motte 主源，同时保留 `motte_1729/` 作为扫描底本校核库。

## 已完成

- 建立 `sources/external/principia_english/` 来源目录。
- 固化来源顺序：Wikisource 1729 主源，Wikisource 1846 与 Project Gutenberg 1846 备份，本地 IA 1729 扫描校核。
- 新增通用抓取、节点提取和自动验证脚本。
- 缓存 Wikisource 1729 Book I Section II 的 HTML、wikitext 和 cleaned text。
- 提取 `book1_section2_prop01_theorem01` raw、clean 和 metadata。
- 自动验证通过：包含 Proposition I 和 Cor. 1-6，且不包含 Proposition II。

## 当前边界

- 自动提取已完成，但公开发布前仍需对照 IA 1729 扫描页人工校核。
- 本次未制作最终网页样板页。
- 本次未复制或删除任何 `motte_1729/` 大体积资产。

## 下一步

对照 Vol.1 IA scan leaf `102-103`、IA PDF 第 `103-104` 页、印刷页 `57-58` 完成人工校核，然后进入“命题1 定理1：扫面积速度恒定”样板页制作。
