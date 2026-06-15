# 2026-05-31 Project Scaffold

## 任务目标

按 `docs/codex_prompts/01_project_scaffold.md` 建立 Newton_course 的 Phase 0 项目脚手架。

## 执行步骤

1. 核对工作区、Node.js、npm、Python 和 Git 环境。
2. 创建项目目录树并初始化本地 Git。
3. 复制 7 个廖老师 Word 稿件副本和前期知乎原型材料，并建立 `articles/`、`demos/`、`assets/` 索引副本。
4. 初始化 Astro + React + TypeScript + MDX 网站。
5. 写入内容模型、版权边界、视觉配置、节点模板和自动化脚本。
6. 执行脚本和网站构建验收。

## 验收结果

- DOCX 文本抽取：7/7 成功。
- 目录种子：从 352 个段落中保守提取 334 个待人工校核候选项。
- 内容状态扫描：当前正式节点为 0，符合“先建框架、不批量生成页面”的要求。
- JSON 校验：项目 JSON 文件均可解析。
- 网站构建：`npm.cmd run build` 成功，生成 1 个静态页面。
- Git 保护：原始资料、文本抽取物和原型参考材料默认排除。

## 生成文件

- 根目录：`README.md`、`PROJECT_STATUS.md`、`TODO.md`、`CHANGELOG.md`、`.gitignore`
- 规范：`docs/standards/*.md`
- 内容：`content/metadata/*`、`content/nodes/_template.mdx`、`content/graph/*`
- 主题：`assets/theme/*`
- 脚本：`scripts/*.py`
- 网站：`web/`

## 未解决问题

- Andrew Motte 1729 英文原典来源、OCR 和页码映射尚未接入。
- 公开授权边界与学校署名规范尚待确认。
- 自动抽取的目录种子仍需人工校核。

## 下一步

执行“命题1 定理1：扫面积速度恒定”标准样板页建设。
