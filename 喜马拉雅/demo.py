# https://www.ximalaya.com/revision/play/v1/show?id=243499154&sort=1&size=30&ptype=1  歌单信息
# https://www.ximalaya.com/revision/play/v1/audio?id=243499154&ptype=1  单首歌信息
# https://www.ximalaya.com/revision/play/v1/audio?id=247031098&ptype=1
import requests
import json
import os

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}


def parse_html(url):
    resp = requests.get(url, headers=header)
    html = resp.text
    html = json.loads(html)
    return html


def get_content(html):
    content_list = html['data']['tracksAudioPlay']
    for content in content_list:
        id = content['trackId']  # 音频ID
        name = content['trackName']  # 音频名称
        urls = 'https://www.ximalaya.com/revision/play/v1/audio?id=%d&ptype=1' % id
        mus_json = parse_html(urls)
        mus_src = mus_json['data']['src']
        img_path = os.path.join(os.path.dirname(__file__), 'music')
        if not os.path.exists(img_path):
            os.mkdir(img_path)
        with open('music/%s.m4a' % name, 'wb') as f:
            m4a = requests.get(mus_src).content
            f.write(m4a)
            print("正在下载->%s" % name)


def main():
    url = 'https://www.ximalaya.com/revision/play/v1/show?id=254038394&sort=1&size=30&ptype=1'
    # url = 'https://www.ximalaya.com/revision/play/v1/show?id=243499154&sort=1&size=30&ptype=1'
    html = parse_html(url)
    get_content(html)


if __name__ == '__main__':
    main()
