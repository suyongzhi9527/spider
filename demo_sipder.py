import xlwt  # 创建excel表格
import re  # 正则
import urllib.request  # 发送请求
import json



# 1.获取网页源码
def getData():  # 封装减少代码量
    for i in range(26700,26716):
        content_list = []
        url = 'http://www.risfond.com/case/fmcg/{}'.format(i)
        html_str = urllib.request.urlopen(url).read().decode("utf-8")  # urlopen()打开网页，read()读取源代码
        # print(html_str)
        # print(url)
        re1 = '<div class="sc_d_c">.*?<span class="sc_d_con">(.*?)</span></div>'
        result = re.findall(re1,html_str)
        print(result)
        content_list.append(result)
        # print(content_list)
    return content_list

def save_execl(content_list):
    newTable = 'work.xls' # 表格名称
    wb = xlwt.Workbook(encoding='utf-8') # 创建excel文件，设置编码
    ws = wb.add_sheet('rsfd') # 表名
    headData = ['职位名称','职位地点','时间','行业','招聘时间','人数','顾问']
    for col in range(0,7):
        ws.write(0,col,headData[col],xlwt.easyxf('font:bold on'))
    index = 1
    for j in range(0,len(content_list)): # 计算数据有多少
        for i in range(0,7):
            ws.write(index,i,content_list[j]) # 行数 列数 数据
        index += 1
    wb.save(newTable)

def save_txt(content_list):
    with open('1.txt','a') as f:
        for content in content_list:
            f.write(json.dumps(content,ensure_ascii=False,indent=2))
            f.write('\n')


if __name__ == "__main__":
   content_list =  getData()
#    save_execl(content_list)
#    save_txt(content_list)

