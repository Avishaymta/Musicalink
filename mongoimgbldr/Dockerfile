## Comments left for peer combing over
## Delete them when done for cleanliness

FROM ubuntu:22.04
ENV DOCKER_HOSTNAME="demo_mongodb1"

SHELL ["/bin/bash", "-c"]
USER root

WORKDIR /

COPY . .
RUN chmod 777 *.sh

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

## Terminal
ENV TERM=xterm

## MongoDB Install (Adds repo, key and installs app)
RUN curl -fsSL https://pgp.mongodb.com/server-7.0.asc | \
    gpg --dearmor | \
    sudo tee /etc/apt/trusted.gpg.d/mongodb-server-7.0.gpg && \
    echo "deb [ arch=amd64] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | \
    sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list && \
    sudo apt-get update && \
    sudo apt-get install -y mongodb-org

## Entrypoint; how the container starts
## Start mongod with config (default)
## Straight after; tail the logs and pipe into jq for pretty print (MongoDB logs are messy JSONs)
CMD /run.sh