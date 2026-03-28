# Bonus: Deploy to Railway

Get your RAG system serving real traffic in ~15 minutes.

Railway runs your Docker containers in the cloud. Your heavy infrastructure
(Qdrant Cloud, Redis Cloud, Gemini API, Voyage AI) is already managed — we
just need to deploy the FastAPI backend and Streamlit frontend.

## Architecture

```
Internet
   |
   v
[Frontend]  <-- public domain (https://frontend-xxx.up.railway.app)
   |
   | private networking (http://backend.railway.internal:8080)
   v
[Backend]   <-- no public URL needed
   |
   v
[Qdrant Cloud, Redis Cloud, Gemini, Voyage, Opik]  <-- managed services
```

Only the frontend is publicly accessible. The backend communicates via
Railway's private networking — faster, more secure, no CORS issues.

---

## Step 1: Create a Railway Account

1. Go to [railway.com](https://railway.com) and click **Sign Up**
2. Sign up with GitHub (recommended) or email
3. Railway gives you a free trial with $5 credit — enough to test your deployment

## Step 2: Install the Railway CLI

Open your terminal and install:

```bash
# macOS
brew install railway

# or npm (any platform — requires Node.js)
npm i -g @railway/cli
```

Verify the installation:

```bash
railway --version
```

You should see something like `railway 4.x.x`.

## Step 3: Login from the CLI

```bash
railway login
```

This opens your browser with a pairing code. Click **Confirm** in the browser
to authenticate. This is a one-time setup.

Verify you're logged in:

```bash
railway whoami
```

Should print your name and email.

## Step 4: Create a Railway Project with Two Services

Go to [railway.com/dashboard](https://railway.com/dashboard) in your browser:

1. Click **New Project** → **Empty Project**
2. Give it a name (e.g., `rag-accelerator`) and click **Create**
3. You're now inside your project. Click **New** (top right) → **Empty Service**
4. A new service card appears. Click the card to open it, then click the
   service name at the top to rename it to `backend`
5. Go back to the project canvas. Click **New** → **Empty Service** again
6. Rename this one to `frontend`

You should now see two service cards on the project canvas: `backend` and
`frontend`.

## Step 5: Set Backend Environment Variables

1. Click the `backend` service card to open it
2. Go to the **Variables** tab
3. Click **RAW Editor** (top right of the variables section)
4. Paste the following (replace placeholder values with your actual keys from `.env`):

```env
QDRANT_URL=https://your-cluster.aws.cloud.qdrant.io:6333
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_COLLECTION=week3_hybrid
GOOGLE_API_KEY=your_google_api_key
VOYAGE_API_KEY=your_voyage_api_key
REDIS_HOST=your-redis-host.cloud.redislabs.com
REDIS_PORT=6379
REDIS_PASSWORD=your_redis_password
REDIS_USERNAME=default
REDIS_SSL=true
LLM_MODEL=gemini-2.5-flash
VOYAGE_EMBED_MODEL=voyage-4-lite
VOYAGE_DIMENSION=2048
SPARSE_MODEL=Qdrant/bm25
CACHE_EMBED_MODEL=voyage-4-lite
CACHE_EMBED_DIMENSION=2048
CACHE_DISTANCE_THRESHOLD=0.06
GRPC_DNS_RESOLVER=native
```

If you have Opik set up, also add:

```env
OPIK_API_KEY=your_opik_api_key
OPIK_WORKSPACE=your_workspace
OPIK_PROJECT_NAME=rag-accelerator-prod
```

5. Click **Update Variables** to save
6. Railway will show a staged change banner at the bottom — click **Deploy**
   to apply the changes

> **Important:** You must click **Deploy** after adding variables. The
> services won't be visible to the CLI until this deploy is triggered.

## Step 6: Set Frontend Environment Variables

1. Go back to the project canvas (click the project name in the breadcrumb)
2. Click the `frontend` service card
3. Go to **Variables** tab → **RAW Editor**
4. Paste:

```env
API_BASE_URL=http://backend.railway.internal:8080
```

This uses Railway's private networking — the frontend talks to the backend
internally without going through the public internet.

5. Click **Update Variables**, then click **Deploy** on the staged change banner

## Step 7: Deploy the Backend Code

Open your terminal:

```bash
cd week5_production/backend
```

Link this directory to the backend service on Railway:

```bash
railway link
```

The CLI will prompt you to select:
- **Workspace** → select your personal workspace
- **Project** → select your project (e.g., `rag-accelerator`)
- **Environment** → select `production`
- **Service** → select `backend`

You should see: `Project ... linked successfully!`

Now deploy:

```bash
railway up
```

This uploads your code, builds the Docker image, and deploys it. You'll see
a build logs URL — open it in your browser to watch the progress.

The first build takes 3-5 minutes (installing Python dependencies +
downloading the BM25 sparse model).

**Wait for the deploy logs to show:**
```
PRODUCTION RAG API READY
```

This means all services initialized successfully (pipeline, cache,
conversation memory, query router).

> **Note:** If the deploy logs show `Uvicorn running on http://0.0.0.0:8080`,
> that confirms the port. If it's different from `8080`, update the frontend's
> `API_BASE_URL` variable to match.

## Step 8: Deploy the Frontend Code

Open a **new terminal** (or navigate to the frontend directory):

```bash
cd week5_production/frontend
```

> **Important:** `railway link` is per-directory. You must link the frontend
> directory separately — it doesn't inherit the backend's link.

```bash
railway link
```

Select:
- **Workspace** → your personal workspace
- **Project** → same project as before
- **Environment** → `production`
- **Service** → `frontend`

Deploy:

```bash
railway up
```

This build is faster (~1 minute — just Streamlit and requests).

## Step 9: Generate a Public URL for the Frontend

Only the frontend needs a public URL (the backend stays private):

1. Go to the Railway dashboard → click the `frontend` service
2. Go to **Settings** tab → scroll to **Networking**
3. Click **Generate Domain**
4. Railway creates a URL like: `https://frontend-production-xxxx.up.railway.app`

Copy this URL and open it in your browser. You should see the chat interface.

## Step 10: Verify Everything Works

Open your frontend URL and test:

- [ ] Chat interface loads
- [ ] Ask "What is Bayes' theorem?" — a streaming answer appears
- [ ] Ask a follow-up like "Can you give me a concrete example?" — query rewriting resolves the reference
- [ ] Click thumbs up/down on an answer — feedback submits successfully
- [ ] If Opik is configured, check your Opik dashboard for traces

---

## Troubleshooting

**CLI says "No services found" after creating them in the dashboard**

You need to click **Deploy** on the staged changes banner after adding
variables. Railway services aren't visible to the CLI until the first
deploy is triggered.

**Container gets killed / OOM errors**

The default setup uses Voyage API for cache embeddings (no large local
model). If you switched `CACHE_EMBED_MODEL` to a local model like
`BAAI/bge-large-en-v1.5` (1.3GB in memory), either switch back to
`voyage-4-lite` or increase memory: Railway dashboard → service →
**Settings → Resource Limits**.

**Deploy logs show `Invalid value for '--port': '$PORT'`**

The Dockerfile CMD must use shell form for variable expansion. Check that
your backend Dockerfile has:
```dockerfile
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
```
Not the exec form (`CMD ["uvicorn", ..., "$PORT"]`) — exec form doesn't
expand variables.

**Frontend shows "Cannot connect to backend"**

- Check `API_BASE_URL` on the frontend service variables
- It must be `http://backend.railway.internal:8080` (not `https`)
- The port must match what the backend is listening on (check backend deploy
  logs for `Uvicorn running on http://0.0.0.0:XXXX`)
- Both services must be in the same Railway project for private networking

**Backend health check fails**

The backend takes 30-60 seconds to start (warming up pipeline components,
downloading models). Railway's health check timeout is set to 120s in
`railway.toml`. Check the deploy logs in the Railway dashboard.

**Redis connection refused**

Check that `REDIS_SSL` matches your Redis Cloud setup. Redis Cloud typically
requires `REDIS_SSL=true`. Double-check `REDIS_HOST`, `REDIS_PORT`, and
`REDIS_PASSWORD`.

**Qdrant / gRPC DNS errors**

Make sure `GRPC_DNS_RESOLVER=native` is set in the backend env vars.

**Cache errors after changing embedding model/dimension**

If you changed `CACHE_EMBED_MODEL` or `CACHE_EMBED_DIMENSION`, the Redis
HNSW index needs to be recreated with the new dimension:

```bash
uv run python setup/03_setup_redis.py --reset
```

**`railway link` fails or picks the wrong service**

Each directory has its own Railway link. If you're in the wrong directory,
`railway up` will deploy to the wrong service. Always verify:

```bash
railway status
```

This shows which project, environment, and service are linked in the
current directory.

---

## Cost

Railway's Hobby plan is $5/month with $5 in included credits. A low-traffic
demo app (backend + frontend) typically costs $3-8/month depending on usage.
You can delete the project anytime to stop billing.

## Alternative: Deploy via GitHub (Auto-Deploy on Push)

Instead of `railway up` from the CLI, you can connect a GitHub repo so
Railway auto-deploys on every push:

1. Railway dashboard → service → **Settings → Source**
2. Click **Connect Repo** and select your GitHub repository
3. Set the **Root Directory** to `week5_production/backend` (for the backend
   service) or `week5_production/frontend` (for the frontend service)
4. Enable **Auto Deploy** — Railway rebuilds and deploys on every push to
   your branch

See Railway's docs for full setup:
[railway.com/docs/guides/github-autodeploys](https://docs.railway.com/guides/github-autodeploys)

## Redeploying After Code Changes

**CLI method:**
```bash
# Backend
cd week5_production/backend
railway up

# Frontend
cd week5_production/frontend
railway up
```

Each directory remembers its linked service from `railway link`, so you
don't need to re-link.

**GitHub method:** Just push to your branch — Railway auto-deploys.

## Redeploying After Environment Variable Changes

Update variables in the Railway dashboard → service → **Variables**. Railway
auto-redeploys when env vars change. If it doesn't, trigger manually:

```bash
railway service redeploy --yes
```

## Tearing Down

To stop incurring charges:

1. Railway dashboard → your project → **Settings** → **Danger Zone** → **Delete Project**

Your Qdrant Cloud, Redis Cloud, and API keys are unaffected — only the
Railway compute is removed.
