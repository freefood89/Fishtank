FROM python:3.4.3

MAINTAINER freefood89

RUN apt-get update && apt-get install -y \
	git \
	vim

RUN mkdir /Fishtank
WORKDIR /Fishtank

RUN git clone -b docker-compose https://github.com/freefood89/fishtank .

RUN pip3 install -r requirements.txt
