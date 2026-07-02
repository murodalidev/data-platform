"""Central config: reads configs/<env>.yml + env vars. Never read env vars ad-hoc elsewhere."""

import os
from functools import lru_cache
from pathlib import Path

import yaml

CONFIG_DIR = Path(__file__).resolve().parents[2] / "configs"


@lru_cache
def get_config() -> dict:
    """Load YAML config for the current APP_ENV (default: dev)."""
    env = os.environ.get("APP_ENV", "dev")
    with open(CONFIG_DIR / f"{env}.yml") as f:
        return yaml.safe_load(f)
