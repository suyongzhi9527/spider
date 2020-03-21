import requests
import re
from lxml import etree
from urllib import request

url = "https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=6&start={}"
base_url = "https://www.pearvideo.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}


def get_html(url):
    response = requests.get(url, headers=headers)  # 发送请求
    if response.status_code == 200:
        # print(response.text)  # 获取网页源代码
        return response.text  # 返回值
    else:
        return None


def get_video(html):
    item = []
    html_str = etree.HTML(html)
    video_urls = html_str.xpath('//div[@class="vervideo-bd"]/a/@href')
    for video_url in video_urls:
        video_url = base_url + video_url
        # print(video_url)
        item.append(video_url)
        # print(video_url)

    for urls in item:
        # print(urls)
        video_html = get_html(urls)
        real_url = re.findall(r'<script.*?srcUrl="(.*?)"', video_html, re.S)
        video_name = re.findall(r'<h1 class="video-tt">(.*?)</h1>', video_html, re.S)

        for name, link in zip(video_name, real_url):
            # name = re.sub(r'[,.!:"\']+', '', name)
            print(name, link)
            request.urlretrieve(link, "video/%s.mp4" % name)


# 1:12,2:24,3:36,4:48,5:60

def main():
    for urls in range(12, 72, 12):
        links = url.format(urls)
        # print(links)
        html = get_html(links)
        get_video(html)


if __name__ == '__main__':
    main()
