#!/usr/bin/env bash

# run black
black --skip-string-normalization --line-length 120 tests
black --skip-string-normalization --line-length 120 src

# run python static validation
prospector --profile-path=. --profile=.prospector.yml --path=src --ignore-patterns=static

# run semgrep
semgrep --config p/python src

# run tests
py.test -n 4 --disable-socket -W error::RuntimeWarning --cov=src --cov-report=html --cov-fail-under=100 tests/
