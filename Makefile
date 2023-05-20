.PHONY: install isort black pip-audit serve sec csu lint

install:
	@poetry install
makemigrations:
	@poetry run src/agenda/manage.py makemigrations
migrate:
	@poetry run src/agenda/manage.py migrate
workers:
	cd src/agenda && poetry run ./manage.py runapscheduler
format:
	@poetry run isort src
	@poetry run black src
lint:
	@poetry run isort src --check
	@poetry run black src --check
sec:
	@poetry run pip-audit .
csu:
	@poetry run src/agenda/manage.py createsuperuser
serve:
	@poetry run src/agenda/manage.py runserver