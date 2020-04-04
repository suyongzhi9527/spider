import requests
from lxml import etree


def get_urls(url):
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/80.0.3987.149Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.text


def html_result(html):
    html = etree.HTML(html)
    img_urls = html.xpath('//div[@class="main-content"]//img/@src')
    return img_urls


def get_image(url, img_name):
    response = requests.get(url)

    with open('img/%s.jpg' % img_name, 'wb') as f:
        f.write(response.content)


def main():
    url = 'https://www.manhuadao.cn/Comic/ComicView?comicid=58ddb12627a7c1392c23c427&chapterid=2182076'
    html = get_urls(url)
    img_urls = html_result(html)

    for url in img_urls:
        img_name = url.split('/')[-1]
        img_name2 = img_name.split('-')[-1]
        img_name3 = img_name2.split('.')[-2]
        get_image(url, img_name3)
        print(img_name3)


if __name__ == '__main__':
    main()
