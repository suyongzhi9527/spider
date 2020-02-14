# -*- coding: utf-8 -*-
import scrapy
from bmw.items import BmwItem


class Bmw5Spider(scrapy.Spider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        # Selectors list
        ui_box = response.xpath('//div[@class="uibox"]')[1:]
        for box in ui_box:
            category = box.xpath('.//div[@class="uibox-title"]/a/text()').get()
            urls = box.xpath('.//ul/li/a/img/@src').getall()
            # for url in urls:
            #     url = "https:" + url
            #     print(url)
            # for url in urls:
            #     url = response.urljoin(url)
            #     print(url)
            urls = list(map(lambda url: response.urljoin(url), urls))
            item = BmwItem(category=category, image_urls=urls)
            yield item
