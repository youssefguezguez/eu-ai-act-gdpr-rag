# Slim image for the API (no torch): ~250 MB RAM at runtime, fits a 512 MB free instance.
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 \
    EMBED_BACKEND=onnx ONNX_DIR=/app/model ORT_THREADS=1
WORKDIR /app

COPY requirements-api.txt .
RUN pip install --no-cache-dir -r requirements-api.txt

# Official ONNX export of bge-small-en-v1.5, pinned revision, checksums verified
COPY scripts/fetch_onnx.py scripts/
RUN python scripts/fetch_onnx.py /app/model

COPY src/ src/
COPY web/ web/
COPY api.py .
COPY data/processed/chunks.jsonl data/processed/
COPY data/index/bge-small-en-v1.5/ data/index/bge-small-en-v1.5/

RUN useradd --create-home app
USER app
EXPOSE 8000
# Render sets $PORT; default 8000 elsewhere. GROQ_API_KEY comes from the host's secret store.
CMD ["sh", "-c", "uvicorn api:app --host 0.0.0.0 --port ${PORT:-8000} --proxy-headers --forwarded-allow-ips='*'"]
