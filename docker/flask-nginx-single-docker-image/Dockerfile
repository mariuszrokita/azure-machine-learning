FROM ubuntu:latest

RUN apt-get update -y && \  
    apt-get install -y python3-pip python3-dev && \
    apt-get install -y uwsgi uwsgi-plugin-python3

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY app app
COPY . /

ENTRYPOINT [ "/bin/bash", "/launcher.sh"]  