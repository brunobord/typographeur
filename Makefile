test: install-test
	flake8 && pytest --cov typographeur --cov-report term-missing

install-test:
	pip install --ignore-installed -e .[test]

ligatures:
	cd assets; python extract_ligatures.py
