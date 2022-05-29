
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
