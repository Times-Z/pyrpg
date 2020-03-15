
FROM python:3.8.1-slim

RUN pip3 install requests && pip3 install colorama

COPY ./app /app
WORKDIR /app

EXPOSE 8080

CMD [ "python3", "/app/main.py" ]