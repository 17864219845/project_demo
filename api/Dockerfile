FROM python:3.12-slim-bookworm AS base

WORKDIR /app/api

# Install uv
ENV UV_VERSION=0.7.13

RUN pip install --no-cache-dir uv==${UV_VERSION}


FROM base AS packages

WORKDIR /app/api

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc g++ libc-dev libffi-dev curl libsqlite3-0 zlib1g \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY pyproject.toml uv.lock entrypoint.sh ./
RUN chmod +x entrypoint.sh
RUN uv sync --locked --active
COPY . /app/api

EXPOSE 5000

#ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
