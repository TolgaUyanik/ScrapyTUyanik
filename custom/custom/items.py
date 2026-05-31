# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CustomItem(scrapy.Item):
    name        = scrapy.Field()
    link        = scrapy.Field()
    description = scrapy.Field()
    field       = scrapy.Field()
    url         = scrapy.Field()
    timestamp   = scrapy.Field()
