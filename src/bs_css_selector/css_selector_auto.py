'''
自动获取CSS选择器

'''

import requests
from bs4 import  BeautifulSoup

result = requests.get('https://www.jd.com')

soup = BeautifulSoup(result.text,'lxml')

aTag = soup.select('#navitems-group1 > li.fore1 > a')
print(aTag[0].string)

tag = soup.select_one ('#navitems-group2 > li.fore2 > a')
print(tag.string)

