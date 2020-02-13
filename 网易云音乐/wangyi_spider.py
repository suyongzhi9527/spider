import requests
import time
import re
from lxml import etree


url = 'https://music.163.com/playlist?id=3010352080'
base_url = 'https://link.hhtjim.com/163/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

resp = requests.get(url, headers=headers).text

dom = etree.HTML(resp)
music_ids = dom.xpath('//a[contains(@href,"song?")]/@href')
music_names = dom.xpath('//a[contains(@href,"song?")]/text()')

for music_name, music_id in zip(music_names, music_ids):
    music_name = re.sub(r'[\\:*?"<>|/]+', '', music_name)
    count_id = music_id.strip('/song?id=')
    if ('$' in count_id) == False:
        song_url = base_url + '%s' % count_id + '.mp3'
        mp3 = requests.get(song_url, headers=headers).content

        with open('./Music/%s.mp3' % music_name, 'wb') as f:
            f.write(mp3)
            print('%s下载完成' % music_name)
            time.sleep(1)
