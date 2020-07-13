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
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format('排名', '学校名称', '总分', chr(12288))) # 输出信息的第一行打印基本信息
    # 当中文宽度不够，系统默认采用西文空白填充
    # format 中输出内容分别为10,10,10 字号，居中。并将空格天空修改为中文类型
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
    print('Num: ' + str(num))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 限制输出的结果数目
main()
