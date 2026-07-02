"""Base extractor: all source connectors subclass this."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class ExtractResult:
    """Raw rows plus extraction metadata for auditing."""

    rows: list[dict[str, Any]]
    row_count: int
    extracted_at: datetime
    source: str


class BaseExtractor(ABC):
    """Contract for all extractors. Must be idempotent for a given interval."""

    @abstractmethod
    def extract(self, start: datetime, end: datetime) -> ExtractResult:
        """Extract rows for [start, end). Never uses wall-clock time internally."""
        ...
