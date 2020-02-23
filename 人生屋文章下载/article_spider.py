import os
import requests
from bs4 import BeautifulSoup


def get_urls(url):
    resp = requests.get(url)
    html = resp.content.decode('gbk')
    soup = BeautifulSoup(html, 'lxml')
    return soup


def main(url):
    path = os.getcwd() + u'/文章/'
    if not os.path.exists(path):
        os.mkdir(path)

    soup = get_urls(url)
    lis = soup.find_all('ul', class_='l1')
    for li in lis:
        urls = li.find_all('li')
        for url in urls:
            detail_url = url.find('a')['href']
            result = get_urls(detail_url)
            title = result.find('div', class_='artview').find('h1').get_text()
            # print(title)
            author = result.find('div', class_='artinfo').get_text().strip().split("　")[-2]
            date = result.find('div', class_='artinfo').get_text().strip().split("　")[0]
            content = result.find('div', class_='artbody').find('p').get_text()

            filename = path + title + '.txt'
            # print(filename)

            new = open(filename, 'w')
            new.write('<<' + title + '>>\n\n')
            new.write(date + ' ' + author + '\n\n')
            new.write(content)
            print(title)
            new.close()


if __name__ == '__main__':
    url = 'http://www.rensheng5.com/zx/onduzhe/'
    main(url)
