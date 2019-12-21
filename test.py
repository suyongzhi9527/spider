from lxml import etree
import requests

url = 'https://tieba.baidu.com/mo/q---771EA4758368849F1B99568B4C102059:FG=1-sz@320_240,,-2-3-0--2/m?kw=python&pn=0&'
res = requests.get(url)
html_str = res.content.decode()

html = etree.HTML(html_str)

li_list = html.xpath("//li[contains(@class,'tl_shadow tl_shadow_new')]")
for li in li_list:
    item = {}
    item['title'] = li.xpath(".//div[@class='ti_title']/span/text()")
    print(item)
