from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import time


class LagouSpider(object):
    driver_path = r'F:\chromedriver_win32\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?labelWords=sug&fromSearch=true&suginput=Python'
        self.postions = []

    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="pager_container"]/span[last()]'))
            )
            self.parse_list_page(source)
            try:
                next_btn = self.driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')
                if "pager_next pager_next_disabled" in next_btn.get_attribute('class'):
                    break
                else:
                    next_btn.click()
            except:
                print(source)
            time.sleep(2)

    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath('//a[@class="position_link"]/@href')
        for link in links:
            self.request_detail_page(link)
            time.sleep(2)

    def request_detail_page(self, url):
        # self.driver.get(url)
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="job-name"]'))
        )
        source = self.driver.page_source
        self.parse_detail_page(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        postion_name = html.xpath('//div[@class="job-name"]/@title')[0]  # 职位
        job_requets_spans = html.xpath('//dd[@class="job_request"]//span/text()')
        salary = job_requets_spans[0].strip()  # 薪资
        city = job_requets_spans[1]  # 城市
        city = re.sub(r'[\s/]', '', city)
        work_years = job_requets_spans[2].strip()  # 工作年限
        work_years = re.sub(r'[\s/]', '', work_years)
        education = job_requets_spans[3].strip()  # 学历要求
        education = re.sub(r'[\s/]', '', education)
        desc = "".join(html.xpath('//dd[@class="job_bt"]//text()')).strip()  # 职位详情
        company_name = html.xpath('//h3[@class="fl"]/em/text()')[0].strip()  # 公司
        postion = {
            'name': postion_name,
            'company': company_name,
            'salary': salary,
            'city': city,
            'work_year': work_years,
            'education': education,
            'desc': desc
        }
        self.postions.append(postion)
        print(postion)
        print('*' * 40)


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()
