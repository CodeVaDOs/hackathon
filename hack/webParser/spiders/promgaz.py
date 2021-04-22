import scrapy

from webParser.spiders.abstractSpider import AbstractSpider


class MetaboSpider(AbstractSpider):
    name = 'promgaz'
    urls = [
        'http://promgazkomplect.com.ua/catalog/fil-tri-gazu'
    ]
