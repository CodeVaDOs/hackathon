import scrapy

from webParser.spiders.abstractSpider import AbstractSpider


class MetaboSpider(AbstractSpider):
    name = 'metabo'
    urls = [
        'https://www.metabo.com/ua/uk/info/sferi-dijalnosti/budivelna-sprava-i-remont/sferi-zastosuvannja'
        '/inzhenerni-komunikaciji/',
    ]
