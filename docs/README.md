# Project Documentation Map

This folder is the project memory for future course production. Start here before changing
content structure, publishing workflow, or media assets.

## Core Operations

- `maintenance_guide.md`: day-to-day rules for adding pages, assets, videos, demos, and deployments.
- `deployment_github_pages.md`: GitHub Pages deployment workflow, Git LFS video publishing, and troubleshooting.
- `standards/workflow.md`: content intake, source handling, page production, and task closeout rules.
- `standards/video_lessons.md`: canonical video locations, Git LFS rules, and video replacement workflow.

## Content And Source Strategy

- `standards/content_model.md`: node metadata, content fields, and page assembly expectations.
- `standards/sample_page_body_baseline.md`: current sample-page section pattern.
- `standards/copyright_and_attribution.md`: publication boundaries and attribution rules.
- `decision_log/`: durable decisions that should not be silently reversed.
- `status/`: append-only status records after meaningful work.

## Current Published Site

- Repository: `https://github.com/wangherb1/Newton_course`
- Site: `https://wangherb1.github.io/Newton_course/`
- Sample page: `https://wangherb1.github.io/Newton_course/nodes/book1-chapter02/prop001-theorem001/`

## Maintenance Principle

Keep the source of truth separated from generated copies:

- Canonical source content: `content/`, `sources/external/`, `assets/`
- Generated website project: `web/`
- Generated publish copies: `web/public/`
- Build output: `web/dist/`
- QA screenshots and exports: `exports/`

Do not hand-edit generated copies when a canonical source or sync script owns them.
