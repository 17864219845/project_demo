FROM python:3.12-slim-bookworm AS base

WORKDIR /app/api

# Install uv
ENV UV_VERSION=0.7.13

RUN pip install --no-cache-dir uv==${UV_VERSION}


FROM base AS packages


RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc g++ libc-dev libffi-dev

# Install Python dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --locked

# production stage
FROM base AS production

# set timezone
ENV TZ=UTC

WORKDIR /app/api

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl libsqlite3-0 zlib1g \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Copy Python environment and packages
ENV VIRTUAL_ENV=/app/api/.venv
COPY --from=packages ${VIRTUAL_ENV} ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

# Copy source code
COPY . /app/api/

# Copy entrypoint
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
