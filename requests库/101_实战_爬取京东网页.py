import requests
    
def getHETMLText(url):
    try:
        hd = {'user-agent': 'Chrome/10'} #修改头部信息
        r = requests.get(url, timeout = 30, headers = hd) #限制访问时间，并模拟浏览器访问
        r.raise_for_status() 
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return "爬取失败"

if __name__ == "__main__":
    url = "https://item.jd.com/100007199883.html" #京东网页
    print(getHETMLText(url))