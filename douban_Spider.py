import requests
from lxml import etree

url = 'https://movie.douban.com/cinema/nowplaying/guangzhou/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Referer': 'https://movie.douban.com/cinema/nowplaying/dongguan/'
}

resp = requests.get(url,headers=headers)
html_str = resp.text

html = etree.HTML(html_str)
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath("./li")
movie_list = []
for li in lis:
    title = li.xpath("@data-title")[0] # 电影名
    score = li.xpath("@data-score")[0] # 评分
    director = li.xpath("@data-director")[0] # 导演
    actors = li.xpath("@data-actors")[0] # 演员
    poster = li.xpath(".//li[@class='poster']//img/@src")[0] # 海报

    movie = {
        'title':title,
        'score':score,
        'director':director,
        'actors':actors,
        'poster':poster
    }
    movie_list.append(movie)
print(movie_list)