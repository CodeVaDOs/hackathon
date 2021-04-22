import scrapy
import json
from abc import ABC

from webParser.items import Title, Body, Image
from scrapy import signals


class AbstractSpider(scrapy.Spider, ABC):
    name = 'fetcher'
    urls = [
        'http://www.kova.net.ua/UA/zemelni-roboti/budivnytstvo-system-kanalizatsii-ta-vodopostachannia.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

