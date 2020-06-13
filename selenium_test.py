# from selenium import webdriver
import requests

# url = "http://www.dianping.com/shop/121937518"

# driver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe")
# driver.get(url)
headers = {
    'Host': 'i.meituan.com',
    'Cookie': 'iuuid=AEEAD89496FD0B29DC7BD12C385220B625AD11A65B04922A85C23E046668E0FF; _lxsdk_cuid=1723a0c4beac8-02a09608215e9a-5f472815-1fa400-1723a0c4bebc8; _lxsdk=AEEAD89496FD0B29DC7BD12C385220B625AD11A65B04922A85C23E046668E0FF; uuid=65701e4826f9489e9592.1591756806.1.0.0; rvct=1; JSESSIONID=sc45maum477sumtwuc5vgs9f; IJSESSIONID=sc45maum477sumtwuc5vgs9f; idau=1; webloc_geo=22.600454%2C114.049087%2Cwgs84%2C-1; __utma=74597006.1081559293.1591757646.1591757646.1591757646.1; __utmc=74597006; __utmz=74597006.1591757646.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ci3=1; latlng=22.600454,114.049087,1591757683999; ci=30; cityname=%E6%B7%B1%E5%9C%B3; __mta=44462619.1591757683827.1591757683827.1591757690532.2; i_extend=H__a100005__b1; _lxsdk_s=1729c196928-d8c-3bb-289%7C%7C76; webp=1; __utmb=74597006.8.9.1591757786586',
    'Referer': 'http://i.meituan.com/s/-%E7%81%AB%E9%94%85/?p=2',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'X-Requested-With': 'XMLHttpRequest'
}
resp = requests.get(
    "http://i.meituan.com/s/a?cid=-1&bid=-1&sid=defaults&p=2&ciid=30&bizType=area&csp=&nocount=true&stid_b=_b2&w=%E7%81%AB%E9%94%85",
    headers=headers)
print(resp.text)
