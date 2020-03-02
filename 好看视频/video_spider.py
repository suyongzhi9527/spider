import requests
import json
import multiprocessing
from urllib.request import urlretrieve


def parse_url(q):
    url = 'https://haokan.baidu.com/videoui/api/videorec?tab=xiaopin&act=pcFeed&pd=pc&num=20'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    dict_data = response.json()
    print(len(dict_data['data']['response']['videos']))
    for i in dict_data['data']['response']['videos']:
        video_name = i['title']
        video_url = i['play_url']
        q.put(video_url)
        q.put(video_name)


def down_video(q):
    while True:
        video_url = q.get()
        video_name = q.get()
        urlretrieve(video_url, 'video/%s.mp4' % video_name)
        print("已下载完成--->%s" % video_name)
        if q.empty():
            break



if __name__ == '__main__':
    q = multiprocessing.Queue()
    t1 = multiprocessing.Process(target=parse_url, args=(q,))
    t2 = multiprocessing.Process(target=down_video, args=(q,))
    t1.start()
    t2.start()
