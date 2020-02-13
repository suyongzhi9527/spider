from typing import List, Any

import xlwt
import re
from urllib import request


def getdata():
    url_list = []
    for i in range(47501, 47521):
        url = 'http://www.risfond.com/case/fmcg/{}'.format(i)
        html = request.urlopen(url).read().decode('utf-8')

        page_list = re.findall(r'<div class="sc_d_c">.*?<span class="sc_d_con">(.*?)</span></div>', html)
        print(page_list)
        url_list.append(page_list)
    return url_list


def execl_write(items):
    newtable = 'text2020.xls'  # 表格名称
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')

    headData = ['职位名称', '职位地点', '时间', '行业', '招聘时间', '人数', '顾问']
    for colnum in range(0, 7):
        ws.write(0, colnum, headData[colnum], xlwt.easyxf('font:bold on'))
    index = 1
    for j in range(0, len(items)):
        for i in range(0, 7):
            ws.write(index, i, items[j][i])
        index += 1

    wb.save(newtable)


items = getdata()
execl_write(items)
