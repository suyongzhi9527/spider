import requests
import re
import time
from urllib import request


if __name__ == '__main__':
    urls = 'http://sc.chinaz.com/tupian/fengjing.html'
    response = requests.get(url=urls)
    html_str = response.content.decode()

    pattern = r'<img.*?alt="(.*?)".*?src2="(.*?)".*?>'
    img_list = re.findall(pattern,html_str,re.S)
    for i in img_list:
        img_title = i[0]
        img_url = i[1]
        request.urlretrieve(img_url,'./image/{}.jpg'.format(img_title))
        print("正在保存图片....")
        time.sleep(1)
