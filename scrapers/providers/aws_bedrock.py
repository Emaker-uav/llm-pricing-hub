"""AWS Bedrock — Anthropic/Amazon models hosted on AWS."""

from scraper_base import BaseScraper


class AWSBedrockScraper(BaseScraper):
    provider_name = "AWS Bedrock"
    category = "overseas-official"

    # AWS Bedrock pricing same as Anthropic official
    # (AWS may have slight variations by region)
    _MODELS = [
        ("Claude Opus 4.7", "Claude", 15.00, 75.00),
        ("Claude Sonnet 4.6", "Claude", 3.00, 15.00),
        ("Claude Haiku 4.5", "Claude", 0.80, 4.00),
        ("GPT-4o", "GPT", 2.50, 10.00),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_usd=i, output_price_usd=o)
                for n, s, i, o in self._MODELS]


SCRAPER = AWSBedrockScraper()
