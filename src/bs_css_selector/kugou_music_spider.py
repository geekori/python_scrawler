'''
项目实战：抓取酷狗音乐榜


requests

Beautiful Soup  CSS Selector

https://www.kugou.com/yy/rank/home/6-8888.html?from=rank

1. 排名
2. 歌手
3. 歌曲名
4. 时长

pip install requests

'''

import  requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

def get_info(url):
    result = requests.get(url,headers = headers)
    soup = BeautifulSoup(result.text,'lxml')
    # 提取名次
    ranks = soup.select('span.pc_temp_num')

    # 提取歌手和歌曲的名字
    names = soup.select('div.pc_temp_songlist > ul > li > a')

    # 提取歌曲时长
    times = soup.select('span.pc_temp_tips_r > span')



    for rank,name,time in zip(ranks,names,times):
        song = ""
        if len(name.get_text().split('-')) > 1:
            song =  name.get_text().split('-')
        data = {
            'rank':rank.get_text().strip(),
            'singer':name.get_text().split('-')[0], # 歌手
            'song':song, # 歌曲
            'time':time.get_text().strip()
        }
        print(data)



if __name__ == '__main__':
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1,11)]
    for url in urls:
        get_info(url)
        time.sleep(1)