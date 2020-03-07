import os
import re
from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup

id = 29
error_num = 0
while (id <= 490):
    try:

        id += 1
        headers = {
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/79.0.3945.117Safari/537.36'
        }
        resp = requests.get('https://www.haodou.com/recipe/' + str(id) + '/', headers=headers)
        html = resp.text
        # print(html)

        soup = BeautifulSoup(html, 'lxml')
        title = soup.find(class_='cover').get('alt')
        print(title)
        img_url = soup.find(class_='cover').get('src')
        print(img_url)

        try:
            urlretrieve(img_url, '菜单\\' + title + '.jpg')
        except Exception as e:
            print(e)
            print(title + '图片下载失败!')
        print("图片下载成功!")

        drop_html = re.compile(r'<div.*data-v-17ffbd4e="">(.*?)</div>', re.S)
        recipe_text = soup.find_all(class_='desc')

        for text in recipe_text:
            text_str = "".join(re.findall(drop_html, str(text)))
            with open('菜单\\' + title + '.txt', 'w') as f:
                f.writelines(text_str)

    except Exception as e:
        print(e)
    else:
        continue
