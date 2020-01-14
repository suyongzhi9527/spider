import requests
import re
import json


class Duanzi:
    def __init__(self):
        self.start_url = 'http://duanziwang.com/category/%E7%BB%8F%E5%85%B8%E6%AE%B5%E5%AD%90/{}/'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

    def url_list(self): # 构造url地址爬取前10页内容
        url_list = []
        for url in range(10):
            url_list.append(self.start_url.format(url))
        return url_list

    def parse_url(self, url): # 发送请求，获取响应
        response = requests.get(url, headers=self.headers)
        return response.content.decode() # 返回响应内容

    def get_first_page_content_list(self, html_str): # 利用正则匹配第一页对应的段子
        content_list = re.findall(r"<p>(.*?)</p>",html_str,re.S)
        # print(type(content_list))
        return content_list

    def save_content_list(self,content_list): # 保存数据到本地txt文件
        with open("duanzi.txt","a",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False)) # Python 列表类型转换为json字符串
                f.write("\n") # 换行写入，一个段子一行
        print("保存成功!")

    def run(self):
        # 1.start_url
        url_list = self.url_list()
        # 2.发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3.提取数据
            content_list = self.get_first_page_content_list(html_str)
            # self.get_first_page_content_list(html_str)
            # 4.保存
            self.save_content_list(content_list)


if __name__ == '__main__':
    duanzi = Duanzi()
    duanzi.run()
