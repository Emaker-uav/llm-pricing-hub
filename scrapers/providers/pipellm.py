"""PIPELLM — API proxy platform."""

from scraper_base import BaseScraper


class PIPELLMScraper(BaseScraper):
    provider_name = "PIPELLM"
    category = "proxy"

    _MODELS = [
        ("Claude Opus 4.7", "Claude", 111.00, 552.00),
        ("Claude Sonnet 4.6", "Claude", 22.20, 111.00),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = PIPELLMScraper()
