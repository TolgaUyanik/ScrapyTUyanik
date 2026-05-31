# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

**Scrapy-TUyanik** — reusable Scrapy template. Three spider archetypes: plain HTTP (`Custom.py`), Playwright JS-rendered (`CustomPlaywright.py`), REST API (`CustomAPI.py`). All commands run from `custom/`.

## Commands

```bash
cd custom

# Run spiders
scrapy crawl CustomSpider
scrapy crawl custompw
scrapy crawl CustomAPI

# Save output
scrapy crawl CustomSpider -o ../testfolder/output.json

# Interactive selector testing
scrapy shell "https://example.com"

# List available spiders
scrapy list
```

## Architecture

```
custom/
  scrapy.cfg                    # project config, points to custom.settings
  user_agents.txt               # 200 UA strings, read by utils.py
  proxies.txt                   # proxy list (gitignored, empty by default)
  custom/
    settings.py                 # DOWNLOAD_DELAY=1, CONCURRENT_REQUESTS_PER_DOMAIN=1
    items.py                    # CustomItem: name, link, description, field, url, timestamp
    utils.py                    # random_user_agent(), random_proxy()
    pipelines.py                # CustomPipeline stub — enable in settings ITEM_PIPELINES
    middlewares.py              # ProxyMiddleware stub (commented out)
    spiders/
      Custom.py                 # Plain HTTP spider (name: CustomSpider)
      CustomPlaywright.py       # Playwright spider (name: custompw)
      CustomAPI.py              # REST API spider (name: CustomAPI)
HTML_Files/                     # Save target page HTML here for selector dev (gitignored)
testfolder/                     # Spider output scratch space (gitignored)
```

## Spider Templates

**Custom.py** — plain HTTP. Set `start_urls`, fill CSS selectors in `parse()`.

**CustomPlaywright.py** — JS-rendered pages. Playwright configured via `custom_settings` on the class. UAs loaded from `user_agents.txt` via `random_user_agent()`. Set `"headless": False` in `PLAYWRIGHT_LAUNCH_OPTIONS` to debug visually.

**CustomAPI.py** — REST API. Set `api_base_url`, pass `API_KEY` env var. Handles both `next`-URL and page-number pagination automatically.

## Key Settings (settings.py)

- `ROBOTSTXT_OBEY = True` — disable per-spider via `custom_settings = {"ROBOTSTXT_OBEY": False}`
- `DOWNLOAD_DELAY = 1` and `CONCURRENT_REQUESTS_PER_DOMAIN = 1` — polite defaults
- Pipelines, middlewares, AutoThrottle, HTTP cache all commented out — uncomment to enable

## Install

```bash
pip install -r requirements.txt
playwright install chromium   # only if using CustomPlaywright.py
```
