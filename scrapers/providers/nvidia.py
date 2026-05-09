"""Nvidia NIM — official API pricing."""

from scraper_base import BaseScraper


class NvidiaScraper(BaseScraper):
    provider_name = "Nvidia"
    category = "overseas-official"

    # Nvidia NIM API pricing. Many models currently free during early access.
    _MODELS = [
        ("Llama 4 NIM", "Llama", 0.00, 0.00),
        ("Llama 3.1 70B NIM", "Llama", 0.00, 0.00),
        ("Mixtral 8x22B NIM", "Mistral", 0.00, 0.00),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = NvidiaScraper()
