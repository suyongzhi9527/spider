# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class ImagespiderPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['img_url']:
            yield Request(image_url)

    def file_path(self, request, response=None, info=None):
        # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
        image_guid = request.url.split('/')[-1]  # 提取url前面名称作为图片名。
        return 'image/%s' % image_guid
