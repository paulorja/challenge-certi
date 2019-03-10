FROM python:3

RUN pip install coverage

RUN mkdir -p /app
WORKDIR /app
COPY . /app

EXPOSE 8080



