import requests
import urllib.request
from urllib import request
from bs4 import BeautifulSoup


def crawl(url):
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/79.0.3945.117Safari/537.36'
    }
    req = request.Request(url, headers=headers)
    page = urllib.request.urlopen(req, timeout=20)
    contents = page.read().decode('utf-8')

    soup = BeautifulSoup(contents, 'lxml')
    imgs = soup.find_all('img')  # 查找所有img标签 列表
    for img in imgs:
        # img_src = img.get('src')  # 获取属性
        img_src = img.attrs['src']
        img_name = img.attrs['title']
        # print(img_name, img_src)
        print("正在下载--->%s" % img_name)
        urllib.request.urlretrieve(img_src, './image/%s.jpg' % img_name)


if __name__ == '__main__':
    for i in range(1, 6):
        url = 'https://www.buxiuse.com/?page={}'.format(i)
        crawl(url)
