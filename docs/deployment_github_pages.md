# GitHub Pages deployment

This project publishes the Astro site in `web/` through GitHub Pages.

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

GitHub rejects ordinary repository files larger than 100 MB. The local sample video
`web/public/assets/videos/book1_chapter02/prop001_theorem001/feynman_equal_area_example.mp4`
is intentionally ignored.

For online video, use one of these options:

- Upload a compressed MP4 under 100 MB only if it is acceptable for repository history.
- Put the video on external hosting and set `PUBLIC_SAMPLE_VIDEO_URL` in the Pages build environment.
- Keep GitHub Pages for the static course site and use a dedicated media host for lectures.
