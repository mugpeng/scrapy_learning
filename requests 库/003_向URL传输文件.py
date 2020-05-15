import requests

fs = {'file': open('data.xls', 'rb')}
r = requests.request('POST', 'URL', files = fs)