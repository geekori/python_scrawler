'''
Flask

'''

from flask import Flask,render_template
from flask import make_response

import json

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
# 响应客户端的请求，并返回json格式的数据

@app.route('/data')
def data():
    data = [
        {'id':1,'name':'PyQt5视频课程'},
        {'id':2,'name':'Electron实战'},
        {'id':3,'name':'征服Flask'}
    ]
    response = make_response(json.dumps(data))
    return response
if __name__ == '__main__':
    app.run()