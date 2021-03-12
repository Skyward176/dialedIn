#!/bin/bash

echo "Docker container started"

echo "SHELL=/bin/bash"

service cron start && python manage.py crontab add

gunicorn dialedIn.wsgi:application --bind 0.0.0.0:$PORT