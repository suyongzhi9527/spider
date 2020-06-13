import requests
from pyquery import PyQuery as pq
from urllib.parse import urlencode

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Referer': 'https://m.weibo.cn/u/2832482174?uid=2832482174&luicode=10000011&lfid=231093_-_selffollowed',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_page():
    params = {
        'uid': '2832482174',
        'luicode': '10000011',
        'lfid': '231093_-_selffollowed',
        'type': 'uid',
        'value': '2832482174',
        'containerid': '1076032832482174'
    }

    url = base_url + urlencode(params)
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
            weibo['id'] = item.get('id')
            weibo['内容'] = pq(item.get('text')).text()
            weibo['点赞数'] = item.get('attitudes_count')
            weibo['评论数'] = item.get('comments_count')
            weibo['转发数'] = item.get('reposts_count')
            yield weibo


if __name__ == "__main__":
    results = get_page()
    for result in  parse_page(results):
        print(result)