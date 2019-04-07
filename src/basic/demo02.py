# 保存爬取的数据

from urllib3 import *
from re import *
import os
import hashlib
http = PoolManager()
disable_warnings()
os.makedirs('download', exist_ok = True)
def computeMD5hash(myString):
    m = hashlib.md5()
    m.update(myString.encode('utf-8'))
    return m.hexdigest()

f = open('download/urls.txt','w')
def download(url):
    result = http.request('GET', url)
    md5 = computeMD5hash(url)
    f.write(url + '\n')
    htmlStr = result.data.decode('utf-8')
    htmlFile =open('download/' + md5,'w')
    htmlFile.write(htmlStr)
    htmlFile.close()
    return htmlStr
#print(download('http://www.weather.com.cn/'))
def analyse(htmlStr):
    # <a href='a.html'>a</a>
    aList = findall('<a[^>]*>',htmlStr)
    result = []
    for a in aList:
        # <a href='a.html'>
        g = search('href[\s]*=[\s]*[\'"]([^>\'""]*)[\'"]',a)
        if g != None:
            url = g.group(1)
            url = 'http://localhost:8888/files/' + url
            result.append(url)
    return result
#print(analyse(download('http://localhost:8888/files')))
def crawler(url):
    print(url)
    html = download(url)
    urls = analyse(html)
    for url in urls:
        crawler(url)
crawler('http://localhost:8888/files')
f.close()

