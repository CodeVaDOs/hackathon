import scrapy
import json
from abc import ABC

from webParser.items import Title, Body, Image
from scrapy import signals


class AbstractSpider(scrapy.Spider, ABC):
    def __init__(self):
        self.output = {
            "titles": [],
            "bodies": [],
            "images": []
        }

    def spider_received(self, item):
        if type(item) is Image:
            self.output['images'].extend(item['image_urls'])
        if type(item) is Title and item['title'].strip():
            self.output['titles'].append(item['title'].strip())
        if type(item) is Body and item['body'].strip():
            self.output['bodies'].append(item['body'].strip().replace('\t', ''))

    def spider_closed(self):
        with open(f'{self.name}.json', 'w', encoding='utf-8') as file:
            json.dump(self.output, file, ensure_ascii=False)

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(AbstractSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_received, signals.item_scraped)
        crawler.signals.connect(spider.spider_closed, signals.spider_closed)

        return spider

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for src in response.xpath("//img[contains(@src, '.jpg') or contains(@src, '.png')]"):
            yield Image(image_urls=[response.urljoin(src.xpath("@src").extract_first())])

        for title in response.css("h2, h1"):
            yield Title(title=title.css("::text").get())

        for body in response.css("p"):
            yield Body(body=body.css("::text").get())
