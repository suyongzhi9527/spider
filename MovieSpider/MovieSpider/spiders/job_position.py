# -*- coding: utf-8 -*-
import scrapy
from MovieSpider.items import MoviespiderItem


class JobPositionSpider(scrapy.Spider):
    name = 'job_position'
    allowed_domains = ['ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    def parse(self, response):
        item = MoviespiderItem()
        for jobs_primary in response.xpath('//table[@class="tbspan"]'):
            item['name'] = jobs_primary.xpath('.//tr/td/b/a[2]/text()').extract()
            item['url'] = jobs_primary.xpath('.//tr/td/b/a[2]/@href').extract()
            yield item
        
        next_url = response.xpath('//a[text()="下一页"]/@href').extract()
        # print(next_url)
        if next_url and len(next_url) > 0:
            next_url = next_url[0]
            yield scrapy.Request("https://www.ygdy8.net/html/gndy/china/" + next_url, callback=self.parse)
