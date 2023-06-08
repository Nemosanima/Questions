# Questions

## Инструкция по локальному запуску

#### Клонируйте проект
```
git clone https://github.com/Nemosanima/Questions.git
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

## Краткий обзор

#### Создать вопросы в базе данных. http метод post
```
http://localhost/questions
```
```
# Request body
{
  "questions_num": 1
}
```
Ответом на запрос будет предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.