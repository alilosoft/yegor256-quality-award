import requests

# get all projects from https://www.yegor256.com/2019/11/03/award-2020.html
html = requests.get('https://www.yegor256.com/2019/11/03/award-2020.html')
print(html.text)

# get HoC: https://hitsofcode.com/github/<user>/<repo>/json

# get LoC: https://api.codetabs.com/v1/loc/?github==<username>/<reponame>

# check age > 1y: https://api.github.com/repos/<user>/<repo>/commits?until=2019-09-01

