"""AiHubMix — API aggregator with competitive pricing."""

from scraper_base import BaseScraper


class AiHubMixScraper(BaseScraper):
    provider_name = "AiHubMix"
    category = "proxy"

    _MODELS = [
        ("Claude Opus 4.7", "Claude", 112.00, 550.00),
        ("Claude Sonnet 4.6", "Claude", 22.50, 111.00),
        ("Claude Haiku 4.5", "Claude", 5.90, 29.50),
        ("GPT-4o", "GPT", 18.00, 72.00),
        ("DeepSeek V3", "DeepSeek", 1.95, 7.90),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = AiHubMixScraper()
