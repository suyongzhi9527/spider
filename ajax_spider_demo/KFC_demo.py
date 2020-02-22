import requests
import json


def get_page(page):
    data = {
        'cname': '广州',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3945.117Safari / 537.36'
    }
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    try:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_content(text):
    item = {}
    item_list = []
    for data in text['Table1']:
        item['storeName'] = data['storeName']
        item['addressDetail'] = data['addressDetail']
        item['pro'] = data['pro']
        item['provinceName'] = data['provinceName']
        item['cityName'] = data['cityName']
        item_list.append(item)
    return item_list


def write_to_file(item):
    with open('KFC.json', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    for i in range(1, 23):
        result = get_page(i)
        item = get_content(result)
        write_to_file(item)
