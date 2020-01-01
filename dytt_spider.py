import requests
from lxml import etree

base_url = 'https://www.dytt8.net/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}


def get_detail_urls(url):
    resp = requests.get(url, headers=headers)
    text = resp.content.decode('gbk', errors='ignore')  # 设置为ignore，则会忽略非法字符；
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url: base_url+url, detail_urls)  # 匿名函数
    return detail_urls


def parse_detail_page(url):
    movie = {}
    resp = requests.get(url, headers=headers)
    text = resp.content.decode('gbk')
    html = etree.HTML(text)

    title = html.xpath("//font[@color='#07519a']/text()")[0]
    movie['title'] = title

    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    poster = imgs[0]
    Screenshot = imgs[1]
    movie['poster'] = poster
    movie['Screenshot'] = Screenshot

    def parse_info(info, rule):
        return info.replace(rule, "").strip()

    infos = zoomE.xpath(".//text()")
    for index, info in enumerate(infos):
        # print(info,index)
        # print("-"*30)
        if info.startswith("◎年　　代"):
            info = parse_info(info, "◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info, "◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info, "◎类　　别")
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info, "◎豆瓣评分")
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info, "◎片　　长")
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info, "◎导　　演")
            movie['director'] = info
        elif info.startswith("◎主　　演"):
            info = parse_info(info, "◎主　　演")
            actors = [info]
            for x in range(index+1, len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith("◎简　　介"):
            info = parse_info(info,"◎简　　介")
            profiles = []
            for x in range(index+1,len(infos)):
                profile = infos[x].strip()
                if profile.startswith("【下载地址】"):
                    break
                profiles.append(profile)
            movie['profile'] = profiles
    
    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url
    return movie


def run():
    url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    movies = []
    for i in range(1, 8):  # 控制页数
        urls = url.format(i)
        detail_urls = get_detail_urls(urls)
        for detail_url in detail_urls:  # 遍历一页当中电影详情URL
            movie = parse_detail_page(detail_url)
            movies.append(movie)
            print(movies)


if __name__ == "__main__":
    run()
