"""MiniMax — official API pricing in CNY."""

from scraper_base import BaseScraper


class MiniMaxScraper(BaseScraper):
    provider_name = "MiniMax"
    category = "domestic-official"

    _MODELS = [
        ("MiniMax M1", "MiniMax", 0.73, 2.90),
        ("MiniMax M1-Lite", "MiniMax", 0.36, 1.45),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = MiniMaxScraper()
