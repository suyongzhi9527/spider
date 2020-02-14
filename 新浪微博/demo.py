from urllib.parse import urlencode
from pyquery import PyQuery as pq
import requests

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Referer': 'https://m.weibo.cn/',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}


def get_page(page):
    data = {
        'containerid': 102803,
        'openApp': 0,
        'since_id': page
    }
    url = base_url + urlencode(data)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')  # 微博ID
            weibo['text'] = pq(item.get('text')).text()  # 文博正文 使用pyquery将正文中的HTML标签去掉
            weibo['attitudes'] = item.get('attitudes_count')  # 点赞数
            weibo['comments'] = item.get('comments_count')  # 评论数
            weibo['reposts'] = item.get('reposts_count')  # 转发数
            yield weibo


if __name__ == '__main__':
    for page in range(1, 6):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
