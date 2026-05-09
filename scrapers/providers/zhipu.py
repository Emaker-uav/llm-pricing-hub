"""Zhipu AI (智谱) — GLM series official pricing in CNY."""

from scraper_base import BaseScraper


class ZhipuScraper(BaseScraper):
    provider_name = "Zhipu GLM"
    category = "domestic-official"

    _MODELS = [
        ("GLM-4 Plus", "GLM", 0.10, 0.10),
        ("GLM-4 Flash", "GLM", 0.00, 0.00),
        ("GLM-4 Air", "GLM", 0.00, 0.00),
        ("GLM-Z1", "GLM", 0.73, 0.73),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = ZhipuScraper()
