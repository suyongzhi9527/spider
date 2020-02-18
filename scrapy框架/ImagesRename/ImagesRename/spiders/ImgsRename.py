# -*- coding: utf-8 -*-
import scrapy
from ImagesRename.items import ImagesrenameItem


class ImgsrenameSpider(scrapy.Spider):
    name = 'ImgsRename'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html', 'http://lab.scrapyd.cn/archives/57.html']

    def parse(self, response):
        item = ImagesrenameItem()
        item['imgUrl'] = response.css(".post img::attr(src)").extract()
        item['imgname'] = response.css(".post-title a::text").extract_first()
        yield item
