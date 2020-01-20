import requests
import time
from bs4 import BeautifulSoup

headers = {
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3945.117Safari / 537.36'
}

link = 'https://beijing.anjuke.com/sale/p1/'
r = requests.get(link, headers=headers)
text = r.text

soup = BeautifulSoup(text, 'lxml')
house_list = soup.find_all('li', class_='list-item')  # 房子全部信息
for house in house_list:
    house_detail_url = house.find('a')
    detail_url = house_detail_url['href']

    detail_resp = requests.get(detail_url, headers=headers)

    detail_text = detail_resp.text
    detail_soup = BeautifulSoup(detail_text, 'lxml')
    long_title = detail_soup.find('h3', class_='long-title').text.strip()
    title = detail_soup.find('span', class_='title-content').text.strip()
    title_content = detail_soup.find('div', class_='houseInfo-item-desc js-house-explain').text.strip()
    print(long_title+':'+title+':'+title_content+'\n')
    time.sleep(2)