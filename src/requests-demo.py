import requests
import os
repo = '32xlevel/iscanner'

# https://towardsdatascience.com/all-the-things-you-can-do-with-github-api-and-python-f01790fca131
# https://gist.github.com/MartinHeinz/e4c7e0936ea0dea2853a10b3e00eb9bf
token = os.getenv('GITHUB_TOKEN')
headers = {'Authorization': f'token {token}'}

ghReq = requests.get(f'https://api.github.com/repos/{repo}/commits?until=2020-09-01', headers = headers)


print(ghReq)
# print(ghReq.json())
print(ghReq.headers)
#
hocReq = requests.get('https://hitsofcode.com/github/' + repo + '/json')
print(hocReq)
print(hocReq.json())
#
locReq = requests.get(f'https://api.codetabs.com/v1/loc/?github={repo}')
print(locReq)
print(locReq.json())
