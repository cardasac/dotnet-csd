deploy:
	eb init -p python-3.11 --region eu-west-1 csd
	eb deploy staging

clone:
	eb init -p python-3.11 --region eu-west-1 csd
	eb clone -n tmp-dev staging

local:
	docker build -t csd .
	docker run -p 80:80 csd

SRC := src app.py

check-format:
	poetry run black --line-length=79 --check $(SRC)

lint:
	poetry run ruff $(SRC)
	poetry run semgrep scan --config auto

format:
	poetry run black --line-length=79 $(SRC) tests
	poetry run docformatter --in-place -r $(SRC)
	poetry run sourcery review --fix $(SRC) tests
	poetry run ruff --fix .

update-deps:
	poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev,test