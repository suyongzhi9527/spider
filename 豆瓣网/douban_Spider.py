import requests
import pymysql
from lxml import etree

db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='scraping',
    port=3306
)

cursor = db.cursor()

url = 'https://movie.douban.com/cinema/nowplaying/guangzhou/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Referer': 'https://movie.douban.com/cinema/nowplaying/dongguan/'
}

resp = requests.get(url, headers=headers)
html_str = resp.text

html = etree.HTML(html_str)
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath("./li")
movie_list = []
for li in lis:
    title = li.xpath("@data-title")[0]  # 电影名
    score = li.xpath("@data-score")[0]  # 评分
    director = li.xpath("@data-director")[0]  # 导演
    actors = li.xpath("@data-actors")[0]  # 演员
    poster = li.xpath(".//li[@class='poster']//img/@src")[0]  # 海报

    cursor.execute("insert into top250(title, score, director, actors, poster) values (%s, %s, %s,%s, %s)",(title, score, director, actors, poster))

    movie = {
        'title': title,
        'score': score,
        'director': director,
        'actors': actors,
        'poster': poster
    }
    movie_list.append(movie)
cursor.close()
db.commit()
db.close()
print(movie_list)
