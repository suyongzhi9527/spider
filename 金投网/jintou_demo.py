from pyquery import PyQuery as pq
import pymysql


def newsUrl():
    url = 'https://stock.cngold.org/rumen'
    doc = pq(url, encoding="utf-8")
    lista = doc('.news_list li a')
    # print(lista)
    for i, item in enumerate(lista):
        yield doc(item).attr('href')


# newsUrl()

def parsePage(url):
    doc = pq(url, encoding="utf-8")
    titleDom = doc('body > div.main.w1000 > div.heading1.w1000.mt20.clearfix > h1')
    title = titleDom.text()
    summary = doc('body > div.main.w1000 > div.article.clearfix > div.main_left.fl > div.summary > p').text()
    tempDom = doc('body > div.main.w1000 > div.article.clearfix > div.main_left.fl > div.article_con')
    tempDom.remove('script')
    content = tempDom.html()
    nextPageUrl = doc('.listPage a:contains("下一页")').attr('href')
    while nextPageUrl:
        tempDoc = pq(nextPageUrl, encoding="utf-8")
        tempDom = tempDoc('body > div.main.w1000 > div.article.clearfix > div.main_left.fl > div.article_con')
        tempDom.remove('script')
        content += tempDom.html()
        nextPageUrl = tempDoc('.listPage a:contains("下一页")').attr('href')
    sql = "insert into stocknews (title,summary,content) values ('{}','{}','{}')".format(title, summary, content)
    cursor.execute(sql)
    db.commit()
    print(title)


if __name__ == '__main__':
    db = pymysql.connect('localhost', 'root', '123456', 'pydata')
    cursor = db.cursor()
    newListUrl = newsUrl()
    for url in newListUrl:
        print(url)
        parsePage(url)
    db.close()
