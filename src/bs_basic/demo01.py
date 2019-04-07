# Beautiful Soup基础：使用Beautiful Soup

# 功能：用于分析HTML代码

'''
安装bs4模块
pip3  install beautifulsoup4
conda install beautifulsoup4

'''
from bs4 import BeautifulSoup

soup1 = BeautifulSoup('<title>测试</title>','html.parser')
'''
优点：
1. Python内置的标准库
2. 执行速度适中
3. 文档容错能力强

缺点：
Python2.7.3或3.2.2以前的版本，对中文容错能力比较差

lxml
优点：
1. 速度快
2. 文档的容错能力强

缺点：
需要安装C语言库

conda install lxml
'''
soup2 = BeautifulSoup('<title>测试</title>','lxml')

'''
html5lib
优点：
1. 最好的容错性
2. 以浏览器的方式解析文档
3. 生成HTML5格式的文档

缺点：
速度慢

conda install html5lib
'''
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
    </body>
</html>
'''
soup3 = BeautifulSoup(html,'html5lib')
print(soup3.title)
print(soup3.title.text)
print(soup3.a['href'])