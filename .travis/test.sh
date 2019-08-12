#!/bin/bash
  set -e
  set -x
  IS_IN_TRAVIS=false
  PYTHON_COMMAND=python
  
  if [ "$TRAVIS_OS_NAME" == "osx" ]
  then
	PYTHON_COMMAND=python3
  fi
  $PYTHON_COMMAND -m pytest Test --cov=pycm --cov-report=term
  $PYTHON_COMMAND Otherfiles/version_check.py
  $PYTHON_COMMAND -m cProfile -s cumtime pycm/pycm_profile.py
  
  if [ "$CI" = 'true' ] && [ "$TRAVIS" = 'true' ]
  then
      IS_IN_TRAVIS=true
  fi

  if [ "$IS_IN_TRAVIS" = 'false' ] || [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]
  then
      $PYTHON_COMMAND -m vulture pycm/ Otherfiles/ setup.py --min-confidence 65 --exclude=build,.eggs --sort-by-size
      $PYTHON_COMMAND -m bandit -r pycm -s B311
      $PYTHON_COMMAND -m pydocstyle --match-dir=pycm
  fi

