import requests
import time

link_list = []
with open('alexa.txt', 'r') as f:
    file_list = f.readlines()
    for eachone in file_list:
        link = eachone.split('\t')[1]  # 以\t进行切割，列表类型取下标为1的元素
        link = link.replace('\n', '')  # 查找换行符替换为空字符
        link_list.append(link)

start = time.time()
for eachone in link_list:
    try:
        r = requests.get(eachone)
        print(r.status_code, eachone)
    except Exception as e:
        print('Error: ', e)
end = time.time()
print('串行的总时间为: ', end - start)
