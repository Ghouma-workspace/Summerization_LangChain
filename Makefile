install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=summarization_inference --cov=summarization_lib test_summarization_inference.py test_summarization_lib.py

format:
	black *.py

lint:
	pylint --disable=R,C summarization_inference.py summarization_lib.py test_summarization_inference.py test_summarization_lib.py

all: install lint test format