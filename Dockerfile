# Базовый образ
FROM mcr.microsoft.com/playwright/python:v1.31.0-focal

# Создание рабочей директории внутри контейнера
WORKDIR /app

# Установка зависимостей Python
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копирование остальных файлов проекта внутрь контейнера
COPY . .

# Запуск тестов
CMD [ "pytest", "-v" ]
