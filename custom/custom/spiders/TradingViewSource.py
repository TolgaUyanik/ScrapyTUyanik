"""
TradingViewSource.py — TVSRC-1. Two-hop TradingView Pine source scraper.

    cd custom
    scrapy crawl tvsource                 # full run over datastore/tv_urls.csv (705)
    scrapy crawl tvsource -a limit=20     # validation slice

HOP 1  www.tradingview.com/script/<slug>/            -> extract PUB;<32hex>
HOP 2  pine-facade.tradingview.com/pine-facade/get/  -> JSON {source, scriptName, ...}

STORAGE CONTRACT (TVSRC-0, frozen):
  ../testfolder/tv_source.jsonl   one row per ATTEMPTED url, INCLUDING every failure
  ../datastore/pine/<slug>.pine   written only where source is present
Schema: url, slug, pub_id, script_name, script_access, version, created, updated,
        source_available, source_len, source_path, pub_selection, error

REASON-CODE PRIORITY LADDER (first match wins — the codes are NOT disjoint):
  no_pub_id > dead_404 > http_error > json_error > protected > captured

RESUME: skips urls whose logged error is TERMINAL {None, dead_404, protected,
no_pub_id}; retries only {http_error, json_error}. Skipping on "error is None"
instead would re-fetch every dead/protected script on every restart and never
converge. The jsonl is append-mode and retried urls therefore appear twice —
LAST ROW WINS. `report_tv_source.py` collapses on url before counting; never
read the identity off a raw line count.

⚠ `source_path` is emitted posix (`.as_posix()`), because TVSRC-4 hands this
file to a separate repo. Rows written BEFORE that fix landed carry Windows
separators, and they are TERMINAL (`error: null`) so resume will never rewrite
them — the artifact cannot self-heal. DECIDED: a one-off normalization pass
over `tv_source.jsonl` runs AFTER the crawl completes (`normalize_source_paths`
in `report_tv_source.py`), rewriting every `source_path` through `.as_posix()`.
Do not rely on the code comment alone; the artifact is only clean once that
pass has run.

⚠ `url` on every emitted row is the WORKLIST url, never `response.url` — see
the comment at the hop-1 Request below for why the difference matters.

⚠ DEVIATION 1 — hop-1 404 is labelled `dead_404` (TERMINAL), not the spec's
`http_error`. Deliberate, and evidence-backed rather than assumed. TVSRC-1 as
written maps every hop-1 non-2xx to `http_error`, which would make these
retryable forever. MEASURED 2026-07-25 on the live run: 64 of 144 rows (44%)
were hop-1 404s (all with pub_id=null). That is 7x the n=6 recon guess, so it
was spot-checked by hand before being accepted — 4 of the 404 urls, fetched
individually with curl (no crawl):
  - 404 with a bare browser UA AND with full Accept/Accept-Language headers
    -> not a header-fingerprint artifact
  - 404 on the id-only form (/script/<id>/) with an EMPTY redirect_url
    -> not a stale/renamed slug
  - a known-good control url returned 200 in the same batch
    -> not a block or a rate-limit onset
  - 404s are interleaved with captures throughout emit order, not a contiguous
    tail -> not "we got banned at time T"
Conclusion: these scripts are genuinely removed from TradingView. TERMINAL is
the correct classification; retrying them forever would be the bug. The n=6
recon figure was explicitly labelled "supports 'dead scripts exist', NOT a
rate" in TODO.md, so this supersedes it rather than contradicting it.

⚠ DEVIATION 2 — `protected` is emitted when NO USABLE SOURCE came back, not
when `scriptAccess != "open_no_auth"` as TVSRC-1 words it. The spec's wording
conflates the access label with whether source was actually returned; obeying
it literally would DISCARD source the facade successfully handed us merely
because the label reads `open` rather than `open_no_auth`. Data loss is the
larger blast radius, so: capture whenever source is present, and record
`script_access` on every row so the distinction stays queryable.
`report_tv_source.py` tallies the access values, so a non-`open_no_auth`
capture is visible rather than silent. TODO.md's ladder wording should be
amended to match.

robots.txt: pine-facade.tradingview.com serves "User-agent: * / Disallow: /".
ROBOTSTXT_OBEY is disabled BELOW IN custom_settings ONLY (never project-wide)
on explicit user instruction 2026-07-25 ("Pass the robot.txt file"), after the
disallow was surfaced. Rate limiting is kept strict as the load mitigation.
Single stable UA — rotating user_agents.txt is deliberately NOT used.

All paths anchor on __file__, never cwd. All I/O explicitly utf-8 (box default
is cp1254; Pine sources carry Turkish/Cyrillic/CJK comments).
"""
import csv
import json
import re
from pathlib import Path

