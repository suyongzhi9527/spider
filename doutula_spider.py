import requests
import os
import re
from lxml import etree
from urllib import request


def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
    }
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    # 过滤class为gif的图片
    imgs = html.xpath(
        '//div[@class="page-content text-center"]//img[@class != "gif"]')
    for img in imgs:
        # img_urls = img.xpath("@data-original")[0]
        img_urls = img.get("data-original")  # 获取图片链接
        alt = img.get("alt")  # 获取图片文本
        alt = re.sub(r'[\?？。.!！,，:：]', '', alt)  # 替换掉特殊字符
        suffix = os.path.splitext(img_urls)[1]  # 截取图片后缀
        filename = alt + suffix  # 拼接后缀,组成图片名
        opener = request.build_opener()
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')
        ]
        request.install_opener(opener)
        img_path = 'images'
        if not os.path.exists(img_path):
            os.mkdir(img_path)
        request.urlretrieve(img_urls, 'images/' + filename)
        print("下载成功-> %s" % filename)


def main():
    for i in range(1, 101):
        url = "http://www.doutula.com/photo/list/?page=%d" % i
        print("################第%d页开始下载################" % i)
        parse_page(url)


if __name__ == "__main__":
    main()
