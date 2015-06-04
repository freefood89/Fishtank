FROM python:3.4.3

MAINTAINER freefood89

RUN apt-get update && apt-get install -y \
	git \
	vim

RUN git clone https://github.com/freefood89/fishtank ~/Fishtank

RUN pip3 install \
	flask \
	pillow \
	pymongo \
	tornado

CMD python3 ~/Fishtank/app.py --log=debug