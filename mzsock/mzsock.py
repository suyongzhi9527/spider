import requests
import re
import os
from lxml import etree
from multiprocessing.dummy import Pool as Po


def get_html(url):
    """
    获取网页源码
    """
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


def get_url(url):
    """
    获取网站各个分类连接，名称
    """
    html = get_html(url)
    ehtml = etree.HTML(html)
    nurl = ehtml.xpath('//*[@id="chenxing_menu"]/li/a/@href')
    ntitle = ehtml.xpath('//*[@id="chenxing_menu"]/li/a/text()')
    urldata = list()
    for i in range(1, len(nurl) - 1):
        urldata.append(nurl[i] + '|' + ntitle[i])
    return urldata


def filter_name(Fname):
    """
    过滤特殊字符
    """
    rstr = r"[\/\\\:\*\?\"\<\>\|]"
    new_name = re.sub(rstr, '_', Fname)
    return new_name


def mkdir(path):
    """
    创建文件夹
    """
    path = path.strip()
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)


def get_data(ulist):
    """
    根据网站分类链接、名称进一步解析  这段代码是下载图片主体代码
    """
    url = ulist.split('|')[0]
    title = ulist.split('|')[1]
    html = get_html(url)
    ehtml = etree.HTML(html)
    # print(ehtml.xpath('//*[@class="more r"]/em/text()'))
    count = ''.join(ehtml.xpath('//*[@class="more r"]/em/text()'))
    page = int(count) // 20
    if int(count) % 20 > 0:
        page += 1
    for i in range(1, page + 1):  # 获取各分类下面所有图集链接
        nurl = url + 'page/' + str(i)
        html = get_html(nurl)
        ehtml = etree.HTML(html)
        lvurl = ehtml.xpath('//*[@class="img"]/@href')
        for j in lvurl:
            html = get_html(j)
            ehtml = etree.HTML(html)
            lvurl = ''.join(ehtml.xpath('//*[@id="imagecx"]/h1/span/text()')).strip()  # 获取图集页数
            title = ''.join(ehtml.xpath('//*[@id="imagecx"]/h1/text()')).strip()  # 获取图集名称
            title = title.replace('()', '').strip()
            lvurl = lvurl.replace('1/', '').strip()
            savepath = 'E:\\mzsock'  # 保存位置
            path = savepath + '\\' + title + '\\' + filter_name(title) + '\\'
            mkdir(path)
            # print(lvurl, title)
            try:
                for k in range(1, int(lvurl)):  # 获取每个图集页面的图片
                    zurl = j.replace('.html', '_' + str(k) + '.html')
                    html = get_html(zurl)
                    ehtml = etree.HTML(html)
                    picurl = ehtml.xpath('//*[@class="image_cx_cont"]/img/@src')
                    # print(picurl)
                    for l in picurl:
                        down_pic(l, path)  # 下载图片
            except Exception as e:
                print('报错跳过!', e)


def down_pic(url, path):
    """
    下载图片函数
    """
    picname = url.split('/')[-1]
    print('download: ' + url)
    picdata = requests.get(url)
    with open(path + picname, 'wb') as f:
        f.write(picdata.content)


if __name__ == '__main__':
    url = 'http://mzsock.com'
    urllist = get_url(url)
    pool = Po(4)
    results = pool.map(get_data, urllist)
    pool.close()
    pool.join()
    print('任务全部完成~！')
