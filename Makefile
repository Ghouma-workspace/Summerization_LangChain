install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=summarization_inference --cov=summarization_lib tests

debug:
	python -m pytest -vv --pdb # invoke debugger

inference-test:
	python -m pytest -vv tests/test_summarization_inference.py::TestSummarizationInference::test_main

format:
	black *.py

lint:
	pylint --disable=R,C summarization_inference.py summarization_lib.py tests

all: install lint test format