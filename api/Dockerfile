FROM python:3.12-slim-bookworm AS base

WORKDIR /app/api

ENV UV_VERSION=0.7.13
ENV UV_VENV=off
ENV TZ=UTC

# 安装依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ libc-dev libffi-dev curl libsqlite3-0 zlib1g \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 安装 uv
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple uv==${UV_VERSION}

# 安装依赖前先拷贝依赖文件（提高缓存效率）
COPY pyproject.toml poetry.lock ./
RUN uv sync --locked

# 再拷贝源码
COPY . ./

# 拷贝并授权 entrypoint
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["bash", "/entrypoint.sh"]
