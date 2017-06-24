FROM python:3.6.1-alpine
MAINTAINER Edward Leoni

RUN mkdir /app
WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

EXPOSE 5000