  set -e
  set -x
  python -m pytest Test --cov=pycm --cov-report=term
  python Otherfiles/version_check.py
  if [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]
  then
      python -m vulture --min-confidence 80 --exclude=pycm,build,.eggs --sort-by-size
      python -m bandit -r pycm -s B311
      python -m pydocstyle --match-dir=pycm
  fi
  python -m cProfile -s cumtime pycm/pycm_profile.py
