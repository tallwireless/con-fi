FROM centos:7

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

RUN yum update -y && yum upgrade -y

RUN yum install -y epel-release
RUN yum install -y python36 python36-devel \
                   python36-pip postgresql-devel \
                   gcc nginx
RUN yum install -y vim

RUN mkdir -p /run/nginx

WORKDIR /home/docker
COPY . .

RUN pip3 install -r reqs.txt

EXPOSE 5000
CMD ["flask","run"]
