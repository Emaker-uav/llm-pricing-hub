"""ByteDance DouBao (豆包) — official API pricing in CNY."""

from scraper_base import BaseScraper


class DouBaoScraper(BaseScraper):
    provider_name = "DouBaoSeed"
    category = "domestic-official"

    _MODELS = [
        ("DouBao 1.5 Pro", "DouBao", 0.58, 1.45),
        ("DouBao 1.5 Lite", "DouBao", 0.15, 0.58),
        ("DouBao 1.5-Vision", "DouBao", 0.15, 0.58),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = DouBaoScraper()
