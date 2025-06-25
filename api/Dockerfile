# 基础镜像
FROM python:3.12-slim-bookworm AS base

WORKDIR /app/api

ENV UV_VERSION=0.7.13

RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple uv==${UV_VERSION}

# build 阶段，安装编译依赖 + 运行时依赖 + 安装 Python 包
FROM base AS build-deps

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ libc-dev libffi-dev libgmp-dev libmpfr-dev libmpc-dev \
    curl libgmp-dev libmpfr-dev libmpc-dev \
    expat libldap-2.5-0 perl libsqlite3-0 zlib1g media-types libmagic1 \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./

RUN uv sync --locked --system

# 生产镜像，只安装运行时依赖
FROM base AS production

WORKDIR /app/api

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl libgmp-dev libmpfr-dev libmpc-dev \
    expat libldap-2.5-0 perl libsqlite3-0 zlib1g media-types libmagic1 \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/api/

ENV FLASK_APP=app.py
ENV TZ=UTC

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["bash", "/entrypoint.sh"]
