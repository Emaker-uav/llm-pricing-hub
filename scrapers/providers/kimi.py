"""Moonshot Kimi — official API pricing in CNY."""

from scraper_base import BaseScraper


class KimiScraper(BaseScraper):
    provider_name = "Kimi"
    category = "domestic-official"

    _MODELS = [
        ("Kimi K2", "Kimi", 3.63, 14.50),
        ("Kimi K2-Turbo", "Kimi", 2.18, 8.70),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = KimiScraper()
