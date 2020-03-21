# -*- coding: utf-8 -*-
import scrapy


class JobSpider(scrapy.Spider):
    name = 'job'  # 爬虫名称
    allowed_domains = ['51job.com']  # 只在这个网站下抓取数据
    start_urls = ['https://search.51job.com/list/040000,000000,0000,00,9,99,Python,2,1.html']  # 开始抓取数据链接

    def parse(self, response):
        """
        :response 网站返回的数据
        """
        # print(response.text)
        selectors = response.xpath('//div[@class="el"]')
        for selector in selectors:
            # 详情页链接
            urls = selector.xpath('./p[contains(@class,"t1")]/span/a/@href').get()
            if urls:
                # yield 生成器 类似return
                yield scrapy.Request(urls, callback=self.parseDetail)

    def parseDetail(self, response):
        """
        处理详情页数据
        """
        title = response.xpath('//div[@class="cn"]/h1/text()').get()  # 职位
        salary = response.xpath('//div[@class="cn"]/strong/text()').get()  # 薪资
        company = response.xpath('//div[@class="cn"]/p[@class="cname"]/a/@title').get()  # 公司

        items = {
            'title': title,
            'salary': salary,
            'company': company
        }
        yield items
