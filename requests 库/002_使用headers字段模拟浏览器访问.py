import requests

hd = {'user-agent': 'Chrome/10'}
r = requests.request('POST', 'URL', headers = hd)