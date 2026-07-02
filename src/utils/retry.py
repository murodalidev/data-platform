"""Standard retry decorator. Use this everywhere — never hand-rolled retry loops."""
from tenacity import retry, stop_after_attempt, wait_exponential


def with_retries(attempts: int = 3):
    """Exponential-backoff retry decorator for I/O calls (APIs, DB)."""
    return retry(
        stop=stop_after_attempt(attempts),
        wait=wait_exponential(multiplier=1, min=2, max=30),
        reraise=True,
    )
