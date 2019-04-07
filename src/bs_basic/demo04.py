# 用Beautiful Soup分析京东首页的HTML代码

from bs4 import *
from urllib3 import *
disable_warnings()

http = PoolManager()
r = http.request('GET','https://www.jd.com')
#print(r.data)

soup = BeautifulSoup(r.data,'lxml')
print(soup.meta)
print(soup.meta['charset'])
print(soup.title.text)
print(soup.body['class'])