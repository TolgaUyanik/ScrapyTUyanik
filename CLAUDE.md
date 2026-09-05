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
      FlirtingWithModels.py     # Real spider — flirtingwithmodels.com (name: fwm)
HTML_Files/                     # Save target page HTML here for selector dev (gitignored)
testfolder/                     # Spider output scratch space (gitignored)
```

## Spider Templates

**Custom.py** — plain HTTP. Set `start_urls`, fill CSS selectors in `parse()`.

**CustomPlaywright.py** — JS-rendered pages. Playwright configured via `custom_settings` on the class. UAs loaded from `user_agents.txt` via `random_user_agent()`. Set `"headless": False` in `PLAYWRIGHT_LAUNCH_OPTIONS` to debug visually.

**CustomAPI.py** — REST API. Set `api_base_url`, pass `API_KEY` env var. Handles both `next`-URL and page-number pagination automatically.

**FlirtingWithModels.py** (`fwm`) — flirtingwithmodels.com episodes. Yields `EpisodeItem` (items.py). Two sources via `-a source=`:

| source | host | eps | fields |
|---|---|---|---|
| `api` (default) | `app.podcastai.com/api/v1` | 125 | everything — handle, chapters, speakers, transcript URL, YouTube/Apple/Spotify IDs |
| `rss` | `feeds.captivate.fm` | 125 | feed-only — no handle, chapters, speakers or transcript URL |

The site's `/episodes` page server-renders just 20 links and hydrates the rest from the podcastai API, so the API is the only route to the full catalog. That host serves `robots.txt: Disallow: /`, so the spider sets `ROBOTSTXT_OBEY = False` in `custom_settings` — deliberate, unauthenticated public read endpoint. `source=rss` touches no disallowed host.

**Transcripts** (`source=api` only) — each episode's raw Deepgram JSON is downloaded to `testfolder/transcripts/<handle>.json` and the path recorded in `transcript_path`. 125 files, ~213 MB, gitignored. Text lives at `results.channels[0].alternatives[0]` — `transcript` (flat string), `words` (word-level timing + speaker) and `paragraphs.paragraphs` (speaker-diarized). Existing files are skipped, so reruns cost nothing. Hosted on `data-1.podcastai.com`, which also serves `Disallow: /` — same override applies.

```bash
scrapy crawl fwm -o ../testfolder/episodes.json              # api, ~2.7 min (125 detail + 125 transcript requests)
scrapy crawl fwm -a source=rss -o ../testfolder/episodes.json # rss, 1 request, no transcripts
python -m custom.spiders.FlirtingWithModels                   # duration-parser self-check
```

## Key Settings (settings.py)

- `ROBOTSTXT_OBEY = True` — disable per-spider via `custom_settings = {"ROBOTSTXT_OBEY": False}`
- `DOWNLOAD_DELAY = 1` and `CONCURRENT_REQUESTS_PER_DOMAIN = 1` — polite defaults
- Pipelines, middlewares, AutoThrottle, HTTP cache all commented out — uncomment to enable

## Install

```bash
pip install -r requirements.txt
playwright install chromium   # only if using CustomPlaywright.py
```
