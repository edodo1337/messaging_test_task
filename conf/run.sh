#!/usr/bin/env sh
sleep 1
python3 ./manage.py makemigrations
python3 ./manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell
gunicorn --forwarded-allow-ips=* --bind 0.0.0.0:8000 -w 2 app.wsgi:application
