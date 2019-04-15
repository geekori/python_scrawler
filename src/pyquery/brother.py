'''

使用siblings方法查找兄弟节点
'''

from pyquery import PyQuery as pq
doc = pq(filename='test.html')

result = doc('.item')
print(result.siblings())
print('------------------')
print(result.siblings('.item2'))