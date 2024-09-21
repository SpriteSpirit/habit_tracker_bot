# Трекер полезных привычек (Backend)

### **Контекст**

В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и
искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился с запросом реализовать трекер
полезных привычек.

В рамках учебного курсового проекта реализована бэкенд-часть SPA веб-приложения.

### **Функционал**

Backend-часть приложения предоставляет API для взаимодействия с фронтом и Telegram-ботом.

Основные возможности:

* **Управление привычками:** добавление, редактирование, удаление привычек.
* **Интеграция с Telegram:** отправка уведомлений о задачах через бота.
* **Пагинация:** разделение данных на страницы для удобства отображения.
* **Валидация данных:** проверка корректности вводимых данных.
* **Управление правами доступа:** обеспечение безопасности данных пользователей.
* **Отложенные задачи:** использование Celery для планирования задач (например, отправки уведомлений).

### **Технологии**

* **Django:** фреймворк для разработки веб-приложений на Python.
* **Django REST Framework:** фреймворк для создания REST API.
* **Celery:** система для обработки отложенных задач.
* **Telegram Bot API:** API для взаимодействия с Telegram-ботом.
* **unittest:** фреймворк для тестирования.

### **Критерии приемки курсовой работы**

Проект соответствует следующим критериям:

1. [x] **CORS:** Настроен.
2. [x] **Telegram интеграция:** Настроена.
3. [x] **Пагинация:** Реализована.
4. [x] **Переменные окружения:** Использованы.
5. [x] **Модели:** Все необходимые модели описаны или переопределены.
6. [x] **Эндпоинты:** Все необходимые эндпоинты реализованы.
7. [x] **Валидаторы:** Все необходимые валидаторы настроены.
8. [x] **Права доступа:** Описанные права доступа заложены.
9. [x] **Отложенная задача (Celery):** Настроена.
10. [x] **Тестирование:** Проект покрыт тестами как минимум на 80%.
11. [x] **Стиль кода:** Код оформлен в соответствии с лучшими практиками.
12. [x] **Список зависимостей:** Имеется.
13. [x] **Flake8:** Результат проверки Flake8 равен 100% (исключая миграции, venv и E501).
14. [x] **GitHub:** Решение выложено на GitHub.

### **Установка и запуск**

**Предварительные условия:**

* Python 3.11
* PostgreSQL
* Poetry
* Redis
* Celery
* Postman

### Информация

Главное приложение проекта - **config**.

 ```  
    habit_tracker_bot/
    ├── config/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── celery.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── habits/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── permissons.py
    │   ├── serializers.py
    │   ├── services.py
    │   ├── tasks.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── validators.py
    │   └── views.py
    ├── users/
    │   ├── fixtures/
    │   ├── managements/
    │   │   ├── commands/
    │   │   │   ├── __init__.py
    │   │   │   └── csu.py
    │   │   └── __init__.py
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── admin.py
    │   ├── urls.py
    │   └── views.py
    ├── .env_example
    ├── .gitignore
    ├── celerybeat-schedule.db
    ├── manage.py
    ├── poetry.lock
    ├── poetry.toml
    └── README.md
```


### Установка:

1. **Клонирование репозитория:**

```powershell
   git clone <репозиторий_GitHub>
   cd <название_репозитория>
```

2. **Установка poetry:**

```bash 
   pip install poetry
```

3. **Установка зависимостей:**

```bash 
   poetry install
```

4. **Настройка переменных окружения:**

Создайте файл .env в корне проекта и заполните его переменными по шаблону **.env_example:**

```
DATABASE_URL=<URL_для_подключения_к_PostgreSQL>
SECRET_KEY=<секретный_ключ>
...
```

5. **Создание базы данных:**

```bash 
  python manage.py migrate
```

6. **Создание администратора:**

```bash 
  python manage.py csu
```

7. **Запуск сервера разработки:**

```bash 
   python manage.py runserver
```

8. **Запуск Celery (для отложенных задач Windows):**

```bash
   celery -A config worker -l info -P gevent
```

9. **Запуск Flower (для мониторинга Celery задач):**

```bash
   celery -A config flower --port=5555
```

### Тестирование

В проекте используются фикстуры, которые подгружают информацию в тесты:

- 3 пользователя:
    - администратор
    - модератор
    - пользователь
- 3 привычки

Для запуска тестов используйте следующую команду:

```bash
   python manage.py test
```

