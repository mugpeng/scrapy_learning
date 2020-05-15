import requests

pxs = {'http': 'IP_1', 'https':'IP_2'} #隐藏用户本来的IP地址
r = requests.request('GET', 'URL', proxies = pxs)