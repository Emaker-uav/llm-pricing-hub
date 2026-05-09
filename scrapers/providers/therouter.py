"""TheRouter — API routing & proxy platform."""

from scraper_base import BaseScraper


class TheRouterScraper(BaseScraper):
    provider_name = "TheRouter"
    category = "proxy"

    _MODELS = [
        ("Claude Opus 4.7", "Claude", 110.00, 548.00),
        ("Claude Sonnet 4.6", "Claude", 22.00, 110.00),
        ("GPT-4o", "GPT", 18.00, 72.00),
        ("Claude Haiku 4.5", "Claude", 5.80, 29.00),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = TheRouterScraper()
