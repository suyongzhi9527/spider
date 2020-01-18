from bs4 import BeautifulSoup

html_str = """
<div class="fr grid-w730">
    <ul class="list-jobs clearfix">
        <li class="item-small">
            <div class="pic"><a target="_blank" href="http://www.haolietou.com/c_1435"><img
                        src="/data/logo/2015/04/22/335950.jpg"></a></div>
            <div class="info">
                <div class="title"><a href="http://www.haolietou.com/j_145995" target="_blank">美国移民顾问</a></div>
                <p><em class="orange">30-35万</em>北京</p>
                <p class="gray">北京盛同华远房地产投资有限公司</p>
            </div>
        </li>
        <li class="item-small">
            <div class="pic"><a target="_blank" href="http://www.haolietou.com/c_1431"><img
                        src="/data/logo/2015/04/22/335946.png"></a></div>
            <div class="info">
                <div class="title"><a href="http://www.haolietou.com/j_145938" target="_blank">技术总监</a></div>
                <p><em class="orange">30-40万</em>北京</p>
                <p class="gray">北京恒信彩虹信息技术有限公司</p>
            </div>
        </li>
        <li class="item-small">
            <div class="pic"><a target="_blank" href="http://www.haolietou.com/c_1511"><img
                        src="/data/logo/2015/04/22/336026.png"></a></div>
            <div class="info">
                <div class="title"><a href="http://www.haolietou.com/j_146229" target="_blank">数据挖掘/算法/nlp/机器学习</a>
                </div>
                <p><em class="orange">30-60万</em>北京</p>
                <p class="gray">上海晶赞科技发展有限公司</p>
            </div>
        </li>
        <li class="item-small" id="item">
            <div class="pic"><a target="_blank" href="http://www.haolietou.com/c_1591"><img
                        src="/data/logo/2015/04/22/336106.png"></a></div>
            <div class="info">
                <div class="title"><a href="http://www.haolietou.com/j_146539" target="_blank">物流总监</a></div>
                <p><em class="orange">30-50万</em>广州</p>
                <p class="gray">广东绿瘦健康信息咨询有限公司</p>
            </div>
        </li>
        <li class="item-small">
            <div class="pic"><a target="_blank" href="http://www.haolietou.com/c_1543"><img
                        src="/data/logo/2015/04/22/336058.png"></a></div>
            <div class="info">
                <div class="title"><a href="http://www.haolietou.com/j_146442" target="_blank">大企业客户部高级销售经理</a></div>
                <p><em class="orange">50-80万</em>北京</p>
                <p class="gray">浪潮电子信息产业股份有限公司</p>
            </div>
        </li>
        <li class="item-small">
            <div class="pic"><a target="_blank" href="http://www.haolietou.com/c_1407"><img
                        src="/data/logo/2015/04/22/335921.png"></a></div>
            <div class="info">
                <div class="title"><a href="http://www.haolietou.com/j_145780" target="_blank">经营分析中心总经理（电商或零售行业经验）</a>
                </div>
                <p><em class="orange">30-80万</em>北京</p>
                <p class="gray">北京惠买在线网络科技有限公司</p>
            </div>
        </li>
    </ul>
</div>
"""

soup = BeautifulSoup(html_str, 'lxml')
print(type(soup))
# table = soup.find("div")
# print(type(table))
# print(soup.prettify())  # 美化格式输出

# lis = soup.find_all("li") # 查找获取所有的li标签
# for li in lis:
#     print(li)

# lis = soup.find_all("li",limit=2)[1] # 列表类型
# print(lis)

# p = soup.find_all("p", class_="gray")
# p = soup.find_all("p", attrs={'class':'gray'})
# for i in p:
#     print(i)
#     print("-"*30)

# lis = soup.find_all("li",id = "item",class_ = "item-small")
# lis = soup.find_all("li",attrs={"id":"item","class":"item-small"})
# for li in lis:
#     print(li)

# aList = soup.find_all("a")
# for a in aList:
#     # 1.通过下标获取元素属性
#     # url = a['href']
#     # print(url)
#     # 2.通过attrs属性方式
#     url = a.attrs['href']
#     print(url)

# lis = soup.find_all("li")
# job_list = []
# for li in lis:
#     item = {}
# a = li.find_all("a")
# title = a[1].string
# pic = a[0]['href']
# em = li.find_all("em")
# salary = em[0].string
# p = li.find_all("p")
# company = p[1].string
# address = p[0].text[6:]
# item['title'] = title
# item['pic'] = pic
# item['salary'] = salary
# item['company'] = company
# item['address'] = address
# job_list.append(item)
# infos = list(li.strings) # 这个方法不完美，会把空格换行等字符输出
#     infos = list(li.stripped_strings)  # 自动去除换行空格字符
#     item['职位'] = infos[0]
#     item['年薪'] = infos[1]
#     item['工作地点'] = infos[2]
#     item['公司'] = infos[3]
#     job_list.append(item)
# print(job_list)

# lis = soup.select("li")
# for li in lis:
#     print(li)
#     print("*"*30)

# lis = soup.select("li")[1]
# print(lis)

# p = soup.select("p.gray")
# print(p)

# a = soup.select("a")
# for i in a:
#     href = i['href']
#     print(href)

# lis = soup.select("li")
# for li in lis:
#     infos = list(li.stripped_strings)
#     print(infos)
