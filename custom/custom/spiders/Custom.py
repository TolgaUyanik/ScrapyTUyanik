import scrapy
from custom.items import CustomItem

class CustomSpider(scrapy.Spider):
    name = "CustomSpider"
    start_urls = [
        "",
    ]

    def parse(self, response):
        item = CustomItem()
        #for info in response.css("div"):
        #item["name"]        = info.css("").get()
        #item["link"]        = info.css("a::attr(href)").get()
        #item["description"] = info.css("").get()
        #item["field"]       = info.css("").getall()
        item["url"]          = response.url
        yield item
