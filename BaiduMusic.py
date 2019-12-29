import requests
import json
from lxml import etree

url = 'http://music.taihe.com/top/dayhot'
base_url = 'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&songid='

resp = requests.get(url).content.decode()

dom = etree.HTML(resp)
song_ids = dom.xpath('//a[contains(@href,"/song/")]/@href')[1:]
song_names = dom.xpath('//a[contains(@href,"/song/")]/text()')[1:]

for song_id,song_name in zip(song_ids,song_names):

    if '/' in song_name:
        song_name = song_name.replace('/','')

    song_url = base_url + '%s' % song_id.split('/')[-1]
    song_url_str = requests.get(song_url).text

    dict_url = json.loads(song_url_str)

    song_url_mp3 = dict_url['bitrate']['file_link']
    print(song_url_mp3)

    mp3 = requests.get(song_url_mp3).content

    # 保存
    with open('F:\spider_learn\music\%s.mp3' % song_name,'wb') as f:
        f.write(mp3)
