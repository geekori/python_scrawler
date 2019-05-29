'''
查找多个节点

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome('./chromedriver')
try:
    browser.get('https://www.jd.com')
    li_list = browser.find_elements_by_tag_name('li')
    print(li_list)
    print(len(li_list))

    print(li_list[0].text)

    ul_list = browser.find_elements(By.TAG_NAME,'ul')

    print(ul_list[1].text)
    browser.close()
except Exception as e:
    print(e)
    browser.close()