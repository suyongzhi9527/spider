import requests
import json


class toutiao_spider:
    def __init__(self):
        self.url_temp = 'https://www.douban.com/rexxar/api/v2/subjext_collection/filter_tv_american_hot/item?start={}&count=18&loc_id=108288'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()
        # print(response.content.decode())

    def get_content_list(self, json_str):
        dict_ret = json.loads(json_str)
        content_list = dict_ret["subject_collection_items"]
        return content_list
        # print(json_str)

    def save_content_list(self, content_list):
        with open("DayToutiao.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def run(self):
        # 1.start_url
        num = 0
        while True:
            url = self.url_temp.format(num)
            # 2.发送请求，获取响应
            json_str = self.parse_url(url)
            # print(json_str)
            # 3.提取数据
            content_list = self.get_content_list(json_str)
            # 4.保存
            self.save_content_list(content_list)
            if len(content_list) < 100:
                break
            # 5.构造下一页的url地址，进入循环
            num += 18


if __name__ == '__main__':
    toutiao_spider = toutiao_spider()
    toutiao_spider.run()
