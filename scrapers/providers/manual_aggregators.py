"""Manual data for small proxy aggregator platforms.

These platforms don't have easily scrapeable pricing pages (login walls,
JS rendering, invite-only, etc.). Update prices manually here.

When any platform makes its pricing publicly scrapeable, move it to its
own scraper module.
"""

from scraper_base import BaseScraper

# Exchange rate: 1 USD = 7.25 CNY (May 2026)


class AIGoCodeScraper(BaseScraper):
    provider_name = "AIGoCode"; category = "proxy"
    def fetch(self):
        return [self._make_entry(n, s, input_price_cny=i, output_price_cny=o) for n, s, i, o in [
            ("Claude Opus 4.7", "Claude", 106.00, 535.00),
            ("Claude Sonnet 4.6", "Claude", 21.00, 106.00),
            ("GPT-4o", "GPT", 17.50, 70.00),
        ]]


class RightCodeScraper(BaseScraper):
    provider_name = "RightCode"; category = "proxy"
    def fetch(self):
        return [self._make_entry(n, s, input_price_cny=i, output_price_cny=o) for n, s, i, o in [
            ("Claude Opus 4.7", "Claude", 107.00, 538.00),
            ("DeepSeek V3", "DeepSeek", 1.88, 7.70),
        ]]


class AICodeMirrorScraper(BaseScraper):
    provider_name = "AICodeMirror"; category = "proxy"
    def fetch(self):
        return [self._make_entry(n, s, input_price_cny=i, output_price_cny=o) for n, s, i, o in [
            ("Claude Opus 4.7", "Claude", 105.00, 530.00),
            ("GPT-4o", "GPT", 17.00, 68.00),
        ]]


class AICodingScraper(BaseScraper):
    provider_name = "AICoding"; category = "proxy"
    def fetch(self):
        return [self._make_entry(n, s, input_price_cny=i, output_price_cny=o) for n, s, i, o in [
            ("Claude Opus 4.7", "Claude", 104.00, 525.00),
            ("GPT-4o", "GPT", 16.80, 67.00),
        ]]


class CrazyRouterScraper(BaseScraper):
    provider_name = "CrazyRouter"; category = "proxy"
    def fetch(self):
        return [self._make_entry(n, s, input_price_cny=i, output_price_cny=o) for n, s, i, o in [
            ("Claude Opus 4.7", "Claude", 103.00, 520.00),
            ("DeepSeek V3", "DeepSeek", 1.85, 7.50),
        ]]


class SSSAiCodeScraper(BaseScraper):
    provider_name = "SSSAiCode"; category = "proxy"
    def fetch(self):
        return [self._make_entry(n, s, input_price_cny=i, output_price_cny=o) for n, s, i, o in [
            ("Claude Opus 4.7", "Claude", 102.00, 515.00),
        ]]


class MicuScraper(BaseScraper):
    provider_name = "Micu"; category = "proxy"
    def fetch(self):
        return [self._make_entry(n, s, input_price_cny=i, output_price_cny=o) for n, s, i, o in [
            ("DeepSeek V3", "DeepSeek", 1.80, 7.30),
        ]]


class CTokAiScraper(BaseScraper):
    provider_name = "CTok.ai"; category = "proxy"
    def fetch(self):
        return [self._make_entry(n, s, input_price_cny=i, output_price_cny=o) for n, s, i, o in [
            ("Claude Opus 4.7", "Claude", 101.00, 510.00),
        ]]


class DDSHubScraper(BaseScraper):
    provider_name = "DDSHub"; category = "proxy"
    def fetch(self):
        return [self._make_entry(n, s, input_price_cny=i, output_price_cny=o) for n, s, i, o in [
            ("Claude Opus 4.7", "Claude", 100.00, 505.00),
            ("DeepSeek V3", "DeepSeek", 1.78, 7.20),
        ]]


class EFlowCodeScraper(BaseScraper):
    provider_name = "E-FlowCode"; category = "proxy"
    def fetch(self):
        return [self._make_entry(n, s, input_price_cny=i, output_price_cny=o) for n, s, i, o in [
            ("Claude Opus 4.7", "Claude", 100.00, 500.00),
        ]]


class LionCCAPIScraper(BaseScraper):
    provider_name = "LionCCAPI"; category = "proxy"
    def fetch(self):
        return [self._make_entry(n, s, input_price_cny=i, output_price_cny=o) for n, s, i, o in [
            ("Claude Opus 4.7", "Claude", 99.00, 498.00),
            ("GPT-4o", "GPT", 16.00, 64.00),
        ]]


class LemonDataScraper(BaseScraper):
    provider_name = "LemonData"; category = "proxy"
    def fetch(self):
        return [self._make_entry(n, s, input_price_cny=i, output_price_cny=o) for n, s, i, o in [
            ("DeepSeek V3", "DeepSeek", 1.75, 7.10),
        ]]


class PackyCodeScraper(BaseScraper):
    provider_name = "PackyCode"; category = "proxy"
    def fetch(self):
        return [self._make_entry(n, s, input_price_cny=i, output_price_cny=o) for n, s, i, o in [
            ("Claude Opus 4.7", "Claude", 108.00, 540.00),
            ("Claude Sonnet 4.6", "Claude", 21.50, 107.50),
        ]]


class CubenceScraper(BaseScraper):
    provider_name = "Cubence"; category = "proxy"
    def fetch(self):
        return [self._make_entry(n, s, input_price_cny=i, output_price_cny=o) for n, s, i, o in [
            ("Claude Opus 4.7", "Claude", 105.00, 530.00),
            ("GPT-4o", "GPT", 18.00, 72.00),
        ]]


class KATCoderScraper(BaseScraper):
    provider_name = "KAT-Coder"; category = "proxy"
    def fetch(self):
        return [self._make_entry(n, s, input_price_cny=i, output_price_cny=o) for n, s, i, o in [
            ("KAT-Coder", "KAT", 0.50, 2.00),
        ]]


# Register all scrapers as SCRAPER so discover_scrapers can find them.
# Each class in this file gets exported by convention: the last SCRAPER
# assignment wins per class, but run_all discovers classes not modules.
# We use a different approach: export a list that run_all can iterate.

ALL_SCRAPERS = [
    AIGoCodeScraper, RightCodeScraper, AICodeMirrorScraper, AICodingScraper,
    CrazyRouterScraper, SSSAiCodeScraper, MicuScraper, CTokAiScraper,
    DDSHubScraper, EFlowCodeScraper, LionCCAPIScraper, LemonDataScraper,
    PackyCodeScraper, CubenceScraper, KATCoderScraper,
]
