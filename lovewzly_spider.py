import requests
import os

"""
http://www.lovewzly.com/api/user/pc/list/search?startage=21&endage=30&gender=2&cityid=76&marry=1&salary=3&page=1
"""


# 设置年龄
def get_age():
    age = int(input("请输入年龄:"))
    if 21 <= age <= 30:
        startage = 21
        endage = 30
    elif 31 <= age <= 40:
        startage = 31
        endage = 40
    else:
        startage = 0
        endage = 0
    return startage, endage


# 设置性别
def get_sex():
    sex = int(input("请输入性别1男2女:"))
    if sex == 1:
        gender = 1
    elif sex == 2:
        gender = 2
    return gender


# 设置薪水
def get_money():
    money = int(input("请输入工资:"))
    if 2000 <= money < 5000:
        salary = 2
    elif 5000 <= money < 10000:
        salary = 3
    elif 10000 <= money < 20000:
        salary = 4
    elif 20000 <= money:
        salary = 5
    else:
        salary = 0
    return salary

# 结婚？未婚，离异，丧偶
def get_marry():
    marry = int(input("输入1未婚3离异4丧偶:"))
    if marry == 1:
        marry = 1
    elif marry == 3:
        marry = 3
    elif marry == 4:
        marry = 4
    else:
        marry = ''
    return marry


# 保存头像
def save_image(item):
    if not os.path.exists('images'):  # 判断文件夹是否存在
        os.mkdir('images')  # 如果不在即新建

    image_url = item['avatar']
    resp = requests.get(image_url)
    if resp.status_code == 200:
        file_path = 'images/{}.jpg'.format(item['username'])

        with open(file_path, 'wb') as f:
            f.write(resp.content)
            print("正在保存{}...".format(item['username']))


# 查询符合条件数据
def get_data():
    startage, endage = get_age()
    gender = get_sex()
    marry = get_marry()
    salary = get_money()
    url = 'http://www.lovewzly.com/api/user/pc/list/search?startage={}&endage={}&gender={}&cityid=76&marry={}&salary={}&page={}'
    for i in range(1,3):
        urls = url.format(startage, endage, gender, marry, salary,i)
        resp = requests.get(urls)
        if resp.status_code == 200:
            wzly_json = resp.json()

            for item in wzly_json['data']['list']:
                print(item)
                save_image(item)


if __name__ == "__main__":
    get_data()
