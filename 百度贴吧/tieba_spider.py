import requests
from lxml import etree
import json


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.start_url = "https://tieba.baidu.com/mo/q---771EA4758368849F1B99568B4C102059:FG=1-sz@320_240,,-2-3-0--2/m?kw=" + tieba_name + "&pn=0"
        self.headers = {
            "User-Agent": "Mozilla / 5.0(iPhone;CPU iPhone OS 11_0 like Mac OS X) AppleWebKit / 604.1.38 (KHTML, like Gecko) Version / 11.0 Mobile/15A372 Safari / 604.1"
        }

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_str):
        html = etree.HTML(html_str)
        li_list = html.xpath("//li[contains(@class,'tl_shadow tl_shadow_new')]")  # 根据li分组
        content_list = []
        for li in li_list:
            item = {}
            item['author'] = li.xpath(".//span[@class='ti_author']/text()")[0].strip() if len(
                li.xpath(".//span[@class='ti_author']/text()")) > 0 else None
            item['time'] = li.xpath(".//span[@class='ti_time']/text()")[0] if len(
                li.xpath(".//span[@class='ti_time']/text()")) > 0 else None
            item['title'] = li.xpath(".//div[@class='ti_title']/span/text()")
            # item['title_list'] = self.get_title_list(item['title_href'])
            content_list.append(item)
        # 提取下一页的url地址
        # next_url = html.xpath("")
        return content_list
        # print(content_list)

    # def get_title_list(self,detail_url): #获取帖子中所有标题
    #     # 3.1提取列表页的url地址和标题
    #     # 3.2请求列表页url地址，获取详情页的第一页
    #     # 3.3提取详情页的第一页的图片，提取下一页的地址
    #     # 3.4请求详情页下一页的地址，进入循环3.2-3.4
    #     return title_list

    def save_content_list(self, content_list):  # 保存数据
        file_name = self.tieba_name + ".txt"
        with open(file_name, "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write("\n")
                print("保存成功")

    def run(self):
        # 1.start_url
        # 2.发送请求，获取响应
        html_str = self.parse_url(self.start_url)
        # 3.提取数据，提取下一页的url地址
        # 3.1提取列表页的url地址和标题
        # 3.2请求列表页url地址，获取详情页的第一页
        # 3.3提取详情页的第一页的图片，提取下一页的地址
        # 3.4请求详情页下一页的地址，进入循环3.2-3.4
        content_list = self.get_content_list(html_str)
        print(content_list)
        # 4.保存数据
        # self.save_content_list(content_list)
        # 5.请求下一页的url地址，进入循环2-5步


if __name__ == '__main__':
    tieba = TiebaSpider('python')
    tieba.run()
