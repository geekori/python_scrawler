'''

项目实战：搜索并抓取图片

https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%A4%96%E6%98%9F%E4%BA%BA&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%A4%96%E6%98%9F%E4%BA%BA&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=90&rn=30&gsm=5a&1557876408116=

word：关键字
pn：图像的索引
'''
import requests
import json
import random
import string
import os

word = input('请输入搜索关键字：')
print(word)

# 随机生成8位的目录名
dir_name = ''.join(random.sample(string.ascii_letters + string.digits,8))
print('图像文件将保存在',dir_name,'目录中')

os.mkdir(dir_name)

max_value = 100

# 当前图像的索引
current_value = 0

# 用于控制图像的文件名
image_index = 1
while current_value < max_value:
    # 开始抓取图像数据
    result = requests.get('https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%A4%96%E6%98%9F%E4%BA%BA&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word={}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30&gsm=5a&1557876408116='.format(word,current_value))
    json_str = result.content
    json_doc = str(json_str,'utf-8')
    image_result = json.loads(json_doc)
    data = image_result['data']
    for image in data:
        url = image.get('middleURL')
        if url != None:
            print('正在下载图片：',url)
            r = requests.get(url)
            filename = dir_name + '/' + str(image_index).zfill(10) + '.png'
            # 保存图像
            with open(filename,'wb') as f:
                f.write(r.content)
            image_index +=1
    current_value +=30
print('图像下载完成')
