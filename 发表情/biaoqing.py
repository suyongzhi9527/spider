import requests
import os
import re
from bs4 import BeautifulSoup

_url = 'https://fabiaoqing.com/biaoqing/lists/page/{}.html'
urls = [_url.format(page) for page in range(1, 201)]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    img_list = soup.find_all('img', class_='ui image lazy')

    for img in img_list:
        img_url = img.get('data-original')
        img_title = img.get('title')
        img_title = re.sub(r'[,./?:;*&@#$%^\'\"\"!]', '', img_title)
        print(img_title)
        with open('image/' + img_title + os.path.splitext(img_url)[-1], 'wb') as f:
            img = requests.get(img_url).content
            f.write(img)
