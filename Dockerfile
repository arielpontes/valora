FROM python:3.12-slim

# Install uv
RUN pip install --no-cache-dir uv

WORKDIR /app

# Copy project metadata first for dependency installation
COPY pyproject.toml uv.lock ./

# Install project dependencies
RUN uv sync --no-progress

# Copy the rest of the project
COPY . .
RUN uv sync --no-progress

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
