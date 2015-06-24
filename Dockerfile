FROM python:3.4.3

MAINTAINER freefood89

RUN apt-get update && apt-get install -y \
	git \
	vim

RUN mkdir /fishtank
VOLUME /fishtank
WORKDIR /fishtank
EXPOSE 8080

CMD pip3 install -r requirements.txt && \
	python3 app.py --log=debug
