# t1

## Инструкция по локальному запуску

#### Клонируйте проект
```
git clone https://github.com/Nemosanima/t1.git
```
#### Создайте .env файл в корневой директории проекта с вашими данными. Например:
```
DB_ENGINE=postgresql
POSTGRES_USER=nemosanima
POSTGRES_PASSWORD=1n2nn3nnn
POSTGRES_DB=questions
DB_HOST=db
DB_PORT=5432
```
#### В корневой директории проект выполните команду
```
docker-compose up -d --build
```
#### Документация
```
http://localhost/docs  # Swagger
http://localhost/redoc # ReDoc
```