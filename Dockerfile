FROM debian:buster-slim

RUN apt-get update \
&& apt-get -y install software-properties-common \
&& apt-get update \
&& apt-get -y install python3 \
&& apt-get -y install python3-pip \
&& pip3 install colorama

COPY ./app /app
WORKDIR /app