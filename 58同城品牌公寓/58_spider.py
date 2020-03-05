from bs4 import BeautifulSoup
import requests
import csv
import time
import lxml

url = 'https://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

page = 0

csv_file = open('rent.csv', 'w', newline="")
csv_writer = csv.writer(csv_file, delimiter=',')

while True:
    page += 1
    print("fetch:", url.format(page=page))
    time.sleep(1)
    response = requests.get(url.format(page=page), headers=headers)
    html = BeautifulSoup(response.text, features="lxml")
    house_list = html.select('.list > li')
    if not house_list:
        break

    for house in house_list:
        house_title = house.select('h2')[0].string.strip()
        house_url = house.select('a')[0]['href']
        house_info_list = house_title.split()

        if '公寓' in house_info_list[1] or '青年公寓' in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]

    house_money = house.select(".money")[0].select("b")[0].string
    csv_writer.writerow([house_title, house_location, house_money, house_url])

csv_file.close()
