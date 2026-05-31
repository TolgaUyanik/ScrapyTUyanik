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


class LetterboxdItem(scrapy.Item):
    rank           = scrapy.Field()
    title          = scrapy.Field()
    year           = scrapy.Field()
    original_title = scrapy.Field()
    director       = scrapy.Field()
    tagline        = scrapy.Field()
    synopsis       = scrapy.Field()
    cast           = scrapy.Field()
    genres         = scrapy.Field()
    runtime        = scrapy.Field()
    country        = scrapy.Field()
    language       = scrapy.Field()
    avg_rating     = scrapy.Field()
    rating_count   = scrapy.Field()
    poster_url     = scrapy.Field()
    url            = scrapy.Field()
