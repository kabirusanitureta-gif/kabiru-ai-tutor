# Deploying Kabiru AI Tutor to Render

[Render](https://render.com) offers a free tier suitable for hosting both the FastAPI backend and the
React frontend. This guide deploys them as two separate services.

> **Note:** Render's free tier has an ephemeral filesystem — your SQLite database and generated
> certificate PDFs will reset on redeploys. For a persistent free option, attach a Render Disk (paid)
> or switch `DATABASE_URL` to a managed Postgres instance (Render offers a free Postgres tier with
> a 90-day limit). For a personal learning project, the ephemeral SQLite setup below is fine to start.

## 1. Push your project to GitHub

```bash
git init
git add .
git commit -m "Initial commit: Kabiru AI Tutor"
git branch -M main
git remote add origin https://github.com/<your-username>/kabiru-ai-tutor.git
git push -u origin main
```

## 2. Deploy the Backend (Web Service)

1. Log in to [render.com](https://render.com) and click **New +** → **Web Service**.
2. Connect your GitHub repository.
3. Configure:
   - **Name:** `kabiru-ai-tutor-backend`
   - **Root Directory:** leave blank (repo root)
   - **Runtime:** Python 3
   - **Build Command:**
     ```
     pip install -r requirements.txt
     ```
   - **Start Command:**
     ```
     cd backend && python -m app.seed.run_seed && uvicorn app.main:app --host 0.0.0.0 --port $PORT
     ```
4. Under **Environment Variables**, add:
   | Key | Value |
   |---|---|
   | `SECRET_KEY` | a long random string (generate with `python -c "import secrets; print(secrets.token_hex(32))"`) |
   | `DATABASE_URL` | `sqlite:///./kabiru_tutor.db` |
   | `OLLAMA_ENABLED` | `false` (Render has no local Ollama — the rule-based tutor fallback handles chat) |
   | `FRONTEND_ORIGIN` | the frontend URL you'll create in step 3, e.g. `https://kabiru-ai-tutor-frontend.onrender.com` |
5. Click **Create Web Service**. Wait for the build and deploy to finish.
6. Note your backend's public URL, e.g. `https://kabiru-ai-tutor-backend.onrender.com`.

## 3. Deploy the Frontend (Static Site)

1. Click **New +** → **Static Site**.
2. Connect the same GitHub repository.
3. Configure:
   - **Name:** `kabiru-ai-tutor-frontend`
   - **Root Directory:** `frontend`
   - **Build Command:** `npm install && npm run build`
   - **Publish Directory:** `dist`
4. Under **Environment Variables**, add:
   | Key | Value |
   |---|---|
   | `VITE_API_URL` | your backend's URL from step 2, e.g. `https://kabiru-ai-tutor-backend.onrender.com` |
5. Click **Create Static Site**.

## 4. Update CORS

Go back to the backend service's environment variables and confirm `FRONTEND_ORIGIN` exactly matches
your deployed frontend URL (including `https://`, no trailing slash), then trigger a manual redeploy
of the backend so the CORS setting takes effect.

## 5. Verify

Visit your frontend URL, register a new account, and confirm you can browse courses, complete a
lesson, and take a quiz. Visit `<backend-url>/docs` to confirm the API is reachable directly.

## Notes on the AI Tutor in Production

Render's free tier cannot run Ollama (no GPU, limited resources). With `OLLAMA_ENABLED=false`, the
AI Chat page automatically uses the built-in rule-based tutor, which still answers common questions
in Hausa and English and explains errors — just with less flexibility than a full local LLM. If you
later deploy on a machine with more resources (e.g. a VPS), you can run Ollama alongside the backend
and set `OLLAMA_ENABLED=true` with `OLLAMA_BASE_URL` pointing to it.
