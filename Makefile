test: install-test
	flake8 && pytest

install-test:
	pip install -e .[test]
