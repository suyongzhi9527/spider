from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree
import time
import random
import csv


class SpiderAll(object):
    # 设置构造器
    def __init__(self, url):
        self.url = url
        self.spider(url)

    def spider(self, url):
        # 创建浏览器对象
        browser = webdriver.Chrome("E:\chromedriver_win32\chromedriver.exe")
        # 打开地址
        browser.get(url)
        # 窗口最大化
        # browser.maximize_window()

        # 打开一个csv文件
        fo = open("湖人数据文件.csv", 'a', encoding="utf-8")
        out = csv.writer(fo)
        out.writerow(
            ["对阵球队", "詹姆斯", "布拉德利", "波谱", "霍华德", "戴维斯", "格林", "卡鲁索", "首发得分", "替补得分", "对阵球队", "对方主力得分", "对方替补得分", "胜负"])
        fo.flush()
        fo.close()  # 关闭输入流

        for i in range(1, 80):
            try:
                # 先找到数据中心
                data_center = browser.find_element_by_xpath('//table/tbody/tr[@class="left"][' + str(i) + ']/td[5]/a')
                # 开赛时间
                sdate = browser.find_element_by_xpath('//table/tbody/tr[@class="left"][' + str(i) + ']/td[4]').text
                # 胜负
                shengfu = browser.find_element_by_xpath('//table/tbody/tr[@class="left"][' + str(i) + ']/td[3]').text
                # 对阵球队
                qiudui = browser.find_element_by_xpath('//table/tbody/tr[@class="left"][' + str(i) + ']/td[1]').text
                ActionChains(browser).click(data_center).perform()  # 单击数据中心
                all_window_handle = browser.window_handles
                browser.switch_to.window(all_window_handle[1])  # 切换到最新的窗口
                # 先找到湖人是主队还是客队  湖人 vs 勇士  左边客队 右边主队  客队在列表中是排在上面  主队排列在下面  J_home_content  J_away_content 客队
                arr = qiudui.split(" vs ")
                tdetail = {}  # 这里的格式是  球员名字:得分_正负值       球队:{球员名:得分_正负值_是否主力}
                # 用来存首发得分和替补得分
                cun_score = {}
                l = 0
                for k in ["J_away_content", "J_home_content"]:
                    n = 0
                    if k == "J_away_content":
                        tdetail.setdefault(arr[0], {})
                        l = 0
                    else:
                        tdetail.setdefault(arr[1], {})
                        l = 1
                    for j in range(2, 15):
                        laker_name = browser.find_element_by_xpath(
                            '//table[@id="' + k + '"]/tbody/tr[' + str(j) + ']/td[1]').text
                        laker_score = browser.find_element_by_xpath(
                            '//table[@id="' + k + '"]/tbody/tr[' + str(j) + ']/td[15]').text
                        laker_xiaoliu = browser.find_element_by_xpath(
                            '//table[@id="' + k + '"]/tbody/tr[' + str(j) + ']/td[16]').text
                        detail = None
                        list_t = ["首发", "替补"]
                        if n == 0:
                            if laker_name not in list_t:
                                detail = laker_score + "_" + laker_xiaoliu + "_首发"
                            else:
                                n = 1
                        else:
                            detail = laker_score + "_" + laker_xiaoliu + "_替补"
                        tdetail[arr[l]][laker_name] = detail
                print(tdetail)
                for (team, list_data) in tdetail.items():
                    cun_score.setdefault(team, {})
                    # 首发分数
                    first_score = 0
                    # 替补分数
                    Substitute_score = 0
                    for (name, str_data) in list_data.items():
                        # 定义计算首发得分和替补得分
                        if str_data != None:
                            # 开始计算首发得分和替补得分
                            if str_data.split("_")[2] == "首发":
                                first_score = first_score + int(str_data.split("_")[0])
                            else:
                                Substitute_score = Substitute_score + int(str_data.split("_")[0])
                    cun_score[team]["首发"] = first_score
                    cun_score[team]["替补"] = Substitute_score
                print(cun_score)
                earm = None
                for m in range(0, 2):
                    print("看这里", arr[m])
                    if arr[m] != "湖人":
                        earm = arr[m]
                    # 开始存数据
                fo = open("湖人数据文件.csv", 'a', encoding="utf-8")
                out = csv.writer(fo)
                print(earm)
                print(tdetail.get("湖人").get("勒布朗-詹姆斯"), type(tdetail.get("湖人").get("勒布朗-詹姆斯")), earm,
                      cun_score.get(earm).get("主力"))
                l = ([qiudui, tdetail.get("湖人").get("勒布朗-詹姆斯"), tdetail.get("湖人").get("埃弗里-布拉德利"),
                      tdetail.get("湖人").get("肯塔维厄斯-考德威尔-波普"), tdetail.get("湖人").get("德怀特-霍华德"),
                      tdetail.get("湖人").get("安东尼-戴维斯"), tdetail.get("湖人").get("丹尼-格林"),
                      tdetail.get("湖人").get("亚历克斯-卡鲁索"), cun_score.get("湖人").get("首发"), cun_score.get("湖人").get("替补"),
                      cun_score.get(earm).get("首发"), cun_score.get(earm).get("替补"), shengfu])
                # out.writerow(["对阵球队","詹姆斯","布拉德利","波谱","霍华德","戴维斯","格林","卡鲁索","首发得分","替补得分","三分命中率","罚球命中率","对阵球队","对方主力得分","对方替补得分","胜负"])
                out.writerow(l)  # 写入数据
                fo.flush()
                fo.close()
            except Exception as e:
                print(e, "这里错误了!")
            # 切换窗口
            browser.close()
            all_window_handle = browser.window_handles
            browser.switch_to.window(all_window_handle[0])  # 切换到最新的窗口
            time.sleep(1)


if __name__ == '__main__':
    url = 'https://nba.hupu.com/schedule/lakers'
    spider = SpiderAll(url)
