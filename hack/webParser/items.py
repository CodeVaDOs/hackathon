# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebparserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Image(scrapy.Item):
    image_urls = scrapy.Field()


class Title(scrapy.Item):
    title = scrapy.Field()


class Body(scrapy.Item):
    body = scrapy.Field()
