import datetime
import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.bilibili.com/ranking'
# 发起网络请求
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')


# 用来保存视频信息的对象
class Video(object):
    def __init__(self, title, rank, score, author, visit_num, barrage, video_url, up_id):
        self.title = title
        self.rank = rank
        self.score = score
        self.author = author
        self.visit_num = visit_num
        self.barrage = barrage
        self.video_url = video_url
        self.up_id = up_id

    def to_csv(self):
        return [self.rank, self.title, self.score, self.visit_num, self.barrage, self.author, self.up_id,
                self.video_url]

    @staticmethod
    def title():
        return ['排名', '标题', '分数', '播放量', '弹幕数', 'Up主', 'UpID', 'URL']


# 提取列表
items = soup.find_all('li', class_='rank-item')
videos = []  # 保存提取出来的video列表
for item in items:
    title = item.find('a', class_='title').get_text()  # 视频标题
    score = item.find('div', class_='pts').get_text()  # 综合评分
    rank = item.find('div', class_='num').get_text()  # 排名
    author = item.find('div', class_='detail').select('span')[2].get_text()  # up主名
    visit_num = item.find('div', class_='detail').select('span')[0].get_text()  # 播放量
    barrage = item.find('div', class_='detail').select('span')[1].get_text()  # 弹幕数
    video_url = item.find('a', class_='title')['href']  # 视频详情页链接
    up_id = item.find_all('a')[2]['href'][len('//space.bilibili.com/'):]  # up主ID
    v = Video(title, rank, score, author, visit_num, barrage, video_url, up_id)
    videos.append(v)

now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'top100_{now}.csv'
with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(Video.title())
    for v in videos:
        writer.writerow(v.to_csv())
