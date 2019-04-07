# Beautiful Soup基础：获取和设置Tag对象的name与text属性
from bs4 import BeautifulSoup
html = '''
<html>
    <head><title>index</title></head>
    <body>
        <a href='a.html'>first page</a>
        <p>
        <a href='b.html'>second page</a>
        <p>
        <a href='c.html'>third page</a>
        <p>
        <x k='123'>hello</x>
    </body>
</html>
'''
soup = BeautifulSoup(html,'lxml')
print(soup.html)
print('----------')
print(soup.head)
print(soup.body)
print('-------')
print(soup.a)
print(soup.body.a)
print(soup.a.text)
# ----设置节点名称------
soup.a.name = 'div'
print(soup)
print('---------')
print(soup.x)
print('--------')
print(soup.x.text)
print(soup.x.string)
#soup.x.text= 'word'
soup.x.string = 'word'
print(soup.x)
