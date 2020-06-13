import requests
import re
import os
import time
from bs4 import BeautifulSoup
from contextlib import closing
from tqdm import tqdm  # Python进度条


# 创建保存目录
save_dir = '妖神记'
if save_dir not in os.listdir('/'):
    os.mkdir(save_dir)

target_url = 'https://www.dmzj.com/info/yaoshenji.html'

# 获取动漫章节链接和名字
response = requests.get(target_url)
soup = BeautifulSoup(response.text, 'lxml')
list_con_li = soup.find('ul', class_="list_con_li")
comic_list = list_con_li.find_all('a')
chapter_names = []
chapter_urls = []

for comic in comic_list:
    href = comic.get('href')
    name = comic.text
    chapter_names.insert(0, name)
    chapter_urls.insert(0, href)
#     # chapter_names.append(name)
#     # chapter_urls.append(href)

# 下载漫画
for i, url in enumerate(tqdm(chapter_urls)):
    download_header = {
        'Referer': url
    }
    name = chapter_names[i]

    while '.' in name:
        name = name.replace('.', '')
    chapter_save_dir = os.path.join(save_dir, name)

    if name not in os.listdir(save_dir):
        os.mkdir(chapter_save_dir)
        r = requests.get(url)
        html = BeautifulSoup(r.text, 'lxml')
        script_info = html.script
        pics = re.findall(r'\d{13,14}', str(script_info))

        for idx, pic in enumerate(pics):
            if len(pic) == 13:
                pics[idx] = pic + '0'
        pics = sorted(pics, key=lambda x: int(x))
        chapterpic_hou = re.findall(r'\|(\d{5})\|', str(script_info))[0]
        chapterpic_qian = re.findall(r'\|(\d{4})\|', str(script_info))[0]

        for idx, pic in enumerate(pics):
            if pic[-1] == '0':
                url = 'https://images.dmzj.com/img/chapterpic/' + \
                    chapterpic_qian + '/' + chapterpic_hou + \
                    '/' + pic[:-1] + '.jpg'
            else:
                url = 'https://images.dmzj.com/img/chapterpic/' + \
                    chapterpic_qian + '/' + chapterpic_hou + '/' + pic + '.jpg'
            pic_name = '%03d.jpg' % (idx + 1)
            pic_save_path = os.path.join(chapter_save_dir, pic_name)
            with closing(requests.get(url, headers=download_header, stream=True)) as f:
                chunk_size = 1024
                if f.status_code == 200:
                    with open(pic_save_path, 'wb') as file:
                        for data in f.iter_content(chunk_size=chunk_size):
                            file.write(data)
                else:
                    print('链接异常!')

        time.sleep(10)
