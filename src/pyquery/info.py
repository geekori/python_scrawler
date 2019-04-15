'''

获取节点信息

1. 节点名称
2. 节点属性值
3. 节点文本
4. 整个节点的HTML代码
5. 节点内部的HTML代码

'''

from pyquery import PyQuery as pq
html = '''
<div id="panel">
    <ul class="list1">
        <li class="item" value1="1234" value2 = "hello world">
            Hello
            123
            <a href="https://geekori.com"> geekori.com</a>
            World
        </li>
        <li class="item1" >
        </li>
    </ul>
    <ul class="list2">
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item"  value1="4321" value2 = "世界你好" >
            <a href="https://www.microsoft.com">微软</a>
        </li>
        <li class="item2"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>
'''

doc = pq(html)
result = doc('.item')

print(type(result[0]))
print(result[0].tag)
print(result[1].tag)

# 获取节点的属性值
print('value1:',result[0].get('value1'))
print('value2:',result[1].get('value2'))
print('value2:',result.attr('value2'))
print('value2:',result.attr.value2)

for li in result.items():
    print(type(li))   # PyQuery
    print(li.attr.value2)
for li in result:
    print(type(li))   # Element
    print(li.get('value1'))
print('-----------------')
# 获取第1个li节点的文本内容
print(result.text())

print(result[0].text)

print('------获取节点的HTML代码---------')
from lxml import etree

for node in result:
    print(str(etree.tostring(node,pretty_print=True,encoding='utf-8'),'utf-8'))
print('------------')
print(result.html())  # 只返回第1个符合条件的节点的内部HTML代码