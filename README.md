# 牛顿《原理》现代精读开放课程

英文名称：Newton Principia Modern Reading Course

本项目用于整理北京理工大学廖日东老师多年积累的牛顿《自然哲学的数学原理》讲义、中文翻译、现代数学物理解释、图示、动态演示和思考题，逐步建设为可长期维护的开放教材型网站。

## 当前阶段

当前为 Phase 1：命题1定理1标准样板页建设与范式迭代。已经建立内容模型、版权边界、主题配置、英文原文主源缓存、原始资料隔离目录、自动化脚本和 Astro + React + TypeScript + MDX 网站，并完成首个可运行样板页。

本阶段不批量生成全书页面，不伪造 Andrew Motte 1729 英文原文，不公开原始 Word/PDF，不建立真实评论后端。

## 目录导航

- `docs/standards/`：内容、命名、视觉、版权、工作流和评论规范。
- `sources/raw/`：本地原始资料副本，默认不纳入公开 Git。
- `sources/external/principia_english/`：英文原文统一工作流，日常数字主源为 Wikisource 1846 页面；译文归属仍为 Andrew Motte 1729 英译本。
- `sources/external/motte_1729/`：Internet Archive 1729 扫描底本校核库。
- `sources/prototypes/`：前期知乎内容和交互原型，仅用于参考。
- `content/`：统一内容模型、节点模板和关系图数据。
- `assets/theme/`：可替换的主题配置。
- `scripts/`：资料抽取和状态检查脚本。
- `web/`：Astro 网站工程。

## 本地运行

```powershell
cd E:\Codex\Newton_course\web
npm.cmd run dev
```

构建检查：

```powershell
npm.cmd run build
```

## 下一步

英文原文日常数字来源已经切换为 Wikisource 1846 页面，并完成 `book1_section2_prop01_theorem01` 自动提取与验证。译文归属仍为 Andrew Motte 1729 英译本。命题1定理1样板页已完成首版。下一步逐项完善样板页细节，同时持续固化可复用范式；人工校对阶段需要对照 1729 扫描页、老师原始 Word 公式和图2.1。
