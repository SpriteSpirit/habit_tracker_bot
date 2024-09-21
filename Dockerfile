FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN addgroup --system app && adduser --system --group app

COPY poetry.lock pyproject.toml ./
RUN python -m pip install --no-cache-dir poetry==1.8.3 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache, artifacts}

COPY . .

USER app
