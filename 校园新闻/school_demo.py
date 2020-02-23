import requests
import nobug
import urllib3
from nobug import buddha


class Hebei(object):
    def __init__(self):
        self.url = 'https://www.hbfu.edu.cn/news/queryListForPage'
        self.detail_url = 'https://www.hbfu.edu.cn/news/findById'
        self.f = open('school_news.txt', 'w')

    # 获取数据
    def get_data(self, data):
        self.html = requests.request('POST', self.url, data=data, verify=False)
        iDdata = []
        for i in range(len(self.html.json()['rows'])):
            # print(self.html.json()['rows'][i]['id'])
            iDdata.append(self.html.json()['rows'][i]['id'])

        # print(iDdata)
        for n in iDdata:
            dataPage = {
                'id': n
            }
            self.detail_html = requests.post(self.detail_url, data=dataPage, verify=False)
            # print(self.detail_html.json()['title'])
            titles = self.detail_html.json()['title']
            contents = self.detail_html.json()['content']
            self.f_write(titles, contents)

    def f_write(self, titles, contents):
        self.f.write(titles + '\n' * 2)
        self.f.write(contents)

    def f_close(self):
        self.f.close()


if __name__ == '__main__':
    school = Hebei()
    urllib3.disable_warnings()
    for i in range(0, 40, 20):
        data = {
            'start': i,
            'limit': 20,
            'type': 1
        }
        school.get_data(data)
    school.f_close()
    nobug
