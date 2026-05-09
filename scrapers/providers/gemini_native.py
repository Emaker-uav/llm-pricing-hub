"""Google Gemini — official API pricing."""

from scraper_base import BaseScraper


class GeminiNativeScraper(BaseScraper):
    provider_name = "Gemini Native"
    category = "overseas-official"

    # Gemini pricing in USD per 1M tokens
    # https://ai.google.dev/pricing
    _MODELS = [
        ("Gemini 2.5 Pro", "Gemini", 1.25, 5.00),
        ("Gemini 2.5 Flash", "Gemini", 0.15, 0.60),
        ("Gemini 2.0 Flash", "Gemini", 0.10, 0.40),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_usd=i, output_price_usd=o)
                for n, s, i, o in self._MODELS]


SCRAPER = GeminiNativeScraper()
