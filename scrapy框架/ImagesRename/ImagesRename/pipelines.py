# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class ImagesrenamePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['imgUrl']:
            yield Request(image_url, meta={'name': item['imgname']})

    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        name = request.meta['name']
        name = re.sub(r'[？\\*|“<>:/]', '', name)
        filename = u'{0}/{1}'.format(name, image_guid)
        return filename
