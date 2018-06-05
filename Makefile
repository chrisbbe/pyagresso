#!make

# load environment variables
include .env
export $(shell sed 's/=.*//' .env)

# declare constant(s)
TEST_PATH=./tests/


all: test

clean:
	rm -rf .pytest_cache/
	rm -rf __pycache__/
	rm -rf *.egg-info
	rm -rf build/
	rm -rf dist/

debug: clean
	pytest --pdb --color=yes $(TEST_PATH)

test: clean
	pip install -e .
	pytest --verbose --color=yes $(TEST_PATH)

build:
	python setup.py sdist
	python setup.py bdist_wheel --universal

upload:
	twine upload dist/*

release: test build upload