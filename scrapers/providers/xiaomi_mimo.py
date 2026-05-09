"""Xiaomi MiMo — Xiaomi's LLM API pricing in CNY."""

from scraper_base import BaseScraper


class XiaomiMiMoScraper(BaseScraper):
    provider_name = "Xiaomi MiMo"
    category = "domestic-official"

    _MODELS = [
        ("Xiaomi MiMo", "MiMo", 0.36, 1.45),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = XiaomiMiMoScraper()
