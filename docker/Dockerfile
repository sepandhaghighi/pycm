FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  software-properties-common \
  && \
  rm -rf /var/lib/apt/lists/*
RUN add-apt-repository ppa:jonathonf/python-3.6 && apt-get update
RUN apt-get install -y \
  git \
  python3.6-dev \
  python3-pip \
  sudo \
  && rm -rf /var/lib/apt/lists/*

# Add user with valid passwrd
RUN useradd -ms /bin/bash user
RUN (echo user ; echo user) | passwd user

# Configure sudo
RUN usermod -a -G sudo user

# Install necessary python libraries
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 setup.py

USER user
WORKDIR /home/user
RUN python3.6 -m pycm

ENTRYPOINT /bin/bash