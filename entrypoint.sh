#!/bin/bash

echo "Docker container started"

echo "SHELL=/bin/bash"

if [ -z "$SSH_CLIENT" ] && [ -n "$HEROKU_EXEC_URL" ];
then
    source <(curl --fail --retry 3 -sSL "$HEROKU_EXEC_URL")
fi

if [[ "$DYNO" =~ ^release.* ]];
then
    set -e
    python3 manage.py migrate
else
    exec gunicorn dialedIn.wsgi  -b 0.0.0.0:${PORT} --reload --access-logfile -
    exec python manage.py createsuperuser --username admin --password $PASSWORD
fi