# -*- coding: utf-8 -*-
import scrapy
from scrapy_test.items import ScrapyTestItem
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList


class ScrapyTestDemoSpider(scrapy.Spider):
    name = 'scrapy_test_demo'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/page/1/']

    def parse(self, response):
        # SelectorList 类型
        div_list = response.xpath("//div[@id='main']/div")
        for div in div_list:
            # Selector类型
            content = div.xpath(".//span[@class='text']/text()").get()  # 获取“Selector”中的第一个文本，返回的是一个str类型
            tag = div.xpath(".//a[@class='tag']/text()").getall()  # 获取“Selector”中所有的文本，返回的是一个列表
            tag = "".join(tag)
            item = ScrapyTestItem(tag=tag, content=content)
            # item = {
            #     'tag': tag,
            #     'content': content
            # }
            yield item
            # 如果数据解析回来，要传给pipline处理，那么可以使用 'yield' 来返回，
            # 或者是加入到列表中，最后统一return 返回。

        next_url = response.xpath("//ol[@class='page-navigator']/li[last()]/a/@href").get()
        no_next = response.xpath("//ol[@class='page-navigator']/li[last()]/@class").get()
        if no_next != "next":
            return
        else:
            yield scrapy.Request(next_url, callback=self.parse)
