import requests
import os

# 为老师上课版本，额外使用了os这个库，可以提供一些linux指令。
# 可以获得图片的名字
root = "/Users/mugpeng/Desktop/pics/"
url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589536355049&di=22886578248b426febf2d78908a026e1&imgtype=0&src=http%3A%2F%2Ffile02.16sucai.com%2Fd%2Ffile%2F2014%2F0704%2Fe53c868ee9e8e7b28c424b56afe2066d.jpg"
path = root + url.split("/")[-1] # 使用/分割url链接，获取末尾的地址中的文件名，添加到root地址末尾
'''
抓取百度的一张照片
'''

try:
    if not os.path.exists(root):
        os.mkdir(root) # 若目录不存在，则创建目录
    if not os.path.exists(path): # 判断文件是否存在
        r = requests.get(url)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("图片抓取成功")
    else:
        print("图片已经存在")
except:
    print("图片抓取失败")
