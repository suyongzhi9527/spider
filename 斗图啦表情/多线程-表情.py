import requests
import threading
import os
import re
import time
import random
from lxml import etree
from urllib.request import urlretrieve
from queue import Queue


class Produce(threading.Thread):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
        "Host": "www.doutula.com",
        "Cookie": "_agep=1589505062; _agfp=28fceb9806d9bfbf44f07f4b55413600; _agtk=318f8caf421b5ad5f37104d7a1fd9faf; Hm_lvt_2fc12699c699441729d4b335ce117f40=1589505062,1591087045; XSRF-TOKEN=eyJpdiI6IkRDdTJpQzV6Q2FjRDhxYnZsNWgwMHc9PSIsInZhbHVlIjoiK2pwN1VLUWxYOXdFXC9mamJyZmVHRUs0VDlseVp5d042THRiSlpEYzU1aXB5NmFKWWJwRVIyUWI5ZFBrREJHbTUiLCJtYWMiOiI3MTFhOTg2MmJhNDkxNjdhYWJmNmRiMGUwOGM2OTI2NDFkZjg1YmMyMjg0MzU1MTk1MTczNTkxNDk1Yzg5NDc2In0%3D; doutula_session=eyJpdiI6Ik5kTUlRNFl3RUthUFZ5SWtRXC9TcEJBPT0iLCJ2YWx1ZSI6IjFEY0F0QkNZNGcyak4rSWVGaG9zbTVjb1daM0lldmVqZ3BseDRLemhnUUhVVkt6WW1CNCtMMXppMnVDd1F3K04iLCJtYWMiOiI0NDIwMzk0ZjI2YTI5MTIzNDU4NDY0NzFkNmI4OGM1ZGMwNTdhOGY3OTk4ZWMwN2YzMzRiYTFhMjYyYjliMjAxIn0%3D; Hm_lpvt_2fc12699c699441729d4b335ce117f40=1591087520"
    }

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Produce, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            time.sleep(random.randint(1, 3))
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        r = requests.get(url, headers=self.headers)
        r.encoding = r.apparent_encoding
        html = etree.HTML(r.text)
        imgs = html.xpath(
            '//div[@class="random_article"]//img[@class != "gif"]')
        for img in imgs:

            # img_url = img.xpath('@data-original') 或者
            img_url = img.get('data-original')
            name = img.get('alt')
            name = re.sub(r'\?？。\.', '', name)
            if name:
                name = img.get('alt')
            else:
                name = img_url[-10:-5]
            suddix = os.path.splitext(img_url)[1]  # 截取后缀
            filename = str(name) + suddix  # 合并图片名字
            self.img_queue.put((img_url, filename))


class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:

            if self.img_queue.empty() and self.page_queue.empty():
                return

            img_url, filename = self.img_queue.get(block=True)

            # print(img_url, filename)
            urlretrieve(img_url, 'E:\\Python程序设计实验项目\\爬虫\\images\\' + filename)
            print(filename+'下载完成')


def main():
    page_queue = Queue(15)
    img_queue = Queue(20)
    for i in range(1, 11):
        url = 'https://www.doutula.com/article/list/?page={}'.format(str(i))
        page_queue.put(url)

    for x in range(6):
        t = Produce(page_queue, img_queue)
        t.start()
    for x in range(6):
        t = Consumer(page_queue, img_queue)
        t.start()


if __name__ == '__main__':
    main()
