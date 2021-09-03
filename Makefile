install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
format:
	black *.py
	
lint:
	pylint --disable=R.C oddoreven.py
	
test:
	python -m pytest -vv --cov=oddoreven test_oddoreven.py -s