# TODO — Scrapy Base Template

## In Progress

## Backlog

## Done

### Fix: Items
- [x] Replace `from resumes.items import ResumesItem` in both spiders with `from custom.items import CustomItem`
- [x] Add common field stubs to `CustomItem` (name, link, description, field, url, timestamp)

### Refactor: User Agents
- [x] Create `custom/user_agents.txt` — one UA string per line (moved from `CustomPlaywright.py`)
- [x] Add utility functions in `custom/custom/utils.py` — `load_user_agents()`, `random_user_agent()`, `load_proxies()`, `random_proxy()`
- [x] Update `CustomPlaywright.py` to use `random_user_agent()` from utils
- [x] `Custom.py` uses same utility (available via import when needed)

### Structure: Test Folder
- [x] Created `testfolder/` at project root with `.gitkeep`
- [x] Added `testfolder/*` to `.gitignore` (keeps folder, ignores output files)

### Stub: Proxy Support
- [x] Create `custom/proxies.txt` — commented format guide, gitignored
- [x] `random_proxy()` utility in `utils.py` — returns None if file empty
- [x] Commented-out `ProxyMiddleware` class in `middlewares.py` with activation instructions

### New Spider: API-Based Scraping
- [x] Created `custom/spiders/CustomAPI.py` — REST API template
  - Auth via `API_KEY` env var (Bearer token)
  - Dual pagination: follows `next` URL or increments page number
  - Maps response fields to `CustomItem`
