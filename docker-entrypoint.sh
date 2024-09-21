#!/bin/bash

echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 1
done

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Apply database migrations
echo "Create superuser admin@localhost - admin"
python manage.py csu

# Выполняем команду, переданную в контейнер (определяется в docker-compose)
exec "$@"
