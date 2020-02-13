# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):  # 重写start_requests方法，爬虫一开始就会发送post请求
        url = 'http://www.renren.com/PLogin.do'
        data = {
            "email": "1125699801@qq.com",
            "password": "1125699801syz"
        }
        request = scrapy.FormRequest(url, formdata=data, callback=self.parse_page)  # 发送post请求
        yield request

    def parse_page(self, response):
        request = scrapy.Request(url="http://www.renren.com/880151247/profile", callback=self.parse_profile)
        yield request

    def parse_profile(self, response):
        with open("dp.html", "w", encoding="utf-8") as f:
            f.write(response.text)
