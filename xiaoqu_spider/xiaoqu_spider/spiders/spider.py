# -*- coding: utf-8 -*-
import scrapy
import re
import requests
from scrapy.http import Request
from pyquery import PyQuery as pq
from xiaoqu_spider.items import XiaoquSpiderItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    url = 'https://sz.loupan.com/index.php/jsdata/common?_=1590998299774'
    response = requests.get(url).text
    urls = list(set(re.findall(r'http://\w+?.loupan.com', response)))
    url_delete = ('http://app.loupan.com', 'http://www.loupan.com',
                  'http://public.loupan.com', 'http://user.loupan.com')
    for url in urls:
        if url in url_delete:
            urls.remove(url)

    def start_requests(self):
        headers = self.settings.get('headers')
        for start_urls in self.urls:
            start_url = start_urls + '/community/'
            response = requests.get(start_url)
            doc = pq(response.text)

            lis = doc('.list li .text h2 a')
            li_doc = pq(lis).items()
            for li in li_doc:
                url = li('a').attr('href')
                yield Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        doc = pq(response.text)
        item = XiaoquSpiderItem()

        url = doc('.pos > a:nth-child(4)').attr('href')  # 小区链接
        item['url'] = url

        name = doc('.t p').text()  # 小区名
        item['name'] = name

        addres = doc('.text_nr.bug2').text()  # 小区地址
        citys = doc('.pos > a:nth-child(2)').text()
        city = ''.join(re.findall(r'(\w+)小区', citys)) + '市'
        districts = doc('span.font_col_o > a').text()  # 所属区
        address = city + districts + addres + name  # 所属详细地址
        item['coord'] = '暂无数据!'
        item['province'] = '暂无数据!'
        item['city'] = city
        item['district'] = districts 
        item['detail_address'] = address 

        id = ''.join(re.findall(r'\d+', url))
        around_url = 'http://sz.loupan.com/community/around/' + id + '.html'  # 周边信息网址
        response = requests.get(around_url)
        around_doc = pq(response.text)
        traffic = around_doc('.trend > p:nth-child(7)').text()  # 交通
        item['traffic'] = traffic.replace('m', 'm,')  # 交通

        prices = doc('div.price > span.dj').text()  # 参考价格
        if prices == '暂无数据':
            price = None
            item['price'] = price
        else:
            price = int(prices)
            item['price'] = price

        item['property_type'] = doc(
            'ul > li:nth-child(1) > span.text_nr').text()  # 物业类型

        property_fees = doc(
            'ul > li:nth-child(2) > span.text_nr').text()  # 物业费
        if property_fees == '暂无数据':
            property_fee = None
            item['property_fee'] = property_fee
        else:
            property_fee = float(
                ''.join(re.findall(r'\d*\.\d*', property_fees)))
            item['property_fee'] = property_fee

        areas = doc('ul > li:nth-child(3) > span.text_nr').text()  # 总建面积
        if areas == '暂无数据':
            area = None
            item['area'] = area
        else:
            area = int(''.join(re.findall(r'\d*', areas)))
            item['area'] = area

        house_counts = doc('ul > li:nth-child(4) > span.text_nr').text()  # 总户数
        if house_counts == '暂无数据' or house_counts == '':
            house_count = None
            item['house_count'] = house_count
        else:
            house_count = int(''.join(re.findall(r'\d*', house_counts)))
            item['house_count'] = house_count

        completion_times = doc(
            'ul > li:nth-child(5) > span.text_nr').text()  # 竣工时间
        if completion_times in ('暂无数据', '', None):
            completion_time = None
            item['completion_time'] = completion_time
        else:
            completion_time = int(
                ''.join(re.findall(r'\d*', completion_times)))
            item['completion_time'] = completion_time

        item['parking_count'] = doc(
            'ul > li:nth-child(6) > span.text_nr').text()  # 停车位

        plot_ratios = doc('ul > li:nth-child(7) > span.text_nr').text()  # 容积率
        if plot_ratios == '暂无数据' or plot_ratios == '':
            plot_ratio = None
            item['plot_ratio'] = plot_ratio
        else:
            plot_ratio = float(''.join(re.findall(r'\d*\.\d*', plot_ratios)))
            item['plot_ratio'] = plot_ratio

        greening_rates = doc(
            'ul > li:nth-child(8) > span.text_nr').text()  # 绿化率
        if greening_rates == '暂无数据':
            greening_rate = None
            item['greening_rate'] = greening_rate
        else:
            greening_rate = ''.join(re.findall(r'\d*\.\d*%', greening_rates))
            item['greening_rate'] = greening_rate

        item['property_company'] = doc(
            'div.ps > p:nth-child(1) > span.text_nr').text()  # 物业公司
        item['developers'] = doc(
            'div.ps > p:nth-child(2) > span.text_nr').text()  # 开发商
        yield item
        # print(item)

        lis = doc(
            'body > div.pages > div.main.esf_xq > div > div.main > div.tj_esf > ul > li')
        li_doc = pq(lis).items()
        for li in li_doc:
            url = li('div.text > a').attr('href')
            yield Request(url=url, callback=self.parse)
