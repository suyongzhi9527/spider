# -*- coding: utf-8 -*-
import re
from  scrapy import Request
from scrapy.spiders import Spider
from meitulu.items import MeituluItem



class PicsSpider(Spider):
    name = 'pics'

    def start_requests(self):
        urls = ['https://www.meitulu.com/t/nvshen/{}.html'.format(str(i)) for i in range(2, 3)] # 页数
        for url in urls:
            # print(url) # https://www.meitulu.com/t/nvshen/2.html
            yield Request(url) # 循环访问爬取页数

    def parse(self, response): # 解析数据
        item = MeituluItem()
        info_url = response.xpath('//ul[@class="img"]/li/a/@href').extract() # 解析出当前url地址
        # print(info_url) # # https://www.meitulu.com/item/19552.html
        # url_code = re.findall('item/(.*?).html', str(info_url))
        
        # for i in range(60):
        #     infor_url = 'https://www.meitulu.com/item/' + url_code[i] + '.html' # 构造url
        #     # print(infor_url) # https://www.meitulu.com/item/19552.html
        #     yield Request(infor_url, callback=self.parse_detail, meta={'item': item})
        for url in info_url:
            yield Request(url, callback=self.parse_detail, meta={'item': item})
    

    def parse_detail(self, response):
        item = MeituluItem()
        info_list = response.xpath('//div[@class="content"]')
        for info in info_list:
            pic = info.xpath('.//img/@src').extract()
            name = info.xpath('.//img/@alt').extract()
            item['name'] = name
            item['img_url'] = pic
            yield item
        
