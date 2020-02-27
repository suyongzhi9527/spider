import requests
from pyquery import PyQuery as pq

url = 'http://news.4399.com/gonglue/lscs/kptj/'
html = requests.get(url).content.decode('gb2312')
doc = pq(html)
uls = doc('#dq_list > li').items()
for li in uls:
    img_url = li.find('img').attr('lz_src')
    img_name = li.find('div').text()
    url_content = requests.get(img_url).content
    print(img_name, img_url)
    with open('img/' + img_name + '.jpg', 'wb') as f:
        f.write(url_content)
print('下载完成...')
