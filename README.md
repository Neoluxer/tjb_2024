# django-aiogram-template (tjb_2024)

Шаблон для создания Telegram-бота на AIOgram с админкой Django.


## Запуск
- скачайте проект
- файл ".env.dist" переименуйте в ".env" и пропишите необходимые настройки
- выполните команды (должен быть запущен Docker):
```bash
# смонтировать контейнер:
docker-compose build
# запустить контейнер:
docker-compose up -d
# остановить контейнер:
docker-compose down
# если в код были внесены изменения, необходимо заново смонтировать контейнер
```
## Переключение из локальной отладочной версии к Докер версии
- Поменять настройки в файлах .env и settings.py
- Запустить "C:\REDIS\redis-server.exe" от имени администратора(Для локальной версии)
- Запустить bot.py  Telegram bot(Для локальной версии)
- Запустить сервер Django (Для локальной версии)
- Запустить Docker (Для Docker версии) + смонтировать и запустить контейнер (стр 11-17)
```bash
python manage.py runserver
```
http://127.0.0.1:8000/admin/


```bash
.env
#POSTGRES_DB = django_db (30) Docker
POSTGRES_DB = new_database # Local
REDIS_HOST=localhost # Local
#REDIS_HOST=redis (16) Docker
dj_ac/settings.py
#POSTGRES_HOST = "db" (95) Docker
POSTGRES_HOST = "localhost" # Local
tgbot/handlers/echo.py 
"19" # Изменить IP
tgbot/handlers/add_profit.py
"71" # Изменить IP
```

## Миграции
Команды выполняются при запущенном контейнере
```bash
# создание миграций
docker-compose exec web sh -c "python manage.py makemigrations"
# применение миграций
docker-compose exec web sh -c "python manage.py migrate"
# синхронизация с БД
docker-compose exec web sh -c "python manage.py migrate --run-syncdb"
# создание суперпользователя
docker-compose exec web sh -c "python manage.py createsuperuser"
```

Теперь можно перейти на http://0.0.0.0:8000/admin/ и войти в админку под суперпользователем

## Просмотр БД через Adminer
Посетите http://localhost:8080/ и введите следующие параметры:
- System: PostgreSQL
- Server: db
- Username: postgres
- Password: postgres
- Database: template-db

## Подключение к Django admin удаленной по ip к серверу на Raspberry Pi
http://192.168.31.150:8000/admin/
0. sudo ifconfig
1. В ipconfig посмотреть wlan0

```bash
sudo ifconfig
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install apache2 php5 liba
sudo service apache2 restart
sudo service apache2 status
sudo service apache2 start

```
3. Логин и пароль задаются 

```bash
docker-compose exec web sh -c "python manage.py createsuperuser"
```