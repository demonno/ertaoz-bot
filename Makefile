install:
	pip install -U pip
	pip install -r requirements.txt

fmt: # Run formatter
	isort src
	black src

lint: # Run linters
	isort --check src
	black --check src
	flake8 src
