import requests

url = "http://m.ip138.com/ip.asp?ip="
hd = {'user-agent' : 'Mozilla/5.0'} #跳过网页robot限制

try:
    r = requests.get(url + '202.204.80.112', headers = hd)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:]) #最后500个字符
except:
    print("抓取失败")

'''
可能是该页面API接口调整
现在已无法正常通过老师给的接口进行使用
所以返回内容与演示不符
'''