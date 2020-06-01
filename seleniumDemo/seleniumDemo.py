import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# chrome_driver = "D:\\driver\\chromedriver.exe"
test_webdriver = webdriver.Chrome()
# test_webdriver = webdriver.PhantomJS()
# test_webdriver = webdriver.Firefox()
test_webdriver.maximize_window()
test_webdriver.implicitly_wait(5)
# test_webdriver.set_window_size(500, 500)


# test_webdriver.get("https://www.echartsjs.com/examples/")
# for item in test_webdriver.find_elements_by_xpath("//h4[@class='chart-title']"):
#     print(item.text)

test_webdriver.get("https://www.baidu.com")
# time.sleep(2)
# test_webdriver.get("https://news.baidu.com")
# time.sleep(2)
# test_webdriver.refresh()
# time.sleep(2)
# test_webdriver.back()
# time.sleep(2)
# test_webdriver.forward()

# above = test_webdriver.find_element_by_id("s-usersetting-top")
# ActionChains(test_webdriver).move_to_element(above).perform()

# element = WebDriverWait(test_webdriver, 5, 0.5).until(EC.presence_of_all_elements_located((By.ID, 'kw')))
# element.send_keys('python')
try:
    test_webdriver.find_element_by_id('kw').send_keys('python')
except NoSuchElementException as e:
    pass



# test_webdriver.find_element_by_xpath("//input[@id='kw']").send_keys("python")
# test_webdriver.find_element_by_xpath("//input[@id='su']").click()

# test_webdriver.find_element_by_id("kw").send_keys("python")
# test_webdriver.find_element_by_id("su").click()

# test_webdriver.find_element_by_name("wd").send_keys("python")
# test_webdriver.find_element_by_class_name("s_ipt").send_keys("python")

time.sleep(5)
# print(test_webdriver.title)
# print(test_webdriver.page_source)
print(test_webdriver.get_cookies())
test_webdriver.quit()