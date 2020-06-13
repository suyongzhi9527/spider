from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time


def main():
    driver = webdriver.Chrome("E:\chromedriver_win32\chromedriver.exe")
    driver.get('https://v.taobao.com/v/content/live?catetype=704&from=taonvlang')
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    for img_tag in soup.body.select('img[src]'):
        # print(img_tag)
        url = img_tag.attrs['src']
        # print(url)
        try:
            if not str(url).startswith('http'):
                if str(url)[-3:] == 'png':
                    continue
                url = 'http:' + url
                # filename = url[url.rfind('/') + 1:]
                filename = url.split('/')[-2]
                print(filename, url)
                resp = requests.get(url)
                with open('images/' + filename + '.jpg', 'wb') as f:
                    f.write(resp.content)
        except OSError:
            print(filename + '下载失败')
    # print('图片下载完成')


if __name__ == '__main__':
    main()
