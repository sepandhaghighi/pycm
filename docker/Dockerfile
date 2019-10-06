FROM ubuntu:16.04

RUN apt-get update && apt-get install -y --no-install-recommends \
  software-properties-common=0.96.20.8 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update && apt-get install -y --no-install-recommends \
  git=1:2.7.4-0ubuntu1.6 \
  python3.6-dev=3.6.8-1~16.04.york1 \
  python3-pip=8.1.1-2ubuntu0.4 \
  sudo=1.8.16-0ubuntu1.7 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Add user with valid passwrd
RUN useradd -ms /bin/bash user
RUN (echo user ; echo user) | passwd user

# Configure sudo
RUN usermod -a -G sudo user

# Install necessary python libraries
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install pycm

USER user
WORKDIR /home/user
RUN python3.6 -m pycm test
RUN python3.6 -m pycm

ENTRYPOINT /bin/bash