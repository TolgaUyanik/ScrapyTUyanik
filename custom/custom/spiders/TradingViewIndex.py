"""
TradingViewIndex.py — TVIDX. Link/discovery spider for the TradingView script index.

    cd custom
    scrapy crawl tvlinks                              # all pages, script_access=all
    scrapy crawl tvlinks -a max_pages=3               # smoke test
    scrapy crawl tvlinks -a script_type=strategies    # indicators|strategies|libraries|all
    scrapy crawl tvlinks -a script_access=open        # open|all

Walks https://www.tradingview.com/scripts/?script_access=all and its
`/scripts/page-N/` pagination, emitting one row per published script to
../datastore/tv_scripts_index.csv.

⚠ ROBOTS: this spider obeys robots.txt and needs NO override. Verified
2026-07-25 — `www.tradingview.com/robots.txt` disallows only `/scripts/search/`
for `User-agent: *`; `/scripts/` and `/scripts/page-N/` are permitted. (Contrast
`tvsource`, which needs an explicit override for the pine-facade host.) If a
future robots change disallows `/scripts/`, STOP and escalate — do not disable
ROBOTSTXT_OBEY here.

WHY PARSE JSON AND NOT CSS
The page renders from an embedded JSON array. Card anchors
(`a[data-qa-id="ui-lib-card-link-title"]`) look tempting but MEASURED 23 anchors
against 24 script links on page 1 — a selector would silently drop ~1 card per
page, ~42 over a full crawl, and nothing would report the loss. The JSON is the
authoritative list the page is built from, it carries the pagination cursor, and
it yields metadata no selector exposes.

⚠ THE PAYOFF — `script_id_part` IS THE `PUB;<hash>` ID, HANDED OVER DIRECTLY.
`tvsource` exists because the script page had to be fetched purely to regex a
`PUB;` id out of it, and on multi-id pages it had to GUESS which one was the
target ("first in document order" — an n=1 hypothesis that cost a whole
name-check gate, a remedy script, and 10 rows that could never be resolved).
The index hands the id over authoritatively. Any consumer of this CSV can go
straight to pine-facade in ONE hop, with zero ambiguity. Do not reintroduce the
guess.

PAGINATION contract, measured 2026-07-25: 24 records per page (`per_page` enum
is only [23, 24] — there is no larger page size to ask for), `"next"` holds the
next path, and the LAST page has `"next": null`. Terminate on null `next`;
never guess a page count.

⚠ `script_access` IS A 3-VALUE INT AND ONLY `1` YIELDS SOURCE. Probed one row of
each against pine-facade, 2026-07-25:
    1 -> scriptAccess "open_no_auth", source returned (48 KB sample)   [441 rows]
    2 -> HTTP 401 Unauthorized                                          [324 rows]
    3 -> HTTP 401 Unauthorized                                          [227 rows]
So of 992 indexed scripts only **441 are open-source**. A consumer that fetches
all 992 burns 551 requests on guaranteed 401s. **Filter `script_access == 1`
before hitting pine-facade.** The index still records 2 and 3 deliberately —
knowing a script exists and is closed is worth more than not knowing it exists.

MEASURED YIELD, full run 2026-07-25: 42 pages, **992 unique scripts**, 1
cross-page duplicate, 0 errors, 257 s. 992 rather than the arithmetic 1000
because pages 9/10/19 returned 22/19/23 — scripts drift between pages under
`latest_popular` while the crawl walks it. That is inherent to paginating a
live-ranked list, not a defect; the dupe/short counts are logged so the gap is
visible rather than inferred.
`script_type`: indicator 931, strategy 54, library 7. 691 distinct authors.

All paths anchor on __file__, never cwd. Output is utf-8 (box default is cp1254).
"""
import json
import re

import scrapy

BASE = "https://www.tradingview.com"
START = "/scripts/"

# Pagination cursor. Also marks the end of the results array.
NEXT_RE = re.compile(r'\],"next":(?:"([^"]*)"|null)')
# Candidate array starts: `:[{"` — cheap prefilter before the real parse.
ARR_RE = re.compile(r':(\[\{")')

_dec = json.JSONDecoder()


def extract_page(html):
    """-> (list_of_records, next_path_or_None). Never raises; ([], next) on miss.

    ⚠ DO NOT "simplify" this back to counting [ and ] backwards from the cursor.
    That was the first implementation and it is BROKEN on real data: brackets
    occur inside JSON string values — TradingView titles are full of them
    ("Reactive Trail System [WillyAlgoTrader]", "RSI Shift Zone [ChartPrime]") —
    and a hand-rolled counter cannot tell a structural bracket from one inside a
    string. MEASURED: it silently returned 0 records on pages 7, 21 and 42 of a
    42-page crawl while succeeding elsewhere, because the failure depends on
    whether a given page's titles happen to balance.

    `raw_decode` is the JSON parser itself, so it is string-aware by
    construction. Scan candidate starts forward and keep the first array whose
    records look like script records.
    """
    m = NEXT_RE.search(html)
    nxt = m.group(1) if m else None
    end = m.start() + 1 if m else len(html)

    for mm in ARR_RE.finditer(html[:end]):
        try:
            val, _ = _dec.raw_decode(html, mm.start(1))
        except json.JSONDecodeError:
            continue
        if isinstance(val, list) and val and isinstance(val[0], dict) and "chart_url" in val[0]:
            return val, nxt
    return [], nxt


