import requests

page = 1
while True:
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '广州',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }
    response = requests.post(url, data=data)
    print(response.json())
    if response.json().get('Table1', ''):
        page += 1
    else:
        break
