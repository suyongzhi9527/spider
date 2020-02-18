# -*- coding: utf-8 -*-
import scrapy
import re


class SfwSpider(scrapy.Spider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        trs = response.xpath('//div[@class="outCont"]//tr')  # 获取所有的tr标签
        province = None
        for tr in trs:
            tds = tr.xpath('.//td[not(@class)]')  # 在当前tr下查找没有class属性的tr标签
            province_id = tds[0]  # 所有的直辖市
            province_text = province_id.xpath('.//text()').get()  # 直辖市名称
            province_text = re.sub(r'\s', '', province_text)
            if province_text:
                province = province_text
            if province == '其它':  # 不爬取海外房源
                continue
            city_id = tds[1]  # 所有城市
            city_links = city_id.xpath('.//a')
            for city_link in city_links:
                city = city_link.xpath('.//text()').get()  # 城市名称
                city_url = city_link.xpath('.//@href').get()  # 城市链接
                # 构建新房url链接
                url_model = city_url.split('.')
                scheme = url_model[0]
                domain = url_model[1]
                last_com = url_model[2]
                if 'bj' in scheme:
                    newhouse_url = 'http://newhouse.fang.com/house/s/'
                    esf_url = 'http://esf.fang.com/'
                else:
                    newhouse_url = scheme + '.newhouse.' + domain + '.' + last_com + 'house/s/'
                    # 构建二手房url链接
                    esf_url = scheme + '.esf.' + domain + '.' + last_com

                yield scrapy.Request(url=newhouse_url, callback=self.parse_newhouse, meta={'info': (province, city)})
                yield scrapy.Request(url=esf_url, callback=self.parse_esf, meta={'info': (province, city)})

    def parse_newhouse(self, response):
        province, city = response.meta.get('info')
        pass

    def parse_esf(self, response):
        province, city = response.meta.get('info')
        pass
