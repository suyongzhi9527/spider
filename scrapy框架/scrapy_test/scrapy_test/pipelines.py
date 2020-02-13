# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exporters import JsonItemExporter

# class ScrapyTestPipeline(object):
#     def __init__(self):
#         self.f = open("duanzi.json", "w", encoding="utf-8")
#
#     def open_spider(self, spider):  # 当爬虫打开时候执行
#         print("爬虫开始了...")
#
#     def process_item(self, item, spider):  # 当爬虫有item传过来的时候会被调用
#         item_json = json.dumps(dict(item), ensure_ascii=False)
#         self.f.write(item_json + "\n")
#         return item
#
#     def close_spider(self, spider):  # 当爬虫关闭的时候执行
#         print("爬虫结束了...")

# class ScrapyTestPipeline(object):
#     def __init__(self):
#         self.f = open("duanzi.json", "wb")
#         self.exporter = JsonItemExporter(self.f, ensure_ascii=False, encoding="utf-8")
#         self.exporter.start_exporting()
#
#     def open_spider(self, spider):  # 当爬虫打开时候执行
#         print("爬虫开始了...")
#
#     def process_item(self, item, spider):  # 当爬虫有item传过来的时候会被调用
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):  # 当爬虫关闭的时候执行
#         self.exporter.finish_exporting()
#         print("爬虫结束了...")


from scrapy.exporters import JsonLinesItemExporter


class ScrapyTestPipeline(object):
    def __init__(self):
        self.f = open("duanzi.json", "wb")
        self.exporter = JsonLinesItemExporter(self.f, ensure_ascii=False, encoding="utf-8")

    def open_spider(self, spider):  # 当爬虫打开时候执行
        print("爬虫开始了...")

    def process_item(self, item, spider):  # 当爬虫有item传过来的时候会被调用
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):  # 当爬虫关闭的时候执行
        self.f.close()
        print("爬虫结束了...")
