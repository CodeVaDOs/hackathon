import scrapy

from webParser.spiders.abstractSpider import AbstractSpider


class SsbbSpider(AbstractSpider):
    name = 'ssbb'
    urls = [
        'https://ssbb.com.ua/uk/injenerni-mereji-kyiv/',
    ]
