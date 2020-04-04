# coding: utf8
import wx_spider

if __name__ == '__main__':

    gongzhonghao = input(u'input weixin gongzhonghao:')
    if not gongzhonghao:
        gongzhonghao = 'spider'
    text = " ".join(wx_spider.run(gongzhonghao))

    print(text)
