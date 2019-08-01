#!/bin/bash
  set -e
  set -x
  
  if [ "$TRAVIS_OS_NAME" == "osx" ]
  then
      pip3 install -r requirements.txt
      python3 setup.py install
      python3 -m pycm test
      python3 -m pycm
	  pip3 install --upgrade --upgrade-strategy=only-if-needed -r dev-requirements.txt --user
  else
	  pip install -r requirements.txt
      python setup.py install
      python -m pycm test
      python -m pycm
	  pip install --upgrade --upgrade-strategy=only-if-needed -r dev-requirements.txt
  fi

