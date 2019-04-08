'''
CSS选择器

1. nodename
2. #idname
3. .classname

'''

html = '''
<div>
    <ul>
        <li class="item1" value1="1234" value2 = "hello world"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com"> 京东商城</a></li>        
    </ul>
    <button id="button1">确定</button>
    <input id = "button1">hh</input>
    <ul>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item2"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>

'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
tags = soup.select('.item')
for tag in tags:
    print(tag)
tag = soup.select_one('.item')
print(tag)

tags = soup.select('#button1')
print(tags)

tags = soup.select('a')[2:]
for tag in tags:
    print(tag)







