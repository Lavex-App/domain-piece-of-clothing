all:
	poetry run isort domain_piece_of_clothing/ tests/
	poetry run black domain_piece_of_clothing/ tests/
	poetry run flake8 domain_piece_of_clothing/ tests/
	poetry run mypy domain_piece_of_clothing/ tests/ --install-types --non-interactive --show-error-codes
	poetry run pylint domain_piece_of_clothing/ tests/
	poetry run wily build domain_piece_of_clothing/
	poetry run wily diff -a --no-detail domain_piece_of_clothing/

style:
	isort domain_piece_of_clothing/
	black --line-length 120 domain_piece_of_clothing/

run:
	uvicorn domain_piece_of_clothing.main:app --host 0.0.0.0 --port 8002 --reload
