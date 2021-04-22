import scrapy
from webParser.spiders.abstractSpider import AbstractSpider


class KovaSpider(AbstractSpider):
    name = 'kova'
    urls = [
        'http://www.kova.net.ua/UA/zemelni-roboti/budivnytstvo-system-kanalizatsii-ta-vodopostachannia.html',
    ]
