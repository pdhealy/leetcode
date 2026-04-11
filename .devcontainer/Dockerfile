FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    ca-certificates \
    curl \
    bash \
    && rm -rf /var/lib/apt/lists/*