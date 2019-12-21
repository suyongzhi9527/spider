import requests


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.req_header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }

    def get_url_list(self):
        url_list = []
        for i in range(1000):
            url_list.append(self.url_temp.format(i * 50))
        return url_list

    def parse_url(self, url):
        print(url)
        res = requests.get(url, headers=self.req_header)
        return res.content.decode()

    def save_html(self, html_str, page_num):
        file_name = "{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(file_name)

    def run(self):
        # 1.构造url列表
        url_list = self.get_url_list()
        # 2.遍历，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3.保存
            page_num = url_list.index(url) + 1  # 页数码
            self.save_html(html_str, page_num)


if __name__ == '__main__':
    tieba = TiebaSpider("李毅")
    tieba.run()
