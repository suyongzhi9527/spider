# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter


class FangPipeline(object):
    def __init__(self):
        self.newhouse_f = open('newhouse.json', 'wb')
        self.esfhouse_f = open('esfhouse.json', 'wb')
        self.newhouse_exporter = JsonLinesItemExporter(self.newhouse_f, ensure_ascii=False)
        self.esfhouse_exporter = JsonLinesItemExporter(self.esfhouse_f, ensure_ascii=False)

    def process_item(self, item, spider):
        self.newhouse_exporter.export_item(item)
        self.esfhouse_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.newhouse_f.close()
        self.esfhouse_f.close()
