import csv

# 将数据写入csv
# with open("data.csv","w") as f:
#     witer = csv.writer(f,delimiter = '*') # 传入文件句柄
#     witer.writerow(['id','name','age'])
#     witer.writerow(['1001','aa','20'])
#     witer.writerow(['1002','bb','25'])
#     witer.writerow(['1003','cc','24'])

# 元祖方式写入
# headers = ['username','age','height']
# values = [
#     ('张三',18,160),
#     ('小三',30,140),
#     ('张四',23,170),
# ]
# with open("data.csv","w",encoding="utf-8",newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(headers)
#     writer.writerows(values)

# 字典方式写入
# with open('data.csv','w') as f:
#     fielnames = ['id','name','age'] # 定义字典里的key
#     writer = csv.DictWriter(f,fieldnames = fielnames)
#     writer.writeheader() # 写入表头数据调用这个方法
#     writer.writerow({'id':'1001','name':'aaa','age':'20'})
#     writer.writerow({'id':'1002','name':'bbb','age':'20'})
#     writer.writerow({'id':'1003','name':'ccc','age':'20'})

with open("data.csv","w",encoding="utf-8-sig",newline="") as f:
    headers = ['name','age','height']
    item = [
        {
            'name':'张三',
            'age':24,
            'height':150
        },
        {
            'name':'张四',
            'age':25,
            'height':124
        },
        {
            'name':'张五',
            'age':26,
            'height':456
        }
    ]
    writer = csv.DictWriter(f,headers)
    writer.writeheader()
    writer.writerows(item)



# 本地读取csv文件
# with open("data.csv","r") as f:
#     data = csv.reader(f)
#     for i in data:
#         name = i[1]
#         age = i[-1]
#         print(name,age)

# with open("data.csv","r") as f:
#     data = csv.DictReader(f)
#     for x in data:
#         value = {'name':x['name'],'age':x['age']}
#         print(value)