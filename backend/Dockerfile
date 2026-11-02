FROM python:3.12-slim

# uv, el gestor que usas en local
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Primero solo las dependencias: así Docker reutiliza esta capa si no cambian
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# Los ejecutables del entorno virtual quedan disponibles en el PATH
ENV PATH="/app/.venv/bin:$PATH"

COPY . .

# Aplica las migraciones y arranca la API en el puerto que asigne Render
CMD ["sh", "-c", "alembic upgrade head && fastapi run main.py --host 0.0.0.0 --port ${PORT:-8000}"]