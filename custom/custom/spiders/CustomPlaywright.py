import scrapy
from custom.items import CustomItem
from custom.utils import random_user_agent


class CustomPlaywrightSpider(scrapy.Spider):
    name = "custompw"
    start_urls = [
        "",
    ]

    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "PLAYWRIGHT_LAUNCH_OPTIONS": {"headless": True},
    }

    def start_requests(self):
        for url in self.start_urls:
            headers = {
                "User-Agent": random_user_agent(),
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
            }
            yield scrapy.Request(
                url,
                meta={"playwright": True},
                headers=headers,
                callback=self.parse,
            )

    async def parse(self, response):
        item = CustomItem()
        for info in response.css(""):
            item["name"]        = info.css("").get()
            item["link"]        = info.css("a::attr(href)").get()
            item["description"] = info.css("").get()
            item["field"]       = info.css("").getall()
            item["url"]         = response.url
            yield item
