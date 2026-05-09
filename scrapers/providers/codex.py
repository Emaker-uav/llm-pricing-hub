"""Codex — OpenAI Codex / coding API."""

from scraper_base import BaseScraper


class CodexScraper(BaseScraper):
    provider_name = "Codex"
    category = "overseas-official"

    _MODELS = [
        ("Codex", "Codex", 0.00, 0.00),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = CodexScraper()
