import re
import scrapy
from custom.items import LetterboxdItem
from custom.utils import random_user_agent


class LetterboxdSpider(scrapy.Spider):
    name = "letterboxd"
    start_urls = ["https://letterboxd.com/official/list/letterboxds-top-500-films/"]

    custom_settings = {
        "ROBOTSTXT_OBEY": False,
        "DOWNLOAD_DELAY": 2,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 1,
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                callback=self.parse_list,
                headers={"User-Agent": random_user_agent()},
            )

    def parse_list(self, response):
        page_num = self._page_num(response.url)

        for div in response.css(".react-component[data-item-link]"):
            film_path = div.attrib.get("data-target-link") or div.attrib.get("data-item-link")
            list_index = int(div.attrib.get("data-list-index", 0))
            rank = (page_num - 1) * 100 + list_index + 1

            if film_path:
                yield response.follow(
                    film_path,
                    callback=self.parse_film,
                    cb_kwargs={"rank": rank},
                    headers={"User-Agent": random_user_agent()},
                )

        next_href = response.css("a.next::attr(href)").get()
        if next_href:
            yield response.follow(
                next_href,
                callback=self.parse_list,
                headers={"User-Agent": random_user_agent()},
            )

    def parse_film(self, response, rank=None):
        item = LetterboxdItem()

        item["rank"] = rank
        item["url"] = response.css("meta[property='og:url']::attr(content)").get()
        item["poster_url"] = response.css("meta[property='og:image']::attr(content)").get()
        item["title"] = response.css("h1.headline-1.primaryname span.name::text").get("").strip()
        item["year"] = response.css(".productioninfo .releasedate a::text").get("").strip()
        item["original_title"] = response.css("h2.originalname em::text").get("").strip()
        item["director"] = ", ".join(
            response.css(".credits .contributorlist a.contributor span.prettify::text").getall()
        )
        item["tagline"] = response.css("h4.tagline::text").get("").strip()

        # synopsis: live HTML uses class="truncate" (browser JS adds condenseable/condensed variants)
        # og:description is more reliable and always has the full text
        item["synopsis"] = response.css(
            "meta[property='og:description']::attr(content)"
        ).get("").strip()

        # Cast: exclude the "Show All…" anchor which has no href starting with /actor/
        item["cast"] = response.css(".cast-list a[href^='/actor/']::text").getall()

        item["genres"] = response.css("#tab-panel-genres a[href*='/films/genre/']::text").getall()

        footer_text = " ".join(response.css(".text-link.text-footer::text").getall())
        runtime_match = re.search(r"(\d+)\s*mins?", footer_text)
        item["runtime"] = int(runtime_match.group(1)) if runtime_match else None

        item["country"] = response.css(
            "#tab-panel-details a[href*='/films/country/']::text"
        ).get("").strip()
        item["language"] = response.css(
            "#tab-panel-details a[href*='/films/language/']::text"
        ).get("").strip()

        # rating histogram loads via JS — use twitter:data2 meta ("4.68 out of 5")
        twitter_rating = response.css("meta[name='twitter:data2']::attr(content)").get("")
        rating_match = re.match(r"([\d.]+)", twitter_rating)
        item["avg_rating"] = float(rating_match.group(1)) if rating_match else None

        # rating_count not in static HTML (requires JS/API); placeholder for future use
        item["rating_count"] = None

        yield item

    @staticmethod
    def _page_num(url):
        m = re.search(r"/page/(\d+)/", url)
        return int(m.group(1)) if m else 1
