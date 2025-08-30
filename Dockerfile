FROM python:3.12-slim

RUN pip install --no-cache-dir uv

WORKDIR /app

# Copy metadata
COPY pyproject.toml uv.lock* ./

# Install dependencies (into .venv, but isolated inside container)
RUN uv sync --no-progress --all-groups

# Copy the rest of the code
COPY . .

# Re-run to install project in editable mode
RUN uv sync --no-progress --all-groups

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
