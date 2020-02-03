#!/bin/bash
set -e

pip install -r src/python/requirements.txt
pip install -r src/python/requirements_test.txt
pip install -r src/python/requirements_dev_tools.txt
black --check --line-length 120 src/python
flake8 src/python
pylint src/python/
safety check -r src/python/requirements.txt
bandit -r src/python
coverage run --source=src/python/example_pkg -m unittest2 src/python/tests/*.py
coverage report --fail-under=100
src/python/build.sh