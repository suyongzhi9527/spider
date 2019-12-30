import requests
import re
from bs4 import BeautifulSoup

url = 'http://58921.com/alltime/2019'
html_str = requests.get(url)
html_str.encoding = 'utf-8'
# print(html_str.text)
html_str = html_str.text

req = r'<td><a href="/film/.*?" title="(.*?)">.*?</a></td>'

title = re.findall(req,html_str)
# print(title)

soup = BeautifulSoup(html_str,'lxml')
img_url = soup.find_all('img')[1:]
# print(img_url)

i = 0
for url in img_url:
    img_src = url.get('src')
    print(img_src)

    img_content = requests.get(img_src).content

    with open(r'F:\\spider_learn\\images\\{}.png'.format(title[i]),'wb') as f:
        f.write(img_content)
    i += 1
