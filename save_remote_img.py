#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 使用requests保存远程图片(或文件)
import requests
import os
import sys


def saveRemoteImage(imgurl):
    imgurl = imgurl
    filename = imgurl.split('/')[-1]
    path = './static/'+filename
    if not os.path.exists(path):
        r = requests.get(imgurl)
        with open(path, 'wb') as f:
            f.write(r.content)
            print('OK')
    else:
        print('Already exists.')

    """
    下载大文件这样写：
    for chunk in r.iter_content():
        f.write(chunk)

    如果不使用requests模块：
    import urllib
    urllib.urlretrieve(url, filename=None, reporthook=None, data=None)
    """

def main():
    if len(sys.argv) < 2:
        print("请输入图片URL地址: ")
        sys.exit()
    imgurl = sys.argv[1]
    saveRemoteImage(imgurl)

if __name__ == "__main__":
    main()
