"""Alpha Architect spiders: the full blog archive and the curated "best of" list.

alphaarchitect.com is WordPress behind a Cloudflare *managed* challenge. Two
facts shape this design:

1. Every request is challenged, robots.txt included, and Playwright chromium
   cannot pass it -- headless and headed both loop on "Just a moment..."
   forever, because the challenge fingerprints the automation build. So there
   is no browser to drive here. `mint_cf_cookie.py` borrows a cf_clearance
   cookie from a normal Chrome session and these spiders crawl plain HTTP.
2. /wp-json/wp/v2 is wide open and content.rendered carries the whole post
   body, so ~2,500 posts arrive in ~25 requests and no post page is ever
   fetched. Markdown is converted in-process and written straight to disk.

    cd custom
    python mint_cf_cookie.py                        # once, and again on 403s
    scrapy crawl aa_bestof -o ../testfolder/aa_bestof.json
    scrapy crawl aa_blog -a pages=1                 # smoke test: 100 posts
    scrapy crawl aa_blog -o ../testfolder/aa_blog.json

robots.txt disallows only /wp-admin/ and /user/, so ROBOTSTXT_OBEY stays on.
"""

import html
import json
import pathlib
import re

import scrapy
from markdownify import markdownify

# ponytail: yields plain dicts, not CustomItem -- WP hands back ~10 fields that
# would only be re-declared as boilerplate. JSON/CSV export is identical.

SITE = "https://alphaarchitect.com"
REST = SITE + "/wp-json/wp/v2"
BESTOF_URL = SITE + "/best-of-blog/"
CF_FILE = pathlib.Path(__file__).resolve().parents[2] / "cf_cookies.json"

# Post permalinks live at the site root: https://alphaarchitect.com/<slug>/.
# So do ordinary pages (/about/, /blog/) -- shape alone cannot tell them apart,
# which is why candidate slugs get verified against the REST post index.
POST_URL_RE = re.compile(r"^https://alphaarchitect\.com/([a-z0-9][a-z0-9-]*)/$")

PER_PAGE = 100


def _clean(text):
    return re.sub(r"\s+", " ", text).strip()


def _detag(markup):
    """WP returns rendered HTML for titles and excerpts; want the plain text."""
    return _clean(html.unescape(re.sub(r"<[^>]+>", " ", markup or "")))


def _yaml(value):
    """YAML is a JSON superset, so json.dumps is a correct scalar/list emitter."""
    return json.dumps(value, ensure_ascii=False)


def bestof_links(response):
    """Curated posts on /best-of-blog/, keyed by slug.

    Links are read from div.post-content only: the fusion-recent-posts block
    below it is an auto-generated "recent posts" widget, not curation. One
    ordered pass over headings and links, so every link keeps the
    h4.fusion-tab-heading section that precedes it.
    """
    found = {}
    section = None
    nodes = response.css("div.post-content").xpath(
        ".//h4[contains(@class, 'fusion-tab-heading')] | .//a[@href]"
    )
    for node in nodes:
        if node.root.tag == "h4":
            section = _clean(" ".join(node.xpath(".//text()").getall()))
            continue
        match = POST_URL_RE.match(response.urljoin(node.attrib["href"]))
        if not match or match.group(1) in found:
            continue
        found[match.group(1)] = {
            "slug": match.group(1),
            "url": match.group(0),
            "section": section,
            "title": _clean(" ".join(node.xpath(".//text()").getall())),
        }
    return found


class _CloudflareSpider(scrapy.Spider):
    """Shared clearance plumbing for alphaarchitect.com."""

    allowed_domains = ["alphaarchitect.com"]
    handle_httpstatus_list = [403]

    @classmethod
    def update_settings(cls, settings):
        # Read here, not at import time, so `scrapy list` still works before
        # the cookie has been minted.
        super().update_settings(settings)
        try:
            cf = json.loads(CF_FILE.read_text(encoding="utf-8"))
        except OSError:
            raise RuntimeError(
                f"{CF_FILE} not found -- run `python mint_cf_cookie.py` from custom/ first"
            )
        # The cookie rides in DEFAULT_REQUEST_HEADERS rather than Request(cookies=...)
        # so it is attached to the robots.txt fetch too, and COOKIES_ENABLED is
        # off so CookiesMiddleware cannot rewrite the header mid-crawl.
        settings.set("USER_AGENT", cf["ua"], priority="spider")
        settings.set("COOKIES_ENABLED", False, priority="spider")
        settings.set(
            "DEFAULT_REQUEST_HEADERS",
            {
                "User-Agent": cf["ua"],
                "Accept-Language": "en-US,en;q=0.9",
                "Cookie": "; ".join(f"{k}={v}" for k, v in cf["cookies"].items()),
            },
            priority="spider",
        )

    def ensure_cleared(self, response):
        """Abort loudly on 403 -- every later request would fail the same way."""
        if response.status == 403:
            raise scrapy.exceptions.CloseSpider(
                f"403 from {response.url} -- cf_clearance expired or your IP changed. "
                "Re-run `python mint_cf_cookie.py`, then restart the crawl."
            )


