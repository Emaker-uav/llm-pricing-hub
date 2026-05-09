"""SiliconFlow — Chinese API proxy platform."""

from scraper_base import BaseScraper


class SiliconFlowScraper(BaseScraper):
    provider_name = "SiliconFlow"
    category = "proxy"

    # SiliconFlow pricing in CNY per 1M tokens
    _MODELS = [
        ("DeepSeek V3", "DeepSeek", 1.96, 7.98),
        ("DeepSeek R1", "DeepSeek", 3.99, 15.88),
        ("Claude Opus 4.7", "Claude", 108.75, 543.75),
        ("Claude Sonnet 4.6", "Claude", 21.75, 108.75),
        ("Claude Haiku 4.5", "Claude", 5.80, 29.00),
        ("Qwen-Max", "Qwen", 2.90, 8.70),
        ("Qwen-Plus", "Qwen", 0.58, 1.74),
        ("GLM-4 Plus", "GLM", 0.10, 0.10),
        ("Kimi K2", "Kimi", 3.63, 14.50),
        ("Gemini 2.5 Pro", "Gemini", 9.06, 36.25),
        ("Gemini 2.5 Flash", "Gemini", 1.09, 4.35),
    ]

    def fetch(self):
        return [self._make_entry(model_name=n, series=s,
                input_price_cny=i, output_price_cny=o)
                for n, s, i, o in self._MODELS]


SCRAPER = SiliconFlowScraper()
