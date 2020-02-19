# -*- coding: utf-8 -*-
import scrapy
import re
from fang.items import NewHouseItem, ESFHouseItem
from scrapy_redis.spiders import RedisSpider


class SfwSpider(RedisSpider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    # start_urls = ['https://www.fang.com/SoufunFamily.htm']
    redis_key = "fang:start_urls"

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
        item = NewHouseItem()
        province, city = response.meta.get('info')
        lis = response.xpath('//div[contains(@class,"nl_con")]/ul/li')
        for li in lis:
            name = li.xpath('.//div[@class="nlcd_name"]/a/text()').get()
            if name == None:
                continue
            item['name'] = name.strip()  # 小区名
            house_type_list = li.xpath('.//div[contains(@class,"house_type")]/a/text()').getall()
            house_type_list = list(map(lambda x: re.sub(r'\s', '', x), house_type_list))
            item['rooms'] = list(filter(lambda x: x.endswith('居'), house_type_list))  # 过滤只以居结尾的  户型
            area = "".join(li.xpath('.//div[contains(@class,"house_type")]/text()').getall())
            item['area'] = re.sub(r'\s|－|/', '', area)  # 面积
            item['address'] = li.xpath('.//div[@class="address"]/a/@title').get()  # 地址
            district_text = "".join(li.xpath('.//div[@class="address"]/a//text()').getall())
            item['district'] = re.search(r'.*\[(.+)\].*', district_text).group(1)  # 行政区
            item['sale'] = li.xpath('.//div[contains(@class, "fangyuan")]/span/text()').get()  # 销售状态
            price = "".join(li.xpath('.//div[@class="nhouse_price"]//text()').getall())
            item['price'] = re.sub(r'\s|广告', '', price)  # 价格
            origin_url = li.xpath('.//div[@class="nlcd_name"]/a/@href').get()
            item['origin_url'] = "https:" + origin_url  # 详情页url
            item['province'] = province
            item['city'] = city
            yield item
        next_url = response.xpath('//div[@class="page"]//a[@class="next"]/@href').get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_newhouse,
                                 meta={'info': (province, city)})

    def parse_esf(self, response):
        province, city = response.meta.get('info')
        dls = response.xpath('//div[contains(@class, "shop_list")]/dl')
        for dl in dls:
            item = ESFHouseItem(province=province, city=city)
            item['name'] = dl.xpath('.//p[@class="add_shop"]/a/@title').get()  # 小区名
            infos = dl.xpath('.//p[@class="tel_shop"]/text()').getall()
            infos = list(map(lambda x: re.sub(r'\s', '', x), infos))
            for info in infos:
                if '厅' in info:
                    item['rooms'] = info  # 户型
                elif '层' in info:
                    item['floor'] = info  # 层数
                elif '向' in info:
                    item['toward'] = info  # 朝向
                elif '㎡' in info:
                    item['area'] = info  # 面积
                elif '建' in info:
                    item['year'] = info.replace('年建', '')  # 年代
            item['address'] = dl.xpath('.//p[@class="add_shop"]/span/text()').get()  # 地址
            item['price'] = "".join(dl.xpath('.//dd[@class="price_right"]/span[1]//text()').getall())  # 总价格
            item['unit'] = dl.xpath('.//dd[@class="price_right"]/span[2]/text()').get()  # 单价
            detail_url = dl.xpath('.//h4[@class="clearfix"]/a/@href').get()
            item['origin_url'] = response.urljoin(detail_url)
            yield item
        next_url = response.xpath('//div[@class="page_al"]/p[1]/a/@href').get()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_esf,
                                 meta={'info': (province, city)})
