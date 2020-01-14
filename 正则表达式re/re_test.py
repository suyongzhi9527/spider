import re

# 1.匹配某个字符串
# text = 'hello'
# ret = re.match('he',text)
# print(ret.group())

# 2.点. 匹配任意字符
# text = 'ahello'
# ret = re.match('.',text)
# print(ret.group())

# 3.\d,匹配任意的数字
# text = '123hello'
# ret = re.match('\d+',text)
# print(ret.group())

# 4.\D,匹配任意非数字
# text = 'hello'
# ret = re.match('\D',text)
# print(ret.group())

# 5.\s,匹配空白字符(\n,\t,\r,空格)
# text = ' '
# ret = re.match('\s',text)
# print(ret.group())

# 6.\w,匹配a-z,A-Z,数字和下划线
# text = 'aaa'
# ret = re.match('\w',text)
# print(ret.group())

# 7.\W,与\w相反
# text = '+'
# ret = re.match('\W',text)
# print(ret.group())

# 8.[]组合方式，只要满足中括号中的字符，就可以匹配
# text = '0668-112356'
# ret = re.match('[\d\-]+',text)
# print(ret.group())

# # 8.1 中括号的形式代替\d
# text = '06'
# ret = re.match('[0-9]',text)
# print(ret.group())

# # 8.2 中括号的形式代替\D
# text = '06'
# ret = re.match('[^0-9]',text)
# print(ret.group())

# 8.3 中括号的形式代替\w
# text = 'z'
# ret = re.match('[a-zA-Z0-9]',text)
# print(ret.group())

# 8.4 中括号的形式代替\W
# text = '+-='
# ret = re.match('[^a-zA-Z0-9]',text)
# print(ret.group())

#####匹配多个字符#####

# 9.*:匹配0或者任意多个字符
# text = '123abcd232'
# ret = re.match('\d*',text)
# print(ret.group())

# # 10.+:匹配1或者多个字符
# text = 'abcd'
# ret = re.match('\w+',text)
# print(ret.group())

# 11.?:匹配0或者1个字符
# text = 'abcd'
# ret = re.match('\w?',text)
# print(ret.group())

# # 12.{m}:匹配m个字符
# text = 'abcd'
# ret = re.match('\w{2}',text)
# print(ret.group())

# 13.{m,n}:匹配m-n个字符
# text = 'abcd'
# ret = re.match('\w{1,4}',text)
# print(ret.group())

#########小案例#########
# 14.验证手机号码
# text = '15219740694'
# ret = re.match('1[3578]\d{9}',text)
# print(ret.group())

# 15.验证邮箱
# text = '1125699801@qq.com'
# ret = re.match('\w+@[a-z0-9]+\.[a-z]+',text)
# print(ret.group())

# 16.验证url
# text = 'https://www.baidu.com'
# ret = re.match('(http|https|fpt)://[^\s]+',text)
# print(ret.group())

# 17.验证url
# text = '440982199711082839'
# ret = re.match('\d{17}[\dxX]',text)
# print(ret.group())

# 匹配1-100之间的数字
# text = '1001'
# ret = re.match('[1-9]\d?$|100$',text)
# print(ret.group())

# group分组
# text = 'apple price is $999,orange price is $666'
# ret = re.search('.*(\$\d+).*(\$\d+)',text)
# print(ret.group(1,2)) #元祖类型
# print(ret.groups())

# findall函数
# text = 'apple price is $999,orange price is $666'
# ret = re.findall('\$\d+',text)
# print(ret) #元祖类型

# sub函数
# text = 'apple price is $999,orange price is $666'
# ret = re.sub('\$\d+','0',text)
# print(ret) #元祖类型

# html = """
# <div class="job-detail">
#         <p>岗位职责</p>
# <p>1、负责设计和开发分布式网络爬虫系统；</p>
# <p>2、解决技术疑难问题，包括反爬、压力控制，提升网页抓取的效率和质量；</p>
# <p>3、参与系统框架优化、性能优化、系统重构等工作；</p>
# <p>4、研究各种网站、链接的形态，发现它们的特点和规律。</p>
# <p><br></p>
# <p>任职要求</p>
# <p>1、计算机及相关专业，本科以上学历，2年以上爬虫开发经验；</p>
# <p>2、精通python、计算机网络，熟练使用多线程，熟悉Scrapy等常用爬虫框架；</p>
# <p>3、熟悉Linux操作、正则表达式，MySQL、MongoDB等常用数据库，了解各种Web前端技术；</p>
# <p>4、能够解决封账号、封IP、验证码识别、图像识别等问题；</p>
# <p>5、具有良好的沟通能力和团队合作意识，有数据分析、文本分析背景者优先。</p>
#         </div>
# """
# ret = re.sub("<.+?>","",html)
# print(ret)

# split函数
# text = 'apple-is-good'
# ret = re.split('-', text)
# print(ret)  # 列表类型

# compile函数
text = 'the number is 20.50'
# r = re.compile('\d+\.?\d+')
r = re.compile("""
    \d+ # 小数点前面的数字
    \.? # 小数点本身
    \d+ # 小数点后面的数字
""",re.VERBOSE)
ret = re.search(r,text)
print(ret.group())