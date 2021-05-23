**Сборка и запуск проекта**
sudo cp example.env .env
sudo docker-compose -f docker-compose.yml build
sudo docker-compose -f docker-compose.yml up

Сваггер доступен по URL: localhost:8000/api/v1/swagger

Аутентификация через сваггер:
**/auth/** - получение токена, далее -> Authorize -> Value = Token {token}

**/register/** - регистрация

Запуск тестов:
python backend/manage.py test api 


