# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from qunar.items import CityItem


class HotelSpider(scrapy.Spider):
    name = 'hotel'
    allowed_domains = ['bnb.qunar.com']
    start_urls = ['http://bnb.qunar.com/hotcity.jsp']

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html, "lxml")
        # 所有数据div
        div_b_allcity = soup.find("div", class_="b_allcity")
        item = CityItem()
        if div_b_allcity is not None:
            for div_cityItem in div_b_allcity.find_all('div'):
                if div_cityItem is not None:
                    ul = div_cityItem.find('ul')
                    if ul is not None:
                        for li_item in ul.find_all('li'):
                            if li_item is not None:
                                item['name'] = li_item.find('a').get_text()
                                item['url'] = li_item.find('a')['href']
                                print(item)