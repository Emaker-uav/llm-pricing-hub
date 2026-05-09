"""Shared configuration for all scrapers."""

from pathlib import Path

# USD to CNY exchange rate (approximate, update periodically)
USD_TO_CNY = 7.25

# Output path for the consolidated pricing JSON
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "data" / "pricing.json"

# HTTP request settings
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

# User-Agent for HTTP requests
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)
