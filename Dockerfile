FROM python:3


WORKDIR /usr/src/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requirements.txt ./
COPY . .


RUN apt-get update &&\
    pip install --no-cache-dir -r requirements.txt

ADD entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
RUN python manage.py createsuperuser --username admin --password $PASSWORD
ENTRYPOINT /entrypoint.sh
