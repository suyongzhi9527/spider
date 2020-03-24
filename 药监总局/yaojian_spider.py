import requests
import json
from pprint import pprint

if __name__ == '__main__':
    detali_data = list()
    for i in range(1, 3):
        url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
        detali_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
        form_data = {
            'on': 'true',
            'page': str(i),
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        response = requests.post(url, data=form_data)
        data = response.json()
        for i in data['list']:
            id = i['ID']
            detali_form_data = {
                'id': id
            }
            detali_res = requests.post(detali_url, data=detali_form_data)
            detali_data.append(detali_res.json())
    pprint(detali_data)
    print(len(detali_data))
