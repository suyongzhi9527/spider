import requests
import json
import urllib

def get_sogou_img(category, length, path):
    imgs = requests.get('https://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=%E5%A3%81%E7%BA%B8&tag='+category+'&start=0&len='+str(length)+'&width=1920&height=1080')
    jd = json.loads(imgs.text)
    jd = jd['all_items']
    imgs_url = []
    for j in jd:
        imgs_url.append(j['pic_url'])
    m = 1
    for img in imgs_url:
        print(str(m)+'.jpg 下载中')
        urllib.request.urlretrieve(img, path+str(m)+'.jpg')
        m += 1
    print('下载完成!')
if __name__ == "__main__":
    get_sogou_img('卡通',5,'D:/Python程序设计实验项目/img/')