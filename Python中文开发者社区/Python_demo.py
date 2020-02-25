import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.pythontab.com/html/pythonhexinbiancheng/index.html'

url_list = []
source_list = []
for i in range(2, 16):
    url_list.append(url)
    url_list.append('https://www.pythontab.com/html/pythonhexinbiancheng/%s.html' % i)

for j in url_list:
    header = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/79.0.3945.117Safari/537.36'
    }
    html = requests.get(j, headers=header).content
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('#catlist > li > h2 > a')
    links = soup.select('#catlist > li > h2 > a')

    for title, link in zip(titles, links):
        data = {
            'title': title.get_text(),
            'link': link.get('href')
        }
        source_list.append(data)

    for i in source_list:
        detail_html = requests.get(i['link'], headers=header).content
        soup = BeautifulSoup(detail_html, 'html.parser')
        text_p = soup.select('#Article > div.content > p')
        text = []
        for t in text_p:
            text.append(t.get_text())

        title_text = i['title']
        title_text = re.sub(r'[,.?/_!*\\"\':：|]', '', title_text)
        print(title_text)

        with open('study/%s.txt' % title_text, 'wb') as f:
            for a in text:
                f.write(a.encode())
