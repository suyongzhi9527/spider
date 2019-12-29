import requests
import json

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'Origin':'https://www.lagou.com'
}

urls = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
s = requests.Session()
s.get(urls,headers = headers,timeout = 3)
cookie = s.cookies

resp = requests.post(url,data=data,headers=headers,cookies=cookie)
dict_list = resp.json()
job_json = dict_list['content']['positionResult']['result']
with open('lagou_job.json','w',encoding='utf-8') as f:
    f.write(json.dumps(job_json,ensure_ascii=False,indent=2))