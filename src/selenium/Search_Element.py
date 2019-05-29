'''
查找单个节点

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome('./chromedriver')

try:
    browser.get('http://localhost/demo.html')
    input = browser.find_element_by_id('name')
    input.send_keys('李宁')

    input = browser.find_element_by_id('age')
    input.send_keys('18')

    input = browser.find_element_by_name('country')
    input.send_keys('中国')

    input = browser.find_element_by_class_name('myclass')
    input.send_keys('400000')

    input = browser.find_element(By.CLASS_NAME,'myclass')
    input.clear()
    input.send_keys('8000000')
except Exception as e:
    print(e)
    browser.close()