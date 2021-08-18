FROM ubuntu:18.04

USER root
RUN apt-get update && \
  apt-get install -y python3-dev python3-pip python3-setuptools
ADD ./requirements.txt /home/ec2-user/hackathon/back/requirements.txt
WORKDIR /home/ec2-user/hackathon/back
RUN pip3 install pip --upgrade
RUN pip3 install setuptools-rust
RUN pip3 install -r requirements.txt
ADD . /home/ec2-user/hackathon/back


RUN ["chmod",  "+x", "/home/ec2-user/hackathon/back/build/app/start.sh"]
ENTRYPOINT ["/home/ec2-user/hackathon/back/build/app/start.sh"]
