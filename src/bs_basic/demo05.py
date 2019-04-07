# 获取所有的节点（Tag对象）
html = '''
<html>
    <head><title>index</title></head>
    <body attr='test xyz' class='style1 style2'>
        <a rel='ok1 ok2 ok3' class='a1 a2' href='a.html'>first page</a>
        <p>
        <a href='b.html'>second page</a>
        <p>
        <a  href='c.html'>third page</a>
        <p>
        <x k='123' attr1='hello' attr2='world'>hello</x>
    </body>
</html>
'''
from bs4 import *
from urllib3 import *
disable_warnings()
soup = BeautifulSoup(html,'lxml')
print(soup.find_all('a'))
aList = soup.find_all('a')
for a in aList:
    print(a['href'])
http = PoolManager()
r = http.request('GET','https://www.taobao.com')
soup = BeautifulSoup(r.data,'lxml')
print(soup.find_all('a'))
aList = soup.find_all('a')
for a in aList:
    print(type(a))
    url = a.get('href')
    if url == None:        
        continue
    if url.startswith('http') or url.startswith('https'):
        print(url)