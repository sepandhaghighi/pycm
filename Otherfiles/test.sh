  set -e
  set -x
  python -m pytest Test --cov=pycm --cov-report=term
  python Otherfiles/version_check.py

  #Check if we are in TRAVIS
  isInTRAVIS=false
  if [ "$CI" = 'true' ] && [ "$TRAVIS" = 'true' ]
  then
      isInTRAVIS=true
  fi

  if [ "$isInTRAVIS" = 'false' ] || { [ "$isInTRAVIS" = 'true' ] && [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]; }
  then
      python -m vulture pycm/ Otherfiles/ setup.py --min-confidence 65 --exclude=build,.eggs --sort-by-size
      python -m bandit -r pycm -s B311
      python -m pydocstyle --match-dir=pycm
  fi
  python -m cProfile -s cumtime pycm/pycm_profile.py
