"""OpenRouter — public API for pricing data."""

from scraper_base import BaseScraper


class OpenRouterScraper(BaseScraper):
    provider_name = "OpenRouter"
    category = "proxy"

    def fetch(self):
        # OpenRouter has a free public endpoint for model pricing
        resp = self._get("https://openrouter.ai/api/v1/models")
        data = resp.json()
        entries = []

        for model in data.get("data", []):
            name = model.get("name", model.get("id", ""))
            pricing = model.get("pricing", {})
            prompt_cost = float(pricing.get("prompt", 0))  # per token → per 1M
            completion_cost = float(pricing.get("completion", 0))

            # Skip models with invalid/negative pricing (e.g. router models)
            if prompt_cost < 0 or completion_cost < 0:
                continue

            # Convert per-token to per-1M-tokens, then USD to CNY
            input_cny = round(prompt_cost * 1_000_000 * 7.25, 2)
            output_cny = round(completion_cost * 1_000_000 * 7.25, 2)

            # Determine series
            series = "Other"
            name_lower = name.lower()
            if "claude" in name_lower:
                series = "Claude"
            elif "gpt" in name_lower or "openai" in name_lower:
                series = "GPT"
            elif "gemini" in name_lower:
                series = "Gemini"
            elif "deepseek" in name_lower:
                series = "DeepSeek"
            elif "llama" in name_lower:
                series = "Llama"
            elif "qwen" in name_lower:
                series = "Qwen"
            elif "mistral" in name_lower:
                series = "Mistral"

            entries.append(self._make_entry(
                model_name=name,
                series=series,
                input_price_cny=input_cny,
                output_price_cny=output_cny,
            ))

        return entries


SCRAPER = OpenRouterScraper()
