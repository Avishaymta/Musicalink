FROM ubuntu:22.04
ENV DOCKER_HOSTNAME="demo_musicalink_web1"

SHELL ["/bin/bash", "-c"]
USER root

WORKDIR /

COPY ../* .
RUN chmod 777 *.sh -R

## Replace shell to BAshell.
RUN rm -f /bin/sh
RUN ln -s /bin/bash /bin/sh

## Timezone for pesky GUI package installs
ENV DOCKER_HOSTNAME="demo"
RUN ln -snf /usr/share/zoneinfo/UTC /etc/localtime && echo UTC > /etc/timezone

## Basics
RUN apt-get update && \
    apt-get install -y \
        net-tools \
        lsof \
        sudo \
        curl \
        gpg \
        openssh-server \
        tzdata \
        jq

RUN apt-get update && \
    apt-get install -y \
    python3.11 \
    python3-pip 

RUN pip3 install -r requirements.txt


## Terminal
ENV TERM=xterm

CMD /run.sh