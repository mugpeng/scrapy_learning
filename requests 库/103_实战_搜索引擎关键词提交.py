import requests

url = "http://www.so.com/s?"
kv = {'q' : 'python'}
try:
    r = requests.get(url,timeout = 30, params = kv) #添加搜索内容，python
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
    print(r.text[:100])
except :
    print("抓取失败")
