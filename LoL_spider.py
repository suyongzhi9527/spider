import requests
import json
import re

"""
分析网页
1.获取JS源码，获取英雄的ID
2.拼接URL地址
3.获取下载图片名称
4.保存图片
"""
def get_lol_image():
    # 获取JS源代码
    url = 'https://lol.qq.com/biz/hero/champion.js'
    html_str = requests.get(url).content.decode()

    # 正则表达式
    regx = r'"keys":(.*?),"data"'
    js_list = re.findall(regx,html_str) # 列表类型
    # print(type(js_list)) # 列表
    # print(type(js_list[0])) # 字符串
    js_dict = json.loads(js_list[0])
    # print(type(js_dict)) # 字典类型

    pic_list = []
    for hero_id in js_dict:
        for i in range(21):
            i = str(i)
            # https://game.gtimg.cn/images/lol/act/img/skin/big154015.jpg
            if len(i) == 1:
                hero_num = "00" + i # 001 002 003
            elif len(i) == 2:
                hero_num = "0" + i # 010 020 030
            hero_nums = hero_id + hero_num
            hero_url = 'https://game.gtimg.cn/images/lol/act/img/skin/big'+hero_nums+'.jpg'
            pic_list.append(hero_url)
    
    # 获取下载图片名称
    list_filepath = []
    path = "F:\spider_learn\images\\"
    for name in js_dict.values():
        for i in range(20):
            filepath = path + name + str(i) + ".jpg"
            list_filepath.append(filepath)

    # 保存图片
    n = 0
    for pic_url in pic_list:
        res = requests.get(pic_url)
        n += 1
        if res.status_code == 200:
            print("正在下载:%s" % list_filepath[n])
            with open(list_filepath[n],'wb') as f:
                f.write(res.content)
get_lol_image()