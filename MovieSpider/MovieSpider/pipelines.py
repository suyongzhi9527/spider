# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd


class MoviespiderPipeline(object):
    def __init__(self):
        self.mypd = pd.DataFrame(columns=['name', 'url'])

    def close_spider(self, spider):
        self.mypd.to_csv("movie.csv")

    def process_item(self, item, spider):
        # print("name:", item["name"])
        # print("url:", item["url"])
        self.mypd = self.mypd.append({'name':item['name'][0],'url':item['url'][0]},ignore_index=True)
        print(len(self.mypd))
