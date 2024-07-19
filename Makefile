VENV=.venv
PYTHON=${VENV}/bin/python3
DEPS_DEV=requirements-dev.txt

${VENV}:
	python3 -mvenv ${VENV}

build: ${VENV}
	${PYTHON} -mpip install -r ${DEPS_DEV}
	${PYTHON} -mbuild

test: ${VENV}
	${PYTHON} -mpip install -r ${DEPS_DEV}
	${PYTHON} -mtox

clean:
	rm -rf dist *.egg-info .tox .mypy_cache .pytest_cache .venv