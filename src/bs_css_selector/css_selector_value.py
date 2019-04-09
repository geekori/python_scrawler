'''

获取节点的属性值与文本

'''

html = '''
<div>
    <ul>
        <li class="item1" value1="1234" value2 = "hello world"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item">
           <a href="https://www.jd.com"> 京东商城</a>
           <a href="https://www.google.com">谷歌</a>
        </li>        
    </ul>
    <ul>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item" ><a href="https://www.microsoft.com">微软</a></li>
    </ul>
</div>


a['href']

a.attrs['href']

a.get_text()

a.string
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
tags = soup.select('.item')
for tag in tags:
    aTags = tag.select('a')
    for aTag in aTags:
        print('href','=',aTag['href'],'text','=',aTag.get_text())

for tag in tags:
    tags = tag.find_all(name='a')
    for aTag in tags:
        print('href', '=', aTag.attrs['href'], 'text', '=', aTag.string)

