# Newton Course Maintenance Guide

This guide records the working project frame after the first GitHub Pages deployment was
successfully connected.

## Repository Roles

- `content/`: structured course nodes, graph data, metadata seeds, and reusable content templates.
- `sources/`: source materials and source-preparation workflows. Raw or restricted sources stay ignored.
- `assets/`: canonical public assets such as hero images, source images, teacher-manuscript images, and videos.
- `scripts/`: repeatable extraction, status, image, and asset-sync helpers.
- `web/`: Astro site source. It consumes `content/` and public assets.
- `web/public/`: generated/static publish copy for the Astro build. Media here should come from `scripts/sync_web_public_assets.py`.
- `web/dist/`: build output. Never commit this directory.
- `exports/`: QA screenshots, status outputs, and generated delivery checks.
- `docs/`: project decisions, standards, status records, and deployment notes.

## Normal Update Flow

Use this sequence for ordinary content or site edits:

```powershell
cd E:\Codex\Newton_course
git status --short
python scripts\sync_web_public_assets.py
cd web
npm.cmd run build
cd ..
git status --short
git add <changed files>
git commit -m "Describe the update"
git push
```

GitHub Actions rebuilds and deploys the Pages site after each push to `main`.

## Adding A New Content Page

1. Add or update canonical node data in `content/`.
2. Add page data or route wiring in `web/src/data/` and `web/src/pages/`.
3. Reuse the existing sample-page structure before inventing new section patterns.
4. Add images to `assets/images/...`, not directly to `web/public/...`.
5. Run `python scripts\sync_web_public_assets.py`.
6. Run `npm.cmd run build` in `web/`.
7. Add a status note in `docs/status/` if the change affects project structure or publishing workflow.

## Adding Or Replacing Videos

Canonical video files live under:

```text
assets/videos/<chapter>/<node>/
```

Large videos are tracked with Git LFS by `.gitattributes`. The generated web copy is:

```text
web/public/assets/videos/<chapter>/<node>/
```

Rules:

- Track large videos only from `assets/videos/`.
- Keep `web/public/assets/videos/` ignored.
- Run `python scripts\sync_web_public_assets.py` before local build checks.
- Keep page video URLs in `/assets/videos/...` form, using `assetPath(...)` where Astro/React code needs GitHub Pages base-path support.
- Watch GitHub LFS storage/bandwidth and the GitHub Pages artifact size as video count grows.

## Adding A Dynamic Demo

1. Put standalone demo HTML under `web/public/demos/<chapter>/<node>/`.
2. Keep a prompt or design note next to it when the demo is generated or substantially revised.
3. Use a small wrapper component to embed the demo with an iframe.
4. Always pass demo URLs through `assetPath(...)` so GitHub Pages subpaths work.
5. Verify both the embedded iframe and the standalone demo URL.

## Deployment Checks

After a deployment-sensitive change, verify:

```powershell
Invoke-WebRequest -Uri "https://wangherb1.github.io/Newton_course/" -UseBasicParsing
Invoke-WebRequest -Uri "https://wangherb1.github.io/Newton_course/nodes/book1-chapter02/prop001-theorem001/" -UseBasicParsing
```

For large videos, also verify:

```powershell
curl.exe -I "https://wangherb1.github.io/Newton_course/assets/videos/book1_chapter02/prop001_theorem001/feynman_equal_area_example.mp4"
curl.exe -L -r 0-1023 -o NUL -w "HTTP=%{http_code} Size=%{size_download} Type=%{content_type}\n" "https://wangherb1.github.io/Newton_course/assets/videos/book1_chapter02/prop001_theorem001/feynman_equal_area_example.mp4"
```

Expected video checks:

- `Content-Type: video/mp4`
- `Accept-Ranges: bytes`
- range request returns `HTTP=206`

## When The Site Stops Matching Local Preview

Check these in order:

1. Did the latest commit push to `origin/main`?
2. Did GitHub Actions complete successfully?
3. Does the generated page use `/Newton_course/...` paths?
4. Did `scripts/sync_web_public_assets.py` run before build?
5. Is a large video tracked by Git LFS rather than ignored or committed as an ordinary Git blob?
6. Is the browser showing a cached Pages asset? Try a cache-busting query string.

## Documentation Closeout

For any meaningful workflow or structure change:

- Update the relevant standards doc.
- Add a status note under `docs/status/`.
- Update `docs/deployment_github_pages.md` if the deployment process changed.
- Keep `docs/README.md` current as the navigation entry.
