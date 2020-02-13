# -*- coding: utf-8 -*-
import scrapy


class CodingSpider(scrapy.Spider):
    name = 'coding'
    allowed_domains = ['codingdict.com']
    start_urls = ['http://codingdict.com/']
    login_url = 'http://codingdict.com/log-in/'

    def parse(self, response):
        form_data = {
            "email_or_username": "1125699801@qq.com",
            "password": "15219740694syz"
        }
        scrf_token = response.xpath('//input[@type="hidden"]/@value').get()
        form_data["csrfmiddlewaretoken"] = scrf_token
        yield scrapy.FormRequest(url=self.login_url, formdata=form_data, callback=self.parse_after_login)

    def parse_after_login(self, response):
        if response.url == 'http://codingdict.com/':
            print("登录成功!")
        else:
            print("登录失败!")
