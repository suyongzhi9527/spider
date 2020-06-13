import requests
import re
import os
import time
import random
import threading
from bs4 import BeautifulSoup
from queue import Queue

path = 'D:/种子下载/'
try:
    os.makedirs(path)
    print('目录创建成功!')
except:
    pass

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    'Host': 'www.lwgod.me'
}


class Producer(threading.Thread):
    def __init__(self, page_queue, url_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.url_queue = url_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            time.sleep(random.randint(1, 3))
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        soup = BeautifulSoup(requests.get(url, headers=headers).text, 'lxml')
        tbody = soup.find_all('tbody')[1:]

        for i in tbody:
            if i.attrs['id'] == 'separatorline':
                continue
            try:
                movie_name = re.findall(r'【龙网BT组】.*】', i.text)[0]
                movie_name = re.sub(r'[:/]', '.', movie_name)
                url = 'http://www.lwgod.me/' + i.find('a')['href']
                parse_url = BeautifulSoup(
                    requests.get(url).text, 'lxml')  # 解析详情页地址
                seed_url = 'http://www.lwgod.me/' + \
                    parse_url.find('ignore_js_op').find('a')['href']
                parse_url2 = BeautifulSoup(requests.get(seed_url).text, 'lxml')
                seed_url2 = 'http://www.lwgod.me/' + \
                    parse_url2.find(class_='dxksst').find('a')['href']

                self.url_queue.put((seed_url2, movie_name))

            except Exception as e:
                print(e)


class Consumer(threading.Thread):
    def __init__(self,  page_queue, url_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.url_queue = url_queue

    def run(self):
        while True:
            if self.url_queue.empty() and self.page_queue.empty():
                return

            urls = self.url_queue.get(block=True)
            url, name = urls
            with open(f'{path}{name}.torrent', 'wb') as f:
                f.write(requests.get(url).content)
                print(f'{name}下载完成!')


def main():
    page_queue = Queue(15)
    url_queue = Queue(20)
    for i in range(1, 6):
        url = 'http://www.lwgod.me/forum-292-{}.html'.format(i)
        page_queue.put(url)

    for x in range(6):
        t = Producer(page_queue, url_queue)
        t.start()

    for x in range(6):
        t = Consumer(page_queue, url_queue)
        t.start()


if __name__ == "__main__":
    main()
