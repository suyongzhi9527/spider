# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from scrapy.exceptions import DropItem
import logging

log = logging.getLogger("SavepicturePipeline")


class MeituluPipeline(object):
    def process_item(self, item, spider):
        return item


class SavepicturePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for img_url in item['img_url']:
            yield Request(url=img_url, meta={'item': item, 'index': item['img_url'].index(img_url)})

    def item_completed(self,  results, item, info):
        if not results[0][0]:
            raise DropItem('下载失败!')
        logging.debug('下载成功!')
        return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        index = request.meta['index']
        image_name = item['name'][index]+'.jpg'

        return image_name
