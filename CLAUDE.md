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

## Live Spiders

**alphaarchitect.py** — two plain-HTTP spiders for alphaarchitect.com, sharing `_CloudflareSpider`.

The site is WordPress behind a Cloudflare **managed challenge** that fires on every request, robots.txt included. Playwright chromium cannot pass it — headless and headed both loop on "Just a moment..." forever, because the challenge fingerprints the automation build. So `custom/mint_cf_cookie.py` attaches to your own running Chrome over CDP, borrows the `cf_clearance` cookie, and the spiders crawl plain HTTP with it. `/wp-json/wp/v2` is wide open and `content.rendered` carries whole post bodies, so no post page is ever fetched and there is no HTML parsing in the blog path.

`robots.txt` disallows only `/wp-admin/` and `/user/`, so `ROBOTSTXT_OBEY` stays on.

```bash
cd custom
python mint_cf_cookie.py                        # once, and again on 403s
scrapy crawl aa_bestof -o ../testfolder/aa_bestof.json
scrapy crawl aa_blog -a pages=1                 # smoke test: 100 posts
scrapy crawl aa_blog -o ../testfolder/aa_blog.json
```

- `aa_bestof` — the hand-curated `/best-of-blog/` list (**38 posts**). Links come from `div.post-content` only; the `fusion-recent-posts` block below it is an auto-generated widget, not curation. Each link keeps the `h4.fusion-tab-heading` section above it. The page also links a few ordinary pages, so candidate slugs are confirmed in one multi-slug REST call before being yielded.
- `aa_blog` — the whole archive (**2,494 posts, 2011-01 → 2026-07**) as one markdown file per post plus a JSON index. Walks the posts endpoint 100 at a time, so a full run is ~30 requests / **~70 seconds** / 21.5 MB. Category and tag IDs are resolved to names up front (85 categories, 252 tags) and `/best-of-blog/` is read once, so curated posts carry `best_of: true` and `best_of_section` in their front matter.
  - `-a out=DIR` markdown destination (default `../output/alpha-architect`, gitignored)
  - `-a pages=N` stop after N pages of 100 posts (0 = all)
  - `-a bestof=0` skip the best-of cross-reference

Output filenames follow `<YYYY-MM-DD>-<slug>.md` with YAML front matter (title, slug, date, modified, url, categories, tags, best_of, source).

**Cookie lifetime:** `cf_clearance` is bound to the exact User-Agent that earned it *and* to your public IP. Both spiders abort the crawl with `CloseSpider` on the first 403 rather than grinding through doomed requests — that means re-run `mint_cf_cookie.py`. Chrome's `chrome://inspect/#remote-debugging` grant also lapses; re-tick it when the minter reports no debuggable Chrome.

Selector-break signals: `aa_bestof` logs an error if `div.post-content` yields no links; `aa_blog` warns instead (it degrades to `best_of: false` everywhere rather than failing).

## Key Settings (settings.py)

- `ROBOTSTXT_OBEY = True` — disable per-spider via `custom_settings = {"ROBOTSTXT_OBEY": False}`
- `DOWNLOAD_DELAY = 1` and `CONCURRENT_REQUESTS_PER_DOMAIN = 1` — polite defaults
- Pipelines, middlewares, AutoThrottle, HTTP cache all commented out — uncomment to enable

## Install

```bash
pip install -r requirements.txt
playwright install chromium   # only if using CustomPlaywright.py
```
