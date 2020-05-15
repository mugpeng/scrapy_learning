import requests

url = "https://www.amazon.cn/dp/B07VD8GV3T/ref=s9_acsd_hps_bw_c2_x_1_i?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-2&pf_rd_r=FDEXFNKQATY2YW7T7260&pf_rd_t=101&pf_rd_p=586edc57-a929-4dcc-be3b-d5fcb1379ae3&pf_rd_i=1519395071"
def getHTMLText(url):
    try:
        hd = {'user-agent':'Mozilla/5.0'} #修改头部信息
        r = requests.get(url, headers = hd)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[500:1000])
    except:
        print('爬取失败')

getHTMLText(url)

