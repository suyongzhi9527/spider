from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class QiangPiao(object):
    def __init__(self):
        self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        self.search_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
        self.initmy_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self.driver = webdriver.Chrome(executable_path='F:\chromedriver_win32\chromedriver.exe')

    def write_input(self):
        self.from_station = input('出发地:')
        self.to_station = input('目的地:')
        self.depart_time = input('出发时间:')
        self.passengers = input('乘客姓名(多个以英文逗号隔开):').split(',')
        self.trains = input('车次(多个以英文逗号隔开):').split(',')

    def _login(self):
        self.driver.get(self.login_url)
        WebDriverWait(self.driver, 1000).until(
            EC.url_to_be(self.initmy_url)
        )
        print('登录成功!')

    def _order_ticket(self):
        # 跳转到查余票的界面
        self.driver.get(self.search_url)
        # 等待出发地是否输入正确
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "fromStationText"), self.from_station)
        )
        # 等待目的地是否输入正确
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "toStationText"), self.to_station)
        )
        # 等待出发时间是否输入正确
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "train_date"), self.depart_time)
        )
        # 等待查询按钮是否可用
        WebDriverWait(self.driver, 1000).until(
            EC.element_to_be_clickable((By.ID, "query_ticket"))
        )
        # 如果可以点击,那就找到按钮执行点击事件
        search_btn = self.driver.find_element_by_id("query_ticket")
        search_btn.click()

    def run(self):
        self.write_input()
        self._login()
        self._order_ticket()


if __name__ == '__main__':
    spider = QiangPiao()
    spider.run()
