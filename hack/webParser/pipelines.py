# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import os
import scrapy
from urllib.parse import urlparse

from scrapy.exceptions import DropItem
from scrapy.pipelines.media import MediaPipeline
from itemadapter import ItemAdapter


# useful for handling different item types with a single interface

# class MyMediaPipeline(MediaPipeline):
#
#     def get_media_requests(self, item, info):
#         adapter = ItemAdapter(item)
#         for file_url in adapter['file_urls']:
#             yield scrapy.Request(file_url)
#
#     def item_completed(self, results, item, info):
#         file_paths = [x['path'] for ok, x in results if ok]
#         if not file_paths:
#             raise DropItem("Item contains no files")
#         adapter = ItemAdapter(item)
#         adapter['file_paths'] = file_paths
#         return item
