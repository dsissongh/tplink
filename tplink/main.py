import requests

routerbase = 'http://172.16.10.1'


request = requests.get(routerbase)
print(request.text)