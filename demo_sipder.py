import requests
from lxml import etree


class work_spider:
    def __init__(self):
        self.url_temp = 'http://www.risfond.com/case/it/47000'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

    def parse_url(self):
        response = requests.get(self.url_temp,headers=self.headers)
        return response.content.decode()
    
    def get_content(self,html_str):
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@class='sc_d_l cf']/div")
        for div in div_list:
            item = {}
            item['title'] = div.xpath(".//span")
            print(item)
        return item
    
    def run(self):
        # 1.start_url
        # 2.发送请求，获取响应
        html_str = self.parse_url()
        # 3.提取数据 
        content = self.get_content(html_str)
        print(content)
        # 4.保存

if __name__ == "__main__":
    work = work_spider()
    work.run()