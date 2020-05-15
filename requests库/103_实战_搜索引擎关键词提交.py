import requests

#抓取360搜索界面中“python”输出的信息
url = "http://www.so.com/s?"
# 360的搜索接口为：http://www.so.com/s?q=keyword
kv = {'q' : 'python'}
try:
    r = requests.get(url,timeout = 30, params = kv) #添加搜索内容，python
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
    print(r.text[:100])
except :
    print("抓取失败")
