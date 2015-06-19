FROM docker.io/centos

MAINTAINER cherryskyj@gmail.com

RUN yum install -y pip

RUN pip install tornado

RUN mkdir /testservice

COPY . /testservice

EXPOSE 8888

WORKDIR /testservie

CMD /usr/bin/python2 tornado_exaple.py

