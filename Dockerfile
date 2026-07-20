FROM python:3.14-slim AS base

# Install system deps
RUN apt-get update &&  \
    apt-get install -y --no-install-recommends curl build-essential  \
    && rm -rf /var/lib/apt/lists/*

# Install uv (Astral)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:/root/.cargo/bin:${PATH}"
ENV UV_LINK_MODE=copy
ENV UV_VENV_PATH=/opt/venv

WORKDIR /app
COPY pyproject.toml .
COPY README.md .
COPY uv.lock .

# Создаём venv ВНЕ /app и используем его
RUN uv venv /opt/venv
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:${PATH}"

# Ставим зависимости в /opt/venv (в активированное окружение)
RUN uv sync --frozen --no-editable

# Копируем проект
COPY . .

# На всякий случай доустановим проект (editable не обязателен в контейнере)
RUN uv sync --frozen

# Install project (editable) + ensure scripts
RUN uv sync --frozen

EXPOSE 8000
ENTRYPOINT ["uv", "run", "uvicorn", "app.main:app"]
CMD ["--host", "0.0.0.0", "--port", "8000"]
