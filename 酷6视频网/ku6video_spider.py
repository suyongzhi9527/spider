import requests
import json

# 爬虫一般思路
# 1. 确定爬取的url路径，headers参数
for i in range(0,2):
    print("====================正在爬取第{}页的视频数据====================".format(i + 1))
    url = 'https://www.ku6.com/video/feed?pageNo={}&pageSize=40&subjectId=76'.format(i)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    }
    # 2. 发送请求 --requests，模拟浏览器发送请求，获取响应内容
    response = requests.get(url,headers=headers)
    text = response.text
    # 3.解释数据 -- json模块，把json字符串转换成Python的数据类型
    # 3.1 数据转换
    json_data = json.loads(text) # 字典
    # 3.2 解释数据
    data_list = json_data['data'] # 列表

    for data in data_list:
        video_title = data['title'] + '.mp4'
        video_url = data['playUrl']

        # 再次请求数据，获取视频数据
        print("正在下载:",video_title)
        video_data = requests.get(video_url,headers=headers).content

        # 4.保存视频数据
        with open(r'video/' + video_title, 'wb') as f:
            f.write(video_data)
            print("下载完成:",video_title)
        

