"""BaiLing (百灵) — Chinese AI platform."""

from scraper_base import BaseScraper


class BaiLingScraper(BaseScraper):
    provider_name = "BaiLing"
    category = "domestic-official"

    _MODELS = [
        ("BaiLing", "BaiLing", 0.00, 0.00),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = BaiLingScraper()
