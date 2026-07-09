# Use Python 3.11 slim for a lean, production-ready image
FROM python:3.11-slim

# Metadata labels
LABEL maintainer="Yashwant (Member 5 — Security & Reporting Lead)"
LABEL description="ROCm Navigator Security & Reporting Microservice"
LABEL version="1.0.0"

# ── Environment setup ──────────────────────────────────────
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    NAVIGATOR_ENV=production

# ── System dependencies ────────────────────────────────────
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ── Non-root user for security best practice ──────────────
RUN groupadd --gid 1001 navigator && \
    useradd --uid 1001 --gid navigator --shell /bin/bash --create-home navigator

# ── Working directory ──────────────────────────────────────
WORKDIR /app

# ── Install Python dependencies ────────────────────────────
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install pytest httpx

# ── Copy source code ───────────────────────────────────────
COPY --chown=navigator:navigator . .

# ── Create necessary directories ───────────────────────────
RUN mkdir -p reports shared/database && \
    chown -R navigator:navigator /app

# ── Switch to non-root user ────────────────────────────────
USER navigator

# ── Expose API port ────────────────────────────────────────
EXPOSE 8000

# ── Health check ───────────────────────────────────────────
HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/')" || exit 1

# ── Default command ────────────────────────────────────────
CMD ["python", "-m", "uvicorn", "services.security-audit.app:app", \
     "--host", "0.0.0.0", "--port", "8000", "--reload"]
