# -*- coding:utf-8 _*-
# @Time : 2020/10/26 16:59
# @Author: Jet Chen
import win32clipboard as w
import win32con
from flask import Flask, request, jsonify

'''
python读取剪切板内容
使用方法：
step 1：window 环境运行 python 脚本 `python clipboard.py 2>&1 &`
step 2：iphone 添加复制和粘贴的快捷指令
'''

app = Flask(__name__)


def get_text():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d.decode('GBK')


def set_text(t):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardText(t, w.CF_TEXT)
    w.CloseClipboard()


@app.route("/clipboard/get", methods=['GET'])
def clipboard_get():
    t = get_text()
    print(t)
    return jsonify(t), 200


@app.route("/clipboard/put", methods=['POST'])
def clipboard_put():
    request_json = request.json
    t = request_json['text']
    print(t)
    set_text(t)
    return jsonify('success'), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088)
