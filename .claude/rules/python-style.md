# Python Style Rules

- Python 3.12, type hints on ALL function signatures
- Use `pathlib.Path`, never string paths
- Use `pydantic` v2 models for all external data schemas (`src/extract/schemas/`)
- Logging via `src/utils/logging.py` — never `print()` in pipeline code
- Retries via `tenacity` decorator from `src/utils/retry.py` — never hand-rolled retry loops
- All I/O functions must accept an explicit connection/client parameter (dependency injection, testable)
- No `datetime.now()` in pipeline logic — pass `execution_date`/`logical_date` explicitly
- Config via `src/utils/config.py` (reads YAML from `configs/` + env vars) — never read env vars ad-hoc
- New extractors: subclass `BaseExtractor`, implement `extract() -> ExtractResult`
- Every public function needs a Google-style docstring with Args/Returns/Raises
