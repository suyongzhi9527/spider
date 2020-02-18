# -*- coding: utf-8 -*-
import scrapy
from ImageSpider.items import ImagespiderItem


class ImgspiderSpider(scrapy.Spider):
    name = 'imgspider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        item = ImagespiderItem()
        imgUrl = response.css(".post img::attr(src)").extract()
        item['img_url'] = imgUrl
        yield item
