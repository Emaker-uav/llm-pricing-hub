"""Alibaba Bailian (百炼) — official Alibaba Cloud LLM pricing in CNY."""

from scraper_base import BaseScraper


class BailianScraper(BaseScraper):
    provider_name = "Bailian"
    category = "domestic-official"

    _MODELS = [
        ("Qwen-Max", "Qwen", 2.90, 8.70),
        ("Qwen-Plus", "Qwen", 0.58, 1.74),
        ("Qwen-Turbo", "Qwen", 0.22, 0.44),
        ("Qwen-Coder", "Qwen", 0.51, 1.45),
        ("Qwen-Max-Latest", "Qwen", 2.90, 8.70),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = BailianScraper()
