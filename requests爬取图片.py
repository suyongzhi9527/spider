import requests
import os
import re
from urllib.request import urlretrieve
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    return html


def get_img(html):
    if not os.path.exists('img'):
        os.mkdir('img')
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    regx = '<script type="text/data" id="initData">(.*?)</script>'
    data = re.findall(regx, html, re.S)
    str_data = str(data)
    regx2 = '"qhimg_url":"(.*?)",'
    result = re.findall(regx2, str_data)
    for img_url in result:
        # https://p3.ssl.qhimgs1.com//t016abf53727b771589.jpg
        img_url = img_url.replace('\\', '')
        name = img_url[-10:-5] + '.jpg'
        print(img_url, name)
        urlretrieve(img_url, 'img/' + name)


if __name__ == "__main__":
    url = 'https://image.so.com/z?ch=beauty&listtype=hot'
    html = get_html(url)
    # print(html)
    get_img(html)
