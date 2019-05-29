'''
Selenium的基本使用方法

1. 如何打开浏览器
2. 获取浏览器页面的特定内容
3. 空在浏览器页面上的控件，如向一个文本输入框输入一个字符串
4. 关闭浏览器

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
browser = webdriver.Chrome('./chromedriver')
try:
    browser.get('https://www.jd.com')

    input = browser.find_element_by_id('key')
    input.send_keys("Python从菜鸟到高手")
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser,4)

    wait.until(ec.presence_of_all_elements_located((By.ID,'J_goodsList')))
    print(browser.title)
    print(browser.current_url)
    print(browser.page_source)
    browser.close()
except Exception as e:
    print(e)
    browser.close()