class AlphaArchitectBestOfSpider(_CloudflareSpider):
    """/best-of-blog/ -> one record per curated post.

    The page also links a handful of ordinary pages, so the collected slugs are
    confirmed against the posts endpoint in a single multi-slug call before
    anything is yielded.
    """

    name = "aa_bestof"
    start_urls = [BESTOF_URL]

    def parse(self, response):
        self.ensure_cleared(response)
        found = bestof_links(response)
        if not found:
            self.logger.error(
                "no curated links parsed -- div.post-content markup changed at %s", response.url
            )
            return
        self.logger.info("best-of: %d candidate links", len(found))
        yield response.follow(
            f"{REST}/posts?slug={','.join(found)}&per_page={PER_PAGE}&_fields=slug",
            callback=self.parse_verify,
            cb_kwargs={"found": found},
        )

    def parse_verify(self, response, found):
        self.ensure_cleared(response)
        real = {p["slug"] for p in json.loads(response.text)}
        dropped = sorted(set(found) - real)
        self.logger.info(
            "best-of: %d posts confirmed, %d non-post links dropped (%s)",
            len(real), len(dropped), ", ".join(dropped) or "none",
        )
        for slug, record in found.items():
            if slug in real:
                yield record


class AlphaArchitectBlogSpider(_CloudflareSpider):
    """Whole blog archive -> one markdown file per post, plus a JSON index.

    Walks /wp-json/wp/v2/posts at 100 posts per page, so ~2,500 posts cost ~25
    requests. Category and tag IDs are resolved to names up front from the two
    taxonomy endpoints (85 categories, 252 tags), and /best-of-blog/ is read
    once so curated posts carry best_of: true in their front matter.

    -a out=DIR      markdown destination   (default ../output/alpha-architect)
    -a pages=N      stop after N REST pages of 100 posts   (0 = all)
    -a bestof=0     skip the best-of cross-reference
    """

    name = "aa_blog"

    def __init__(self, out="../output/alpha-architect", pages=0, bestof=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.out = pathlib.Path(out)
        self.max_pages = int(pages)  # 0 = no limit
        self.want_bestof = str(bestof) not in ("0", "", "False", "false")
        self.terms = {"categories": {}, "tags": {}}
        self.bestof = {}
        self.written = 0

    async def start(self):
        self.out.mkdir(parents=True, exist_ok=True)
        yield self.term_request("categories", 1)

    # --- taxonomy ---------------------------------------------------------
    # Resolved before any post is written, so front matter carries names rather
    # than the bare numeric IDs the posts endpoint returns.

    def term_request(self, kind, page):
        return scrapy.Request(
            f"{REST}/{kind}?per_page={PER_PAGE}&page={page}&_fields=id,name",
            callback=self.parse_terms,
            cb_kwargs={"kind": kind, "page": page},
        )

    def parse_terms(self, response, kind, page):
        self.ensure_cleared(response)
        for term in json.loads(response.text):
            self.terms[kind][term["id"]] = term["name"]

        if page < int(response.headers.get("x-wp-totalpages", b"1")):
            yield self.term_request(kind, page + 1)
            return

        self.logger.info("%s: %d resolved", kind, len(self.terms[kind]))
        if kind == "categories":
            yield self.term_request("tags", 1)
        elif self.want_bestof:
            yield scrapy.Request(BESTOF_URL, callback=self.parse_bestof)
        else:
            yield self.posts_request(1)

    def parse_bestof(self, response):
        self.ensure_cleared(response)
        # No REST verification pass here: a stray page slug simply never matches
        # a post being written, so it can only ever fail to flag anything.
        self.bestof = bestof_links(response)
        if not self.bestof:
            self.logger.warning(
                "no curated links parsed -- best_of will be false for every post"
            )
        self.logger.info("best-of: %d slugs flagged", len(self.bestof))
        yield self.posts_request(1)

    # --- posts ------------------------------------------------------------

    def posts_request(self, page):
        fields = "id,slug,date,modified,title,link,content,excerpt,categories,tags"
        return scrapy.Request(
            f"{REST}/posts?per_page={PER_PAGE}&page={page}"
            f"&orderby=date&order=desc&_fields={fields}",
            callback=self.parse_posts,
            cb_kwargs={"page": page},
        )

    def parse_posts(self, response, page):
        self.ensure_cleared(response)
        posts = json.loads(response.text)
        total_pages = int(response.headers.get("x-wp-totalpages", b"1"))
        self.logger.info("posts page %d/%d: %d posts", page, total_pages, len(posts))

        for post in posts:
            yield self.write_post(post)

        if self.max_pages and page >= self.max_pages:
            self.logger.info("stopping at -a pages=%d", self.max_pages)
            return
        if page < total_pages:
            yield self.posts_request(page + 1)

    def write_post(self, post):
        slug = post["slug"]
        date = (post.get("date") or "")[:10]
        title = _detag(post["title"]["rendered"])
        summary = _detag(post["excerpt"]["rendered"])
        body = markdownify(
            post["content"]["rendered"], heading_style="ATX", strip=["script", "style"]
        ).strip()

        front = {
            "title": title,
            "slug": slug,
            "date": date,
            "modified": (post.get("modified") or "")[:10],
            "url": post.get("link"),
            "categories": [self.terms["categories"].get(i, i) for i in post.get("categories", [])],
            "tags": [self.terms["tags"].get(i, i) for i in post.get("tags", [])],
            "best_of": slug in self.bestof,
            "source": "alphaarchitect.com",
        }
        if slug in self.bestof:
            front["best_of_section"] = self.bestof[slug]["section"]

        lines = ["---"]
        lines += [f"{k}: {_yaml(v)}" for k, v in front.items()]
        lines += ["---", "", f"# {title}", ""]
        if summary:
            lines += [f"> {summary}", ""]
        lines += [body, ""]

        path = self.out / f"{date}-{slug}.md"
        path.write_text("\n".join(lines), encoding="utf-8")
        self.written += 1

        return dict(front, path=str(path), chars=len(body))

    def closed(self, reason):
        self.logger.info("wrote %d markdown files to %s (%s)", self.written, self.out, reason)
