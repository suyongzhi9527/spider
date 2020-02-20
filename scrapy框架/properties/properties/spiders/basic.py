# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['gumtree.com']
    start_urls = ['https://www.gumtree.com/property-for-sale']

    def parse(self, response):
        title = response.xpath('//*[@class="listing-title"]/text()').extract()
        print('*' * 50)
        print(title)
        print('*' * 50)
