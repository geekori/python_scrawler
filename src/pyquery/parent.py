'''

使用parent和parents方法查找父节点

parent：得到直接父节点
parents：得到所有的父节点


'''

from pyquery import PyQuery as pq
doc = pq(filename='test.html')

result = doc('.item')
print(result.parent())

print('-------------')
print(result.parents())
print('---------------')
print(result.parents('#panel'))