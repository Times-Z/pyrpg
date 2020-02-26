
FROM python:3.8.1-slim

RUN pip3 install colorama

COPY ./app /app
WORKDIR /app

CMD ["python3", "./main.py"]
