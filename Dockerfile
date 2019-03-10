FROM python:3

RUN pip install coverage
RUN pip install requests

RUN mkdir -p /app
WORKDIR /app
COPY . /app

EXPOSE 8080

CMD ["python", "lib/http_server.py"]