import scrapy

ROOT = Path(__file__).resolve().parents[3]          # -> ScrapyTUyanik/

WORKLIST = ROOT / "datastore" / "tv_urls.csv"
PINE_DIR = ROOT / "datastore" / "pine"
JSONL    = ROOT / "testfolder" / "tv_source.jsonl"

FACADE = "https://pine-facade.tradingview.com/pine-facade/get/PUB%3B{}/last"

# Hardened: the naive r'PUB;[0-9a-f]{32}' is lowercase-only and assumes the id
# appears unescaped, which fails when it sits inside an embedded JSON blob.
PUB_RE = re.compile(r"PUB(?:;|%3B|\\u003[Bb])([0-9a-fA-F]{32})")

TERMINAL = {None, "dead_404", "protected", "no_pub_id"}

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")


def _blank(url, slug, **over):
    row = {"url": url, "slug": slug, "pub_id": None, "script_name": None,
           "script_access": None, "version": None, "created": None, "updated": None,
           "source_available": False, "source_len": 0, "source_path": None,
           "pub_selection": None, "error": None}
    row.update(over)
    return row


class TradingViewSourceSpider(scrapy.Spider):
    name = "tvsource"

    custom_settings = {
        "ROBOTSTXT_OBEY": False,              # spider-scoped only — see module docstring
        "DOWNLOAD_DELAY": 5,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 1,
        "CONCURRENT_REQUESTS": 2,             # one per host, so the two hops interleave
        "RETRY_TIMES": 2,
        "HTTPERROR_ALLOWED_CODES": [404],     # a dead script is a logged row, not a drop
        # USER_AGENT, not DEFAULT_REQUEST_HEADERS: the latter REPLACES Scrapy's
        # default {Accept, Accept-Language} dict, so every request would claim to
        # be Chrome while sending no Accept headers — a signature no real browser
        # produces, i.e. more bot-shaped than the default it was meant to improve.
        "USER_AGENT": UA,
        "LOG_LEVEL": "INFO",
    }

    def __init__(self, limit=None, worklist=None, try_closed=None, *a, **kw):
        super().__init__(*a, **kw)
        self.limit = int(limit) if limit else None
        # -a worklist=tv_scripts_index_union.csv  -> ONE-HOP mode (see start_requests)
        self.worklist = (ROOT / "datastore" / worklist) if worklist else WORKLIST
        # -a try_closed=1 -> request script_access 2/3 anyway instead of recording
        # them as `protected` unrequested. They 401 (probed), so this only costs
        # requests; it does not add rows. Exists so the skip is an explicit choice.
        self.try_closed = bool(try_closed)
        self._fh = None
        self.stats_rows = 0
        self.skipped_closed = 0

    # ---- lifecycle ---------------------------------------------------------

    def _resumable(self):
        """Return {url: error} for rows already logged, so terminal ones are skipped."""
        done = {}
        if JSONL.exists():
            with open(JSONL, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        r = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    done[r["url"]] = r.get("error")
        return done

    async def start(self):                       # Scrapy >= 2.13 entry point
        for r in self.start_requests():
            yield r

    def start_requests(self):
        PINE_DIR.mkdir(parents=True, exist_ok=True)
        JSONL.parent.mkdir(parents=True, exist_ok=True)
        self._fh = open(JSONL, "a", encoding="utf-8")

        done = self._resumable()
        with open(self.worklist, encoding="utf-8", newline="") as f:
            work = list(csv.DictReader(f))

        pending = [w for w in work if done.get(w["url"], "___") not in TERMINAL]
        self.logger.info(
            "worklist %s | %d rows | already terminal %d | pending %d",
            self.worklist.name, len(work), len(work) - len(pending), len(pending))

        if self.limit:
            pending = pending[: self.limit]
            self.logger.info("SLICE MODE: %d urls", len(pending))

        for w in pending:
            # ---- ONE-HOP MODE ------------------------------------------------
            # tv_scripts_index_*.csv (from the `tvlinks` spider) already carries
            # `pub_id` straight from TradingView's own index JSON, so hop 1 —
            # fetching the script page purely to regex a PUB; id out of it — is
            # pure waste, AND it removes the multi-PUB guess entirely: the id is
            # authoritative here, not "first match in document order" (an n=1
            # hypothesis that previously cost a name-check gate, a remedy script,
            # and 10 rows that could never be resolved).
            pub = (w.get("pub_id") or "").strip()
            if pub.startswith("PUB;"):
                # `script_access` 2 and 3 are 401 Unauthorized at pine-facade
                # (probed 2026-07-25). Record them as `protected` WITHOUT spending
                # a request — on the 992-row `all` index that is 551 requests saved.
                acc = (w.get("script_access") or "").strip()
                if acc and acc != "1" and not self.try_closed:
                    self._emit(_blank(w["url"], w["slug"], pub_id=pub,
                                      script_name=w.get("title"), script_access=acc,
                                      error="protected"))
                    self.skipped_closed += 1
                    continue
                yield scrapy.Request(
                    FACADE.format(pub.removeprefix("PUB;")),
                    callback=self.parse_source, errback=self.err_facade,
                    cb_kwargs={"url": w["url"], "slug": w["slug"],
                               "pub": pub.removeprefix("PUB;")},
                    dont_filter=True)
                continue

            # ---- TWO-HOP MODE (url-only worklists, e.g. tv_urls.csv) ---------
            yield scrapy.Request(
                # Carry the WORKLIST url, not response.url: RedirectMiddleware
                # rewrites the latter on a renamed script, producing a row whose
                # url is absent from tv_urls.csv -> _resumable() never matches it
                # (re-fetched every restart, never converges) and the reporter's
                # {url: row} collapse gains an extra key, pushing the six-term
                # identity past 705 for a reason the report cannot explain.
                w["url"], callback=self.parse_page, errback=self.err_page,
                cb_kwargs={"slug": w["slug"], "url": w["url"]},
                dont_filter=True)

    def closed(self, reason):
        if self._fh:
            self._fh.close()
        self.logger.info("wrote %d jsonl rows (%d closed-source skipped without a "
                         "request) (reason=%s)", self.stats_rows, self.skipped_closed, reason)

    def _emit(self, row):
        self._fh.write(json.dumps(row, ensure_ascii=False) + "\n")
        self._fh.flush()
        self.stats_rows += 1

    # ---- hop 1 -------------------------------------------------------------

    def parse_page(self, response, slug, url):
        # DEVIATION 1 (see module docstring): hop-1 404 -> TERMINAL dead_404.
        # Hand-verified these are genuinely removed scripts, not blocking.
        if response.status == 404:
            self._emit(_blank(url, slug, error="dead_404"))
            return

        m = PUB_RE.search(response.text)
        if not m:
            # Guaranteed to happen: some pages expose only USER;<hash>.
            self._emit(_blank(url, slug, error="no_pub_id"))
            return

        pub = m.group(1)
        yield scrapy.Request(
            FACADE.format(pub), callback=self.parse_source, errback=self.err_facade,
            cb_kwargs={"url": url, "slug": slug, "pub": pub},
            dont_filter=True)

    def err_page(self, failure):
        rq = failure.request
        self._emit(_blank(rq.cb_kwargs.get("url", rq.url), rq.cb_kwargs.get("slug", ""), error="http_error"))

    # ---- hop 2 -------------------------------------------------------------

    def parse_source(self, response, url, slug, pub):
        if response.status == 404:
            self._emit(_blank(url, slug, pub_id=f"PUB;{pub}", error="dead_404"))
            return

        try:
            d = json.loads(response.text)
        except json.JSONDecodeError:
            self._emit(_blank(url, slug, pub_id=f"PUB;{pub}", error="json_error"))
            return
        if not isinstance(d, dict):
            # facade returns a bare string on access denial
            self._emit(_blank(url, slug, pub_id=f"PUB;{pub}", error="protected"))
            return

        src = d.get("source") or ""
        access = d.get("scriptAccess")
        # DEVIATION 2 (see module docstring): `protected` == no usable source came
        # back, NOT `access != "open_no_auth"`. Source that arrives is kept and its
        # access label recorded; report_tv_source.py tallies the labels so a
        # non-open_no_auth capture is visible rather than silently discarded.
        if not src:
            self._emit(_blank(url, slug, pub_id=f"PUB;{pub}",
                              script_name=d.get("scriptName"), script_access=access,
                              error="protected"))
            return

        path = PINE_DIR / f"{slug}.pine"
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(src)

        self._emit(_blank(
            url, slug, pub_id=f"PUB;{pub}", script_name=d.get("scriptName"),
            script_access=access, version=d.get("version"), created=d.get("created"),
            updated=d.get("updated"), source_available=True, source_len=len(src),
            source_path=path.relative_to(ROOT).as_posix(),   # posix: TVSRC-4 hands this to another repo
            pub_selection="first", error=None))

    def err_facade(self, failure):
        rq = failure.request
        k = rq.cb_kwargs
        self._emit(_blank(k.get("url", rq.url), k.get("slug", ""),
                          pub_id=f"PUB;{k.get('pub')}", error="http_error"))
