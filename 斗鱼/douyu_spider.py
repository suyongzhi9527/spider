# conding = utf-8
from selenium import webdriver
import time
import json


class DouyuSpider:
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome(r"F:\chromedriver.exe")

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//ul[@class='layout-Cover-list']/li")
        content_list = []
        for li in li_list:
            item = {}
            item["room_img"] = li.find_element_by_xpath(".//div[@class='DyListCover-imgWrap']//img").get_attribute("src")
            item["room_title"] = li.find_element_by_xpath(".//div[@class='DyListCover-content']//h3").get_attribute("title")
            item["room_cate"] = li.find_element_by_xpath(".//div[@class='DyListCover-content']//span[@class='DyListCover-zone']").text
            item["author_name"] = li.find_element_by_xpath(".//div[@class='DyListCover-content']//h2").text
            item["watch_num"] = li.find_element_by_xpath(".//div[@class='DyListCover-info'][2]/span").text
            print(item)
            content_list.append(item)
        # 获取下一页的元素
        next_url = self.driver.find_elements_by_xpath("//ul[@class='dy-Pagination ListPagination']//li[@class=' dy-Pagination-next']")
        print(next_url)
        next_url = next_url[0] if len(next_url) > 0 else None
        return content_list,next_url

    def save_content_list(self,content_list):
        with open("douyu.txt","a",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False,indent=2))
                f.write("\n")
            print("写入成功！")

    def run(self):
        # 1.start_url
        # 2.发送请求，获取响应
        self.driver.get(self.start_url)
        # 3.提取数据，提取下一页的元素
        time.sleep(10)
        content_list,next_url = self.get_content_list()
        # 4.保存数据
        self.save_content_list(content_list)
        # 5.点击下一页元素，循环
        while next_url is not None:
            next_url.click()
            time.sleep(10)
            content_list,next_url = self.get_content_list()
            self.save_content_list(content_list)


if __name__ == "__main__":
    douyu = DouyuSpider()
    douyu.run()
