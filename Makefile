.PHONY: setup test lint dbt-run dbt-test airflow-up airflow-down

setup:
	uv sync

test:
	uv run pytest tests/ -v

lint:
	uv run ruff check src/ dags/ tests/
	uv run ruff format --check src/ dags/ tests/
	uv run sqlfluff lint dbt/models/

dbt-run:
	cd dbt && dbt run --profiles-dir .

dbt-test:
	cd dbt && dbt test --profiles-dir .

airflow-up:
	docker compose up -d

airflow-down:
	docker compose down
