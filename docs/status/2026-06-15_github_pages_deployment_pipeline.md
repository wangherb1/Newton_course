# 2026-06-15 GitHub Pages Deployment Pipeline

## Objective

Connect the local Newton course project to GitHub, publish it with GitHub Pages, and prove that
large lesson videos can be displayed online with the same page-level video layout as local preview.

## Result

- GitHub repository: `https://github.com/wangherb1/Newton_course`
- GitHub Pages site: `https://wangherb1.github.io/Newton_course/`
- Sample page: `https://wangherb1.github.io/Newton_course/nodes/book1-chapter02/prop001-theorem001/`
- Deployment workflow: `.github/workflows/deploy-pages.yml`
- Large video route: `https://wangherb1.github.io/Newton_course/assets/videos/book1_chapter02/prop001_theorem001/feynman_equal_area_example.mp4`

## Implemented Pipeline

1. Local Git repository uses `main` and tracks `origin/main`.
2. GitHub Pages source is set to GitHub Actions.
3. GitHub Actions checks out LFS objects with `actions/checkout@v4` and `lfs: true`.
4. The build runs `python scripts/sync_web_public_assets.py`.
5. The Astro site builds from `web/`.
6. `web/dist` is uploaded with `actions/upload-pages-artifact@v4`.
7. `actions/deploy-pages@v4` publishes the site.

## Large Video Handling

Canonical videos live in:

```text
assets/videos/
```

Generated web copies live in:

```text
web/public/assets/videos/
```

The canonical sample video is tracked by Git LFS:

```text
assets/videos/book1_chapter02/prop001_theorem001/feynman_equal_area_example.mp4
```

Validation after deployment:

- Page returned `200`.
- Video returned `200`, `Content-Type: video/mp4`, and `Content-Length: 413364261`.
- Range request returned `206`, confirming byte-range playback support.

## Current Commit Trail

- `c16bcaa` fixed the GitHub Pages deployment workflow.
- `63d73b3` fixed sample-page media module paths and iframe base path handling.
- `1ac99b8` published the sample lecture video through Git LFS and restored the real video player.

## Operational Notes

- Do not commit `web/dist`.
- Do not commit `web/public/assets/videos/`; it is a sync output.
- Do commit authorized public videos from `assets/videos/`, with Git LFS enabled.
- Watch GitHub LFS quota and Pages artifact size as the course grows.
- If video scale exceeds GitHub Pages/LFS comfort limits, keep the same page player but move video delivery to a dedicated media host.