class TradingViewIndexSpider(scrapy.Spider):
    name = "tvlinks"

    custom_settings = {
        # True, deliberately — /scripts/ is permitted. See the ROBOTS note above.
        "ROBOTSTXT_OBEY": True,
        "DOWNLOAD_DELAY": 5,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 1,
        "RETRY_TIMES": 2,
        # USER_AGENT, not DEFAULT_REQUEST_HEADERS — the latter REPLACES Scrapy's
        # default {Accept, Accept-Language}, producing a Chrome UA with no Accept
        # headers, which is a signature no real browser sends.
        "USER_AGENT": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"),
        # ⚠ Output path is PARAMETERISED on script_type via %(kind)s. With a fixed
        # filename + overwrite:True, running `-a script_type=strategies` would
        # silently destroy the index from a previous `all` run. Each filter gets
        # its own file: tv_scripts_index_all.csv, _strategies.csv, _indicators.csv…
        "FEEDS": {
            "../datastore/tv_scripts_index_%(kind)s.csv": {
                "format": "csv",
                "encoding": "utf-8",
                "overwrite": True,
                "fields": ["url", "title", "slug", "pub_id", "author", "script_type",
                           "script_access", "version", "likes", "views", "comments",
                           "created_at", "page", "description"],
            }
        },
        "LOG_LEVEL": "INFO",
    }

    @property
    def kind(self):
        """Feeds `%(kind)s` in the output path — keeps each script_type in its own CSV."""
        return self.script_type or "all"

    def __init__(self, max_pages=None, script_type=None, script_access="all", *a, **kw):
        super().__init__(*a, **kw)
        self.max_pages = int(max_pages) if max_pages else None
        self.script_type = script_type
        self.script_access = script_access
        self.seen = set()
        self.pages = 0
        self.dupes = 0

    def _qs(self):
        parts = []
        if self.script_access:
            parts.append(f"script_access={self.script_access}")
        if self.script_type:
            parts.append(f"script_type={self.script_type}")
        return ("?" + "&".join(parts)) if parts else ""

    async def start(self):                       # Scrapy >= 2.13 entry point
        for r in self.start_requests():
            yield r

    def start_requests(self):
        yield scrapy.Request(BASE + START + self._qs(), callback=self.parse,
                             cb_kwargs={"page": 1})

    def parse(self, response, page):
        records, nxt = extract_page(response.text)
        self.pages += 1
        if not records:
            # Loud, not silent: an empty page mid-crawl means the embed changed.
            self.logger.error("page %d yielded 0 records (next=%r) — embed may have "
                              "changed; check %s", page, nxt, response.url)

        new, dupes = 0, 0
        for r in records:
            url = r.get("chart_url") or ""
            if not url:
                continue
            if url in self.seen:
                # ⚠ Expected, not a bug. The index is ordered `latest_popular`, so
                # ranks shift between our page requests (5 s apart, 42 pages ≈ 4 min)
                # and a script can slide from page N+1 back onto page N. Deduping on
                # url is why the final count is under pages*24; the gap is counted
                # and reported rather than left to look like data loss.
                dupes += 1
                continue
            self.seen.add(url)
            new += 1
            user = r.get("user") or {}
            yield {
                "url": url,
                "title": r.get("name"),
                # Same slug rule as build_tv_worklist.py: whole final path segment,
                # 8-char id INCLUDED. Verified collision-free there; do not change
                # one without the other or the two CSVs stop joining.
                "slug": url.rstrip("/").rsplit("/", 1)[-1],
                # ⚠ The whole point of this spider — the PUB id, no page fetch, no guess.
                "pub_id": r.get("script_id_part"),
                "author": user.get("username"),
                "script_type": r.get("script_type"),
                "script_access": r.get("script_access"),
                "version": r.get("version"),
                "likes": r.get("likes_count"),
                "views": r.get("views_count"),
                "comments": r.get("comments_count"),
                "created_at": r.get("created_at"),
                "page": page,
                "description": (r.get("description") or "").replace("\n", " ")[:500],
            }

        self.dupes += dupes
        self.logger.info("page %d: %d records (%d new, %d dupe) | total %d | next=%s",
                         page, len(records), new, dupes, len(self.seen), nxt)

        if not nxt:
            self.logger.info("no `next` — last page reached at page %d. "
                             "%d unique scripts, %d cross-page duplicates skipped "
                             "(rank drift under `latest_popular`, expected)",
                             page, len(self.seen), self.dupes)
            return
        if self.max_pages and self.pages >= self.max_pages:
            self.logger.info("max_pages=%d reached — stopping early with %d scripts "
                             "(NOT a complete crawl)", self.max_pages, len(self.seen))
            return
        yield scrapy.Request(BASE + nxt + self._qs(), callback=self.parse,
                             cb_kwargs={"page": page + 1})
