"""胜算云 — Chinese API proxy platform."""

from scraper_base import BaseScraper


class ShengSuanYunScraper(BaseScraper):
    provider_name = "胜算云"
    category = "proxy"

    _MODELS = [
        ("Claude Opus 4.7", "Claude", 115.00, 560.00),
        ("Claude Sonnet 4.6", "Claude", 23.00, 112.00),
        ("Claude Haiku 4.5", "Claude", 5.90, 29.50),
        ("GPT-4o", "GPT", 18.50, 74.00),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = ShengSuanYunScraper()
