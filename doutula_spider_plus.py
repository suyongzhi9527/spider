import requests
import os
import re
import threading
from lxml import etree
from urllib import request
from queue import Queue


class Procuder(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    proxies = {
        "https": "129.205.106.42:8080"
    }

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Procuder, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = requests.get(url, headers=self.headers,proxies=self.proxies)
        text = response.text
        html = etree.HTML(text)
        # 过滤class为gif的图片
        imgs = html.xpath(
            '//div[@class="page-content text-center"]//img[@class != "gif"]')
        for img in imgs:
            # img_urls = img.xpath("@data-original")[0]
            img_urls = img.get("data-original")  # 获取图片链接
            alt = img.get("alt")  # 获取图片文本
            alt = re.sub(r'[\?？。.!！,，*]', '', alt)  # 替换掉特殊字符
            suffix = os.path.splitext(img_urls)[1]  # 截取图片后缀
            filename = alt + suffix  # 拼接后缀,组成图片名
            self.img_queue.put((img_urls, filename))


class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            opener = request.build_opener()
            opener.addheaders = [
                ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
            ]
            request.install_opener(opener)
            img_urls, filename = self.img_queue.get()
            request.urlretrieve(img_urls, 'images/' + filename)
            print("下载成功-> %s" % filename)


def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)
    for i in range(1, 101):
        url = "http://www.doutula.com/photo/list/?page=%d" % i
        page_queue.put(url)

    for i in range(5):
        t = Procuder(page_queue, img_queue)
        t.start()

    for i in range(5):
        t = Consumer(page_queue, img_queue)
        t.start()


if __name__ == "__main__":
    main()
