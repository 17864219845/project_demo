FROM python:3.12-slim-bookworm AS base

WORKDIR /app/api

ENV UV_VERSION=0.7.13

RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple uv==${UV_VERSION}

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ libc-dev libffi-dev curl \
    libsqlite3-0 zlib1g \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

ENV UV_VENV=off
COPY pyproject.toml uv.lock ./
RUN uv sync --locked

ENV TZ=UTC

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["bash", "/entrypoint.sh"]
