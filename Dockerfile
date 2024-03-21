FROM python:2.7-alpine

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV DB_HOST=""
ENV DB_DATABASE=""
ENV DB_USER=""
ENV DB_PASSWORD=""

WORKDIR /app/text-map-api

CMD gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app