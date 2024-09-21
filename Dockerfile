FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN groupadd --gid 1001 app && useradd --uid 1001 --gid 1001 --shell /bin/bash --create-home app

COPY poetry.lock pyproject.toml ./
RUN python -m pip install --no-cache-dir poetry==1.8.3 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache, artifacts}

COPY . .

USER app

# Улучшение: создание не привилегированного пользователя
# Улучшение: использование slim-buster для уменьшения размера образа
# Улучшение: явно указание gid и uid для пользователя

# Добавить COPY для статических файлов (если есть)
# Добавить команду для сбора статических файлов

# Добавлен этап очистки, удаление лишних файлов после сборки.
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 8000