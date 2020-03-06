import requests
import re
import pymysql


url = 'https://pvp.qq.com/web201605/js/herolist.json'

response = requests.get(url)
resList = response.json()
# print(resList)

db = pymysql.connect('localhost', 'root', '123456', 'pydata')
cursor = db.cursor()
for i in range(len(resList)):
    item = resList[i]
    # print(item)
    cursor = db.cursor()
    sql = 'insert into `heros` (`name`,`cname`,`title`,`new_type`,hero_type,skin_name) values ("{}","{}","{}","{}","{}","{}")'
    sql = sql.format(item['ename'], item['cname'], item['title'], item['new_type'], item['hero_type'],
                     item.get('skin_name'))
    # print(sql)
    cursor.execute(sql)
    db.commit()


def getHeroInfo(name):
    url = 'https://pvp.qq.com/web201605/herodetail/{}.shtml'.format(name)
    result = requests.get(url)
    result.encoding = 'gbk'
    # print(result.text)
    reg = re.compile(r'(<div class="skill-show">.*?</div>)\s+</div>\s+</div>.*?<p class="sugg-tips">(.*?)</p>', re.S)
    regRes = reg.findall(result.text)
    skill = regRes[0][0]
    suggtips = regRes[0][1]
    sql = "update heros set skill='{}',`sugg-tips`='{}' where `name` = '{}'".format(skill, suggtips, name)
    print(sql)
    cursor.execute(sql)
    db.commit()


httpUrl = 'https://pvp.qq.com/web201605/js/herolist.json'
resList = requests.get(httpUrl)
resList = resList.json()

for i in range(len(resList)):
    item = resList[i]
    getHeroInfo(item['ename'])
