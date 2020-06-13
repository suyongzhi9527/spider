import requests
import datetime
from urllib.request import urlretrieve
from lxml import etree

BASE_URL = "https://www.mn52.com"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
}


def menu():
    print("""
    (1)==> 需要输入：文件储存路径,例如 D:/image
           下载的图片都会保存在这个文件夹
    (2)==> 图片类别 Number
            性感美女 ==>[ 1 ]
            清纯美女 ==>[ 2 ]
            韩国美女 ==>[ 3 ]
            欧美图片 ==>[ 4 ]
            美女明星 ==>[ 5 ]
    (3)==> 下载的起始页和末尾页的页码数
            起始页[ startPage ]
            末尾页[ endPage(不包含末尾页)]
    """)


def downloadImage(url, path):
    response = requests.get(url, headers=headers)
    content = response.text
    html = etree.HTML(content)
    src = html.xpath("//div[@id='originalpic']/img/@src")  # 图片真实地址
    firstsrc = src[0]
    filetype = firstsrc[-4:]  # 通过切片获取图片类型 jpg, png

    for img in src:
        img_name = img[-12:-4]
        if str(img[1:4]) == "img":
            imgUrl = BASE_URL + img
        else:
            imgUrl = "https:" + img
        save_path = path + "/" + str(img_name) + str(filetype)
        urlretrieve(imgUrl, save_path)
        print("图片下载成功!", imgUrl)


def get_url(typeNum):
    type = ""
    if typeNum == 1:
        type = "xingganmeinv"
    elif typeNum == 2:
        type = "meihuoxiezhen"
    elif typeNum == 3:
        type = "rihanmeinv"
    elif typeNum == 4:
        type = "jingyannenmo"
    elif typeNum == 5:
        type = "meinvmingxing"
    url1 = "https://www.mn52.com/"
    url2 = "/list_"
    url = url1 + type + url2 + str(typeNum) + "_"
    return url


def main():
    path = input("1.输入文件存储路径(例如 D:/image):")
    typeNum = int(input("2.请输入下载分类: "))
    urlList = get_url(typeNum)
    startPage = int(input("3.请输入起始页:"))
    endPage = int(input("4.请输入末尾页:"))
    print("== 精彩资源即将开始 ==")

    startTime = datetime.datetime.now()
    for n in range(startPage, endPage):
        reurl = urlList + str(n) + ".html"
        response = requests.get(reurl, headers=headers)
        content = response.text
        html = etree.HTML(content)
        detail_src = ["https://" + i[2:] for i in
                      html.xpath("//div[@class='row']//div[@class='item-box']/a/@href")]  # 获取详情页url
        for url in detail_src:
            indexImg = detail_src.index(url)
            try:
                print("开始下载组图:", url)
                starttime = datetime.datetime.now()
                downloadImage(url, path)
                endtime = datetime.datetime.now()
                print("  下载成功，耗时：" + str(endtime - starttime))
                print("  =========> 第" + str(indexImg + 1) + "组图片下载完成 <=========")
            except Exception as e:
                print(e)
        print("===========================> 第" + str(n) +
              "个图片列表下载完成 <===========================")
    endTime = datetime.datetime.now()
    print("下载成功，耗时：：" + str(endTime - startTime))


if __name__ == '__main__':
    menu()  # 显示菜单
    main()
