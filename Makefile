lint:
	pip install -r requirements.txt
	flake8 src
	pylint src
	mypy src

format:
	pip install -r requirements.txt
	black --verbose --config black.toml src
	isort src/**/*.py