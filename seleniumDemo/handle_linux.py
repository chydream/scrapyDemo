import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--headless')
test_webdriver = webdriver.Chrome(chrome_options=chrome_options)
test_webdriver.maximize_window()
test_webdriver.get("https://www.baidu.com")
test_webdriver.find_element_by_xpath("//input[@id='kw']").send_keys("python")
test_webdriver.find_element_by_xpath("//input[@id='su']").click()
time.sleep(5)
print(test_webdriver.title)
test_webdriver.quit()