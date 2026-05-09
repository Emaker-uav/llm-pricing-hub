"""Orchestrator: runs all scrapers, merges results, writes pricing.json."""

import json
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

from config import OUTPUT_PATH


def discover_scrapers():
    """Import all scraper modules from the providers/ directory."""
    providers_dir = Path(__file__).parent / "providers"
    scrapers = []

    for py_file in sorted(providers_dir.glob("*.py")):
        if py_file.name.startswith("_"):
            continue
        module_name = py_file.stem
        try:
            mod = __import__(f"providers.{module_name}", fromlist=["SCRAPER", "ALL_SCRAPERS"])
            if hasattr(mod, "ALL_SCRAPERS"):
                for item in mod.ALL_SCRAPERS:
                    scrapers.append(item() if callable(item) else item)
            elif hasattr(mod, "SCRAPER"):
                s = mod.SCRAPER
                scrapers.append(s() if callable(s) else s)
        except Exception:
            print(f"[WARN] Failed to load scraper: {module_name}")
            traceback.print_exc()

    return scrapers


def run_all():
    scrapers = discover_scrapers()
    all_models = []
    success = 0
    fail = 0

    for scraper in scrapers:
        name = scraper.provider_name or type(scraper).__name__
        try:
            entries = scraper.fetch()
            if entries:
                all_models.extend(entries)
                print(f"[OK] {name}: {len(entries)} models")
                success += 1
            else:
                print(f"[EMPTY] {name}: no models returned")
                fail += 1
        except Exception:
            print(f"[FAIL] {name}")
            traceback.print_exc()
            fail += 1

    # Sort by input price ascending
    all_models.sort(key=lambda m: m["input_price_cny"])

    output = {
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "models": all_models,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nDone. {success} scrapers OK, {fail} failed. "
          f"Total: {len(all_models)} models -> {OUTPUT_PATH}")


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent))
    run_all()
