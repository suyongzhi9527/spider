import requests
import re
from urllib.parse import urljoin


def get_urls(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text
    img_url = r'<img.*?src="(.*?)".*?/>'
    url_list = re.findall(img_url, html, re.S)
    return url_list


def get_img(url, name):
    response = requests.get(url)
    response.encoding = 'utf-8'
    with open('F:\\spider_learn\\表情党\\image\\%d.gif' % name, 'wb') as f:
        f.write(response.content)
        print("正在下载第%d张表情" % name)


if __name__ == '__main__':
    urls = ['https://qq.yh31.com/zjbq/1020669.html', 'https://qq.yh31.com/zjbq/1020669_2.html',
            'https://qq.yh31.com/zjbq/1020669_3.html']
    for url in urls:
        url_list = get_urls(url)
        a = 1
        for url in url_list:
            com_url = urljoin("https://qq.yh31.com", url)
            get_img(com_url, a)
            a += 1
