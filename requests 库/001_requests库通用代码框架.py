import requests
    
def getHETMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status() #如果状态不是200，引发HTTPError 异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://www.baidu.com" #如若去掉http:// 则会产生异常
    print(getHETMLText(url))