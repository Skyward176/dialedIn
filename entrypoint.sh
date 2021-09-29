#!/bin/bash

echo "Docker container started"

echo "SHELL=/bin/bash"

gunicorn dialedIn.wsgi:application --bind 0.0.0.0:$PORT
