Перед запуском проэкта:
1) Создать виртуальное окружение virtualenv --python=python3.6 venv
2) Установить зависимостри pip install -r requerements.txt
3) Запустить docker-compose up
4) Создать пользователя в проекте с помощью python manage.py createsuperuser
5) Провести миграции python manage.py migrate
6) Запустить django с помощью python manage.py runserver 127.0.0.1:8080
7) Запустить celery с помощью команды celery -A transitionapi  worker -l info

Для раюботы с api нужно провести аунтентификацию

Аунтентификация на ходиться по сслыке:

http://127.0.0.1:8080/users/api-token-auth/

Метод: POST

Тело протокола: form-data

Тело:

username:admin@admin.com
password:qw123

В ответ api вышлет Token в формате json

```json
{
    "token": "59b883b52894d1802e9b733e3e1dddea0e9c2b0f"
}
```

Для подальшец работы с api необходимо поставить в заголовки с token слудующего вида

Authorization:Token 59b883b52894d1802e9b733e3e1dddea0e9c2b0f

Где Authorization - название заголовка
Token 59b883b52894d1802e9b733e3e1dddea0e9c2b0f - значение заголовка

Api для создание лимитов:

http://127.0.0.1:8080/incoming/proxy-project/

Пример данных

```json
{
	"name": "test_project",
	"endpoint": "http://127.0.0.1:8080/testendpoint/test/",
	"limits": [
		{
			"amount": "1000",
			"time_limit": 86400
		},
		{
			"amount": "1000",
			"time_limit": 3600
		},
		{
			"amount": "1000",
			"time_limit": 60
		},
		{
			"amount": "1000",
			"time_limit": 1
		}
	]
}
```

Параметры

name - название проетка
endpoint - ссылка на апи 
limits - массив объектов лимитов

Параметры limits:

amount - строка с значением суммы
time_limit - временной лимит задаваемый в секундах

Удалить созданные настрой можно по ссылке

http://127.0.0.1:8080/incoming/proxy-project/{id}

Указав заголовок DELETE

id - идентификатор настройки


Просмотреть все созданные точки api можно по ссылке
http://127.0.0.1:8080/incoming/proxy-project/

Указав метод GET

Для публикации сообщения используеться ссылка 
http://127.0.0.1:8080/incoming/send-message/

Метод POST
Тело в формате json

Примет тела: 

```json
{
	"proxy_project": "test_project",
	"amount": "1000",
	"request_data": {
		"card_id": "stripe_zaxcnjja11",
		"amount": "1000" 
	}
}
```

Где proxy_project - название проекта
amount - сумма
request_data - объект данных для передачи

Пример ответа от api

```json
{
    "id": "d040ebbd-0a13-468a-a458-809191e9686e",
    "created_time": "2019-11-05T11:05:45.734315Z",
    "delivered_time": null,
    "proxy_project": "test_project",
    "response_message": null,
    "amount": 1000.0,
    "request_data": {
        "card_id": "stripe_zaxcnjja11",
        "amount": "1000"
    },
    "status": "processing"
}
```

Сообщение передаеться в очередь на обработку

Проверить статус сообщения можно с помощью ссылки  http://127.0.0.1:8080/incoming/message/{uuid_message}

Где uuid_message - id сообщения