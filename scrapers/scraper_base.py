"""Base scraper class with HTTP client, retry logic, and unified output format."""

import time
import requests
from datetime import datetime, timezone
from config import REQUEST_TIMEOUT, MAX_RETRIES, RETRY_DELAY, USER_AGENT, USD_TO_CNY


class BaseScraper:
    """Base class for provider-specific scrapers.

    Subclasses must override:
      - provider_name: str
      - category: str  (one of: overseas-official, domestic-official, proxy)
      - fetch() -> list[dict]
    """

    provider_name: str = ""
    category: str = "proxy"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})

    def _get(self, url: str, **kwargs) -> requests.Response:
        """GET with retry logic."""
        for attempt in range(MAX_RETRIES):
            try:
                resp = self.session.get(url, timeout=REQUEST_TIMEOUT, **kwargs)
                resp.raise_for_status()
                return resp
            except requests.RequestException as e:
                if attempt == MAX_RETRIES - 1:
                    raise
                time.sleep(RETRY_DELAY * (attempt + 1))

    def _make_entry(self, model_name: str, series: str,
                    input_price_usd: float = None, output_price_usd: float = None,
                    input_price_cny: float = None, output_price_cny: float = None) -> dict:
        """Create a standardized pricing entry. Accepts either USD or CNY.

        If USD is provided, converts to CNY using the exchange rate.
        If CNY is provided directly, uses it as-is.
        """
        if input_price_cny is None and input_price_usd is not None:
            input_price_cny = round(input_price_usd * USD_TO_CNY, 2)
        if output_price_cny is None and output_price_usd is not None:
            output_price_cny = round(output_price_usd * USD_TO_CNY, 2)

        return {
            "model_name": model_name,
            "provider": self.provider_name,
            "category": self.category,
            "series": series,
            "input_price_cny": input_price_cny or 0,
            "output_price_cny": output_price_cny or 0,
            "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

    def fetch(self) -> list[dict]:
        """Scrape pricing data. Override in subclasses.

        Returns a list of pricing dicts in the standard format.
        """
        raise NotImplementedError
