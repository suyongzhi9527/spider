import requests
from bs4 import BeautifulSoup


def get_movies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Host': 'movie.douban.com'
    }
    movie_list = []
    for i in range(0, 10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers=headers, timeout=10)
        print(str(i + 1), "页响应码:", r.status_code)
        soup = BeautifulSoup(r.text, 'lxml')
        hd_list = soup.find_all('div', class_='hd')
        for each in hd_list:
            movie = each.a.span.text.strip()
            movie_en = each.find('a').contents[3].text.strip().replace('/\xa0', '')
            movie_gt = each.find('span', class_='other').text.strip().replace('/\xa0', '')
            movie_list.append([movie, movie_en, movie_gt])
    return movie_list


movies = get_movies()
print(movies)
