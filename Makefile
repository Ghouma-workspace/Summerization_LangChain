install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=summarization_inference --cov=summarization_lib tests

format:
	black *.py

lint:
	pylint --disable=R,C summarization_inference.py summarization_lib.py tests

all: install lint test format