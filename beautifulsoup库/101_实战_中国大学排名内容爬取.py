import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        hd = {'user-agent': 'Chrome/10'} # 修改头部信息
        r = requests.get(url, timeout = 30, headers = hd)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.tbody.children:
        if isinstance(tr, bs4.element.Tag): # 筛选tbody 中的子节点 tr 的类型，需要为tag 类型
            tds = tr('td') # 将 tr 标签中的 td赋值给tds
            ulist.append([tds[0].string, tds[1].string, tds[4].string]) 
            # 分别对应td标签中的第1，2，5 列信息，并定义为str类型，添加到ulist中，并封包为一个表格。

def printUnivList(ulist, num):
    print('%s \t %s \t %s \t' % ('排名', '学校名称', '总分')) # 输出信息的第一行打印基本信息
    for i in range(num):
        u = ulist[i]
        print('%s \t %s \t %s \t' % (u[0], u[1], u[2]))
    print('Num: ' + str(num))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 限制输出的结果数目
main()
