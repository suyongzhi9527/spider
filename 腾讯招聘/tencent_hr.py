import requests
import json


headers = {
    'referer': 'https://careers.tencent.com/search.html?query=ci_5&index=1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

def parse(url):
    resp = requests.get(url,headers=headers)
    html_str = resp.json()
    job_lists = html_str['Data']['Posts']
    job_list = []
    for job in job_lists:
        job_item = {}
        job_item['title'] = job['RecruitPostName']
        job_item['CountryName'] = job['CountryName']
        job_item['LocationName'] = job['LocationName']
        job_item['CategoryName'] = job['CategoryName']
        job_item['Responsibility'] = job['Responsibility'].replace("\n","")
        job_item['LastUpdateTime'] = job['LastUpdateTime']
        job_list.append(job_item)
    return job_list

def save_content(job_list):
    with open('job.josn','a',encoding='utf-8') as f:
        for job in job_list:
            f.write(json.dumps(job,ensure_ascii=False,indent=2))

def run():
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1577878865960&countryId=&cityId=5&pageIndex={}&pageSize=10'
    for i in range(1,19):
        urls = url.format(i)
        job_list = parse(urls)
        print(job_list)
        print('*'*30)
        save_content(job_list)


if __name__ == "__main__":
    run()
        