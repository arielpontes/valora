FROM python:3.11-slim

# Install uv
RUN pip install --no-cache-dir uv

WORKDIR /app

# Copy project metadata first for dependency installation
COPY pyproject.toml ./
# Install project dependencies
RUN uv sync --no-progress

# Copy the rest of the project
COPY . .

EXPOSE 8000
CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
