import requests
import json
import os
from urllib import request


def get_request_data(url, page):
    cookies = {
        '_dg_abtestInfo.7b6028a56aac520d.ce42': '1',
        '_dg_check.7b6028a56aac520d.ce42': '-1',
        '_dg_playback.7b6028a56aac520d.ce42': '1',
        '_dg_antiBotFlag.7b6028a56aac520d.ce42': '1',
        '_dg_antiBotInfo.7b6028a56aac520d.ce42': '10%7C%7C%7C3600',
        'SESSION': 'NmVkYWM0OGUtZTU2My00NmNkLTk1OGEtZWFmYjk1MGU3MDky',
        '_dg_id.7b6028a56aac520d.ce42': '2d75030a713ee930%7C%7C%7C1582114186%7C%7C%7C1%7C%7C%7C1582176846%7C%7C%7C1582176846%7C%7C%7C%7C%7C%7Cf978d31c5f870a89%7C%7C%7C%7C%7C%7C%7C%7C%7C0%7C%7C%7Cundefined',
        '_dg_antiBotMap.7b6028a56aac520d.ce42': '202002201334%7C%7C%7C1',
    }

    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        'Content-Type': 'application/json',
        'Origin': 'https://www.ssyer.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    data = '{"cateId":2,"order":2,"recommendType":1,"page":{"showCount":20,"currentPage":%d}}' % page
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    json_data = response.json()
    return json_data


if __name__ == '__main__':
    video_path = os.path.join(os.getcwd(), 'video')
    if not os.path.exists(video_path):
        os.mkdir(video_path)

    url = 'https://www.ssyer.com/apis/20001'
    for page in range(1, 4):
        json_data = get_request_data(url, page)
        result = json_data['data']
        print(result)
        for item in range(len(result)):
            # print(item)
            print('正在下载第{}个视频'.format(item))
            video_url = result[item]['video']

            file_path = video_path + '/%s' % (item + 1) + '.mp4'
            request.urlretrieve(video_url, file_path)
