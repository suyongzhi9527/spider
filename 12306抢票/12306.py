import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class QiangPiao(object):
    def __init__(self):
        self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        self.search_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
        self.initmy_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self.passengers_url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
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

        # 再点击查询按钮之后，等待车次信息是否显示出来
        WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, ".//tbody[@id='queryLeftTable']/tr"))
        )

        # 找到所有没有datatran属性的tr标签，这些标签是存储了车次信息
        tr_list = self.driver.find_elements_by_xpath(".//tbody[@id='queryLeftTable']/tr[not(@datatran)]")

        # 遍历所有满足条件tr标签
        for tr in tr_list:
            tran_number = tr.find_element_by_class_name("number").text  # 获取车次
            print(tran_number)
            if tran_number in self.trains:
                left_ticket = tr.find_element_by_xpath(".//td[3]").text  # 二等座
                if left_ticket == "有" or left_ticket.isdigit:
                    orderBtn = tr.find_element_by_class_name("btn72")
                    orderBtn.click()

                    # 等待是否来到了确认乘客的页面
                    WebDriverWait(self.driver, 1000).until(
                        EC.url_to_be(self.passengers_url)
                    )
                    print("来到了确认页面")
                    normal_passenger = self.driver.find_elements_by_xpath('//ul[@id="normal_passenger_id"]')
                    for passenger in normal_passenger:
                        normalPassenger = passenger.find_element_by_tag_name('label')
                        print(normalPassenger)

    def run(self):
        self.write_input()
        self._login()
        self._order_ticket()


if __name__ == '__main__':
    spider = QiangPiao()
    spider.run()
