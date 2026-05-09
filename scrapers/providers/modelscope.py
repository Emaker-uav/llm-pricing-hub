"""ModelScope — Alibaba model hub with API proxy service."""

from scraper_base import BaseScraper


class ModelScopeScraper(BaseScraper):
    provider_name = "ModelScope"
    category = "proxy"

    _MODELS = [
        ("Claude Opus 4.7", "Claude", 110.00, 545.00),
        ("Claude Sonnet 4.6", "Claude", 22.00, 110.00),
        ("Claude Haiku 4.5", "Claude", 6.00, 30.00),
        ("DeepSeek V3", "DeepSeek", 2.00, 8.00),
        ("Qwen-Max", "Qwen", 2.90, 8.70),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = ModelScopeScraper()
