'''

修改节点属性和内容

attr：用于添加或修改属性的值，arg1：属性名   arg2：属性值
removeAttr：移除属性的
text：文本内容
html：Html内容

'''

from pyquery import PyQuery as pq

html = '''
<div id="panel">
    <ul class="list1" >
        <li class="item1 item2 item3" >谷歌</li>
        <li class="item1 item2">微软</li>
    </ul>

</div>
'''

doc = pq(html)
li = doc('.item1.item2')
print(li)
print(li.text())
print(li.html())

# 为所有的li节点添加id属性
li.attr('id','my_li')
li.attr('class','myitem1 myitem2')
print(li)

li.removeAttr('id')
li.remove_attr('class')
print(li)

# 设置所有li节点的文本内容
li.text('我的列表')
print(li)

li.text('<a href="https://www.baidu.com"/>')
print(li)

li.html('<a href="https://www.baidu.com"/>')
print(li)

print("text:",li.text())
print("html:",li.html())