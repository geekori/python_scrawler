'''

pyquery的基本使用方法

jquery

pip install pyquery

CSS选择器查找节点

BS



'''

html = '''
<div>
    <ul>
        <li class="item1" value1="1234" value2 = "hello world"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com"> 京东商城</a></li>        
    </ul>
    <ul>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item2"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>

'''

from pyquery import PyQuery as pq
doc = pq(html)
for a in doc('a'):
    print(a.get('href'),a.text)

doc = pq(url='https://www.jd.com')
print(doc('title')[0].text)

doc = pq(filename='demo.html')
print(doc('title')[0].text)


