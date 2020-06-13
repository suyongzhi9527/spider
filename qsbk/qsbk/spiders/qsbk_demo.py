# -*- coding: utf-8 -*-
import scrapy

from qsbk.items import QsbkItem
from scrapy import Request

class QsbkDemoSpider(scrapy.Spider):
    name = 'qsbk_demo'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/1']

    def parse(self, response):
        item = QsbkItem()
        outerbox = response.xpath('//div[@class="col1 old-style-col1"]/div')
        for box in outerbox:
            # author = box.xpath('.//div[@class="author clearfix"]/a/h2/text()').extract_first().strip()
            content_url = box.xpath('.//a[@class="contentHerf"]/@href').extract_first()
            content_url = 'https://www.qiushibaike.com' + content_url
            yield Request(content_url, callback=self.parse_detail, meta={'item': item})

        next_url = response.xpath('//ul[@class="pagination"]//li[8]/a/@href').extract()
        if next_url and len(next_url) > 0:
            next_url = next_url[0]
            yield Request('https://www.qiushibaike.com' + next_url, callback=self.parse)
    
    def parse_detail(self, response):
        item = QsbkItem()
        author = response.xpath('//div[@class="side-user-top"]/span[@class="side-user-name"]/text()').extract()
        div_content = response.xpath('//div[@class="content"]/text()').extract()
        item['author'] = author
        item['content'] = div_content
        yield item
