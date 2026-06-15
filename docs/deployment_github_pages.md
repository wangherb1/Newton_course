# GitHub Pages deployment

This project publishes the Astro site in `web/` through GitHub Pages.

For the broader maintenance workflow, see `docs/maintenance_guide.md`.

## First-time setup

1. Create a GitHub repository named `Newton_course`.
2. Add it as the local remote:

   ```powershell
   git remote add origin https://github.com/<your-user>/Newton_course.git
   git branch -M main
   git push -u origin main
   ```

3. In GitHub, open the repository settings:
   - `Settings` -> `Pages`
   - `Build and deployment` -> `Source` -> `GitHub Actions`

4. The workflow `.github/workflows/deploy-pages.yml` builds `web/` and publishes `web/dist`.

The expected public URL is:

```text
https://<your-user>.github.io/Newton_course/
```

## Normal update flow

After editing local content:

```powershell
cd E:\Codex\Newton_course
git status --short
cd web
npm.cmd run build
cd ..
git add .
git commit -m "Update Newton course site"
git push
```

Every push to `main` triggers a new Pages deployment.

## Large videos

GitHub rejects ordinary repository files larger than 100 MB. Course videos are tracked from
the canonical `assets/videos/` directory with Git LFS, then copied into `web/public/assets/videos/`
during the GitHub Actions build.

The workflow uses:

- `actions/checkout` with `lfs: true`
- `python scripts/sync_web_public_assets.py`
- `astro build`

Keep `web/public/assets/videos/` ignored; it is a generated publish copy.

For many future full-length videos, monitor GitHub LFS storage/bandwidth and the GitHub Pages
artifact size. If the course grows beyond the Pages/LFS comfort zone, move videos to a media host
and set page video URLs through `PUBLIC_SAMPLE_VIDEO_URL` or a video manifest.

- GitHub repository blobs: ordinary files over 100 MB are blocked.
- Git LFS: supports large binary files, but storage and bandwidth are metered.
- GitHub Pages artifact: keep the published site near or below 1 GB for reliable deployment.
