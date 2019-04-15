'''
使用find和children方法查找子节点

find：查找子节点（包括子孙子节点）
children：只能查找直接子节点

'''

from pyquery import PyQuery as pq
from lxml import etree
doc = pq(filename='test.html')

result = doc('.list2')
print(type(result))
a_list = result.find('a')

for a in a_list:
    print(str(etree.tostring(a,pretty_print=True,encoding='utf-8'),'utf-8'))
print('-----------------')
a_list = result.children('a')
for a in a_list:
    print(str(etree.tostring(a,pretty_print=True,encoding='utf-8'),'utf-8'))
print('---------------')
result = doc('.item')
a_list = result.children('a')
for a in a_list:
    print(str(etree.tostring(a,pretty_print=True,encoding='utf-8'),'utf-8'))
