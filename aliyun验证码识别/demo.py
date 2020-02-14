import requests
from urllib import request
from base64 import b64encode

# captcha_url = 'https://passport.qyer.com/qcross/passport/captcha?scene=mobile_register_sms'
#
# request.urlretrieve(captcha_url, 'captcha.png')
# with open('captcha.png', 'rb') as f:
#     img = f.read()
#     data = b64encode(img)
#     print(data)


recognize_url = 'http://imgurlocr.market.alicloudapi.com/urlimages'

formdata = {}

formdata['image'] = 'https://passport.qyer.com/qcross/passport/captcha?scene=mobile_register_sms&timer=1581603591701'

appcode = '6853ea9b54564233915676ca869a8cdd'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Authorization': 'APPCODE ' + appcode
}
resp = requests.post(recognize_url, headers=headers, data=formdata)
print(resp.text)
