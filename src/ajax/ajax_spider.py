import requests
from lxml import etree
import json
result = requests.get('http://localhost:5000')
tree = etree.HTML(result.text)
print(tree.xpath('//*[@id="video_list"]/li[2]')[0].text)
#print(tree.xpath('//*[@id="video_list"]/li[6]')[0].text)

result = requests.get('http://localhost:5000/data')
text = result.text.encode('utf-8').decode('unicode-escape')
print(text)
data = json.loads(text)
for value in data:
    print(value['name'])