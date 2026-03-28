FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for fastembed and grpc
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies via pip (Docker doesn't use uv)
RUN pip install --no-cache-dir \
    "fastapi>=0.115.0" \
    "uvicorn[standard]>=0.30.0" \
    "haystack-ai>=2.16.1" \
    "google-genai-haystack>=2.1.1" \
    "voyage-embedders-haystack>=1.8.0" \
    "fastembed-haystack>=1.5.0" \
    "fastembed>=0.7.1" \
    "qdrant-client>=1.10.0" \
    "voyageai>=0.3.0" \
    "redis[hiredis]>=5.0.0" \
    "pydantic-settings>=2.1.0" \
    "python-dotenv>=1.0.0" \
    "numpy>=1.24.0" \
    "opik>=0.1.0"

# Pre-download FastEmbed sparse model so it's baked into the image
RUN python -c "from fastembed import SparseTextEmbedding; SparseTextEmbedding('Qdrant/bm25')"

# Copy application code
COPY app/ ./app/

EXPOSE 8000

# $PORT is set by Railway; defaults to 8000 for local docker compose
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
