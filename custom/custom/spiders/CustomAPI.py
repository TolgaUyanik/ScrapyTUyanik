import os
import scrapy
from custom.items import CustomItem


class CustomAPISpider(scrapy.Spider):
    name = "CustomAPI"

    # Base API endpoint — override via -s API_BASE_URL=https://...
    api_base_url = "https://api.example.com/items"

    # Auth — set via environment variable or override here
    api_key = os.getenv("API_KEY", "")

    # Pagination: set initial page and page size
    page = 1
    page_size = 100

    def start_requests(self):
        yield self._build_request(self.page)

    def _build_request(self, page):
        url = f"{self.api_base_url}?page={page}&per_page={self.page_size}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
        }
        return scrapy.Request(url, headers=headers, callback=self.parse, cb_kwargs={"page": page})

    def parse(self, response, page):
        data = response.json()

        # Adapt these keys to the actual API response shape
        results = data.get("results") or data.get("data") or data or []

        for record in results:
            item = CustomItem()
            item["name"]        = record.get("name")
            item["link"]        = record.get("url") or record.get("link")
            item["description"] = record.get("description")
            item["field"]       = record.get("tags") or record.get("categories")
            item["url"]         = response.url
            yield item

        # Follow pagination — handles both "next URL" and "page number" styles
        next_url = data.get("next")
        if next_url:
            yield scrapy.Request(next_url, headers=response.request.headers, callback=self.parse, cb_kwargs={"page": page + 1})
        elif results and len(results) == self.page_size:
            yield self._build_request(page + 1)
