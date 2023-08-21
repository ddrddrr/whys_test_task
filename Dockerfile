﻿FROM python:3.9.17

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY shop_project .
WORKDIR /app

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
