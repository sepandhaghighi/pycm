#!/bin/bash
  set -e
  set -x
  IS_IN_TRAVIS=false
  if [ "$CI" = 'true' ] && [ "$TRAVIS" = 'true' ]
  then
      IS_IN_TRAVIS=true
  fi

  if [ "$IS_IN_TRAVIS" = 'false' ] && [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]
  then
      python -m vulture pycm/ Otherfiles/ setup.py --min-confidence 65 --exclude=build,.eggs --sort-by-size
      python -m bandit -r pycm -s B311
      python -m pydocstyle --match-dir=pycm
  fi
  
  if [ "$TRAVIS_OS_NAME" == "osx" ]
  then
	python3 -m pytest Test --cov=pycm --cov-report=term
	python3 Otherfiles/version_check.py
	python3 -m cProfile -s cumtime pycm/pycm_profile.py
  else
	python -m pytest Test --cov=pycm --cov-report=term
	python Otherfiles/version_check.py
	python -m cProfile -s cumtime pycm/pycm_profile.py
  fi

