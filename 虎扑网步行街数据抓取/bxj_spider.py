import requests
import pymysql
from lxml import etree
from bs4 import BeautifulSoup
import datetime

db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='scraping',
    port=3306
)

cursor = db.cursor()  # 创建一个游标对象


def get_page(link):
    headers = {
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3945.117Safari / 537.36'
    }

    r = requests.get(link, headers=headers)
    html = r.content
    html = html.decode('utf-8')
    html_str = etree.HTML(html)
    # soup = BeautifulSoup(html, 'lxml')
    # return soup
    return html_str


def get_data(post_list):
    data_list = []
    # for post in post_list:
    #     titles = post.find_all('div', class_='titlelink box')
    #     for title_ in titles:
    #         title = title_.find('a', class_='truetit').text
    #         title_url = 'https://bbs.hupu.com' + title_.find('a')['href']
    #         data_list.append([title, title_url])
    #     authors = post.find_all('div', class_='author box')
    #     for author_ in authors:
    #         author = author_.find('a', class_='aulink').text
    #         time = author_.contents[5].text
    #         data_list.append([author, time])
    #     endauthors = post.find_all('div', class_='endreply box')
    #     for endauthor_ in endauthors:
    #         endauthor = endauthor_.find('span', class_='endauthor').text
    #         data_list.append(endauthor)
    #
    # print(data_list)

    # for post in post_list:
    #     # print(type(post))
    #     data_item = {}
    #     data_item['title'] = post.xpath('.//div[@class="titlelink box"]/a//text()')[0] if len(
    #         post.xpath('.//div[@class="titlelink box"]/a//text()')) > 0 else None
    #     data_item['author'] = post.xpath('.//div[@class="author box"]/a/text()')[0]
    #     data_item['endauthor'] = post.xpath('.//div[@class="endreply box"]/span/text()')[0]
    #
    #     data_list.append(data_item)
    # # print(data_list)
    # return data_list

    for post in post_list:
        title = post.xpath('.//div[@class="titlelink box"]/a//text()')[0] if len(
            post.xpath('.//div[@class="titlelink box"]/a//text()')) > 0 else None
        author = post.xpath('.//div[@class="author box"]/a/text()')[0]
        endauthor = post.xpath('.//div[@class="endreply box"]/span/text()')[0]
        cursor.execute("insert into urls(title, author, endauthor) values (%s, %s, %s)",(title, author, endauthor))
    cursor.close()
    db.commit()
    db.close()


def main():
    link = 'https://bbs.hupu.com/bxj-1'
    soup = get_page(link)
    post_list = soup.xpath('//ul[@class="for-list"]/li')
    # print(post_list)
    # data_list = get_data(post_list)
    get_data(post_list)
    # for each in data_list:
    #     print(each)


if __name__ == '__main__':
    main()
