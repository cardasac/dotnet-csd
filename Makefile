deploy:
	eb init -p python-3.11 --region eu-west-1 csd
	eb deploy staging

clone:
	eb init -p python-3.11 --region eu-west-1 csd
	eb clone -n tmp-dev staging

run:
	flask --app app:create_app --debug run

local:
	docker build -t csd .
	docker run -p 8000:8000 -e FLASK_SECRET_KEY=$$(openssl rand -base64 32) csd

SRC := src app.py

check-format:
	poetry run ruff format --check

lint:
	poetry run ruff $(SRC)
	poetry run semgrep scan --config auto

format:
	poetry run ruff format
	poetry run sourcery review --fix $(SRC) tests
	poetry run ruff --fix .
	djlint --reformat src/templates/ --profile="jinja"
update-deps:
	poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev,test
