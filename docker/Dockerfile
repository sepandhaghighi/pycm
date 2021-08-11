FROM ubuntu:16.04

RUN apt-get update && apt-get install -y --no-install-recommends \
  software-properties-common \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y --no-install-recommends \
  git \
  python3.6 \
  python3.6-dev \
  python3-pip \
  sudo \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Add user with valid passwrd
RUN useradd -ms /bin/bash user
RUN (echo user ; echo user) | passwd user

# Configure sudo
RUN usermod -a -G sudo user

# Install necessary python libraries
RUN python3.6 -m pip install pip --upgrade
RUN sleep 80 && python3.6 -m pip install pycm

USER user
WORKDIR /home/user
RUN python3.6 -m pycm test
RUN python3.6 -m pycm

ENTRYPOINT /bin/bash