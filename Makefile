install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

format:	
	black *.py 

test:
	python -m pytest -vv --cov=main test_*.py

#container-lint:
	#docker run --rm -i hadolint/hadolint < Dockerfile

#refactor: format lint

#deploy:
	#deploy goes here
		
all: install lint format test
