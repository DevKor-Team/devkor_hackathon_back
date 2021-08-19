FROM ubuntu:18.04

USER root
RUN apt-get update && \
  apt-get install -y python3-dev python3-pip python3-setuptools

ADD ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip3 install pip --upgrade
RUN pip3 install setuptools-rust
RUN pip3 install -r requirements.txt

ADD . /app

RUN ["chmod",  "+x", "/app/build/app/start.sh"]
ENTRYPOINT ["sh", "/app/build/app/start.sh"]
