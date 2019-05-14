'''
项目实战：抓取当当图书排行榜

requests、pyquery、css选择器

分页规律
第1页：http://search.dangdang.com/?key=python&act=input&sort_type=sort_default&page_index=1
第2页：http://search.dangdang.com/?key=python&act=input&sort_type=sort_default&page_index=2
...
第n页：http://search.dangdang.com/?key=python&act=input&sort_type=sort_default&page_index=n

需要抓取的数据
1. 图书主页的URL
2. 图书名
3. 图书当前价格
4. 图书作者
5. 出版日期
6. 出版社
7. 评论数
8. 简介


'''

from pyquery import PyQuery as pq
import requests
import time
# 用于下载指定URL的页面，并返回页面内容
def get_one_page(url):
    try:
        result = requests.get(url)
        if result.status_code == 200:
            return result.text
        return None
    except Exception:
        return None
# 用于分析页面代码，是一个产生器函数
def parse_one_page(html):
    doc = pq(html)
    # 提取图书列表
    ul = doc('.bigimg')
    li_list = ul('li')
    for li in li_list.items():
        # 获取当前li节点的第1个a子节点
        a = li('a:first-child')
        # 提取图书主页的URL
        href = a[0].get('href')
        # 提取图书名
        title = a[0].get('title')

        span = li('.search_now_price')
        # 提取当前价格
        price = span[0].text[1:]

        p = li('.search_book_author')

        # 提取图书作者
        author = p('a:first-child').attr('title')

        # 提取图书出版日期
        date = p('span:nth-child(2)').text()[1:]

        # 提取图书出版社
        publisher = p('span:nth-child(3) > a').text()

        # 提取图书评论数
        comment_number = li('.search_comment_num').text()[:-3]

        # 提取图书简介
        detail = li('.detail').text()

        yield {
            'href':href,
            'title':title,
            'price':price,
            'author':author,
            'date':date,
            'publisher':publisher,
            'comment_number':comment_number,
            'detail':detail
        }
if __name__ == '__main__':
    urls = ['http://search.dangdang.com/?key=python&act=input&sort_type=sort_default&page_index={}'.format(str(i)) for i in range(1,4)]
    print(urls)

    for url in urls:
        book_infos = parse_one_page(get_one_page(url))
        for book_info in book_infos:
            print(book_info)
            time.sleep(1)