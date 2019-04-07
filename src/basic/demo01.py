# 编写第一个网络爬虫
'''
从若干个Web页面中获取Url

index.html
<a href='a.html'>a</a>
<a href='b.html'>b</a>
a.html    aa.html  bb.html
b.html    cc.html

网络爬虫需要两个核心技术
1.  下载Web资源（html、css、js、json)
2.  分析Web资源

download(url)：下载url指定的Web资源，如果下载成功，该函数会返回html代码
analyse(html)：downlaod函数下载的html代码传入analyse函数，并进行分析
该函数返回由url组成的列表，如果没有url，就返回[]

crawler(url)
{
    html = download(url)
    urls = analyse(html)
    for url in urls
    {
        crawler(url)
    }
}

'''
from urllib3 import *
from re import *
http = PoolManager()
disable_warnings()

def download(url):
    result = http.request('GET', url)
    htmlStr = result.data.decode('utf-8')
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