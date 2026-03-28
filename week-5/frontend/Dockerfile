FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    "streamlit>=1.53.0" \
    "requests>=2.31.0"

COPY app.py ./app.py

EXPOSE 8501

# $PORT is set by Railway; defaults to 8501 for local docker compose
CMD streamlit run app.py --server.port=${PORT:-8501} --server.address=0.0.0.0 --server.headless=true --server.fileWatcherType=none --browser.gatherUsageStats=false
