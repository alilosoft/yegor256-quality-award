import requests

r = requests.get('https://www.yegor256.com/2019/11/03/award-2020.html')
print(r.text)
