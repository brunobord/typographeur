test: install-test
	flake8 && pytest

install-test:
	pip install -e .[test]

ligatures:
	cd assets; python extract_ligatures.py
