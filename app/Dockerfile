FROM python:3.6.7

RUN mkdir /dockyard
COPY . /dockyard/
WORKDIR /dockyard
RUN pip install -r requirements.txt

RUN apt-get -y update
RUN apt-get install -y ffmpeg



