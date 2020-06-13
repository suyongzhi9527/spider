# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Image360Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 图片的标题
    tag = scrapy.Field()  # 图片的标签
    width = scrapy.Field()  # 图片的宽度
    height = scrapy.Field()  # 图片的高度
    url = scrapy.Field()  # 图片的url
