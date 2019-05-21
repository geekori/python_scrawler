'''
项目实战：抓取京东图书评论信息

https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv65&productId=12417265&score=0&sortType=5&page=4&pageSize=10&isShadowSku=0&rid=0&fold=1

page：页码（从0开始）
pageSize：每页的评论数（10）

'''

import requests
import json

header = {
    'Host': 'sclub.jd.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://item.jd.com/12417265.html',
    'Connection': 'keep-alive',
    'Cookie': 'TrackID=1do45iqFSB4LnOssM_eORri8VThrz7_Km7ZeDCfgLULidAdSm6N0JlbFGzeo4Kap7ZYGgPZAmym5-Uoy2zs6qERc5NMu60gNs-8BLjvdcnu3CwagMThGmaBatZs0EOgIX|||s0IBhCevYWc; __jda=122270672.1535170218510296784454.1535170219.1558147526.1558398681.7; __jdu=1535170218510296784454; shshshfp=3aebc2953e473f94aa8435ee5e69efb5; shshshfpa=c63a74ee-423b-d284-6617-88ddf175b363-1535170219; shshshfpb=022e7b1218024202795b0adb8a9d449b1aa21606e0d2f9c815b80d6ab4; 3AB9D23F7A4B3C9B=TSFK3ZR4ANMS25RQS55PRALBT7FIGR7N64TXVUNFN6RVJNXNAPWT4SA6IHKBJWE2E54U5QEKCEDNHPBPVHNVEWQEYA; __jdv=122270672|direct|-|none|-|1558147526266; areaId=8; ipLoc-djd=8-560-50827-50850; shshshsID=8525c94a4cab337420ad7637d65e3644_1_1558398680402; __jdb=122270672.1.1535170218510296784454|7.1558398681; __jdc=122270672; JSESSIONID=193C528C2DEF75DE87DF04C378141538.s1',
    'TE': 'Trailers'
}
# 限定抓取的评论数
fetch_comment_count = 25
index = 0
page_index = 0
flag = True
while flag:
    url = 'https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv65&productId=12417265&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1'.format(page_index)

    page_index+=1
    html = requests.get(url,headers = header)
    text = str(html.content,encoding='iso-8859-1')

    json_str = text.replace('fetchJSON_comment98vv65(','')
    json_str = json_str.replace(')','')
    json_str = json_str.replace('null','"null"')
    json_str = json_str.replace(';','')
    json_obj = json.loads(json_str)

    for i in range(0,len(json_obj['comments'])):
        try:
            comment = json_obj['comments'][i]['content'].encode(encoding='iso-8859-1').decode('GB18030')

            if comment != '此用户未填写评论内容':
                print('<',index+1,'>',comment)
                creation_time = json_obj['comments'][i]['creationTime']
                # 获取昵称
                nickname = json_obj['comments'][i]['nickname'].encode(encoding='iso-8859-1').decode('GB18030')
                print(creation_time)
                print(nickname)
                print('---------------')
                index += 1
        except:
            pass
        if index == fetch_comment_count:
            flag = False
            break