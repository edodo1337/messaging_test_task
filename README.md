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

**Чтобы попробывать отправить сообщение сначала зарегестрируйтесь через API**

Отправка сообщений:
**POST** /message/

При превышении лимита в 10 сообщений в минуту - срабатывает троттлинг,
если во время троттлинга попытаться написать более 10 сообщений - будет бан на 10 минут и сообщение в debug.log.



