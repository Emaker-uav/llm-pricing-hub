"""Novita AI — API proxy platform."""

from scraper_base import BaseScraper


class NovitaAIScraper(BaseScraper):
    provider_name = "Novita AI"
    category = "proxy"

    _MODELS = [
        ("Claude Opus 4.7", "Claude", 109.50, 546.00),
        ("Claude Sonnet 4.6", "Claude", 21.90, 109.50),
        ("Claude Haiku 4.5", "Claude", 5.85, 29.20),
        ("DeepSeek V3", "DeepSeek", 1.95, 7.95),
        ("GPT-4o", "GPT", 18.10, 72.40),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = NovitaAIScraper()
