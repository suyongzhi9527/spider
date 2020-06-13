import requests
import re
import os
from bs4 import BeautifulSoup

path = 'E:/种子下载/'
try:
    os.makedirs(path)
    print('目录创建成功!')
except:
    pass

url_list = list()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    'Host': 'www.lwgod.me'
}

for i in range(1, 2):
    url = 'http://www.lwgod.me/forum-292-{}.html'.format(i)
    url_list.append(url)

# print(url_list)

for url in url_list:
    soup = BeautifulSoup(requests.get(url, headers=headers).text, 'lxml')
    
    tbody = soup.find_all('tbody')[1:]

    for i in tbody:
        if i.attrs['id'] == 'separatorline':
            continue
        try:
            movie_name = re.findall(r'【龙网BT组】.*】', i.text)[0]
            print(movie_name)
            movie_name = re.sub(r'[:]', '.', movie_name)
            url = 'http://www.lwgod.me/' + i.find('a')['href']
            parse_url = BeautifulSoup(requests.get(url).text, 'lxml') # 解析详情页地址
            seed_url = 'http://www.lwgod.me/' + parse_url.find('ignore_js_op').find('a')['href']
            parse_url2 = BeautifulSoup(requests.get(seed_url).text, 'lxml')
            seed_url2 = 'http://www.lwgod.me/' + parse_url2.find(class_='dxksst').find('a')['href']
            with open(f'{path}{movie_name}.torrent', 'wb') as f:
                f.write(requests.get(seed_url2).content)
                print(f'{movie_name}下载完成!')
        except Exception as e:
            print(e)


