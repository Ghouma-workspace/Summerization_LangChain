install:
	pip install --upgrade pip &&\
		pip install -e .

inference-streamlit:
	streamlit run stream-chat/app.py

test:
	python -m pytest -vv --cov=summarization_inference --cov=summarization_lib tests

debug:
	python -m pytest -vv --pdb # invoke debugger

inference-test:
	python -m pytest -vv tests/test_summarization_inference.py::TestSummarizationInference::test_main

format:
	black *.py

lint:
	pylint --disable=R,C summarization_inference.py tests summarization_lib

all: install lint test format