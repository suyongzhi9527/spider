import time
import re
import os
import requests
from multiprocessing.pool import Pool
from urllib.parse import urlencode

headers = {
    'user-agent': 'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/81.0.4044.92Safari/537.36',
    'cookie': 'tt_webid=6816139975647217165; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6816139975647217165; ttcid=2f6ff5f77ca54fafacb34bde638c1abd41; csrftoken=3b1d29b19d137a5409be34dae687990f; SLARDAR_WEB_ID=2a908f81-7853-4257-8d2e-9cadd2f3987f; _ga=GA1.2.1917885242.1587689594; s_v_web_id=verify_kaonu670_Y7cC0iTl_2rXw_4UDb_84uw_v0Y0wsgCmeXu; __tasessionId=kqsmcgzlv1590546493644; __ac_nonce=05ecdd03f007874f45e28; __ac_signature=qLxevAAgEBBu6-cx-fY06Ki9X6AAPaAbSSpoiBbdBbwoQCeNQXcYBTofteiQQBBD-x8x1Rg9NZnl1UERBLozkmAsL38-mO9gu5j6Ymwvp7tW4780ZBqyrjfftP71BzWbhqn; tt_scid=gwloz-P387AdL.iSZiDsDw.4Hwo-zOWOo7jviVTDD5qwqb.EfQquumy5GUB5157A68c9',
    'referer': 'https://www.toutiao.com/search/?keyword=%E7%BE%8E%E5%A5%B3',
    'x-requested-with': 'XMLHttpRequest'
}


def get_page(offset):
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '美女',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': int(time.time())
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)  # 构造url
    url = url.replace('=+', '=')
    # print(url)
    try:
        r = requests.get(url, headers=headers, params=params)
        r.content.decode('utf-8')
        if r.status_code == 200:
            return r.json()
    except requests.ConnectionError as e:
        print(e)


def get_image(json):  # 获取图片
    if json.get('data'):  # 如果data存在
        for item in json.get('data'):
            if item.get('title') is None:  # 如果标题是空的就跳过这层循环
                continue
            title = item.get('title')
            if item.get('article_url') == None:
                continue
            url_page = item.get('article_url')
            rr = requests.get(url_page, headers=headers)
            if rr.status_code == 200:
                pat = '<script>var BASE_DATA = .*?articleInfo:.*?content:(.*?)groupId.*?</script>'
                match = re.search(pat, rr.text, re.S)
                if match != None:
                    result = re.findall(r'img src&#x3D;\\&quot;(.*?)\\&quot;', match.group(), re.S)
                    yield {
                        'title': title,
                        'image': result
                    }


def save_image(content):
    path = 'D://今日头条美女//'
    if not os.path.exists(path):
        os.mkdir(path)
        os.chdir(path)
    else:
        os.chdir(path)

    if not os.path.exists(content['title']):  # 创建单个文件夹
        if '\t' in content['title']:  # 以title为标题创建单个文件夹
            title = content['title'].replace('\t', '')  # 去除特殊符号 不然创建不了文件名称
            os.mkdir(title + '//')
            os.chdir(title + '//')
            print(title)
        else:
            title = content['title']
            os.mkdir(title + '//')  # 创建文件夹
            os.chdir(title + '//')
            print(title)
    else:  # 如果存在
        if '\t' in content['title']:  # 以title为标题创建单个文件夹
            title = content['title'].replace('\t', '')  # 去除特殊符号 不然创建不了文件名称
            os.chdir(title + '//')
            print(title)
        else:
            title = content['title']
            os.chdir(title + '//')
            print(title)

    for q, u in enumerate(content['image']):  # 遍历图片地址列表
        u = u.encode('utf-8').decode('unicode_escape')

        # 先编码在解码 获得需要的网址链接
        #  开始下载
        r = requests.get(u, headers=headers)
        if r.status_code == 200:
            # file_path = r'{0}/{1}.{2}'.format('美女', q, 'jpg')  # 文件的名字和地址，用三目运算符来调试文件夹的名字
            # hexdisgest() 返回十六进制图片
            with open(str(q) + '.jpg', 'wb') as fw:
                fw.write(r.content)
                print(f'该系列----->下载{q}张')


def main(offset):
    data_json = get_page(offset)
    # print(data_json)
    for content in get_image(data_json):
        try:
            save_image(content)
        except FileExistsError and OSError:
            print('创建文件格式错误，包含特殊字符串')
            continue


if __name__ == '__main__':
    # pool = Pool()
    # groups = [j * 20 for j in range(8)]
    groups = 20
    # pool.map(main, groups)  # 传offset偏移量
    # print(groups)
    main(groups)
    # pool.close()
    # pool.join()
    # info = '机场高速、西直门北大街、中关村大街、动物园路交通管理措施结束。\u200b\u200b\u200b\u200b,2020-05-25 14:04'
    # pattern_word = re.compile(r'\\u[a-z0-9]+')
    # res = re.sub(pattern_word, '',info)
    # print(res)