Для проверки покрытия тестами используйте coverage:

```bash
   coverage run --source='.' manage.py test
```

```bash
   coverage report
```
### PEP8
**Для формирования отчета при помощи flake8-html выполните команду:**
```bash
  flake8 --format=html --ignore=migrations/,venv/,E501 --htmldir=flake8_report ./
```

**--format=html** - параметр, указывающий на тип формата отчета

**--ignore=migrations/,venv,E501** - параметр принимает: игнорируемые директории, файлы, коды ошибок

**--htmldir=flake8_report ./** - параметр для создания директории с отчетом

**./** - это корневая директория проекта для создания папки flake8_report

**index.html** - файл с отчетом

### Развертывание с помощью Docker и Docker Compose
Этот проект можно легко развернуть с помощью Docker и Docker Compose. Для этого необходимо установить Docker и Docker Compose на вашей системе.

1. **Создайте файлы Dockerfile и docker-compose.yaml в корне проекта:**
#### Dockerfile
 - описывает шаги для создания образа Docker для приложения Django, используя Poetry для управления зависимостями:

```dockerfile
FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry==1.8.3 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache, artifacts}

COPY . .

RUN apt-get update && apt-get install -y procps netcat curl && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y netcat

# Копируем и устанавливаем точку входа
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

```
#### Docker Compose
Файл `docker-compose.yaml` описывает сервисы, необходимые для запуска приложения, включая Django, PostgreSQL, Redis и Celery:
    
```yaml
services:
  db:
    image: postgres:16
    restart: always
    env_file:
      - .env
    environment:
      POSTGRES_DB: ${DATABASE_NAME}
      POSTGRES_USER: ${DATABASE_USER}
      POSTGRES_PASSWORD: ${DATABASE_PASSWORD}
      PGDATA: /var/lib/postgresql/data/pgdata
    volumes:
      - db_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DATABASE_USER} -d ${DATABASE_NAME}"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:alpine
    restart: always
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 5s
      retries: 5

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    restart: always
    volumes:
      - .:/app
    ports:
      - "8090:8000"
    env_file:
      - .env
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    healthcheck:
      test: [ "CMD-SHELL", "pgrep -f runserver || exit 1" ]
      interval: 20s
      timeout: 10s
      retries: 5

  celery_worker:
    build: .
    command: celery -A config worker -l info
    restart: always
    volumes:
      - .:/app
    env_file:
      - .env
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
      web:
        condition: service_healthy

  celery_beat:
    build: .
    command: celery -A config beat -l info -S django
    restart: always
    volumes:
      - .:/app
    env_file:
      - .env
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
      web:
        condition: service_healthy

volumes:
  db_data:

```
2. **Запустите контейнеры Docker Compose:**

   ```bash
   docker-compose up --build
   ```

   Этот процесс создаст и запустит все необходимые контейнеры. Для запуска в фоновом режиме используйте:

   ```bash
   docker-compose up --build -d
   ```

3. **Примените миграции Django:**
 ```bash
   docker-compose exec app python manage.py migrate
   ```

4. **Приложение будет доступно по адресу `http://localhost:8000`.**

## Остановка и очистка

- **Остановить контейнеры:**

  ```bash
  docker-compose down
  ```

- **Очистить тома данных (если используются):**

  ```bash
  docker-compose down -v
  ```

## Примечания

- Убедитесь, что у вас установлен Docker и Docker Compose.
- Измените `your_password` в файле `.env` на свой пароль для PostgreSQL.
- Вы можете остановить контейнеры с помощью команды `docker-compose down`.
- Убедитесь, что порты, используемые в `docker-compose.yaml`, свободны на вашем хосте.
- Для доступа к базе данных PostgreSQL внутри контейнера используйте `docker-compose exec db psql -U your_db_user your_db_name`.
- Для просмотра логов Celery или Django используйте `docker-compose logs -f celery` или `docker-compose logs -f app`.

## Дополнительно

- **Резервное копирование данных:** Регулярно создавайте резервные копии данных PostgreSQL, если это необходимо.
- **Обновления:** Время от времени обновляйте образы Docker и зависимости проекта для безопасности и производительности.
- **Poetry:** Убедитесь, что версия Poetry, указанная в Dockerfile, совпадает с той, что используется в вашем проекте для избежания конфликтов зависимостей.



### **Автор**

```Халуева Ангелина||Sprite_Spirit```
