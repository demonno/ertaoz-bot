install:
	pip install -U pip
	pip install -r requirements.txt

fmt: # Run formatter
	isort bots dal
	black bots dal

lint: # Run linters
	isort --check bots dal
	black --check bots dal
	flake8 bots,dal
