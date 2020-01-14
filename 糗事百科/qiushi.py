import requests
import json
import threading
from queue import Queue
from lxml import etree


class QiuShi_Spider:
    def __init__(self):
        self.url_temp = "http://m.qiushi.92game.net/?page={}"
        # self.url_temp = "http://m.qiushi.92game.net/?page=1"
        self.url_queue = Queue()
        self.html_str = Queue()
        self.content_list = Queue()
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

    def get_url_list(self):  # 构造url
        # return [self.url_temp.format(i) for i in range(1, 10)]
        for i in range(1,71):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):  # 发送请求，获取响应
        while True:
            url = self.url_queue.get()
            print(url)
            response = requests.get(url, headers=self.headers)
            # return response.content.decode()
            self.html_str.put(response.content.decode())
            self.url_queue.task_done()

    def get_content_list(self):  # 提取数据
        while True:
            html_str = self.html_str.get()
            html = etree.HTML(html_str)
            div_list = html.xpath("//body[@class='index']")  # 分组
            content_list = []
            # print(div_list)
            for div in div_list:
                item = {}
                item["user"] = div.xpath(".//p[@class='user']/a/text()")[0]
                item["title"] = div.xpath(".//div[@class='qiushi']/text()")[0]
                # item["vote"] = div.xpath(".//a[@class='vote']//span[@id='up-21']/text()") if len(div.xpath(".//a[@class='vote']//span[@id='up-21']/text()")) > 0 else None
                # item["down"] = div.xpath(".//a[@class='down']//span[@id='dn-21']/text()") if len(div.xpath(".//a[@class='down']//span[@id='dn-21']/text()")) > 0 else None
                # item["comments"] = div.xpath(".//a[@class='qiushi_comments']/strong/text()") if len(div.xpath(".//a[@class='qiushi_comments']/strong/text()")) > 0 else None
                content_list.append(item)
            # return content_list
            self.content_list.put(content_list)
            self.html_str.task_done()

    def save_content_list(self):
        while True:
            content_list = self.content_list.get()
            with open("qiushi.txt","a",encoding="utf-8") as f:
                for content in content_list:
                    f.write(json.dumps(content,ensure_ascii=False,indent=2))
                    f.write("\n")
                print("保存成功!")
            # for i in content_list:
            #     # print(i)
            #     pass
                self.content_list.task_done()

    def run(self):  # 实现主要逻辑
        thread_list = []
        # 1.url_list
        # 2.遍历，发送请求，获取响应
        # url_list = self.get_url_list()
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)
        # for url in url_list:
        #     html_str = self.parse_url(url)
        for i in range(3):
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)
        # 3.提取数据
        # content_list = self.get_content_list(html_str)
        for i in range(3):
            t_html = threading.Thread(target=self.get_content_list)
            thread_list.append(t_html)
        # 4.保存
        # self.save_content_list(content_list)
        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)
        for t in thread_list:
            t.setDaemon(True) # 把子线程设置为守护线程，该线程不重要主线程结束，子线程结束
            t.start()

        for q in [self.url_queue,self.html_str,self.content_list]:
            q.join() # 让主线程等待阻塞，等待队列的任务完成之后再完成
        print("主线程结束")


if __name__ == '__main__':
    qiushi = QiuShi_Spider()
    qiushi.run()
