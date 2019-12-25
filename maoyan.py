import requests
import json
from requests.exceptions import RequestException
import re
import time


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile(
        r'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield {
            '索引': item[0],
            '图片': item[1],
            '电影名': item[2],
            '明星': item[3].strip()[3:],
            '上映时间': item[4].strip()[5:],
            '评分': item[5] + item[6]
        }


def save_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    # print(html)
    for item in parse_one_page(html):
        print(item)
        save_to_file(item)


if __name__ == "__main__":
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
