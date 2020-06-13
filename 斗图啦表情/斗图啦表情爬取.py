import threading
import requests
import os
import random
import time
from lxml import etree
from queue import Queue

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
}


# 生产者
class Producer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            # 停止几秒
            time.sleep(random.randint(1, 3))
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = requests.get(url, headers=headers)
        text = response.text
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='random_picture']//a/img")
        for img in imgs:
            # 过滤动图
            if img.get("class") == "gif":
                continue

            # 获取图片url
            img_url = img.xpath(".//@data-backup")[0]
            if img_url.split(".")[-1] == "gif":
                continue

            # 获取图片后缀
            suffix = os.path.splitext(img_url)[
                1]  # ('http://img.doutula.com/production/uploads/image/2020/05/15/20200515476863_flpJAF', '.jpg')

            # # 获取图片名称
            alt = img.xpath(".//@alt")[0]
            img_name = alt + suffix
            self.img_queue.put((img_url, img_name))

# 消费者


class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                return

            img = self.img_queue.get(block=True)
            # ('http://img.doutula.com/production/uploads/image/2020/05/15/20200515503746_NFsxhr.jpg', '后宫基友三千.jpg')
            url, filename = img
            with open("E:\\Python程序设计实验项目\\爬虫\\images\\" + filename, "wb") as f:
                f.write(requests.get(url, timeout=30, headers=headers).content)
                print(filename + "下载完成!")


def main():
    # url队列
    page_queue = Queue(15)
    img_queue = Queue(20)
    for x in range(1, 6):
        url = "https://www.doutula.com/photo/list/?page={}".format(str(x))
        page_queue.put(url)

    for x in range(6):
        t = Producer(page_queue, img_queue)
        t.start()

    for x in range(6):
        t = Consumer(page_queue, img_queue)
        t.start()


if __name__ == '__main__':
    main()
