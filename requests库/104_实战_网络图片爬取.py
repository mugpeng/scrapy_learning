import requests
import os

path = "/Users/mugpeng/Desktop/abc.jpg"
url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589536355049&di=22886578248b426febf2d78908a026e1&imgtype=0&src=http%3A%2F%2Ffile02.16sucai.com%2Fd%2Ffile%2F2014%2F0704%2Fe53c868ee9e8e7b28c424b56afe2066d.jpg"
'''
抓取百度的一张照片
'''

try:
    r = requests.get(url)
    r.raise_for_status()
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()
        print("图片抓取成功")
except:
    print("图片抓取失败")
