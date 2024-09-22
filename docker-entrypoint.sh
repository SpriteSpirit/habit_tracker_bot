#!/bin/bash

echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 1
done

# Применяем миграции в БД
echo "Apply database migrations"
python manage.py migrate

# Создаем суперпользователя
echo "Create superuser admin@localhost - admin"
python manage.py csu

# Выполняем команду, переданную в контейнер (определяется в docker-compose)
exec "$@"
