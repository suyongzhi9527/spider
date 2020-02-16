# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import ArticleItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath('//section[@class="ouvJEz"]//h1[@class="_1RuRku"]/text()').get()
        author = response.xpath('//section[@class="ouvJEz"]//a[@class="_1OhGeD"]/text()').get()
        avatar = response.xpath('//section[@class="ouvJEz"]//img[@class="_13D2Eh"]/@src').get()
        pub_time = response.xpath('//section[@class="ouvJEz"]//div[@class="s-dsoj"]/time/text()').get()
        content = response.xpath('//section[@class="ouvJEz"]//article[@class="_2rhmJa"]').get()
        word_count = response.xpath('//section[@class="ouvJEz"]//div[@class="s-dsoj"]/span[2]').get()
        read_count = response.xpath('//section[@class="ouvJEz"]//div[@class="s-dsoj"]/span[3]').get()
        comment_count = response.xpath('//div[@class="_10KzV0"]//span[@class="_2R7vBo"]/text()').get()
        like_count = response.xpath('//div[@class="_2LKTFF"]//span[@class="_1GPnWJ"][1]/text()').get()
        subjects = ",".join(response.xpath('//div[@class="_2Nttfz"]//a[@class="_3s5t0Q _1OhGeD"]/span/text()').getall())
        url = response.url
        url1 = url.split("?")[0]
        article_id = url1.split("/")[-1]
        item = ArticleItem(
            title=title,
            author=author,
            avatar=avatar,
            pub_time=pub_time,
            article_id=article_id,
            origin_url=url,
            content=content,
            word_count=word_count,
            read_count=read_count,
            comment_count=comment_count,
            like_count=like_count,
            subjects=subjects
        )
        yield item
