lint-all: 
	poetry run isort clickr test
	poetry run flake8 clickr test
	poetry run pylint clickr test --disable=missing-docstring
	
