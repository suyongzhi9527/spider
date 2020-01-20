import pymysql
import requests
from bs4 import BeautifulSoup

db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='scraping',
    port=3306
)

cursor = db.cursor()  # 创建一个游标对象
# 查询数据
# cursor.execute("select * from urls")
# result = cursor.fetchall()
# print(result)

link = 'http://www.santostang.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
r = requests.get(link, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
title_list = soup.find_all("h1", class_="post-title")
for eachone in title_list:
    url = eachone.a['href']
    title = eachone.a.text.strip()
    cursor.execute("insert into urls(url,content) values (%s, %s)", (url, title))
cursor.close()
db.commit()
db.close()

# 条件查询
# sql = """
# select * from tb_college where collid = 3
# """
# cursor.execute(sql)
# result = cursor.fetchone()
# print(result)

# fetchone()函数使用
# sql = """
# select * from tb_college
# """
# cursor.execute(sql)
# while True:
#     result = cursor.fetchone()
#     if result:
#         print(result)
#     else:
#         break

# fetchall()函数使用
# sql = """
# select * from tb_college
# """
# cursor.execute(sql)
# results = cursor.fetchall()
# for result in results:
#     print(result)

# fetchmany()函数使用
# sql = """
# select * from tb_college
# """
# cursor.execute(sql)
# results = cursor.fetchmany(6)
# for result in results:
#     print(result)

# 插入一条数据
# sql = """
# insert into tb_college(collid,collname,collmaster) values(4,'Python学院','苏勇智')
# """
# cursor.execute(sql)
# db.commit()

# sql = """
# insert into tb_college(collid,collname,collmaster) values(null,%s,%s)
# """
# name = 'Python爬虫学院'
# master = '小苏'
# cursor.execute(sql,(name,master))
# db.commit()

# 删除数据
# sql = """
# delete from tb_college where collid = 5
# """
# cursor.execute(sql)
# # 插入、删除、更新都需要执行commit()操作
# db.commit()

# 更新数据
# sql = """
# update tb_college set collmaster = '封于修' where collid = 3
# """
# cursor.execute(sql)
# db.commit()

# db.close()
