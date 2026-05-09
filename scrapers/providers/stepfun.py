"""StepFun (阶跃星辰) — official API pricing in CNY."""

from scraper_base import BaseScraper


class StepFunScraper(BaseScraper):
    provider_name = "StepFun"
    category = "domestic-official"

    _MODELS = [
        ("Step-2", "StepFun", 0.73, 2.90),
        ("Step-2-Lite", "StepFun", 0.36, 1.45),
        ("Step-1.5V", "StepFun", 0.73, 2.90),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = StepFunScraper()
