'''
删除节点

remove

'''

from pyquery import PyQuery as pq

html = '''
<div id="panel">
    <ul class="list1" >
        <li class="item1 item2" >谷歌<p>微软</p>Facebook</li>        
    </ul>

</div>
'''

doc = pq(html)
li = doc('.item1.item2')
print(li.text())

li.remove('p')
print('---------')
print(li.text())

li = doc('.item1.item2')
li.find('p').remove()
print(li.text())