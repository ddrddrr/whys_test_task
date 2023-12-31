﻿FROM python:3.9.17

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY shop_project shop_project
WORKDIR shop_project

CMD python manage.py makemigrations; python manage.py migrate; python manage.py runserver 0.0.0.0:8000

