import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree


class BossSpider(object):
    driver_path = r'F:\chromedriver_win32\chromedriver.exe'
    c_options = Options()
    c_options.add_argument('--headless')

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path, chrome_options=self.c_options)
        self.url = 'https://www.zhipin.com/'

    def run(self):
        self.driver.get(self.url)
        source = self.driver.page_source
        # print(source)
        self.parse_list_page(source)
        time.sleep(1)

    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath('//ul[@class="cur"]//a[@class="job-info"]/@href')
        for link in links:
            link = 'https://www.zhipin.com/' + link
            self.request_detail_page(link)
            time.sleep(1)

    def request_detail_page(self, url):
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        source = self.driver.page_source
        self.parse_detail_page(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        name = html.xpath('//div[@class="name"]/h1/text()')[0]
        company_name = html.xpath('//div[@class="job-sec"]//div[@class="name"]/text()')[0]
        salary = html.xpath('//div[@class="name"]//span/text()')[0].strip()
        desc = "".join(html.xpath('//div[@class="job-sec"]//div[@class="text"]//text()')).strip()
        postion = {
            'name': name,
            'company': company_name,
            'salary': salary,
            'desc': desc
        }
        print(postion)
        print('*' * 50)


if __name__ == '__main__':
    boss = BossSpider()
    boss.run()
