FROM python:3.9.17

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ../work_please/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ../work_please/shop_project .
EXPOSE 8000
WORKDIR /app

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
