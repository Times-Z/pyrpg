FROM debian:buster-slim

RUN apt-get update \
&& apt-get -y install software-properties-common \
&& apt-get update \
&& apt-get -y install python3 \
&& apt-get -y install python3-pip \
&& pip3 install colorama

RUN echo "alias alias start='python3 /app/main.py'" >> ~/.bash_profile

COPY ./app /app
WORKDIR /app