"""DeepSeek — official API pricing."""

from scraper_base import BaseScraper


class DeepSeekScraper(BaseScraper):
    provider_name = "DeepSeek"
    category = "domestic-official"

    # Manual entries (DeepSeek pricing is simple and stable)
    # Prices in CNY per 1M tokens
    _MODELS = [
        ("DeepSeek V3", "DeepSeek", 1.96, 7.98),
        ("DeepSeek R1", "DeepSeek", 3.99, 15.88),
        ("DeepSeek V3-0324", "DeepSeek", 1.96, 7.98),
    ]

    def fetch(self):
        entries = []
        for name, series, inp, outp in self._MODELS:
            entries.append(self._make_entry(
                model_name=name, series=series,
                input_price_cny=inp, output_price_cny=outp,
            ))
        return entries


SCRAPER = DeepSeekScraper()
