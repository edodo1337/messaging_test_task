#!/usr/bin/env sh
sleep 1
python3 ./manage.py makemigrations
python3 ./manage.py migrate
gunicorn --forwarded-allow-ips=* --bind 0.0.0.0:8000 -w 2 app.wsgi:application
