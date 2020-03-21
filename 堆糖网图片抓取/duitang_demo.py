import urllib.parse
import requests
import json
import jsonpath
from pprint import pprint

url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&type=feed&_type=&start={}'
kw = input('请输入需要抓取的图片类型:')
kw = urllib.parse.quote(kw)

num = 1
for i in range(0, 73, 24):
    urls = url.format(kw, i)
    response = requests.get(urls)
    data = response.text

    html = json.loads(data)
    photos = jsonpath.jsonpath(html, '$..path')

    for i in photos:
        img_content = requests.get(i)
        with open('img/{}.jpg'.format(num), 'wb') as f:
            f.write(img_content.content)
            print("正在下载第{}张图片".format(num))
            num += 1
