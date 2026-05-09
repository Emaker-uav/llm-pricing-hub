"""Anthropic Claude — official API pricing."""

from scraper_base import BaseScraper


class ClaudeOfficialScraper(BaseScraper):
    provider_name = "Claude Official"
    category = "overseas-official"

    # Anthropic pricing page: https://www.anthropic.com/pricing
    # Prices in USD per 1M tokens
    _MODELS = [
        ("Claude Opus 4.7", "Claude", 15.00, 75.00),
        ("Claude Sonnet 4.6", "Claude", 3.00, 15.00),
        ("Claude Haiku 4.5", "Claude", 0.80, 4.00),
    ]

    def fetch(self):
        entries = []
        for name, series, inp, outp in self._MODELS:
            entries.append(self._make_entry(
                model_name=name, series=series,
                input_price_usd=inp, output_price_usd=outp,
            ))
        return entries


SCRAPER = ClaudeOfficialScraper()
