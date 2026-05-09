"""Longcat — Chinese LLM platform."""

from scraper_base import BaseScraper


class LongcatScraper(BaseScraper):
    provider_name = "Longcat"
    category = "domestic-official"

    _MODELS = [
        ("Longcat", "Longcat", 0.36, 1.45),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = LongcatScraper()
