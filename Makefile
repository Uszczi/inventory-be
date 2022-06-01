APP_PATH=src/inv

run:
	cd ${APP_PATH}/main && uvicorn app:app --reload --lifespan=off --host 0.0.0.0 --port 8010

###############################
#                             #
#      Requirements           #
#                             #
###############################
install-piptools:
	python -m pip install pip-tools

compile-deps: install-piptools
	python -m piptools compile --no-header "requirements/dev.in"
	python -m piptools compile --no-header "requirements/prod.in"

recompile-deps: install-piptools
	python -m piptools compile --no-header --upgrade "requirements/dev.in"
	python -m piptools compile --no-header --upgrade "requirements/prod.in"

sync-deps: install-piptools
	python -m piptools sync "requirements/dev.txt"
	python -m pip install -e .

##################
### Migrations ###
##################
makemigrations:
	cd ${APP_PATH}/models/alembic; alembic revision --autogenerate

migrate:
	cd ${APP_PATH}/models/alembic; alembic upgrade head
