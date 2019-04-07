# 从百度抓取比基尼美女

imageUrl = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1394152664,540491199&fm=27&gp=0.jpg'
from urllib3 import *
import os
import re
import json
http = PoolManager()
disable_warnings()

os.makedirs('download/images', exist_ok = True)
def str2Headers(file):
    headerDict = {}
    f = open(file,'r')
    
    headersText = f.read()

    # Linux、Unix、Mac OS X：\n
    # Windows：\r\n
    headers = re.split('\n',headersText)
    for header in headers:
        result = re.split(':',header, maxsplit=1)
        headerDict[result[0]] = result[1]        
    f.close()
    return headerDict

headers = str2Headers('image_headers.txt')
def processResponse(response):
    global count
    if count > 100:
        return
    s = response.data.decode('utf-8')
    d = json.loads(s)
    n = len(d['data'])
    for i in range(n - 1):
        if count > 100:
            return
        imageUrl = d['data'][i]['hoverURL'].strip()
        if imageUrl != '':
            print(imageUrl)
            r = http.request('GET', imageUrl,headers = headers)
            count += 1
            imageFile = open('download/images/%0.5d.jpg' % count,'wb')
            imageFile.write(r.data)
            imageFile.close()
count = 0
pn = 30
rn = 30
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%AF%94%E5%9F%BA%E5%B0%BC%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%AF%94%E5%9F%BA%E5%B0%BC%E7%BE%8E%E5%A5%B3&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={pn}&rn={rn}&gsm=1e&1512281761218='.format(pn=pn,rn=rn) 

while count <= 100:
    r = http.request('GET',url)
    processResponse(r)
    pn += 30
'''
r = http.request('GET',imageUrl,headers = headers)
f = open('image.jpg','wb')
f.write(r.data)
f.close()
'''



