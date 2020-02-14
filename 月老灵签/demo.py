import time
import requests

BIRTH = input("请输入出生年月日:")
FIRST_NAME = input("姓氏:")
GENDER = input("性别:")
LAST_NAME = input("名字:")

# querys = 'BIRTH=%s&FIRST_NAME=%s&GENDER=%s&LAST_NAME=%s' % (BIRTH, FIRST_NAME, GENDER, LAST_NAME)
url = 'http://yllq.market.alicloudapi.com/ai_metaphysics/yue_lao_lin_qian/elite'
appcode = '6853ea9b54564233915676ca869a8cdd'
UUID = str(time.time())
headers = {
    'Authorization': 'APPCODE ' + appcode,
    'X-Ca-Nonce': UUID,
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
data = {
    'BIRTH': BIRTH,
    'FIRST_NAME': FIRST_NAME,
    'GENDER': GENDER,
    'LAST_NAME': LAST_NAME
}
#
resp = requests.get(url, headers=headers, data=data)
print(resp.url)
result = resp.json()
item = {
    '名字': result['FIRT_NAME'] + result['LAST_NAME'],
    '性别': result['GENDER'],
    '生日': result['BIRTH'],
    '农历年份': result['YEAR'],
    '农历月份': result['MONTH'],
    '农历日期': result['DAY'],
    '农历时辰': result['HOUR'],
    '属相': result['ANIMAL'],
    '签名称': result['SIGN_NAME'],
    '签号': result['SIGN_ID'],
    '签类型': result['SIGN_TYPE'],
    '签标题': result['SIGN_TITLE'],
    '签诗': result['SIGN_INTRO'],
    '签诗注解': result['SIGN_INTRO'],
    "属性实体信息": {  # 签属性实体信息
        "事业注解": result['SIGN_ENTITY']['SIGN_CAREER'],  # 签实体_事业注解
        "家庭注解": result['SIGN_ENTITY']['SIGN_FAMILY'],  # 签实体_家庭注解
        "情感注解": result['SIGN_ENTITY']['SIGN_EMOTION'],  # 签实体_情感注解
        "学业注解": result['SIGN_ENTITY']['SIGN_ACADEMIC'],  # 签实体_学业注解
        "投资注解": result['SIGN_ENTITY']['SIGN_INVEST'],  # 签实体_投资注解
        "健康注解": result['SIGN_ENTITY']['SIGN_HEALTH'],  # 签实体_健康注解
        "转换注解": result['SIGN_ENTITY']['SIGN_SWITCH'],  # 签实体_转换注解
        "官司注解": result['SIGN_ENTITY']['SIGN_LAWSUIT'],  # 签实体_官司注解
        "寻物注解": result['SIGN_ENTITY']['SIGN_LOST'],  # 签实体_寻物注解
        "出行注解": result['SIGN_ENTITY']['SIGN_TRAVEL'],  # 签实体_出行注解
        "求子注解": result['SIGN_ENTITY']['SIGN_CHILD']  # 签实体_求子注解
    }
}

print(item)
