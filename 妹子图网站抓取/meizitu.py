import requests
import time
import os
from urllib import request
from pyquery import PyQuery as pq
from lxml import etree

headers = {
    'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3945.117Safari / 537.36'
}


def Index():
    """ 请求首页地址,获取详情页url """
    url = 'https://www.mzitu.com/'
    response = requests.get(url, headers=headers).text
    # pyquery 数据提取
    # 数据初始化
    doc = pq(response)
    # 通过ID选择器获取数据
    pins = doc('#pins li a').items()  # 返回查询集
    for i in pins:
        title = i.text()  # 图片标题
        detail_url = i.attr('href')  # 详情页地址
        Detail(detail_url, title)  # 调用详情页函数


def Detail(detail_url, title):
    """ 请求详情页地址，获取图片地址 """
    headers = {
        'referer': detail_url,
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3945.117Safari / 537.36'
    }
    for page in range(1, 11):
        urls = detail_url + '/' + str(page)
        response = requests.get(urls, headers=headers).text
        html = etree.HTML(response)
        img_url = html.xpath('//div[@class="main-image"]//img/@src')[0]
        img_title = html.xpath('//div[@class="main-image"]//img/@alt')[0]
        # Image(img_url, img_title)
        # print(img_url)

def Image(img_url, img_title):
    """ 请求图片地址，保存到本地 """
    headers = {
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3945.117Safari / 537.36'
    }
    file_path = "image/{0}.jpg".format(img_title)
    # if not os.path.exists(file_path):
    #     os.mkdir(os.path.join("image/",img_title))
    for i in range(len(img_title)):
        with open(file_path,"wb") as f:
            resposne = requests.get(img_url, headers = headers)
            f.write(resposne.content)
            print("正在保存!!!")


if __name__ == '__main__':
    Index()
