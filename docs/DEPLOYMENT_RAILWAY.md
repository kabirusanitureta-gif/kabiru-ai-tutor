# Deploying Kabiru AI Tutor to Railway

[Railway](https://railway.app) offers simple container-based deployment with a small free usage
allowance, and supports persistent volumes — useful for keeping your SQLite database and generated
certificates between deploys.

## 1. Push your project to GitHub

```bash
git init
git add .
git commit -m "Initial commit: Kabiru AI Tutor"
git branch -M main
git remote add origin https://github.com/<your-username>/kabiru-ai-tutor.git
git push -u origin main
```

## 2. Create a New Railway Project

1. Log in to [railway.app](https://railway.app) and click **New Project**.
2. Choose **Deploy from GitHub repo** and select your `kabiru-ai-tutor` repository.
3. Railway will detect multiple possible services — you'll set up the backend and frontend as two
   separate services within the same project.

## 3. Configure the Backend Service

1. In the project, click **+ New** → **GitHub Repo** (select the same repo again) to add a second
   service, or edit the auto-detected one.
2. Under **Settings** for this service:
   - **Root Directory:** leave as repo root (the Dockerfile handles paths)
   - **Dockerfile Path:** `docker/Dockerfile.backend`
3. Under **Variables**, add:
   | Key | Value |
   |---|---|
   | `SECRET_KEY` | a long random string |
   | `DATABASE_URL` | `sqlite:///./kabiru_tutor.db` |
   | `OLLAMA_ENABLED` | `false` (unless you're also running Ollama on a Railway-connected host) |
   | `FRONTEND_ORIGIN` | your frontend's Railway URL (set after step 4) |
4. Under **Settings → Networking**, click **Generate Domain** to get a public URL, e.g.
   `kabiru-backend-production.up.railway.app`.
5. **(Recommended)** Attach a **Volume** mounted at `/app/backend` so your SQLite database file
   persists across deploys, and another mounted at `/app/certificates` for generated PDFs.

## 4. Configure the Frontend Service

1. Add another service from the same GitHub repo.
2. Under **Settings**:
   - **Dockerfile Path:** `docker/Dockerfile.frontend`
   - **Build Args:** set `VITE_API_URL` to your backend's public URL from step 3
     (e.g. `https://kabiru-backend-production.up.railway.app`)
3. Under **Settings → Networking**, click **Generate Domain** for the frontend too.

## 5. Update CORS

Go back to the backend service's **Variables**, set `FRONTEND_ORIGIN` to the exact frontend domain
from step 4 (including `https://`), and redeploy the backend service so CORS takes effect.

## 6. Verify

Visit your frontend's Railway domain, register an account, browse a course, complete a lesson, and
confirm a quiz submission and certificate download work end-to-end. Visit
`<backend-domain>/docs` to confirm the API responds directly.

## Notes

- Railway's free tier includes limited monthly usage hours — check current limits on their pricing
  page before relying on this for long-term hosting.
- If you want the full local-AI experience (Ollama with an auto-detected model) in production, you'll need a paid
  Railway plan with enough RAM (8B-parameter models typically need 8GB+ RAM), or run the backend on
  your own VPS/home server instead, where you control the hardware.
