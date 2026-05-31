# Scrapy-TUyanik

Reusable Scrapy project template. Three spider archetypes: plain HTTP, Playwright (JS-rendered), and REST API. Copy this repo, configure the spider for your target, run.

---

## Setup

### 1. Clone

```bash
git clone <repo-url>
cd Scrapy-TUyanik
```

### 2. Create virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Install Playwright browsers

Required only if using `CustomPlaywright.py`. Skip for plain HTTP or API spiders.

```bash
playwright install chromium
```

---

## Saving HTML for selector development

Before writing CSS selectors, save the target page's HTML locally:

**Option A — Browser**
Open the target page → right-click → Save As → "Webpage, HTML Only" → save to `HTML_Files/`.

**Option B — curl / PowerShell**
```bash
# curl
curl -o HTML_Files/target.html https://example.com/page

# PowerShell
Invoke-WebRequest -Uri "https://example.com/page" -OutFile "HTML_Files\target.html"
```

**Option C — Scrapy shell** (captures exactly what Scrapy sees, including headers)
```bash
cd custom
scrapy shell "https://example.com/page"
# In the shell:
with open("../HTML_Files/target.html", "w", encoding="utf-8") as f:
    f.write(response.text)
```

`HTML_Files/` is gitignored — use it as a local scratch space.

---

## Choosing the right spider

| Situation | Use |
|-----------|-----|
| Page content is in the raw HTML source (visible in View Source) | `Custom.py` — plain Scrapy, fastest |
| Content only appears after JavaScript runs (blank in View Source, visible in DevTools Elements) | `CustomPlaywright.py` — headless browser |
| Site has a public or documented JSON API | `CustomAPI.py` — cleanest, most reliable |

**How to check:** Open the target URL → Ctrl+U (View Source) → search for a piece of text you want to scrape. If it's there, plain Scrapy works. If it's missing, you need Playwright or the API.

**Prefer API > Playwright > plain HTTP** in that order. APIs don't break on layout changes and need no browser overhead. Playwright is slower and more fragile but handles any JS-rendered page.

---

## Finding selectors with Claude

1. Save the page HTML to `HTML_Files/` (see above).
2. Open Claude and attach or paste the HTML file.
3. Ask: *"Find the CSS selector for [the thing you want] in this HTML."*
4. Paste the selector into the spider's `parse()` method and verify in the Scrapy shell:

```bash
cd custom
scrapy shell "https://example.com/page"
response.css("your-selector-here").getall()
```

Use `.get()` for a single value, `.getall()` for a list, `::text` for inner text, `::attr(href)` for attributes.

---

## Running spiders

All commands run from the `custom/` directory.

```bash
cd custom

# Run and print to terminal
scrapy crawl CustomSpider
scrapy crawl custompw
scrapy crawl CustomAPI

# Save output to testfolder/
scrapy crawl CustomSpider -o ../testfolder/output.json
scrapy crawl CustomSpider -o ../testfolder/output.csv

# Pass API key for the API spider
API_KEY=your_key_here scrapy crawl CustomAPI -o ../testfolder/output.json
```

---

## Project structure

```
ScrapyBaseProject/
  custom/
    custom/
      spiders/
        Custom.py           # Plain HTTP spider template
        CustomPlaywright.py # Playwright (JS-rendered) spider template
        CustomAPI.py        # REST API spider template
      items.py              # CustomItem with common fields
      utils.py              # random_user_agent(), random_proxy()
      middlewares.py        # ProxyMiddleware stub (commented out)
      settings.py           # Global config
    user_agents.txt         # 200 rotating user agent strings
    proxies.txt             # Add proxies here (gitignored)
  HTML_Files/               # Saved HTML for selector development (gitignored)
  testfolder/               # Spider output files (gitignored)
```

---

## Enabling proxies

1. Add proxies to `custom/proxies.txt` — one per line: `http://ip:port`
2. In `middlewares.py`, uncomment `ProxyMiddleware` and the import at the top.
3. In `settings.py`, add:

```python
DOWNLOADER_MIDDLEWARES = {
    "custom.middlewares.ProxyMiddleware": 100,
}
```
