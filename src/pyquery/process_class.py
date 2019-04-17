'''

添加和移除节点的样式

class

addClass
removeClass


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

li.addClass('myitem')
print('-----------')
print(li)

li.removeClass('item1')
print('-----------------')
print(li)

li.add_class("class1 class2")
print('-----------')
print(li)

li.removeClass("item2 item3")
print('--------------')
print(li)



