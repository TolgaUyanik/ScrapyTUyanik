"""Flirting with Models episode spider.

Two sources, selectable with `-a source=`:

  api (default)  https://app.podcastai.com/api/v1 — the backend the site's own
                 /episodes page calls. All 125 episodes plus chapters, speakers,
                 transcript URL and platform IDs. That host serves
                 `robots.txt: Disallow: /`, so this spider sets
                 ROBOTSTXT_OBEY=False. It is an unauthenticated public read
                 endpoint, but the override is deliberate — know that before you
                 run it.

  rss            https://feeds.captivate.fm/flirting-with-models/ — the public
                 podcast feed (no robots.txt). All 125 episodes, but only the
                 fields a podcast feed carries: no handle, chapters, speakers or
                 transcript URL.

  scrapy crawl fwm -o ../testfolder/episodes.json
  scrapy crawl fwm -a source=rss -o ../testfolder/episodes.json
"""

from pathlib import Path

import scrapy

from custom.items import EpisodeItem

SHOW = "flirting-with-models"
API = f"https://app.podcastai.com/api/v1/portal/shows/{SHOW}"
RSS = f"https://feeds.captivate.fm/{SHOW}/"
SITE = "https://www.flirtingwithmodels.com"

ITUNES = "http://www.itunes.com/dtds/podcast-1.0.dtd"

# Raw Deepgram transcript JSON, one file per episode (~1.8 MB each, ~225 MB total).
# Relative to custom/, matching the `-o ../testfolder/...` convention.
TRANSCRIPTS_DIR = Path("../testfolder/transcripts")


def to_seconds(hms):
    """'56:39' / '1:02:03' / '3355' -> int seconds. None if unparseable."""
    if not hms:
        return None
    parts = hms.strip().split(":")
    try:
        nums = [int(p) for p in parts]
    except ValueError:
        return None
    total = 0
    for n in nums:
        total = total * 60 + n
    return total


class FlirtingWithModelsSpider(scrapy.Spider):
    name = "fwm"
    source = "api"          # -a source=rss
    page_size = 100         # API caps a page at 100 regardless of limit

    custom_settings = {
        # Required for source=api — see module docstring.
        "ROBOTSTXT_OBEY": False,
        "DEFAULT_REQUEST_HEADERS": {"Accept": "application/json, application/xml;q=0.9, */*;q=0.8"},
    }

    def start_requests(self):
        if self.source == "rss":
            yield scrapy.Request(RSS, callback=self.parse_rss)
        elif self.source == "api":
            yield self._list_request(0)
        else:
            raise ValueError(f"source must be 'api' or 'rss', got {self.source!r}")

    # ---------- api ----------

    def _list_request(self, offset):
        url = f"{API}/episodes?limit={self.page_size}&offset={offset}"
        return scrapy.Request(url, callback=self.parse_list, cb_kwargs={"offset": offset})

    def parse_list(self, response, offset):
        episodes = response.json()["data"]

        for ep in episodes:
            # The detail endpoint adds audio_url, chapters and guid; the list
            # endpoint has everything else already.
            yield scrapy.Request(
                f"{API}/episodes/{ep['handle']}",
                callback=self.parse_episode,
            )

        if len(episodes) == self.page_size:
            yield self._list_request(offset + self.page_size)

    def parse_episode(self, response):
        ep = response.json()
        item = EpisodeItem()
        item["handle"]             = ep.get("handle")
        item["title"]              = ep.get("title")
        item["description"]        = ep.get("description")
        item["season"]             = ep.get("seasonNumber")
        item["episode"]            = ep.get("episodeNumber")
        item["type"]               = ep.get("type")
        item["published_at"]       = ep.get("publishedAt")
        item["duration"]           = ep.get("duration")
        item["audio_url"]          = ep.get("audioURL")
        item["audio_length"]       = ep.get("audioLength")
        item["image_url"]          = ep.get("imageURL")
        item["transcript_url"]     = ep.get("transcriptURL")
        item["transcript_path"]    = None
        item["chapters"]           = ep.get("tableOfContents")
        item["speakers"]           = [s["name"] for s in ep.get("speakers") or [] if s.get("name")]
        item["yt_video_id"]        = ep.get("ytVideoHandle")
        item["apple_episode_id"]   = ep.get("appleEpisodeID")
        item["spotify_episode_id"] = ep.get("spotifyEpisodeID")
        item["guid"]               = ep.get("guid")
        item["page_url"]           = f"{SITE}/episodes/{ep['handle']}"
        item["source"]             = "api"
        item["url"]                = response.url

        if not item["transcript_url"]:
            yield item
            return

        path = TRANSCRIPTS_DIR / f"{item['handle']}.json"
        if path.exists():
            item["transcript_path"] = str(path)
            yield item
            return

        yield scrapy.Request(
            item["transcript_url"],
            callback=self.save_transcript,
            errback=self.transcript_failed,
            cb_kwargs={"item": item, "path": path},
        )

    def save_transcript(self, response, item, path):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(response.body)
        item["transcript_path"] = str(path)
        yield item

    def transcript_failed(self, failure):
        item = failure.request.cb_kwargs["item"]
        self.logger.warning("transcript download failed for %s: %s", item["handle"], failure.value)
        yield item

    # ---------- rss ----------

    def parse_rss(self, response):
        response.selector.register_namespace("itunes", ITUNES)

        for node in response.xpath("//item"):
            item = EpisodeItem()
            item["title"]        = node.xpath("title/text()").get()
            item["description"]  = node.xpath("description/text()").get()
            item["season"]       = node.xpath("itunes:season/text()").get()
            item["episode"]      = node.xpath("itunes:episode/text()").get()
            item["type"]         = node.xpath("itunes:episodeType/text()").get()
            item["published_at"] = node.xpath("pubDate/text()").get()
            item["duration"]     = to_seconds(node.xpath("itunes:duration/text()").get())
            item["audio_url"]    = node.xpath("enclosure/@url").get()
            item["audio_length"] = node.xpath("enclosure/@length").get()
            item["image_url"]    = node.xpath("itunes:image/@href").get()
            item["guid"]         = node.xpath("guid/text()").get()
            item["source"]       = "rss"
            item["url"]          = response.url
            yield item


if __name__ == "__main__":
    assert to_seconds("56:39") == 3399
    assert to_seconds("1:02:03") == 3723
    assert to_seconds("3355") == 3355
    assert to_seconds(None) is None
    assert to_seconds("n/a") is None
    print("ok")
