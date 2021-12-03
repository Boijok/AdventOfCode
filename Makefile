install_mac_environment_in_local:
	@brew update
	pyenv --version || @brew install pyenv
	pyenv install -s 3.8.10
	pyenv local 3.8.10
	poetry --version || @brew install poetry
	poetry env use $(pyenv prefix)"/bin/python"
	poetry install
	poetry run pre-commit install
	echo "Your local environment is ready \!"

poetry_test:
	poetry run python -m pytest tests

typecheck:
	poetry run mypy src tests

coverage:
	poetry run coverage run -m pytest --with-snowflake
	poetry run coverage report -m
	poetry run coverage html
