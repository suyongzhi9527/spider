import requests
import time
import threading
from queue import Queue
from urllib import request


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}
urlQueue = Queue()
[urlQueue.put('https://v.6.cn/coop/mobile/index.php?act=recommend&padapi=minivideo-getlist.php&page={}'.format(i))
 for i in range(1, 6)]


def parse_html(urlQueue,times = 1):
    while True:
        try:
            url = urlQueue.get_nowait()
        except:
            break

        try:
            resp = requests.get(url, headers=headers,timeout = 3).json()
            data = resp['content']['list']
            for i in data:
                title = i['title']
                urls = i['playurl']
                request.urlretrieve(
                    urls, r'F:\spider_learn\手机端六间房直播\video\{}.mp4'.format(title))
                print("正在下载小姐姐===>{}".format(title))
        except:
            trytimes = 3
            if times < trytimes:
                times += 1
                return parse_html(urlQueue,times)
            return '响应时间过久，已停止!!'


if __name__ == "__main__":
    threads = []
    threadnum = 10
    for i in range(0, threadnum):
        t = threading.Thread(target=parse_html, args=(urlQueue,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
