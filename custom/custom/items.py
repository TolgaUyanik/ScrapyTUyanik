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


class EpisodeItem(scrapy.Item):
    """Podcast episode — union of the podcastai API and the Captivate RSS feed.

    Fields the active source cannot supply are left unset.
    """
    handle              = scrapy.Field()   # site slug, e.g. /episodes/<handle>  (api only)
    title               = scrapy.Field()
    description         = scrapy.Field()
    season              = scrapy.Field()
    episode             = scrapy.Field()
    type                = scrapy.Field()   # full | trailer | bonus
    published_at        = scrapy.Field()
    duration            = scrapy.Field()   # seconds
    audio_url           = scrapy.Field()
    audio_length        = scrapy.Field()   # bytes
    image_url           = scrapy.Field()
    transcript_url      = scrapy.Field()   # api only
    transcript_path     = scrapy.Field()   # api only — saved raw Deepgram JSON
    chapters            = scrapy.Field()   # api only — [{start, title, end}]
    speakers            = scrapy.Field()   # api only — [name]
    yt_video_id         = scrapy.Field()   # api only
    apple_episode_id    = scrapy.Field()   # api only
    spotify_episode_id  = scrapy.Field()   # api only
    guid                = scrapy.Field()   # rss only
    page_url            = scrapy.Field()   # api only
    source              = scrapy.Field()   # "api" | "rss"
    url                 = scrapy.Field()   # request URL this item came from
