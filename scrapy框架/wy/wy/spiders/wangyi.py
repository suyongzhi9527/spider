# -*- coding: utf-8 -*-
import scrapy
import copy
from selenium import webdriver


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.wangyi.com']
    start_urls = ['https://news.163.com/']

    def __init__(self):
        self.bro = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe')

    def closd(self, spider):
        self.bro.quit()

    def parse(self, response):
        # 获取四大板块URL：国内，国际，军事，航空
        li_list = response.xpath('//div[@class="ns_area list"]/ul/li')
        item_list = list()
        for li in li_list:
            url = li.xpath('./a/@href').extract_first()
            title = li.xpath('./a/text()').extract_first().strip()
            # 过滤出 国内，国际，军事，航空
            if title in ['国内', '国际', '军事', '航空']:
                item = dict()
                item['title'] = title
                item['url'] = url

                yield scrapy.Request(url=item['url'], callback=self.parse_content, meta={'title': title})

    def parse_content(self, response):
        title = response.meta.get('title')
        div_list = response.xpath("//div[@class='ndi_main']/div")

        print(len(div_list))

        for div in div_list:
            item = {}
            item['group'] = title
            img_url = div.xpath('./a/img/@src').extract_first()
            article_url = div.xpath('./a/img/@href').extract_first()
            head = div.xpath('./a/img/@alt').extract_first()
            keywords = div.xpath('//div[@class="keywords"]//text()').extract()
            # 将列表内容转换成字符串
            content = "".join([i.strip() for i in keywords])
            item['img_url'] = img_url
            item['article_url'] = article_url
            item['head'] = head
            item['keywords'] = keywords

            yield scrapy.Request(
                url=article_url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

    def parse_detail(self, response):
        pass
