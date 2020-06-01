import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
from selenium.webdriver.chrome.options import Options

class Handle_webdriver(object):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.maximize_window()

    def handle_job(self):
        self.driver.get("https://search.51job.com/list/000000,000000,0000,00,9,99,%2520,2,1.html")
        if WebDriverWait(self.driver,5,0.5).until(EC.presence_of_all_elements_located((By.ID, 'kwdselectid'))):
            input_keyword = input("请输入要查找的岗位信息：")
            self.driver.find_element_by_id('kwdselectid').send_keys(input_keyword)
            self.driver.find_element_by_class_name('p_but').click()
            if WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_all_elements_located((By.ID, 'resultList'))):
                while True:
                    time.sleep(2)
                    self.handle_parse(self.driver.page_source)
                    if self.driver.find_element_by_xpath("//li[@class='bk'][2]/a").text == '下一页':
                        self.driver.find_element_by_xpath("//li[@class='bk'][2]/a").click()
                    else:
                        break
            time.sleep(5)
            self.driver.quit()

    def handle_parse(self, page_source):
        html_51job = etree.HTML(page_source)
        all_div = html_51job.xpath("//div[@id='resultList']//div[@class='el']")
        info_list = []
        for item in all_div:
            info = {}
            info['job_name'] = item.xpath("./p/span/a/@title")
            info['company_name'] = item.xpath(".//span[@class='t2']/a/@title")[0]
            info['company_address'] = item.xpath(".//span[@class='t3']/text()")[0]
            try:
                info['money'] = item.xpath(".//span[@class='t4']/text()")[0]
            except Exception as e:
                info['money'] = '无数据'
            info['date'] = item.xpath(".//span[@class='t5']/text()")[0]
            print(info)
        #     info_list.append(info)
        # return info_list


test_selenium = Handle_webdriver()
test_selenium.handle_job()