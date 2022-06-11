install:
	poetry install
build:
	poetry build
package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
gendiff:
	poetry run gendiff
lint:
	poetry run flake8 gendiff
