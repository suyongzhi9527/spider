import requests
import json
from lxml import etree

url = 'http://music.taihe.com/top/dayhot'
base_url = 'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&songid='

resp = requests.get(url).content.decode()  # 获取页面数据

dom = etree.HTML(resp)  # 传入HTML文本，调用HTML类初始化，构造XPath解析对象
song_ids = dom.xpath('//a[contains(@href,"/song/")]/@href')[1:]  # 列表类型
song_names = dom.xpath('//a[contains(@href,"/song/")]/text()')[1:]  # 列表类型

for song_id, song_name in zip(song_ids, song_names):

    if '/' in song_name:  # 这里判断如果斜杠'/'存在song_name
        song_name = song_name.replace('/', '')  # 调用replace()方法，查找斜杠以空字符替换

    song_url = base_url + '%s' % song_id.split('/')[-1]
    song_url_str = requests.get(song_url).text  # 发送请求,获取文本响应

    dict_url = json.loads(song_url_str)  # 将str网页文本转换为json类型

    song_url_mp3 = dict_url['bitrate']['file_link']
    print(song_url_mp3)

    mp3 = requests.get(song_url_mp3).content

    # 保存
    with open(r'F:\\spider_learn\\music\\%s.mp3' % song_name, 'wb') as f:
        f.write(mp3)
