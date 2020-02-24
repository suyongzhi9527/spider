import requests
import re
import json
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from lxml import etree


class zbxx_spider:
    def __init__(self):
        self.url_temp = "http://www.dg.gov.cn/machong/zbxx/list.shtml", "http://www.dg.gov.cn/machong/zbxx/list_{}.shtml"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }

    def get_url_list(self):
        url_list = []
        for url in range(2, 11):
            url_list.append(self.url_temp[0])
            url_list.append(self.url_temp[1].format(url))
        return url_list

    def parsse_url(self, url):
        # print(url)
        res = requests.get(url, headers=self.headers)
        return res.content.decode()

    def get_content_list(self, html_str):
        pattern = re.compile(r'<div.*?list-right_title.*?a href="(.*?)".*?>(.*?)</a>.*?td.*?left.*?>(.*?)</td>', re.S)
        items = re.findall(pattern, html_str)
        for item in items:
            yield {
                '链接': urljoin("http://www.dg.gov.cn", item[0]),
                '标题': item[1],
                '日期': item[2].strip()[27:]
            }

    def save_file(self, content):
        with open('招标信息.txt', 'a', encoding='utf-8') as f:
            # print(type(json.dumps(content)))
            f.write(json.dumps(content, ensure_ascii=False) + '\n')
            print("保存成功!")

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            html_str = self.parsse_url(url)
            # content = self.get_content_list(html_str)
            for item in self.get_content_list(html_str):
                print(item)
                # self.save_file(item)


if __name__ == '__main__':
    zbxx = zbxx_spider()
    zbxx.run()
