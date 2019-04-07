# 读取和设置节点的属性
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

soup = BeautifulSoup(html,'lxml')
print(type(soup.body.attrs))
print('body.class','=',soup.body['class'])
print('body.attr','=',soup.body['attr'])
print('a.class','=',soup.a['class'])
print('x.attr1','=',soup.x['attr1'])

soup.body['class'] = ['x','y','z']
#print(soup.body)
#soup.body['class'] = 'xyz123 uio'
#print(soup.body)
soup.body['class'].append('ok')
print(soup.body)
#soup.body['ok'] = '443'
#del soup.body['class']
#print(soup.body)
print(soup.a['rel'])
# rel,rev,accept-charset,headers,accesskey

