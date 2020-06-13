# -*- coding: utf-8 -*-
import scrapy
from json import loads
from image360.items import Image360Item
from urllib.parse import urlencode


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['image.so.com']

    # start_urls = ['http://image.so.com/']

    # 因为不和以前一样给一个初始url，所以需要重写父类的start_requests方法
    def start_requests(self):
        # 定义一个基础的url
        base_url = 'https://image.so.com/zjl?'
        # 把固定的参数保存在一个字典中
        param = {
            'ch': 'beauty',
            'listtype': 'hot',
            'temp': 1
        }
        # 我们拿数据只需要改变sn的值，所以我们来个循环，我们拿300条数据
        for page in range(10):
            # 把sn和对应的数添加到字典里
            param['pn'] = page * 30
            # 完整url
            full_url = base_url + urlencode(param)
            # 返回一个生成器
            yield scrapy.Request(url=full_url, callback=self.parse)

    def parse(self, response):
        # 把从接口拿到的数据转换成字典
        model_dict = loads(response.text)
        for elem in model_dict['list']:
            item = Image360Item()
            item['title'] = elem['title']
            item['tag'] = elem['tag']
            item['width'] = elem['qhimg_thumb_width']
            item['height'] = elem['qhimg_thumb_height']
            item['url'] = elem['qhimg_url']
            yield item
            # print(item)
