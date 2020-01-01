from lxml import etree
import json

"""
什么是XPath?
是一门在XML和HTML文档中查找信息的语言，可用来在XML和HTML文档中对元素和属性进行遍历

选择节点：
nodename 选取此节点所有节点
/   选取当前节点下面的子节点
//  从全局节点中选择节点，任意位置
@   选取某个节点的属性

通配符:
*   匹配任意节点
@*  匹配节点中任意属性

"""

# html_str = """
# <div>
#     <ul>
#         <li>aaaa</li>
#         <li>bbbb</li>
#         <li>cccc</li>
#         <li>dddd</li>
#         <li>ffff</li>
#     </ul>
# </div>
# """
# htmlElement = etree.HTML(html_str)
# print(type(htmlElement)) # 元素对象
# print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8')) # 自动补全 

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('lietou.html',parser=parser)

offers_list = []
div_list = html.xpath("//ul[@class='list-jobs clearfix']/li")
for div in div_list:
    title = div.xpath(".//div[@class='title']/a/text()")[0] if len(div.xpath(".//div[@class='title']/a/text()")) > 0 else None
    salary = div.xpath(".//em[@class='orange']/text()")[0] if len(div.xpath(".//em[@class='orange']/text()")) > 0 else None
    address = div.xpath(".//p[1]/text()")[0] if len(div.xpath(".//p[1]/text()")) > 0 else None
    company = div.xpath(".//p[2]/text()")[0] if len(div.xpath(".//p[2]/text()")) > 0 else None
    
    Job_Offers = {
        'title':title,
        'salary':salary,
        'address':address,
        'company':company
    }
    offers_list.append(Job_Offers)

    with open('list.json','w',encoding='utf-8') as f:
        for offers in offers_list:
            f.write(json.dumps(offers,ensure_ascii=False,indent=2))
    
