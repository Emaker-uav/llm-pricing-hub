"""GitHub Copilot — subscription-based (not per-token)."""

from scraper_base import BaseScraper


class GitHubCopilotScraper(BaseScraper):
    provider_name = "GitHub Copilot"
    category = "overseas-official"

    # GitHub Copilot is a flat subscription, not per-token pricing
    _MODELS = [
        ("GitHub Copilot", "Copilot", 0.00, 0.00),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = GitHubCopilotScraper()
