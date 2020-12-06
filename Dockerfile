
FROM python:3.8.1-slim

RUN pip3 install requests && pip3 install colorama && pip3 install websocket debugpy python-dotenv

COPY ./app /app
WORKDIR /app

EXPOSE 8080
EXPOSE 5678

CMD [ "python3", "/app/main.py" ]
