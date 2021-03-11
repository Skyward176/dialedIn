FROM python:3

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN service cron start

COPY . .

CMD gunicorn dialedIn.wsgi:application --bind 0.0.0.0:$PORT
