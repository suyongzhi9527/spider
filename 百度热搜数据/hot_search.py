import time
import pymysql
import traceback
from selenium import webdriver
from selenium.webdriver import ChromeOptions


def get_conn():
    """
    :return 连接，游标
    """
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        database='cov',
        port=3306
    )
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def get_baidu_hot():
    """
    爬取百度热搜数据
    """
    opt = ChromeOptions()
    opt.add_argument("--headless")  # 隐藏浏览器
    opt.add_argument("--no-sandbox")
    driver = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe', options=opt)
    driver.get("https://voice.baidu.com/act/virussearch/virussearch/?from=osari_map&tab=0&infomore=1")

    # print(driver.page_source)
    btn = driver.find_element_by_xpath('//div[@class="VirusHot_1-4-9_1Fqxy-"]')
    btn.click()
    time.sleep(1)
    VirusHot = driver.find_elements_by_xpath(
        '//div[@class="VirusHot_1-4-9_32AY4F VirusHot_1-4-9_2RnRvg"]//a//span[@class="VirusHot_1-4-9_24HB43"]')
    content = [i.text for i in VirusHot]
    return content


def update_hotsearch():
    """
    将热搜数据插入数据库
    """
    cursor = None
    conn = None
    try:
        content = get_baidu_hot()
        print(f"{time.asctime()}开始更新热搜数据")
        conn, cursor = get_conn()
        sql = "insert into hotsearch(dt, content) values (%s, %s)"
        ts = time.strftime("%Y-%m-%d %X")
        for i in content:
            cursor.execute(sql, (ts, i))
        conn.commit()
        print(f"{time.asctime()}数据跟新完成")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


if __name__ == '__main__':
    get_baidu_hot()
    update_hotsearch()
