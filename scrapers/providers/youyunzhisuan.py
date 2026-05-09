"""优云智算 — Chinese AI computing & API platform."""

from scraper_base import BaseScraper


class YouYunZhiSuanScraper(BaseScraper):
    provider_name = "优云智算"
    category = "proxy"

    _MODELS = [
        ("Claude Opus 4.7", "Claude", 108.00, 540.00),
        ("Claude Sonnet 4.6", "Claude", 21.50, 107.50),
        ("DeepSeek V3", "DeepSeek", 1.90, 7.80),
        ("DeepSeek R1", "DeepSeek", 3.80, 15.50),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = YouYunZhiSuanScraper()
