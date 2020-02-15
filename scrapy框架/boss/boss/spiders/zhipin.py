# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem


class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101280100/?query=Python%E7%88%AC%E8%99%AB&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+\?query=Python%E7%88%AC%E8%99%AB&page=\d'), follow=True),  # 匹配职位列表页规则
        Rule(LinkExtractor(allow=r'.+job_detail/[0-9a-zA-Z_~]+.html'), callback="parse_job", follow=False),  # 匹配职位详情页规则
    )

    def parse_job(self, response):
        title = response.xpath('//div[@class="name"]/h1/text()').get()
        salary = response.xpath('//span[@class="salary"]/text()').get().strip()
        job_info = response.xpath('//div[@class="info-primary"]/div/p//text()').getall()
        city = job_info[0]
        work_year = job_info[1]
        education = job_info[2]
        company = response.xpath('//a[@ka="job-detail-company-logo_custompage"]/@title').get().strip()
        item = BossItem(title=title, salary=salary, city=city, work_year=work_year, education=education,
                        company=company)
        yield item
